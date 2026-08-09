# MAPA-GR

**Monitoramento e Análise da Formação Acadêmica na Graduação**

Sistema interativo e gratuito para explorar a qualidade da graduação brasileira pelos
indicadores do **INEP/SINAES** — CPC, ENADE, IDD e IGC — em **47.091 cursos** de todas as
9 grandes áreas do conhecimento.

### 🔗 Abrir o aplicativo: **https://david888azv.github.io/Mapa-GR/**

| | |
|---|---|
| 📊 **Painel principal** | https://david888azv.github.io/Mapa-GR/ |
| 📈 **Estatísticas** | https://david888azv.github.io/Mapa-GR/estatisticas.html |
| ⚖️ **Comparador de cursos** | https://david888azv.github.io/Mapa-GR/comparador.html |
| 🎓 **Censo da Educação Superior** | https://david888azv.github.io/Mapa-GR/censo.html |
| 📖 **Documentação e fontes** | https://david888azv.github.io/Mapa-GR/help-doc.html |

Parte do projeto de divulgação científica **DA ciência** — https://daciencia.org

## Escopo

- **Cobertura**: 47.091 cursos de graduação, em 9 grandes áreas (Exatas, Biológicas,
  Engenharias, Agrárias, Saúde, Sociais Aplicadas, Humanas, Letras e Tecnólogos)
- **Ciclos ENADE**: 2017, 2021 e 2023 (conforme a área)
- **Censo da Educação Superior**: matrículas, ingressantes e concluintes, 2017–2023
- **Indicadores**: CPC, ENADE, IDD, IGC, % Doutores, Infraestrutura, Organização
  Didático-Pedagógica, Regime de Trabalho
- **Instituição de referência** (v2.5): ao abrir, escolhe-se uma entre **264 instituições
  públicas** — 112 federais, 117 estaduais e 35 municipais — que passa a ser destacada (★)
  na comparação. Busca por sigla, nome, UF ou esfera; link direto por sigla
  (`?ies=UFMG`) ou pelo código da IES do INEP (`?ies=568`). O seletor define só o
  destaque: os cursos de **todas** as instituições, inclusive privadas, sempre entram na
  análise. Privadas selecionáveis em versão futura.
- **Códigos e-MEC** (v2.6): cada linha do ranking traz os códigos e-MEC da **IES** e do
  **curso** (`2 / 1188880`); no CSV saem separados em `cod_ies_emec` e `cod_curso_emec`.
  São os códigos vigentes na inscrição do ENADE daquele ciclo, não os do cadastro atual
- **Sugestões** (v2.8): botão **"💡 Sugerir melhoria"** na barra lateral das quatro telas,
  que abre o formulário em `daciencia.org/sugestao` — sigla da IES obrigatória, nome e
  e-mail opcionais, texto de até 250 palavras. No painel principal a sigla da instituição
  de referência já vai preenchida. O formulário fica **fora** do aplicativo, em outro
  domínio
- **Funciona offline** (PWA) e não coleta dados de quem usa — o botão de sugestões não muda
  isso: só sai daqui o que a pessoa escrever, de propósito, no formulário

> A **USP não consta da base**: não participa do ENADE, então não tem Conceito ENADE e
> não entra nos Indicadores de Qualidade publicados pelo INEP. É ausência da fonte.

## Distinção MAPA-PG × MAPA-GR

| | MAPA-PG | MAPA-GR |
|---|---|---|
| Nível | Pós-graduação | Graduação |
| Órgão | CAPES | INEP/SINAES |
| Escala | 1–7 | 1–5 |
| Unidade | Programa | Curso |

**Projeto irmão (pós-graduação): MAPA-PG**
- Aplicativo: https://david888azv.github.io/Mapa-PG-UnB/
- Repositório: https://github.com/david888azv/Mapa-PG-UnB

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
├── build/
│   └── gerar_ies_publicas.py  # índice das 264 IES públicas (seletor de referência)
├── docs/                    # PWA servida pelo GitHub Pages
│   ├── index.html
│   ├── manifest.json
│   ├── sw.js
│   ├── chart.umd.min.js
│   ├── dados_inep.json
│   ├── help-doc.html
│   ├── dados/               # área-*.json + ies_publicas.json
│   └── icons/
├── offline/                 # distribuição local, 5 páginas autocontidas
│   └── gerar_offline.py     # regera a versão offline a partir de docs/
└── logos/
```

A pasta `dados_inep/` local (arquivos XLSX brutos do INEP, ~15 MB) não é commitada — ver `.gitignore`. Para regenerar o dataset, baixe os arquivos dos Indicadores de Qualidade do portal INEP e rode `python3 gerar_mapa_gr.py`.

Para reconstruir o índice do seletor de referência: `python3 build/gerar_ies_publicas.py`
(lê os `docs/dados/*.json` de curso e grava `docs/dados/ies_publicas.json`). Depois de
alterar `docs/`, regere a versão local com `cd offline && python3 gerar_offline.py`.

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
