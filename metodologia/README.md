# Metodologia — Estimativa de matrículas a partir do ENADE/CPC

Esta pasta contém **scripts de pesquisa** (standalone, não integrados ao app MAPA-GR) usados para uma investigação metodológica: **é possível estimar o número de matrículas no ensino superior brasileiro usando apenas os dados do CPC/ENADE do INEP?**

> **TL;DR**: a fórmula funciona para **agregado nacional** (erro ~1-5%), mas **falha em granularidade útil** (grau, área, UF específica). Para qualquer análise abaixo do nacional é imprescindível usar os **microdados do Censo da Educação Superior**, que já estão integrados ao dashboard principal (`docs/censo.html`).

## Arquivos

### `estimar_matriculas.py`
Aplica a fórmula empírica:
```
matrículas ≈ n_inscritos × duração × α / r
```
Parâmetros calibrados na v2 (por modalidade):
- α_presencial = 0,60 | α_EAD = 0,55
- r_presencial = r_área × 1,20 | r_EAD = r_área × 0,45
- Duração: 4 anos padrão | 5 para Engenharia/Arquitetura/Direito/Odonto/Vet/Farm/Agro | 6 para Medicina | 2,5 para Tecnológico

Fonte: dados ENADE/CPC agregados em `../mapa-gr/docs/dados/*.json` (9 grandes áreas × 1-5 ciclos cada).

**Como rodar:**
```bash
python estimar_matriculas.py
```

**Saída:** relatório em texto com estimativa por grande área, grau, modalidade, região e top 15 UFs, mais sanity-check contra Sinopse INEP 2022.

### `auditoria_estimativa.py`
Compara a estimativa acima com os **valores reais do Censo 2023** (`../mapa-gr/docs/dados/censo_superior_consolidado.json`). Reporta:
- Erro absoluto e relativo por dimensão
- Fator de correção que faria a estimativa casar com o real
- Classificação de qualidade (ótimo <10% / bom <25% / ruim <50% / péssimo >50%)

**Como rodar:**
```bash
python auditoria_estimativa.py
```

## Resultados da auditoria (Censo 2023 como baseline)

| Dimensão | Qualidade | Observação |
|---|---|---|
| **Total nacional** | −1,5% ✓ | Excelente no agregado |
| **Por modalidade** | ±11% ~ | Presencial −12%, EAD +10% |
| **Por grau** | ✗ −93% a +59% | **Inútil** — 74% dos cursos no CPC têm grau "Outro" |
| **Por grande área** | 4/8 erro >50% ✗ | Mapping CPC↔CINE imperfeito + heterogeneidade interna |
| **Por região** | 1/5 ótimo | Sudeste +5% ✓, Sul +58%, Norte −51% |
| **Por UF** | 3/15 ótimo | RJ +0,2%, PE −4%, DF −10% acertam; PR +150%, MT −61% falham |

## Por que o modelo falha em granularidade fina

1. **Campo `grau` mal classificado no CPC**: 20.542 de 27.698 cursos aparecem como "Outro" (inclui quase toda engenharia, medicina, direito, pós). Isso destrói análises por grau.

2. **Mapeamento CPC↔Censo não é 1:1**:
   - CPC separa "Biologicas" como grande área; Censo via CINE junta em "Exatas" (CINE 05) ou "Saúde" (CINE 09)
   - CPC tem "Tecnólogos" como dataset separado; Censo distribui por área CINE
   - Censo tem "Serviços" (294k matrículas reais em 2023) que CPC não cobre

3. **Heterogeneidade interna das áreas**: Engenharia (Elétrica 5a, Civil 5a, Produção 4a), Saúde (Medicina 6a, Enfermagem 4a, EAD 4a), Humanas (Pedagogia EAD vs Filosofia Presencial) têm D/r muito diferentes que o modelo não captura.

4. **Viés regional do EAD**: Paraná concentra ~800 mil matrículas EAD em poucas IES (UNOPAR/UNINTER). Modelo super/subestima grosseiramente por UF.

## Decisão

Por essas limitações, o **modelo não foi integrado ao dashboard do MAPA-GR**. O app tem duas páginas complementares cobrindo cada abordagem com o dado apropriado:

- **`docs/estatisticas.html` (ENADE/CPC)** — indicador de **qualidade** (faixa CPC 1-5, ENADE contínuo, IDD, taxa de participação)
- **`docs/censo.html` (Censo INEP)** — indicador de **estoque** (matrículas, ingressantes, concluintes, gênero, raça, idade, financiamento)

Esses dois indicadores são **complementares** (ver nota didática em `docs/help-doc.html` → seção "Indicadores"):
- ENADE responde "quão bem o curso forma?"
- Censo responde "quantos estão cursando?"

## Quando o modelo é útil

Apenas para:
- **Estimativas de ordem de grandeza** em nível nacional
- **Projeções intermediárias** entre ciclos do Censo (ex: estimar 2024 antes do INEP publicar)
- **Validação cruzada** — se a estimativa diverge muito do Censo num ano específico, vale investigar se houve mudança metodológica

Para análise real, **sempre prefira o Censo da Educação Superior**.

## Fontes

- **Portal INEP — Microdados do Censo da Ed. Superior**: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/microdados/censo-da-educacao-superior
- **Portal INEP — CPC/ENADE**: https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos/indicadores-educacionais/indicadores-de-qualidade-da-educacao-superior
- TCU/INEP — Relatórios de Diplomação e Evasão (fonte dos valores-base de r)
- Ristoff (1999) e Silva Filho et al. (2007) — estudos clássicos sobre evasão na graduação

---

*Prof. David L. Azevedo — MAPA-GR | Metodologia v2, abril de 2026*
