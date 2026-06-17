# MAPA-GR

**Monitoramento e Análise da Formação Acadêmica na Graduação**

Sistema interativo para acompanhamento dos cursos de graduação em **Física** no Brasil, usando os indicadores de qualidade publicados pelo INEP/MEC (SINAES).

**PWA disponível em:** https://david888azv.github.io/Mapa-GR/

## Escopo v1.0

- **Área**: Física (Licenciatura + Bacharelado)
- **Ciclos**: ENADE 2017 e 2021
- **Total**: 518 cursos em 159 IES, cobertura nacional (27 UFs)
- **Indicadores**: CPC, ENADE, IDD, IGC, % Doutores, Infraestrutura, Organização Didático-Pedagógica, Regime de Trabalho

## Distinção MAPA-PG × MAPA-GR

| | MAPA-PG | MAPA-GR |
|---|---|---|
| Nível | Pós-graduação | Graduação |
| Órgão | CAPES | INEP/SINAES |
| Escala | 1–7 | 1–5 |
| Unidade | Programa | Curso |

Projeto irmão (pós-graduação): **MAPA-PG-UnB** — https://github.com/david888azv/Mapa-PG-UnB
(app: https://david888azv.github.io/Mapa-PG-UnB/)

## Como instalar no celular (Android)

1. Abra https://david888azv.github.io/Mapa-GR/ no Chrome
2. Menu `⋮` → *Adicionar à tela inicial*
3. O app aparece com ícone próprio, funciona offline após a primeira abertura e atualiza automaticamente

## Estrutura do repositório

```
mapa-gr/
├── 1.0-mapa-gr.html         # versão standalone
├── dados_inep.json          # dataset consolidado (gerado por gerar_mapa_gr.py)
├── help-doc.html            # documentação
├── gerar_mapa_gr.py         # script de extração dos XLSX do INEP
├── docs/                    # PWA servida pelo GitHub Pages
│   ├── index.html
│   ├── manifest.json
│   ├── sw.js
│   ├── chart.umd.min.js
│   ├── dados_inep.json
│   ├── help-doc.html
│   └── icons/
└── logos/
```

A pasta `dados_inep/` local (arquivos XLSX brutos do INEP, ~15 MB) não é commitada — ver `.gitignore`. Para regenerar o dataset, baixe os arquivos dos Indicadores de Qualidade do portal INEP e rode `python3 gerar_mapa_gr.py`.

## Fontes de dados

Todos os dados provêm do **Portal de Dados Abertos do INEP** (https://www.gov.br/inep/pt-br/acesso-a-informacao/dados-abertos), publicados sob a Lei de Acesso à Informação (Lei n. 12.527/2011).

URLs específicas documentadas em `help-doc.html`.

## Autor

**Prof. Titular David Lima Azevedo**
Grupo de Dinâmica e Ab Initio (GDAI) · Núcleo de Estrutura da Matéria
Instituto de Física — Universidade de Brasília (UnB)

- ORCID: https://orcid.org/0000-0002-3456-554X
- Google Scholar: https://scholar.google.com.br/citations?hl=en&user=o-qWsUAAAAAJ&view_op=list_works&sortby=pubdate
- Lattes: http://lattes.cnpq.br/3892893860696339
- E-mail: david888azv@unb.br

## Como citar

AZEVEDO, D. L. **MAPA-GR — um sistema interativo para monitoramento e análise da
graduação brasileira: aplicação a dados do Censo e do ENADE com estudo de caso da
UnB, das Ciências Exatas e da Física**. *Physicae Organum*, Brasília, v. 11, n. 1,
2026. DOI: [10.26512/2446-564X2026e62165](https://doi.org/10.26512/2446-564X2026e62165).

Veja também `CITATION.cff` (formato legível por máquina).
