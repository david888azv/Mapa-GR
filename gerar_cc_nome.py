#!/usr/bin/env python3
"""
Helper de build do MAPA-GR — mapa `cc` (codigo e-MEC) -> nome real do curso.

O CPC/ENADE identifica cada curso apenas pela AREA DE AVALIACAO do ENADE, nao pelo
nome. Cursos sem exame proprio caem na area generica "ENGENHARIA" (e afins), entao
a UFPE, por exemplo, mostra 4 entradas "ENGENHARIA" indistinguiveis (Biomedica,
Energia, Materiais, Naval). O Censo da Educacao Superior, por outro lado, traz o
nome real por codigo de curso (CO_CURSO -> NO_CURSO).

Este script le os microdados do Censo (censo_sup/cache/*.zip) e grava um mapa
`dados_inep/cc_nome.json` = { "58856": "Engenharia Biomedica", ... }, consumido
pelo gerar_mapa_gr_multi.py para preencher o campo `nc` de cada curso.

Regras:
  - O codigo e-MEC e PERSISTENTE entre anos; um curso de 2018 (sem microdado
    proprio) se resolve pelo Censo de 2017/2021. Consolidamos todos os anos.
  - Ano mais recente VENCE (renomeacoes): processamos em ordem crescente, o
    ultimo a escrever prevalece.
  - Nome normalizado para Title Case pt-BR (o Censo mistura CAIXA ALTA e Title).

Uso:  python3 gerar_cc_nome.py         # gera/atualiza dados_inep/cc_nome.json
Idempotente. Rode antes de gerar_mapa_gr_multi.py (ou só quando os censos mudarem).
"""

import zipfile
import csv
import io
import json
import os

BASE = os.path.dirname(os.path.abspath(__file__))
CENSO_CACHE = os.path.join(BASE, '..', 'censo_sup', 'cache')
OUT = os.path.join(BASE, 'dados_inep', 'cc_nome.json')

# Ordem crescente: o ultimo (2023) sobrescreve os anteriores em caso de renomeacao.
ANOS = ['2017', '2021', '2022', '2023']

# Conectivos que ficam em minuscula no meio do nome (Title Case pt-BR).
_MINUS = {'de', 'da', 'do', 'das', 'dos', 'e', 'em', 'a', 'o', 'as', 'os',
          'com', 'para', 'por', 'na', 'no', 'nas', 'nos', 'à', 'ao', 'aos'}


def title_ptbr(nome):
    """Title Case pt-BR: 'ENGENHARIA BIOMÉDICA' -> 'Engenharia Biomédica',
    'CIÊNCIAS BIOLÓGICAS (BACHARELADO)' -> 'Ciências Biológicas (Bacharelado)',
    mantendo conectivos (de/da/e/...) em minuscula, exceto na 1a palavra."""
    if not nome:
        return nome
    palavras = nome.strip().split()
    out = []
    for i, p in enumerate(palavras):
        low = p.lower()
        if i > 0 and low in _MINUS:
            out.append(low)
        elif p.startswith('(') and len(p) > 1:
            out.append('(' + p[1:2].upper() + p[2:].lower())
        else:
            out.append(low[:1].upper() + low[1:])
    return ' '.join(out)


def carregar_ano(ano):
    """Retorna dict {co_curso: no_curso_bruto} do microdado do Censo daquele ano."""
    zpath = os.path.join(CENSO_CACHE, f'microdados_censo_superior_{ano}.zip')
    if not os.path.exists(zpath):
        print(f'  [aviso] microdado {ano} ausente ({zpath}) — pulado')
        return {}
    zf = zipfile.ZipFile(zpath)
    nome = next((n for n in zf.namelist()
                 if n.upper().endswith(f'CURSOS_{ano}.CSV')), None)
    if nome is None:
        print(f'  [aviso] CSV de CURSOS nao encontrado no zip {ano} — pulado')
        return {}
    out = {}
    with zf.open(nome) as fh:
        rd = csv.reader(io.TextIOWrapper(fh, encoding='latin-1'), delimiter=';')
        head = next(rd)
        try:
            ico = head.index('CO_CURSO')
            ino = head.index('NO_CURSO')
        except ValueError:
            print(f'  [aviso] colunas CO_CURSO/NO_CURSO ausentes no {ano} — pulado')
            return {}
        for r in rd:
            if len(r) > max(ico, ino):
                cc, no = r[ico].strip(), r[ino].strip()
                if cc and no:
                    out[cc] = no
    return out


def main():
    mapa = {}
    for ano in ANOS:
        d = carregar_ano(ano)
        mapa.update(d)   # ordem crescente => ano recente vence
        print(f'  Censo {ano}: {len(d):>7,} cursos  (mapa acumulado: {len(mapa):,})')
    # normalizar nomes
    mapa = {cc: title_ptbr(no) for cc, no in mapa.items()}
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w', encoding='utf-8') as f:
        json.dump(mapa, f, ensure_ascii=False, separators=(',', ':'))
    kb = os.path.getsize(OUT) / 1024
    print(f'\n  -> {OUT}')
    print(f'     {len(mapa):,} codigos | {kb:,.0f} KB')
    # amostra de verificacao (os 4 codigos de Engenharia da UFPE)
    print('\n  Amostra (Engenharia UFPE):')
    for cc in ['58856', '117384', '1136141', '1188497']:
        print(f'    {cc}: {mapa.get(cc, "(ausente)")}')


if __name__ == '__main__':
    main()
