"""
Auditoria da estimativa grosseira (estimar_matriculas.py) contra os valores
REAIS do Censo da Educação Superior (INEP 2017-2023).

Compara estimativa × real em várias dimensões e reporta:
  - Erro absoluto e relativo (%)
  - Fator de correção que faria a estimativa casar com o real
  - Onde o modelo acerta (<±10%), onde superestima/subestima

Objetivo: decidir se a estimativa baseada em ENADE vale a pena ser
exposta no dashboard como comparação didática.
"""
from __future__ import annotations

import json
import pathlib
import sys
from collections import defaultdict

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from estimar_matriculas import (
    load_all, ultimo_ciclo_por_curso, estimar, modalidade,
    AREA_ORDER, REGIAO_NOME, UF_REGIAO,
)

# Labels canônicos das grandes áreas (pegos de metadata.json do MAPA-GR)
GRANDE_AREA_LABEL = {
    "exatas":      "Ciências Exatas e da Terra",
    "biologicas":  "Ciências Biológicas",
    "engenharias": "Engenharias",
    "saude":       "Ciências da Saúde",
    "agrarias":    "Ciências Agrárias",
    "sociais":     "Ciências Sociais Aplicadas",
    "humanas":     "Ciências Humanas",
    "letras":      "Linguística, Letras e Artes",
    "tecnologos":  "Cursos Tecnólogos",
}

CENSO_PATH = pathlib.Path(__file__).resolve().parent.parent / "docs" / "dados" / "censo_superior_consolidado.json"
ANO_REF = "2023"  # ano do Censo usado como baseline real
# (o script "último ciclo por curso" já projeta uma foto próxima de 2021-2023)


# ---------- Mapping helpers ----------
# Slugs CPC → slugs Censo. CPC tem biologicas e tecnologos separados;
# Censo (via CINE) distribui biologicas em exatas/saude e tecnologos
# através das áreas. Agrupamos para comparação justa:
CPC_TO_CENSO = {
    "exatas":      "exatas",
    "biologicas":  "exatas",      # biologia segue CINE 05 → Ciências Naturais
    "engenharias": "engenharias",
    "saude":       "saude",
    "agrarias":    "agrarias",
    "sociais":     "sociais",
    "humanas":     "humanas",
    "letras":      "letras",
    "tecnologos":  "SKIP",        # tecnólogo não tem bucket único no Censo
}

GRAU_CPC_TO_CENSO = {
    "Bacharelado":  "1",
    "Licenciatura": "2",
    "Tecnológico":  "3",
    "Outro":        None,         # CPC "Outro" inclui graus mistos
    "?":            None,
    "":             None,
}

MOD_CPC_TO_CENSO = {"Presencial": "1", "EAD": "2"}


def _fmt_int(n):
    if n is None:
        return "—"
    return f"{int(round(n)):,}".replace(",", ".")


def _err_pct(est, real):
    if not real:
        return None
    return (est - real) / real * 100


def _err_class(e):
    if e is None:
        return ""
    a = abs(e)
    if a <= 10:
        return "✓"      # acerta
    if a <= 25:
        return "~"      # aceitável
    if a <= 50:
        return "!"      # alerta
    return "✗"          # ruim


def _print_row(nome, est, real, max_nome=32):
    err = _err_pct(est, real)
    sinal = "+" if (err is not None and err >= 0) else ""
    err_s = f"{sinal}{err:>6.1f}%" if err is not None else "   —  "
    cls = _err_class(err)
    print(f"  {nome[:max_nome]:<{max_nome}}  "
          f"{_fmt_int(est):>12}  {_fmt_int(real):>12}  {err_s}  {cls}")


def _print_tbl(titulo, items, totais_fallback=None):
    print()
    print(titulo)
    print("─" * 82)
    print(f"  {'Dimensão':<32}  {'Estimado':>12}  {'Real':>12}  {'Erro':>7}  ")
    print("─" * 82)
    tot_est = tot_real = 0
    for nome, est, real in items:
        _print_row(nome, est, real)
        tot_est += est or 0
        tot_real += real or 0
    if totais_fallback is not None:
        tot_est, tot_real = totais_fallback
    print("─" * 82)
    _print_row("TOTAL", tot_est, tot_real)


# ---------- Load estimate ----------
print("=" * 82)
print("  AUDITORIA — Estimativa grosseira (ENADE+fórmula) × Censo da Ed. Superior")
print(f"  Ano de referência do Censo: {ANO_REF}")
print("=" * 82)
print()

meta, dados = load_all()
todos = []
for slug in dados:
    todos.extend(dados[slug]["cursos"])
cursos = ultimo_ciclo_por_curso(todos)
cursos_ni = [c for c in cursos if (c.get("ni") or 0) > 0]
print(f"Estimativa: {len(cursos_ni):,} observações de curso (último ciclo com ENADE)".replace(",", "."))

est_total = 0.0
est_por_slug    = defaultdict(float)
est_por_mod     = defaultdict(float)
est_por_grau    = defaultdict(float)
est_por_uf      = defaultdict(float)
est_por_regiao  = defaultdict(float)
est_por_area_mod = defaultdict(float)

for c in cursos_ni:
    e = estimar(c)
    est_total += e
    slug = c.get("_ga")
    est_por_slug[slug]     += e
    est_por_mod[modalidade(c)] += e
    est_por_grau[c.get("g") or "Outro"] += e
    est_por_uf[c.get("u")] += e
    est_por_regiao[c.get("_r")] += e
    est_por_area_mod[(slug, modalidade(c))] += e


# ---------- Load real ----------
censo = json.loads(CENSO_PATH.read_text())
tot_real_nacional = censo["totais_nacionais_por_ano"][ANO_REF]["mat"]
rows_ga_mod_grau = censo["agregacoes_por_ano"]["por_ga_mod_grau"][ANO_REF]
rows_uf_ga_mod_grau = censo["agregacoes_por_ano"]["por_uf_ga_mod_grau"][ANO_REF]
rows_reg_ga_mod_grau = censo["agregacoes_por_ano"]["por_reg_ga_mod_grau"][ANO_REF]

real_por_censo_slug = defaultdict(int)
real_por_mod = defaultdict(int)
real_por_grau = defaultdict(int)
real_por_area_mod = defaultdict(int)
real_por_uf = defaultdict(int)
real_por_regiao = defaultdict(int)

# por_ga_mod_grau é o source "limpo" (sem exigir UF não-null)
for r in rows_ga_mod_grau:
    mat = r.get("mat", 0)
    real_por_censo_slug[r.get("ga")]     += mat
    real_por_mod[r.get("mod")]           += mat
    real_por_grau[r.get("grau")]         += mat
    real_por_area_mod[(r.get("ga"), r.get("mod"))] += mat

# por_reg_ga_mod_grau — tem regiao como dimensão
for r in rows_reg_ga_mod_grau:
    real_por_regiao[r.get("regiao")] += r.get("mat", 0)

# por_uf_ga_mod_grau — para UF
for r in rows_uf_ga_mod_grau:
    real_por_uf[r.get("uf")] += r.get("mat", 0)


# ---------- 1. Total nacional ----------
_print_tbl("1. TOTAL NACIONAL", [
    ("Matrículas — graduação BR", est_total, tot_real_nacional),
])
fator_global = tot_real_nacional / est_total if est_total > 0 else 0
print(f"  Fator de correção global: {fator_global:.3f}  (multiplicar estimativa por este valor)")


# ---------- 2. Por modalidade ----------
items = []
for mod_cpc, mod_censo in MOD_CPC_TO_CENSO.items():
    items.append((mod_cpc, est_por_mod.get(mod_cpc, 0), real_por_mod.get(mod_censo, 0)))
_print_tbl("2. POR MODALIDADE", items)


# ---------- 3. Por grau ----------
items = []
for grau_cpc, grau_censo in GRAU_CPC_TO_CENSO.items():
    if grau_censo is None:
        # soma real das CPCs que não mapeiam bem (área básica + outros)
        continue
    items.append((grau_cpc, est_por_grau.get(grau_cpc, 0), real_por_grau.get(grau_censo, 0)))
# CPC outros (Outro + ? + '') agregam os graus não classificados
outros_est = sum(est_por_grau.get(k, 0) for k in ("Outro", "?", ""))
outros_real = real_por_grau.get("4", 0) + real_por_grau.get("", 0)
items.append(("Outro/Área básica (CPC 'Outro')", outros_est, outros_real))
_print_tbl("3. POR GRAU ACADÊMICO", items)


# ---------- 4. Por grande área (com mapeamento CPC→Censo) ----------
items = []
# CPC slugs com mapeamento direto
for slug in AREA_ORDER:
    target = CPC_TO_CENSO.get(slug, "?")
    if target == "SKIP":
        # tecnologos — vamos incluir apenas como informação
        items.append((f"{slug} (sem bucket Censo)", est_por_slug.get(slug, 0), None))
        continue
    nome = GRANDE_AREA_LABEL.get(slug, slug)
    items.append((nome, est_por_slug.get(slug, 0), real_por_censo_slug.get(target, 0)))
# Para o real, temos censo slugs que podem não estar em CPC direto — "servicos" é um
if "servicos" in real_por_censo_slug and "servicos" not in est_por_slug:
    items.append(("servicos (só no Censo)", 0, real_por_censo_slug["servicos"]))
_print_tbl("4. POR GRANDE ÁREA (mapping CPC→Censo não-perfeito)", items)
print("  NOTA: CPC 'biologicas' foi mapeada para Censo 'exatas' (CINE 05).")
print("  NOTA: CPC 'tecnologos' não tem bucket único — é distribuído por CINE no Censo.")


# ---------- 5. Por região ----------
items = []
for r in ["N","NE","CO","SE","S"]:
    items.append((REGIAO_NOME[r], est_por_regiao.get(r, 0), real_por_regiao.get(r, 0)))
_print_tbl("5. POR REGIÃO", items)


# ---------- 6. Top 10 UFs ----------
real_uf_sorted = sorted(real_por_uf.items(), key=lambda x: -x[1])[:15]
items = [(uf, est_por_uf.get(uf, 0), r_val) for uf, r_val in real_uf_sorted]
_print_tbl("6. TOP 15 UFs (ranqueadas por Censo real)", items)


# ---------- 7. Cruzamento área × modalidade ----------
print()
print("7. CROSSTAB GRANDE ÁREA × MODALIDADE")
print("─" * 98)
print(f"  {'Área':<28}{'Modalid':<12}{'Estimado':>12}{'Real':>12}{'Erro':>9}  Fator corr.")
print("─" * 98)
for slug in AREA_ORDER:
    target = CPC_TO_CENSO.get(slug)
    if target == "SKIP" or target is None:
        continue
    nome = GRANDE_AREA_LABEL.get(slug, slug).replace("Ciências ", "")[:26]
    for mod_cpc, mod_censo in MOD_CPC_TO_CENSO.items():
        est = est_por_area_mod.get((slug, mod_cpc), 0)
        real = real_por_area_mod.get((target, mod_censo), 0)
        err = _err_pct(est, real)
        sinal = "+" if (err is not None and err >= 0) else ""
        err_s = f"{sinal}{err:>6.1f}%" if err is not None else "   —  "
        fator = real / est if est > 0 else 0
        print(f"  {nome:<28}{mod_cpc:<12}{_fmt_int(est):>12}{_fmt_int(real):>12}  {err_s}  {fator:>6.3f}")


# ---------- 8. Resumo de qualidade ----------
print()
print("8. RESUMO DE QUALIDADE")
print("─" * 82)
# Total nacional
err_tot = _err_pct(est_total, tot_real_nacional)
print(f"  Total nacional: estimativa {est_total/1e6:.2f}M × real {tot_real_nacional/1e6:.2f}M → erro {err_tot:+.1f}%")

# Bucket por magnitude de erro
def audit_bucket(name, pairs):
    good = mid = bad = worst = miss = 0
    for n, est, real in pairs:
        if not real or real == 0 or not est:
            miss += 1
            continue
        e = abs(_err_pct(est, real))
        if e <= 10: good += 1
        elif e <= 25: mid += 1
        elif e <= 50: bad += 1
        else: worst += 1
    total = good+mid+bad+worst
    if total == 0:
        return
    print(f"  {name:<28}  ótimo(<10%): {good}/{total}  bom(<25%): {mid}  ruim(<50%): {bad}  péssimo(>50%): {worst}  sem dado: {miss}")

audit_bucket("Por modalidade",
    [(k, est_por_mod.get(k, 0), real_por_mod.get(v, 0)) for k, v in MOD_CPC_TO_CENSO.items()])

audit_bucket("Por grau",
    [(k, est_por_grau.get(k, 0), real_por_grau.get(v, 0))
     for k, v in GRAU_CPC_TO_CENSO.items() if v])

audit_bucket("Por região",
    [(r, est_por_regiao.get(r, 0), real_por_regiao.get(r, 0))
     for r in ["N","NE","CO","SE","S"]])

audit_bucket("Por grande área",
    [(slug, est_por_slug.get(slug, 0),
      real_por_censo_slug.get(CPC_TO_CENSO.get(slug, "?"), 0))
     for slug in AREA_ORDER if CPC_TO_CENSO.get(slug) not in (None, "SKIP")])

audit_bucket("Por UF (top 15)",
    [(uf, est_por_uf.get(uf, 0), r_val) for uf, r_val in real_uf_sorted])

print()
print("─" * 82)
print("  Conclusão: ver interpretação na tela / discussão com o usuário")
print("─" * 82)
