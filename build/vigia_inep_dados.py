#!/usr/bin/env python3
"""Vigia semanal dos dados abertos do INEP para o MAPA-GR.

O INEP não tem API: os arquivos ficam em páginas do gov.br (a de indicadores
carrega cada ano numa aba em URL própria) e em download.inep.gov.br. O vigia
colhe os links de download dessas páginas e lê de cada arquivo, por HEAD, o
Last-Modified e o tamanho. Avisa quando aparece aba/ano novo, arquivo novo ou
arquivo republicado (o INEP republica sem mudar o nome: o Censo 2023 foi
reatualizado em 30/12/2025).

Estado em 16/09/2026 (linha de base): o app usa indicadores até 2023 e Censo até
2023, mas o INEP já publicou o Censo 2024 (10/07/2026) e o Conceito Enade 2025
de Licenciaturas (26/05/2026) e de Medicina (07/07/2026). CPC/IDD/IGC 2025 ainda
não existiam.

download.inep.gov.br serve cadeia de certificado incompleta; para esse host, e só
para a leitura de cabeçalhos, a verificação TLS é desligada.

Uso:
  python3 vigia_inep_dados.py            # compara e imprime
  python3 vigia_inep_dados.py --email    # idem, e manda e-mail se houver novidade
"""
import html
import json
import os
import re
import smtplib
import ssl
import sys
import urllib.error
import urllib.request
from datetime import datetime
from email.message import EmailMessage
from email.utils import formatdate, make_msgid

AQUI = os.path.dirname(os.path.abspath(__file__))
ESTADO = os.path.join(AQUI, "vigia_inep_estado.json")
LOG = os.path.join(AQUI, "vigia_inep.log")
DESTINO = os.environ.get("INEP_AVISO_PARA") or os.environ.get("SMTP_FROM", "contato@daciencia.org")
UA = "Mozilla/5.0 (X11; Linux x86_64) Firefox/128.0 mapa-gr-vigia/1.0"

DA = "https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos"
INDICADORES = DA + "/indicadores-educacionais/indicadores-de-qualidade-da-educacao-superior"
PAGINAS = {
    "censo": DA + "/microdados/censo-da-educacao-superior",
    "enade": DA + "/microdados/enade",
}
ANO_MIN = 2021  # anos anteriores não mudam mais; não vale o HEAD

SEM_VERIFICAR = ssl.create_default_context()
SEM_VERIFICAR.check_hostname = False
SEM_VERIFICAR.verify_mode = ssl.CERT_NONE


def com_tentativas(f, *a, **k):
    # Os servidores do governo derrubam conexão de vez em quando (visto em 16/09/2026
    # nos dois portais ao mesmo tempo); três tentativas espaçadas bastam.
    import time
    for n in range(3):
        try:
            return f(*a, **k)
        except (urllib.error.URLError, ConnectionError, TimeoutError, OSError) as e:
            if isinstance(e, urllib.error.HTTPError) or n == 2:
                raise
            time.sleep(10 * (n + 1))


def baixa(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read().decode("utf-8", "replace")


def cabecalho(url):
    req = urllib.request.Request(url, method="HEAD", headers={"User-Agent": UA})
    ctx = SEM_VERIFICAR if "download.inep.gov.br" in url else None
    try:
        with urllib.request.urlopen(req, timeout=120, context=ctx) as r:
            return "%s|%s" % (r.headers.get("Last-Modified", "?"), r.headers.get("Content-Length", "?"))
    except urllib.error.HTTPError as e:
        return "HTTP %d" % e.code


def links(pagina):
    out = {}
    for m in re.finditer(r'<a[^>]+href="([^"]+)"[^>]*>(.*?)</a>', pagina, re.S):
        u = html.unescape(m.group(1))
        if "download.inep.gov.br" not in u:
            continue
        rot = html.unescape(re.sub(r"<[^>]+>|\s+", " ", m.group(2))).strip()
        out[u] = rot
    return out


def atualizado(pagina):
    m = re.search(r"Atualizado em\s*</span>\s*<span[^>]*>\s*([0-9/]+ [0-9h]+)", pagina)
    return m.group(1) if m else "?"


def instantaneo():
    est = {"paginas": {}, "abas_indicadores": [], "arquivos": {}}
    pag = com_tentativas(baixa, INDICADORES)
    est["paginas"]["indicadores"] = atualizado(pag)
    abas = re.findall(r'data-id="(\d{4})" data-url="([^"]+)"', pag)
    if not abas:
        raise RuntimeError("página de indicadores sem abas — layout mudou?")
    est["abas_indicadores"] = sorted({a for a, _ in abas})
    alvos = {}
    for ano, url in abas:
        if int(ano) >= ANO_MIN:
            for u, rot in links(com_tentativas(baixa, url)).items():
                alvos[u] = "indicadores %s: %s" % (ano, rot)
    for nome, url in PAGINAS.items():
        pag = com_tentativas(baixa, url)
        est["paginas"][nome] = atualizado(pag)
        for u, rot in links(pag).items():
            anos = [int(a) for a in re.findall(r"20\d\d", u)]
            if anos and max(anos) >= ANO_MIN:
                alvos[u] = "%s: %s" % (nome, rot)
    for u, rot in sorted(alvos.items()):
        est["arquivos"][u] = {"rotulo": rot, "cabecalho": com_tentativas(cabecalho, u)}
    return est


def compara(antes, agora):
    linhas = []
    for aba in sorted(set(agora["abas_indicadores"]) - set(antes["abas_indicadores"])):
        linhas.append("ANO NOVO nos Indicadores de Qualidade: %s  <<<" % aba)
        linhas.append("  %s/%s" % (INDICADORES, aba))
    for nome, data in agora["paginas"].items():
        if antes["paginas"].get(nome) != data:
            linhas.append("PÁGINA ATUALIZADA (%s): %s -> %s" % (nome, antes["paginas"].get(nome), data))
    for u in sorted(set(agora["arquivos"]) - set(antes["arquivos"])):
        a = agora["arquivos"][u]
        linhas.append("ARQUIVO NOVO: %s  [%s]" % (a["rotulo"], a["cabecalho"]))
        linhas.append("  %s" % u)
    for u in sorted(set(agora["arquivos"]) & set(antes["arquivos"])):
        a, b = antes["arquivos"][u], agora["arquivos"][u]
        if a["cabecalho"] != b["cabecalho"]:
            linhas.append("ARQUIVO REPUBLICADO: %s  [%s -> %s]" % (b["rotulo"], a["cabecalho"], b["cabecalho"]))
            linhas.append("  %s" % u)
    return linhas


def manda_email(texto):
    faltando = [k for k in ("SMTP_HOST", "SMTP_USER", "SMTP_PASS") if not os.environ.get(k)]
    if faltando:
        print("[aviso] e-mail NÃO enviado — falta %s no ambiente." % ", ".join(faltando))
        return False
    msg = EmailMessage()
    msg["From"] = os.environ.get("SMTP_FROM", "contato@daciencia.org")
    msg["To"] = DESTINO
    msg["Subject"] = "MAPA-GR: novidade nos dados abertos do INEP"
    msg["Date"] = formatdate(localtime=True)
    msg["Message-ID"] = make_msgid(domain="daciencia.org")
    msg.set_content(texto)
    s = smtplib.SMTP(os.environ["SMTP_HOST"], int(os.environ.get("SMTP_PORT", "587")))
    s.starttls(context=ssl.create_default_context())
    s.login(os.environ["SMTP_USER"], os.environ["SMTP_PASS"])
    s.send_message(msg)
    s.quit()
    print("[ok] aviso enviado para %s" % DESTINO)
    return True


def registra(texto):
    with open(LOG, "a", encoding="utf-8") as f:
        f.write("%s  %s\n" % (datetime.now().isoformat(timespec="seconds"), texto))


def grava(est):
    with open(ESTADO, "w", encoding="utf-8") as f:
        json.dump(est, f, ensure_ascii=False, indent=1)


def main():
    agora = instantaneo()
    if not os.path.exists(ESTADO):
        grava(agora)
        registra("linha de base gravada: %d arquivos" % len(agora["arquivos"]))
        print("nada novo (linha de base gravada: %d arquivos)" % len(agora["arquivos"]))
        return
    with open(ESTADO, encoding="utf-8") as f:
        antes = json.load(f)
    linhas = compara(antes, agora)
    if not linhas:
        registra("nada novo (%d arquivos)" % len(agora["arquivos"]))
        print("nada novo")
        return
    texto = ("Mudanças nos dados abertos do INEP desde a última verificação:\n\n"
             + "\n".join(linhas)
             + "\n\nPróximo passo: baixar para mapa-gr/dados_inep/ (indicadores) ou "
               "censo_sup/cache/ (Censo) e regenerar o MAPA-GR.\n")
    print(texto)
    registra("NOVIDADE: %d linhas" % len(linhas))
    enviado = "--email" in sys.argv and manda_email(texto)
    if enviado or "--email" not in sys.argv:
        grava(agora)


if __name__ == "__main__":
    main()
