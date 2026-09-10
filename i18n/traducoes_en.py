# -*- coding: utf-8 -*-
"""
Tabela PT -> EN do MAPA-GR. Aplicada por gerar_ingles.py sobre as paginas de
docs/, que continuam sendo as unicas editaveis a mao.

Regra: cada chave e um trecho LITERAL da pagina em portugues e tem de aparecer
nela exatamente uma vez. Chave que nao bate = o gerador para. E assim que se
evita a versao inglesa silenciosamente defasada.

CUIDADO QUE ESTA TABELA TEM E QUE UMA TRADUCAO EM BLOCO NAO TERIA: nestas
paginas, a mesma palavra e ora rotulo, ora DADO. Em

    <input type="checkbox" class="cat-chk" value="Pública Federal" checked> Pública Federal

o `value=` casa com o dado do INEP e o texto depois do `>` e o rotulo. As chaves
daqui incluem o `>` e o `</label>` de proposito, para pegar so o rotulo. Traduzir
o `value=` quebraria o filtro sem erro visivel — a tela ficaria simplesmente
vazia.

Nao se traduz: siglas e nomes proprios (CPC, ENADE, IDD, IGC, INEP, SINAES, UF,
e-MEC, MAPA-GR), nomes de instituicao e de curso (que sao dados), e as chaves de
objeto do JS.
"""

INDEX = [

    # ------------------------------------------------------------------ <head>
    ("<title>MAPA-GR — Análise da Graduação Brasileira (INEP/SINAES)</title>",
     "<title>MAPA-GR — Analysis of Brazilian Undergraduate Education (INEP/SINAES)</title>"),

    ('content="MAPA-GR — Análise da graduação brasileira a partir dos indicadores '
     'SINAES/INEP (CPC, ENADE, IDD, IGC). Dados de ~47.000 cursos em 9 grandes áreas.">',
     'content="MAPA-GR — Analysis of Brazilian undergraduate education through the official '
     'SINAES/INEP indicators (CPC, ENADE, IDD, IGC). Data on ~47,000 programmes across 9 '
     'broad fields.">'),

    ('<meta property="og:title" content="MAPA-GR — Análise da Graduação Brasileira (INEP/SINAES)">',
     '<meta property="og:title" content="MAPA-GR — Analysis of Brazilian Undergraduate '
     'Education (INEP/SINAES)">'),

    ('<meta property="og:description" content="Sistema interativo e gratuito para explorar os '
     'indicadores da graduação brasileira (CPC, ENADE, IDD, IGC): ~47.000 cursos, 9 grandes '
     'áreas, dados públicos do INEP/SINAES.">',
     '<meta property="og:description" content="A free, interactive system for exploring the '
     'indicators of Brazilian undergraduate education (CPC, ENADE, IDD, IGC): ~47,000 '
     'programmes, 9 broad fields, public data from INEP/SINAES.">'),

    ('<meta name="twitter:title" content="MAPA-GR — Análise da Graduação Brasileira (INEP/SINAES)">',
     '<meta name="twitter:title" content="MAPA-GR — Analysis of Brazilian Undergraduate '
     'Education (INEP/SINAES)">'),

    ('<meta name="twitter:description" content="Indicadores da graduação brasileira (CPC, '
     'ENADE, IDD, IGC) de ~47.000 cursos, em 9 grandes áreas. Dados públicos do INEP/SINAES.">',
     '<meta name="twitter:description" content="Indicators of Brazilian undergraduate '
     'education (CPC, ENADE, IDD, IGC) for ~47,000 programmes across 9 broad fields. Public '
     'data from INEP/SINAES.">'),

    ('<meta property="og:image:alt" content="DA ciência — Ciência com dados. Educação com evidência.">',
     '<meta property="og:image:alt" content="DA ciência — Science with data. Education with evidence.">'),

    ('<meta name="twitter:image:alt" content="DA ciência — Ciência com dados. Educação com evidência.">',
     '<meta name="twitter:image:alt" content="DA ciência — Science with data. Education with evidence.">'),

    # --------------------------------------------------------------- cabecalho
    ('<button class="menu-toggle" id="menuToggle" aria-label="Abrir filtros">☰</button>',
     '<button class="menu-toggle" id="menuToggle" aria-label="Open filters">☰</button>'),

    ("<h1><span>MAPA-GR</span> — Análise da Graduação Brasileira (INEP/SINAES)</h1>",
     "<h1><span>MAPA-GR</span> — Brazilian Undergraduate Education (INEP/SINAES)</h1>"),

    # ------------------------------------------------------------ barra lateral
    ('style="width:100%;">↺ Trocar instituição de referência</button>',
     'style="width:100%;">↺ Change reference institution</button>'),

    ("<h3>🔍 Buscar (sigla, curso ou área)</h3>",
     "<h3>🔍 Search (acronym, programme or field)</h3>"),

    ('<label><input type="checkbox" id="searchEnabled"> Filtrar por texto</label>',
     '<label><input type="checkbox" id="searchEnabled"> Filter by text</label>'),

    ('placeholder="ex: UFPE, Biomédica, ENGENHARIA"',
     'placeholder="e.g.: UFPE, Biomédica, ENGENHARIA"'),

    ('Casa a sigla da IES, o nome do curso ou a área ENADE (acento‑insensível). '
     'Ex.: "Biomédica" acha a Engenharia Biomédica.</p>',
     'Matches the institution acronym, the programme name or the ENADE field '
     '(accent-insensitive). Data are in Portuguese: e.g. "Biomédica" finds Engenharia '
     'Biomédica (Biomedical Engineering).</p>'),

    ("<h3>Área (multiselecionar)</h3>", "<h3>Field (multi-select)</h3>"),
    ("<h3>Ciclo</h3>", "<h3>Assessment cycle</h3>"),
    ("<h3>Grau</h3>", "<h3>Degree type</h3>"),

    ('value="Licenciatura" checked> Licenciatura</label>',
     'value="Licenciatura" checked> Teaching degree</label>'),
    ('value="Bacharelado" checked> Bacharelado</label>',
     'value="Bacharelado" checked> Bachelor\'s</label>'),
    ('value="Outro" checked> Tecnólogo/Outro</label>',
     'value="Outro" checked> Technologist / other</label>'),

    ("<h3>Modalidade</h3>", "<h3>Delivery mode</h3>"),
    ('value="Presencial" checked> Presencial</label>',
     'value="Presencial" checked> On campus</label>'),
    ('value="EAD" checked> EAD</label>',
     'value="EAD" checked> Distance learning</label>'),

    ("<h3>Categoria</h3>", "<h3>Institution type</h3>"),
    ('value="Pública Federal" checked> Pública Federal</label>',
     'value="Pública Federal" checked> Federal public</label>'),
    ('value="Pública Estadual" checked> Pública Estadual</label>',
     'value="Pública Estadual" checked> State public</label>'),
    ('value="Pública Municipal" checked> Pública Municipal</label>',
     'value="Pública Municipal" checked> Municipal public</label>'),
    ('value="Privada sem fins lucrativos" checked> Priv. s/ fins</label>',
     'value="Privada sem fins lucrativos" checked> Private non-profit</label>'),
    ('value="Privada com fins lucrativos" checked> Priv. c/ fins</label>',
     'value="Privada com fins lucrativos" checked> Private for-profit</label>'),
    ('value="Especial" checked> Especial</label>',
     'value="Especial" checked> Special</label>'),

    ("<h3>Faixa CPC/ENADE</h3>", "<h3>CPC/ENADE band</h3>"),

    ("<h3>Região</h3>", "<h3>Region</h3>"),
    ('value="N" checked> Norte</label>', 'value="N" checked> North</label>'),
    ('value="NE" checked> Nordeste</label>', 'value="NE" checked> Northeast</label>'),
    ('value="CO" checked> Centro-Oeste</label>', 'value="CO" checked> Central-West</label>'),
    ('value="SE" checked> Sudeste</label>', 'value="SE" checked> Southeast</label>'),
    ('value="S" checked> Sul</label>', 'value="S" checked> South</label>'),

    ("<h3>UF (Estado)</h3>", "<h3>State (UF)</h3>"),
    ('cursor:pointer;">Todos</button>', 'cursor:pointer;">All</button>'),
    ('cursor:pointer;">Nenhum</button>', 'cursor:pointer;">None</button>'),

    ("<h3>Métrica principal</h3>", "<h3>Main metric</h3>"),
    ('<option value="pc" selected>CPC contínuo</option>',
     '<option value="pc" selected>CPC (continuous)</option>'),
    ('<option value="e">ENADE contínuo</option>',
     '<option value="e">ENADE (continuous)</option>'),
    ('<option value="ip">IDD (contínuo/padronizado)</option>',
     '<option value="ip">IDD (continuous/standardised)</option>'),
    ('<option value="dr">% Doutores (padronizada)</option>',
     '<option value="dr">% with doctorate (standardised)</option>'),
    ('<option value="ms">% Mestres (padronizada)</option>',
     '<option value="ms">% with master\'s (standardised)</option>'),
    ('<option value="rg">Regime de trabalho (pad)</option>',
     '<option value="rg">Faculty contract type (std)</option>'),
    ('<option value="nf">Infraestrutura (pad)</option>',
     '<option value="nf">Infrastructure (std)</option>'),
    ('<option value="op">Org. Didático-Ped. (pad)</option>',
     '<option value="op">Teaching organisation (std)</option>'),

    ('onclick="analisar()">Analisar</button>', 'onclick="analisar()">Analyse</button>'),
    ('onclick="marcarTodos()">Marcar todos</button>',
     'onclick="marcarTodos()">Select all</button>'),
    ('onclick="desmarcarTodos()">Desmarcar todos</button>',
     'onclick="desmarcarTodos()">Clear all</button>'),
    ('onclick="exportReport()">Relatório</button>',
     'onclick="exportReport()">Report</button>'),
    ('onclick="exportCSV()">Exportar CSV</button>',
     'onclick="exportCSV()">Export CSV</button>'),
    ('margin-top:8px;">⚔️ Comparar cursos entre UFs</button>',
     'margin-top:8px;">⚔️ Compare programmes across states</button>'),
    ('margin-top:4px;">🏆 TOP 10 / 27 — Cursos mais e menos bem avaliados</button>',
     'margin-top:4px;">🏆 TOP 10 / 27 — Best and worst rated programmes</button>'),
    ('margin-top:16px;">📊 Estatísticas ENADE</button>',
     'margin-top:16px;">📊 ENADE statistics</button>'),
    ('margin-top:4px;">📈 Censo Ed. Superior 2017-2023</button>',
     'margin-top:4px;">📈 Higher Education Census 2017-2023</button>'),
    # ======================================================================
    # Strings do JAVASCRIPT. Aqui mora o cuidado principal desta tabela: ao
    # lado de rotulo de interface ha nome de instituicao, sigla e chave de
    # objeto. So entra o que e mostrado ao leitor.
    # ======================================================================

    # --------------------------------------------- rotulos das metricas
    ("pc:'CPC contínuo', e:'ENADE contínuo', ip:'IDD (pad/cont)',",
     "pc:'CPC (continuous)', e:'ENADE (continuous)', ip:'IDD (std/cont)',"),
    ("dr:'% Doutores (pad)', ms:'% Mestres (pad)', rg:'Regime trab. (pad)',",
     "dr:'% w/ doctorate (std)', ms:'% w/ MSc (std)', rg:'Contract type (std)',"),
    # NB: nada de apostrofe nas traducoes que vao para dentro de string JS de
    # aspas simples — um "master's" ali fecha a string e quebra a pagina inteira.
    # Foi o que aconteceu na primeira geracao; por isso existe testar_ingles.py.
    ("nf:'Infraestrutura (pad)', op:'Org. Didático-Ped. (pad)'",
     "nf:'Infrastructure (std)', op:'Teaching org. (std)'"),

    # --------------------------------------------- modal de licenca/creditos
    ("Monitoramento e Análise da Formação Acadêmica na Graduação</p>",
     "Monitoring and Analysis of Undergraduate Education</p>"),
    ("v${VERSION} — Agosto 2026</p>", "v${VERSION} — August 2026</p>"),
    ("Prof. Titular David Lima Azevedo</p>", "Prof. David Lima Azevedo, Full Professor</p>"),
    ("Grupo de Dinâmica e Ab Initio (GDAI) · Núcleo de Estrutura da Matéria · Instituto de Física — UnB<br>",
     "Dynamics and Ab Initio Group (GDAI) · Matter Structure Centre · Institute of Physics — UnB<br>"),

    ("<p><strong>Fonte dos dados:</strong> <strong>Portal de Dados Abertos do INEP</strong>",
     "<p><strong>Data source:</strong> <strong>INEP Open Data Portal</strong>"),
    ("</a>) — dados públicos e de livre acesso (INEP/MEC), Lei de Acesso à Informação "
     "(n. 12.527/2011). URLs de download documentadas no arquivo <strong>help-doc.html</strong> "
     "(botão <strong>? Ajuda / Documentação</strong> na barra lateral).</p>",
     "</a>) — public, freely accessible data (INEP/MEC) under the Brazilian Freedom of "
     "Information Act (no. 12.527/2011). Download URLs are documented in "
     "<strong>help-doc.html</strong> (the <strong>? Help / Documentation</strong> button in "
     "the sidebar).</p>"),

    ("<p>Ao utilizar este software, você concorda com os seguintes termos:</p>",
     "<p>By using this software, you agree to the following terms:</p>"),
    ("<li>Não remover, alterar ou ocultar informações de <strong>autoria</strong> ou "
     "créditos do desenvolvedor.</li>",
     "<li>Not to remove, alter or conceal <strong>authorship</strong> information or "
     "developer credits.</li>"),
    ('<li>Manter a identificação <strong>"Prof. David L. Azevedo"</strong> e '
     '<strong>"MAPA-GR"</strong> <strong>em todas as cópias, resultados obtidos e '
     'aplicativos derivados</strong>.</li>',
     '<li>To keep the attribution <strong>"Prof. David L. Azevedo"</strong> and '
     '<strong>"MAPA-GR"</strong> <strong>in every copy, in results obtained and in derived '
     'applications</strong>.</li>'),

    ("<strong>Soluções sob medida:</strong> também desenvolvemos análises específicas para "
     "qualquer curso de graduação de qualquer instituição do país. Contato:",
     "<strong>Tailored analyses:</strong> we also produce specific analyses for any "
     "undergraduate programme at any institution in the country. Contact:"),
    ("· conheça o projeto em <a href=\"https://daciencia.org\"",
     "· learn about the project at <a href=\"https://daciencia.org\""),

    ("<strong>Como citar:</strong> AZEVEDO, D. L. <em>MAPA-GR — um sistema interativo para "
     "monitoramento e análise da graduação brasileira: aplicação a dados do Censo e do ENADE "
     "com estudo de caso da UnB, das Ciências Exatas e da Física</em>. Physicae Organum, "
     "v. 11, n. 1, 2026. DOI:",
     "<strong>How to cite:</strong> AZEVEDO, D. L. <em>MAPA-GR — um sistema interativo para "
     "monitoramento e análise da graduação brasileira: aplicação a dados do Censo e do ENADE "
     "com estudo de caso da UnB, das Ciências Exatas e da Física</em> [in Portuguese]. "
     "Physicae Organum, vol. 11, no. 1, 2026. DOI:"),

    (">Concordo e desejo continuar</button>", ">I agree and wish to continue</button>"),

    # --------------------------------------------- seletor de instituicao
    ('placeholder="Buscar por sigla, nome, UF ou esfera (ex.: UEMA, UFMG, estadual, MA)…"',
     'placeholder="Search by acronym, name, state or sphere (e.g.: UEMA, UFMG, estadual, MA)…"'),

    # --------------------------------------------- estado e carregamento
    ('<p id="loadingMsg">Carregando metadata...</p>', '<p id="loadingMsg">Loading metadata...</p>'),
    ("`Área desconhecida: ${slug}`", "`Unknown field: ${slug}`"),
    ("setStatus(`Carregando ${meta.label}...`)", "setStatus(`Loading ${meta.label}...`)"),
    ("textContent = `Carregando ${META.grandes_areas[slug].label}...`",
     "textContent = `Loading ${META.grandes_areas[slug].label}...`"),
    ("Erro ao carregar metadata.json: ${e.message}", "Failed to load metadata.json: ${e.message}"),
    ("setStatus('Buscando em todas as áreas…')", "setStatus('Searching all fields…')"),
    ("setStatus('Filtro vazio')", "setStatus('No results')"),
    ("<h2>Nenhum curso encontrado</h2><p>Ajuste os filtros na barra lateral.</p>",
     "<h2>No programme found</h2><p>Adjust the filters in the sidebar.</p>"),
    ("'🔎 Busca global (todas as áreas)'", "'🔎 Global search (all fields)'"),
    ("${partialCount} sem CPC composto", "${partialCount} without a composite CPC"),
    ("setStatus(`${cursos.length} cursos mostrados em ${CURRENT.label}`)",
     "setStatus(`${cursos.length} programmes shown in ${CURRENT.label}`)"),

    # --------------------------------------------- caixas de numeros e tabela
    ('<div class="label">Cursos filtrados</div>', '<div class="label">Programmes</div>'),
    ('<div class="label">UFs</div>', '<div class="label">States</div>'),
    ('<div class="label">${metricaLabel} (média)</div>', '<div class="label">${metricaLabel} (mean)</div>'),
    ('<div class="label">Faixa 5</div>', '<div class="label">Band 5</div>'),
    ('<div class="label">Faixa 4</div>', '<div class="label">Band 4</div>'),
    ('<div class="label">Faixa 3</div>', '<div class="label">Band 3</div>'),
    ('<div class="label">Faixa 2</div>', '<div class="label">Band 2</div>'),
    ('<div class="label">Faixa 1</div>', '<div class="label">Band 1</div>'),
    ("<h2>Ranking (${cursos.length}, mostrando top ${showLimit}) — por ${metricaLabel}</h2>",
     "<h2>Ranking (${cursos.length}, showing top ${showLimit}) — by ${metricaLabel}</h2>"),
    ("<th>Sigla</th><th>UF</th><th>Ano</th><th>G</th><th>M</th>",
     "<th>Acronym</th><th>State</th><th>Year</th><th>Deg.</th><th>Mode</th>"),
    ("<th>Área / Município</th>", "<th>Field / municipality</th>"),
    ('<th title="Código e-MEC da IES e do curso, como divulgados pelo INEP">e-MEC<br>IES / curso</th>',
     '<th title="e-MEC code of the institution and of the programme, as published by INEP">'
     'e-MEC<br>inst. / progr.</th>'),
    ("<th>Faixa</th><th>CPC cont</th>", "<th>Band</th><th>CPC cont.</th>"),
    ('title="Códigos e-MEC vigentes na inscrição do ENADE ${c.y}"',
     'title="e-MEC codes in force at ENADE ${c.y} registration"'),

    # --------------------------------------------- graficos
    ("<h2>Distribuição por Faixa</h2>", "<h2>Distribution by band</h2>"),
    ("<h2>Top 15 IES — ${metricaLabel}</h2>", "<h2>Top 15 institutions — ${metricaLabel}</h2>"),
    ("<h2>Cursos por UF</h2>", "<h2>Programmes by state</h2>"),
    ("<h2>Evolução temporal — ${metricaLabel}</h2>", "<h2>Trend over time — ${metricaLabel}</h2>"),
    ("labels: faixas.map(fx => `Faixa ${fx}`)", "labels: faixas.map(fx => `Band ${fx}`)"),
    # aparece nos dois graficos; cada chave leva o contexto que a distingue
    ("title: { display: true, text: 'Nº de cursos' }",
     "title: { display: true, text: 'No. of programmes' }", 2),
    ("`Cursos: ${p.n}`", "`Programmes: ${p.n}`"),
    ("`UFs: ${p.ufs.join(', ')}`", "`States: ${p.ufs.join(', ')}`"),
    ("label: `${METRIC_LABELS[metrica]} — média`", "label: `${METRIC_LABELS[metrica]} — mean`"),

    # --------------------------------------------- avisos
    ("toast('Nenhuma aba carregada')", "toast('No tab loaded')"),
    ("toast('Nenhum curso no filtro atual')", "toast('No programme matches the current filter')"),
    ("toast(`Relatório salvo: ${filename}`)", "toast(`Report saved: ${filename}`)"),
    ("toast('Nada a exportar')", "toast('Nothing to export')"),
    ("toast(`${cursos.length} cursos exportados`)", "toast(`${cursos.length} programmes exported`)"),
    # ------------------------------------------------------------------------
    # Os nomes das 9 GRANDES AREAS vem de dados/metadata.json, que e compartilhado
    # com a versao em portugues e nao se duplica. Em vez de traduzir o dado, a
    # pagina em ingles sobrescreve os rotulos depois de carregar o JSON. As
    # CHAVES (exatas, saude, ...) continuam as mesmas — sao elas que ligam ao
    # arquivo de cada area; so o que se le na tela muda.
    # ------------------------------------------------------------------------
    ("""        META = await r.json();
        renderTabs();""",
     """        META = await r.json();
        const _EN_GRANDES_AREAS = {
            exatas: 'Exact and Earth Sciences', biologicas: 'Biological Sciences',
            engenharias: 'Engineering', saude: 'Health Sciences',
            agrarias: 'Agricultural Sciences', sociais: 'Applied Social Sciences',
            humanas: 'Humanities', letras: 'Linguistics, Literature and Arts',
            tecnologos: 'Technologist Programmes'
        };
        for (const k in _EN_GRANDES_AREAS) {
            if (META.grandes_areas[k]) META.grandes_areas[k].label = _EN_GRANDES_AREAS[k];
        }
        renderTabs();"""),

    # o `.replace(/Ciências /,'')` encurtava o rotulo portugues; em ingles nao ha
    # o que encurtar, e o replace vira inofensivo — fica, para nao mexer no PT.
    ("${m.icon} ${m.label.replace(/Ciências /,'')} <span class=\"count\">"
     "(${m.n_cursos.toLocaleString('pt-BR')})</span>",
     "${m.icon} ${m.label.replace(/Ciências /,'')} <span class=\"count\">"
     "(${m.n_cursos.toLocaleString('en-US')})</span>"),

    ("★ ${REF_NOME} (${unbCursos.length} curso${unbCursos.length>1?'s':''})",
     "★ ${REF_NOME} (${unbCursos.length} programme${unbCursos.length>1?'s':''})"),

    ('<div class="label">IES</div>', '<div class="label">Institutions</div>'),

    # O rotulo da area vem DUAS vezes de lugares diferentes: de metadata.json
    # (ja traduzido acima, alimenta as abas) e de dentro do arquivo da propria
    # area, que e o que abastece CURRENT.label — o titulo do cartao. Sem esta
    # segunda passagem, as abas ficavam em ingles e o cartao em portugues.
    ("""        CURRENT = await loadArea(slug);""",
     """        CURRENT = await loadArea(slug);
        if (META.grandes_areas[slug]) CURRENT.label = META.grandes_areas[slug].label;"""),

    ('style="background:#607D8B;color:#fff;margin-top:4px;">? Ajuda / Documentação</button>',
     'style="background:#607D8B;color:#fff;margin-top:4px;">? Help / Documentation</button>'),
    ('title="Pedir um ajuste, apontar um dado errado ou sugerir uma melhoria">💡 Sugerir melhoria</button>',
     'title="Ask for a change, report wrong data or suggest an improvement">💡 Suggest an improvement</button>'),
    ('<p style="font-size:11px;color:#7F8C8D;margin-bottom:6px;">Clique no cabeçalho para reordenar.</p>',
     '<p style="font-size:11px;color:#7F8C8D;margin-bottom:6px;">Click a column header to sort.</p>'),
]


COMPARADOR = [

    # ------------------------------------------------------------------ <head>
    ('content="MAPA-GR — Comparador Especial de Cursos por UF. Compare até 10 cursos da '
     'mesma área em UFs diferentes.">',
     'content="MAPA-GR — Special programme comparator by state. Compare up to 10 programmes '
     'in the same field across different Brazilian states.">'),
    ("<title>MAPA-GR — Comparador Especial / TOP 10</title>",
     "<title>MAPA-GR — Special Comparator / TOP 10</title>"),
    ('<meta property="og:title" content="MAPA-GR — Comparador Especial / TOP 10">',
     '<meta property="og:title" content="MAPA-GR — Special Comparator / TOP 10">'),
    ('<meta property="og:description" content="Compare até 10 cursos da mesma área em UFs '
     'diferentes pelos indicadores do INEP/SINAES (CPC, ENADE, IDD).">',
     '<meta property="og:description" content="Compare up to 10 programmes in the same field '
     'across different states, using the INEP/SINAES indicators (CPC, ENADE, IDD).">'),

    # --------------------------------------------------------------- cabecalho
    ('<h1 id="pageTitle"><span>MAPA-GR</span> — Comparador Especial (IFES por UFs)</h1>',
     '<h1 id="pageTitle"><span>MAPA-GR</span> — Special Comparator (institutions by state)</h1>'),
    ("            ← Voltar\n", "            ← Back\n"),

    # ------------------------------------------------------------ passos 1 a 5
    ("<h3>1. Grande Área</h3>", "<h3>1. Broad field</h3>"),
    ('<option value="">— escolha —</option>', '<option value="">— choose —</option>'),
    ("<h3>2. Curso / Área</h3>", "<h3>2. Programme / field</h3>"),
    ('<select id="areaSelect" class="select-full" disabled><option value="">— selecione a '
     'grande área —</option></select>',
     '<select id="areaSelect" class="select-full" disabled><option value="">— select the '
     'broad field —</option></select>'),
    ('<p class="hint">Apenas um curso por comparação.</p>',
     '<p class="hint">One programme per comparison.</p>'),
    ("<h3>3. UFs (até 10)</h3>", "<h3>3. States (up to 10)</h3>"),
    ("Selecione o curso primeiro</span>", "Select the programme first</span>", 6),
    ('<p class="uf-count">Selecionadas: <strong id="ufCount">0</strong>/10</p>',
     '<p class="uf-count">Selected: <strong id="ufCount">0</strong>/10</p>'),
    ('<h3 id="stepThresholdsTitle">4. Faixas mínimas</h3>',
     '<h3 id="stepThresholdsTitle">4. Minimum bands</h3>'),
    ('<p class="hint" id="stepThresholdsHint">Filtros aplicados ao selecionar o melhor curso '
     'de cada UF.</p>',
     '<p class="hint" id="stepThresholdsHint">Filters applied when picking the best programme '
     'in each state.</p>'),
    ('<h3 id="stepTipoTitle">5. Tipo de IES</h3>',
     '<h3 id="stepTipoTitle">5. Institution type</h3>'),
    ('value="pub" checked style="margin-right:6px;accent-color:var(--roxo);"> Pública</label>',
     'value="pub" checked style="margin-right:6px;accent-color:var(--roxo);"> Public</label>'),
    ('value="priv" checked style="margin-right:6px;accent-color:var(--roxo);"> Privada</label>',
     'value="priv" checked style="margin-right:6px;accent-color:var(--roxo);"> Private</label>'),
    ('<p class="hint" id="stepTipoHint">Ambas marcadas: mostra a melhor pública <em>e</em> a '
     'melhor privada de cada UF. Só uma: a melhor daquele tipo por UF.</p>',
     '<p class="hint" id="stepTipoHint">Both ticked: shows the best public <em>and</em> the '
     'best private one in each state. Only one: the best of that type per state.</p>'),

    # --------------------------------------------------------- filtros do TOP
    ("<h3>🔍 Buscar por sigla da IES</h3>", "<h3>🔍 Search by institution acronym</h3>"),
    ('id="tSearchEnabled" style="margin-right:6px;accent-color:var(--roxo);"> Filtrar por sigla</label>',
     'id="tSearchEnabled" style="margin-right:6px;accent-color:var(--roxo);"> Filter by acronym</label>'),
    ('placeholder="ex: UNB, UF, IF"', 'placeholder="e.g.: UNB, UF, IF"'),
    ('<p class="hint">Busca parcial: "UF" encontra UFMT, UFRJ, etc.</p>',
     '<p class="hint">Partial match: "UF" finds UFMT, UFRJ, and so on.</p>'),

    ("<h3>Região</h3>", "<h3>Region</h3>"),
    ('value="N" checked style="margin-right:6px;accent-color:var(--roxo);"> Norte</label>',
     'value="N" checked style="margin-right:6px;accent-color:var(--roxo);"> North</label>'),
    ('value="NE" checked style="margin-right:6px;accent-color:var(--roxo);"> Nordeste</label>',
     'value="NE" checked style="margin-right:6px;accent-color:var(--roxo);"> Northeast</label>'),
    ('value="CO" checked style="margin-right:6px;accent-color:var(--roxo);"> Centro-Oeste</label>',
     'value="CO" checked style="margin-right:6px;accent-color:var(--roxo);"> Central-West</label>'),
    ('value="SE" checked style="margin-right:6px;accent-color:var(--roxo);"> Sudeste</label>',
     'value="SE" checked style="margin-right:6px;accent-color:var(--roxo);"> Southeast</label>'),
    ('value="S" checked style="margin-right:6px;accent-color:var(--roxo);"> Sul</label>',
     'value="S" checked style="margin-right:6px;accent-color:var(--roxo);"> South</label>'),

    ("<h3>UF (Estado)</h3>", "<h3>State (UF)</h3>"),
    ('cursor:pointer;">Todos</button>', 'cursor:pointer;">All</button>'),
    ('cursor:pointer;">Nenhum</button>', 'cursor:pointer;">None</button>'),
    ('<p class="hint">Padrão: todas as UFs com cursos marcadas.</p>',
     '<p class="hint">By default, every state that offers the programme is ticked.</p>'),

    ('<h3 style="color:#D4AF37;border-bottom-color:#D4AF37;">🏆 Modos TOP</h3>',
     '<h3 style="color:#D4AF37;border-bottom-color:#D4AF37;">🏆 TOP modes</h3>'),
    ("Escolha a grande área e o curso, ajuste (opcional) os filtros de <strong>sigla</strong>, "
     "<strong>região</strong> e <strong>UF</strong> e clique no relatório desejado. A ordenação "
     "é sempre por <strong>CPC → ENADE → IDD</strong>.",
     "Choose the broad field and the programme, optionally adjust the <strong>acronym</strong>, "
     "<strong>region</strong> and <strong>state</strong> filters, then click the report you "
     "want. Ordering is always by <strong>CPC → ENADE → IDD</strong>."),
    ("<li><strong>TOP 10 / TOP 10 mais baixas</strong>: os 10 cursos do país pelo CPC "
     "<em>contínuo</em> (não pela nota 1–5). Um curso nota 4 de uma UF pode não entrar se "
     "houver 10+ com CPC maior.</li>",
     "<li><strong>TOP 10 / bottom 10</strong>: the 10 programmes in the country by "
     "<em>continuous</em> CPC (not by the 1–5 band). A band-4 programme in one state may not "
     "make the list if 10 or more have a higher CPC.</li>"),
    ("<li><strong>TOP 27 / TOP 27 mais baixas</strong>: 1 curso (melhor/pior) por estado — "
     "use este para ver o curso de uma UF específica.</li>",
     "<li><strong>TOP 27 / bottom 27</strong>: one programme (best/worst) per state — use "
     "this to see the programme in a particular state.</li>"),

    # ----------------------------------------------------------------- botoes
    ('<button id="btnCompare" class="btn btn-main" disabled>Comparar</button>',
     '<button id="btnCompare" class="btn btn-main" disabled>Compare</button>'),
    ('style="background:#D4AF37;">🏆 TOP 10 melhores do país</button>',
     'style="background:#D4AF37;">🏆 TOP 10 best in the country</button>'),
    ('style="background:#B8860B;">🗺️ TOP 27 — melhor por estado</button>',
     'style="background:#B8860B;">🗺️ TOP 27 — best per state</button>'),
    ('style="background:#C0392B;">🔻 TOP menores notas do país</button>',
     'style="background:#C0392B;">🔻 TOP lowest scores in the country</button>'),
    ('style="background:#922B21;">🔻 TOP 27 — menores notas por UF</button>',
     'style="background:#922B21;">🔻 TOP 27 — lowest per state</button>'),
    ('<button id="btnReset" class="btn btn-reset">Limpar seleção</button>',
     '<button id="btnReset" class="btn btn-reset">Clear selection</button>'),
    ('title="Pedir um ajuste, apontar um dado errado ou sugerir uma melhoria">💡 Sugerir melhoria</button>',
     'title="Ask for a change, report wrong data or suggest an improvement">💡 Suggest an improvement</button>'),

    # ------------------------------------------------------------ tela inicial
    # Esta tela existe DUAS vezes no arquivo (o modo TOP reconstroi o estado
    # vazio com o mesmo texto); as duas sao traduzidas.
    ('<h2 style="color:var(--roxo);margin-bottom:8px;">Comparador Especial de Cursos</h2>',
     '<h2 style="color:var(--roxo);margin-bottom:8px;">Special Programme Comparator</h2>', 2),
    ("<p>Compare o <strong>mesmo curso</strong> em até <strong>10 Unidades da Federação</strong> "
     "diferentes.</p>",
     "<p>Compare the <strong>same programme</strong> across up to <strong>10 different "
     "states</strong>.</p>", 2),
    ("O app seleciona automaticamente o <strong>melhor curso</strong> (por CPC, ENADE e IDD) "
     "de cada UF dentro dos filtros escolhidos.</p>",
     "The app automatically picks the <strong>best programme</strong> (by CPC, ENADE and IDD) "
     "in each state, within the filters you choose.</p>", 2),
    ("Siga os passos 1 → 2 → 3 → 4 na barra lateral e clique em <strong>Comparar</strong>.</p>",
     "Follow steps 1 → 2 → 3 → 4 in the sidebar and click <strong>Compare</strong>.</p>", 2),
]

# --------------------------------------------------------------------------
# Comparador — strings do JavaScript.
# Nenhuma traducao daqui usa apostrofe: estas strings vivem entre aspas
# simples no JS e uma apostrofe fecharia a string, matando a pagina inteira.
# --------------------------------------------------------------------------
COMPARADOR += [
    ("${m.icon} ${m.label} (${m.n_cursos.toLocaleString('pt-BR')} cursos)",
     "${m.icon} ${m.label} (${m.n_cursos.toLocaleString('en-US')} programmes)"),
    ("'Erro ao carregar metadata: '", "'Failed to load metadata: '"),
    ("'<option value=\"\">— escolha o curso —</option>'",
     "'<option value=\"\">— choose the programme —</option>'"),
    ("'<option value=\"\">— selecione a grande área —</option>'",
     "'<option value=\"\">— select the broad field —</option>'"),
    ('title="Sem cursos disponíveis para ${area}"',
     'title="No programmes available for ${area}"', 2),
    ("`Máximo ${MAX_UFS} UFs — nem todos os estados da região foram marcados`",
     "`At most ${MAX_UFS} states — not every state in the region was ticked`"),
    ("`Máximo ${MAX_UFS} UFs por comparação`",
     "`At most ${MAX_UFS} states per comparison`"),
    ("'Todas as UFs com oferta estão marcadas: no máximo um curso por estado.'",
     "'Every state that offers it is ticked: at most one programme per state.'"),
    ("'Só parte das UFs está marcada: os 27 do recorte, podendo repetir estado.'",
     "'Only some states are ticked: the 27 of the selection, states may repeat.'"),
    ("'🗺️ TOP 27 — melhores no recorte'", "'🗺️ TOP 27 — best in the selection'"),
    ("'🔻 TOP 27 — menores notas no recorte'", "'🔻 TOP 27 — lowest in the selection'"),
    ("'Selecione grande área e curso'", "'Select a broad field and a programme'", 2),
    ("'Selecione ao menos um tipo de IES (Pública/Privada)'",
     "'Select at least one institution type (public/private)'", 3),
    ("'Erro ao filtrar: '", "'Filtering error: '"),
    ("'Nenhum curso encontrado com os filtros atuais (tipo/sigla/região/UF)'",
     "'No programme found with the current filters (type/acronym/region/state)'"),
    ("'Erro ao renderizar: '", "'Rendering error: '", 2),
    ("'com as menores notas'", "'with the lowest scores'", 3),
    ("'mais bem avaliados'", "'best rated'", 3),
    ("`TOP ${picks.length} — Menores notas por UF (uma por estado)`",
     "`TOP ${picks.length} — Lowest scores by state (one per state)`"),
    ("`TOP ${picks.length} — Melhor curso por estado (um por UF)`",
     "`TOP ${picks.length} — Best programme per state (one per state)`"),
    ("`TOP ${picks.length} — Cursos ${qual} em ${nUfs} UF(s) selecionada(s)`",
     "`TOP ${picks.length} — Programmes ${qual} in ${nUfs} selected state(s)`"),
    ("`TOP ${picks.length} — Cursos com as menores notas`",
     "`TOP ${picks.length} — Programmes with the lowest scores`"),
    ("`TOP ${picks.length} — Cursos mais bem avaliados`",
     "`TOP ${picks.length} — Best rated programmes`"),
    ("' (nacional)'", "' (nationwide)'", 2),
    ("` em ${nUfs} UF(s)`", "` in ${nUfs} state(s)`", 2),
    ("'todas as regiões'", "'all regions'"),
    ("'regiões: '", "'regions: '"),
    ("'todas as UFs'", "'all states'"),
    ("`${filt.ufs.length} UF(s)`", "`${filt.ufs.length} state(s)`"),
    ("` · sigla contém \"${filt.searchTerm}\"`", "` · acronym contains \"${filt.searchTerm}\"`"),
    ("'somente públicas'", "'public only'"),
    ("'somente privadas'", "'private only'"),
    ("'públicas e privadas'", "'public and private'"),
    ("'ordenação ascendente por CPC → ENADE → IDD (mais baixas primeiro)'",
     "'ascending order by CPC → ENADE → IDD (lowest first)'"),
    ("'ordenação por CPC → ENADE → IDD (melhores primeiro)'",
     "'ordered by CPC → ENADE → IDD (best first)'"),
    ("'em todo o país'", "'across the whole country'"),
    ("`nas ${nUfs} UF(s) selecionada(s)`", "`in the ${nUfs} selected state(s)`"),
    ("'com os menores'", "'with the lowest'"),
    ("'com os maiores'", "'with the highest'"),
    ("'a menor nota'", "'the lowest score'", 3),
    ("'o melhor curso'", "'the best programme'", 3),
    ("'entre as menores notas'", "'among the lowest scores'"),
    ("'entre os melhores'", "'among the best'"),
    ("'Selecione pelo menos 2 UFs'", "'Select at least 2 states'"),
    ("'Erro ao selecionar cursos: '", "'Error while selecting programmes: '"),
    ("`Nenhum curso encontrado para \"${area}\" em nenhuma UF`",
     "`No programme found for \"${area}\" in any state`"),
    ("`Nenhum curso encontrado com os filtros (UFs sem dados: ${missing.join(', ')})`",
     "`No programme found with these filters (states without data: ${missing.join(', ')})`"),
    ("'Seleção limpa'", "'Selection cleared'"),
    ("'Erro ao carregar dados: '", "'Failed to load data: '"),

    # avisos e rotulos de grafico/tabela
    ('<div class="warn-box">ℹ️ Os cursos foram avaliados em ciclos ENADE diferentes: '
     '<strong>${years.filter(y=>y!=null).sort().join(\', \')}</strong>. A comparação direta '
     'deve considerar essa diferença temporal.</div>',
     '<div class="warn-box">ℹ️ These programmes were assessed in different ENADE cycles: '
     '<strong>${years.filter(y=>y!=null).sort().join(\', \')}</strong>. Direct comparison '
     'should take that time gap into account.</div>'),
    ('<div class="warn-box">ℹ️ Os cursos foram avaliados em ciclos ENADE diferentes: '
     '<strong>${years.sort().join(\', \')}</strong>. A comparação direta deve considerar '
     'essa diferença temporal.</div>',
     '<div class="warn-box">ℹ️ These programmes were assessed in different ENADE cycles: '
     '<strong>${years.sort().join(\', \')}</strong>. Direct comparison should take that time '
     'gap into account.</div>'),
    ('<div class="warn-box">⚠️ Nenhum curso encontrado para as UFs: <strong>${missing.join(\', \')}'
     '</strong> com os filtros atuais. Tente reduzir as faixas mínimas.</div>',
     '<div class="warn-box">⚠️ No programme found for these states: <strong>${missing.join(\', \')}'
     '</strong> with the current filters. Try lowering the minimum bands.</div>'),
    ('<div class="warn-box">ℹ️ ${27 - missing.length} UFs tinham cursos disponíveis (de 27 '
     'totais). Outras UFs não oferecem esse curso.</div>',
     '<div class="warn-box">ℹ️ ${27 - missing.length} states had programmes available (out of '
     '27). The other states do not offer this programme.</div>'),
    ('title="Código e-MEC da IES e do curso, como divulgados pelo INEP"',
     'title="e-MEC code of the institution and of the programme, as published by INEP"', 2),
    ('title="Códigos e-MEC vigentes na inscrição do ENADE ${c.y}"',
     'title="e-MEC codes in force at ENADE ${c.y} registration"', 2),
    ("${pub?'Pública':'Privada'}", "${pub?'Public':'Private'}", 2),
    ("`TOP ${picks.length} Nacional — ${gaMeta.label}`",
     "`TOP ${picks.length} nationwide — ${gaMeta.label}`"),
    ("' · um por UF, varredura nacional das 27 unidades da federação'",
     "' · one per state, nationwide sweep of all 27 states'"),
    ("` · faixas mínimas: CPC≥${thresholds.cpcMin}, ENADE≥${thresholds.enadeMin}, "
     "IDD≥${thresholds.iddMin}`",
     "` · minimum bands: CPC≥${thresholds.cpcMin}, ENADE≥${thresholds.enadeMin}, "
     "IDD≥${thresholds.iddMin}`"),
    ("'IDD (cont)'", "'IDD (cont.)'"),
    ("'ENADE (cont)'", "'ENADE (cont.)'"),
    ("'CPC (cont)'", "'CPC (cont.)'"),
    ("`IES: ${c.ie || '—'}`", "`Institution: ${c.ie || '—'}`"),
    ("`Município: ${c.mu || '—'}`", "`Municipality: ${c.mu || '—'}`"),
    ("`Faixa CPC: ${c.pf || '—'}`", "`CPC band: ${c.pf || '—'}`"),
    ("`Categoria: ${c.ct || '—'}`", "`Type: ${c.ct || '—'}`"),
    ("`Comparativo: ${area}`", "`Comparison: ${area}`"),
    ("'⚠ Ciclos ENADE diferentes entre os cursos — veja legenda abaixo do gráfico'",
     "'⚠ Different ENADE cycles across programmes — see the note below the chart'"),
    ("'Curso (SIGLA / UF / ano de avaliação)'",
     "'Programme (ACRONYM / state / assessment year)'"),
    ("'Pontuação acumulada (CPC + ENADE + IDD)'",
     "'Cumulative score (CPC + ENADE + IDD)'"),
    ("'MAPA-GR — TOP Cursos (melhores / mais baixas)'",
     "'MAPA-GR — TOP programmes (best / lowest)'"),
    ("'<span>MAPA-GR</span> — 🏆 TOP Cursos — melhores e mais baixas'",
     "'<span>MAPA-GR</span> — 🏆 TOP programmes — best and lowest'"),
    ("'Tipo de IES'", "'Institution type'"),
    ("'Ambas marcadas: ranking com todas as IES. Só uma: TOP apenas entre instituições daquele tipo.'",
     "'Both ticked: ranking with every institution. Only one: TOP among institutions of that type only.'"),
]


# ==========================================================================
# Comparador — BLOCOS GRANDES de HTML dentro de template literal do JS.
#
# Ficam numa lista propria porque tem de ser aplicados ANTES das strings
# curtas: varios destes blocos CONTEM os ternarios curtos (`${worst ? 'com os
# menores' : ...}`) que a lista de cima traduz. Se as curtas fossem primeiro, a
# chave do bloco grande nao existiria mais e o gerador pararia.
#
# Por isso os ternarios aparecem INTACTOS dos dois lados de cada par aqui: sao
# strings JS independentes, traduzidas depois pelas entradas curtas.
# ==========================================================================
_BLOCOS_COMPARADOR = [

    # tela inicial do modo TOP
    ('<h2 style="color:#D4AF37;margin-bottom:8px;">TOP Cursos — melhores e mais baixas</h2>\n'
     '    <p>Gere o ranking dos cursos do Brasil para o curso escolhido, ordenado por '
     '<strong>CPC → ENADE → IDD</strong>.</p>\n'
     '    <p style="margin-top:12px;font-size:12px;">\n'
     '        <strong>🏆 TOP 10</strong> / <strong>🔻 TOP 10 mais baixas</strong>: os 10 cursos do país.<br>\n'
     '        <strong>🗺️ TOP 27</strong> / <strong>🔻 TOP 27 mais baixas</strong>: 1 curso (melhor/pior) por estado.\n'
     '    </p>\n'
     '    <p style="margin-top:8px;font-size:12px;">Escolha a <strong>grande área</strong> e o '
     '<strong>curso</strong>; ajuste (opcional) os filtros de <strong>sigla</strong>, '
     '<strong>região</strong> e <strong>UF</strong> — por padrão todos marcados = país inteiro.</p>',

     '<h2 style="color:#D4AF37;margin-bottom:8px;">TOP programmes — best and lowest</h2>\n'
     '    <p>Generate the nationwide ranking for the chosen programme, ordered by '
     '<strong>CPC → ENADE → IDD</strong>.</p>\n'
     '    <p style="margin-top:12px;font-size:12px;">\n'
     '        <strong>🏆 TOP 10</strong> / <strong>🔻 bottom 10</strong>: the 10 programmes in the country.<br>\n'
     '        <strong>🗺️ TOP 27</strong> / <strong>🔻 bottom 27</strong>: one programme (best/worst) per state.\n'
     '    </p>\n'
     '    <p style="margin-top:8px;font-size:12px;">Choose the <strong>broad field</strong> and the '
     '<strong>programme</strong>; optionally adjust the <strong>acronym</strong>, '
     '<strong>region</strong> and <strong>state</strong> filters — everything ticked, the default, '
     'means the whole country.</p>'),

    # aviso de cobertura no seletor de UFs
    ('<strong>${ufsComCursos.size} de ${TODAS_UFS.length} UFs</strong> ofertam este curso.\n'
     '            As <strong>${semOferta}</strong> sem oferta aparecem esmaecidas e não podem ser marcadas —\n'
     '            por isso o <strong>TOP 27 “por estado”</strong> devolve, no máximo,\n'
     '            <strong>${ufsComCursos.size} linha(s)</strong>.',
     '<strong>${ufsComCursos.size} of ${TODAS_UFS.length} states</strong> offer this programme.\n'
     '            The <strong>${semOferta}</strong> that do not are greyed out and cannot be ticked —\n'
     '            which is why the <strong>“per state” TOP 27</strong> returns at most\n'
     '            <strong>${ufsComCursos.size} row(s)</strong>.'),

    # caixa 1: TOP N nacional
    ("ℹ️ <strong>Como é definido este TOP ${N}:</strong> são os ${picks.length} cursos "
     "${worst ? 'com os menores' : 'com os maiores'} valores\n"
     "            <strong>contínuos</strong> de CPC → ENADE → IDD ${escopoTxt}${(filt.tipos && "
     "filt.tipos.length === 1) ? ` (${tipoTxt})` : ''},\n"
     "            independentemente da UF — <strong>pode haver mais de um curso do mesmo estado</strong>.\n"
     "            A classificação usa o <strong>valor contínuo</strong>, não a faixa/nota (1–5):\n"
     "            um curso com <strong>nota 4</strong> pode ficar de fora se houver ao menos ${N} outros com CPC contínuo\n"
     "            ${worst ? 'menor' : 'maior'} — inclusive outros também com nota 4 ou 5.\n"
     "            Para ver ${worst ? 'a menor nota' : 'o melhor curso'} de <strong>cada estado</strong>, "
     "marque <strong>todas as UFs</strong> e use o <strong>TOP 27</strong>.",

     "ℹ️ <strong>How this TOP ${N} is defined:</strong> these are the ${picks.length} programmes "
     "${worst ? 'com os menores' : 'com os maiores'} \n"
     "            <strong>continuous</strong> CPC → ENADE → IDD values ${escopoTxt}${(filt.tipos && "
     "filt.tipos.length === 1) ? ` (${tipoTxt})` : ''},\n"
     "            regardless of state — <strong>the same state may appear more than once</strong>.\n"
     "            The ranking uses the <strong>continuous value</strong>, not the 1–5 band:\n"
     "            a <strong>band-4</strong> programme may be left out if at least ${N} others have a "
     "${worst ? 'menor' : 'maior'} continuous CPC — including others also in band 4 or 5.\n"
     "            To see ${worst ? 'a menor nota' : 'o melhor curso'} in <strong>each state</strong>, "
     "tick <strong>every state</strong> and use the <strong>TOP 27</strong>."),

    # caixa 2: TOP 27 genuinamente um por estado
    ("ℹ️ <strong>Este TOP 27 é “um por estado”:</strong> com <strong>todas as ${cob.habilitadas} "
     "UF(s) com oferta deste curso</strong>\n"
     "            selecionadas, a lista traz ${worst ? 'a menor nota' : 'o melhor curso'} de "
     "<strong>cada</strong> unidade da federação — no máximo\n"
     "            um por estado, mesmo que um mesmo estado tenha vários cursos "
     "${worst ? 'entre as menores notas' : 'entre os melhores'}.\n"
     "            ${cob.habilitadas < TODAS_UFS.length ? `<br><br><strong>Por que são ${picks.length} "
     "e não 27:</strong> este curso é ofertado\n"
     "            em <strong>${cob.habilitadas} das ${TODAS_UFS.length} UFs</strong>. As demais não têm "
     "curso a indicar, então não entram\n"
     "            na lista — o resultado não está truncado.` : ''}\n"
     "            <br><br>\n"
     "            <strong>Se você desmarcar qualquer UF, esta opção muda de significado:</strong> "
     "passa a listar os\n"
     "            <strong>27 cursos ${worst ? 'com as menores notas' : 'mais bem avaliados'} dentre as "
     "UFs marcadas</strong>, e aí\n"
     "            <strong>pode haver mais de um curso do mesmo estado</strong>.",

     "ℹ️ <strong>This TOP 27 really is “one per state”:</strong> with <strong>all "
     "${cob.habilitadas} state(s) that offer this programme</strong>\n"
     "            selected, the list brings ${worst ? 'a menor nota' : 'o melhor curso'} of "
     "<strong>each</strong> state — at most\n"
     "            one per state, even where a single state has several programmes "
     "${worst ? 'entre as menores notas' : 'entre os melhores'}.\n"
     "            ${cob.habilitadas < TODAS_UFS.length ? `<br><br><strong>Why ${picks.length} and not "
     "27:</strong> this programme is offered\n"
     "            in <strong>${cob.habilitadas} of the ${TODAS_UFS.length} states</strong>. The others "
     "have nothing to contribute, so they are\n"
     "            not on the list — the result is not truncated.` : ''}\n"
     "            <br><br>\n"
     "            <strong>Untick any state and this option changes meaning:</strong> it then lists the\n"
     "            <strong>27 programmes ${worst ? 'com as menores notas' : 'mais bem avaliados'} among "
     "the ticked states</strong>, and then\n"
     "            <strong>the same state may appear more than once</strong>."),

    # caixa 3: TOP 27 que NAO e um por estado
    ("ℹ️ <strong>Atenção — este TOP 27 NÃO é “um por estado”:</strong> como <strong>${nUfs} de "
     "${cob.habilitadas} UF(s)</strong>\n"
     "            com oferta estão selecionadas, a lista traz até <strong>27 cursos "
     "${worst ? 'com as menores notas' : 'mais bem avaliados'} dentre essas UFs</strong>,\n"
     "            e <strong>pode haver mais de um curso do mesmo estado</strong> — inclusive todos de "
     "um só, se for lá que estão.\n"
     "            ${picks.length < N ? `<br><br><strong>São ${picks.length} e não 27</strong> porque "
     "esse é o total de cursos no recorte:\n"
     "            as ${nUfs} UF(s) selecionadas têm ${filt.cursos.length} curso(s) com CPC contínuo.` : ''}\n"
     "            <br><br>\n"
     "            Para obter ${worst ? 'a menor nota' : 'o melhor curso'} de <strong>cada</strong> "
     "estado, <strong>marque todas as UFs</strong>\n"
     "            (botão “Todos” no filtro de UF): aí o TOP 27 devolve no máximo um curso por unidade "
     "da federação.",

     "ℹ️ <strong>Careful — this TOP 27 is NOT “one per state”:</strong> since <strong>${nUfs} of "
     "${cob.habilitadas} state(s)</strong>\n"
     "            that offer it are selected, the list brings up to <strong>27 programmes "
     "${worst ? 'com as menores notas' : 'mais bem avaliados'} among those states</strong>,\n"
     "            and <strong>the same state may appear more than once</strong> — all of them from a "
     "single state, if that is where they are.\n"
     "            ${picks.length < N ? `<br><br><strong>There are ${picks.length} and not 27</strong> "
     "because that is the total in the selection:\n"
     "            the ${nUfs} selected state(s) have ${filt.cursos.length} programme(s) with a "
     "continuous CPC.` : ''}\n"
     "            <br><br>\n"
     "            To get ${worst ? 'a menor nota' : 'o melhor curso'} in <strong>each</strong> state, "
     "<strong>tick every state</strong>\n"
     "            (the “All” button in the state filter): the TOP 27 then returns at most one "
     "programme per state."),

    # tabelas e detalhes (dois blocos gemeos: modo TOP e modo comparacao)
    ("<h2>Tabela de indicadores\n            <small>Todos os 8 componentes do CPC por curso</small>",
     "<h2>Indicator table\n            <small>All 8 CPC components for each programme</small>", 2),
    ("<h2>Detalhes das Instituições\n            <small>Informações institucionais de cada curso "
     "ranqueado</small>",
     "<h2>Institution details\n            <small>Institutional information for each ranked "
     "programme</small>"),
    ("<h2>Detalhes das Instituições\n            <small>Informações institucionais de cada curso "
     "comparado</small>",
     "<h2>Institution details\n            <small>Institutional information for each compared "
     "programme</small>"),
    ("f = faixa (1-5). Tipo: Pública (Federal/Estadual/Municipal) ou Privada (demais categorias). "
     "%Dr/Ms/Regime/Infra/Org.Ped são notas padronizadas do CPC.",
     "f = band (1-5). Type: public (federal/state/municipal) or private (all other categories). "
     "%Dr/Ms/Contract/Infra/Teach.org are standardised CPC component scores.", 2),
    ("Código e-MEC da IES: ${c.ci != null ? c.ci : 'n/d'}", "e-MEC institution code: ${c.ci != null ? c.ci : 'n/d'}", 2),
    ("Código e-MEC do curso: ${c.cc != null ? c.cc : 'n/d'}", "e-MEC programme code: ${c.cc != null ? c.cc : 'n/d'}", 2),
    ("Ano da avaliação: ${c.y || 'n/d'}", "Assessment year: ${c.y || 'n/d'}", 2),
    ("Ano de fundação: n/d", "Year founded: n/a"),
]

_BLOCOS_COMPARADOR += [
    # cabecalho do cartao de resultados
    ("<small>Curso: <strong>${area}</strong> · ${gaMeta.label}</small>",
     "<small>Programme: <strong>${area}</strong> · ${gaMeta.label}</small>"),
    ("${picks.length} de ${filt.cursos.length} curso(s) no recorte · ${ordTxt}\n"
     "            <br>Filtros: ${tipoTxt} · ${regTxt} · ${ufTxt}${sigTxt}",
     "${picks.length} of ${filt.cursos.length} programme(s) in the selection · ${ordTxt}\n"
     "            <br>Filters: ${tipoTxt} · ${regTxt} · ${ufTxt}${sigTxt}"),
]

COMPARADOR = _BLOCOS_COMPARADOR + COMPARADOR


# ==========================================================================
# estatisticas.html
#
# Esta pagina escreve acentos de duas formas: ENTIDADES no HTML (&#237;) e
# ESCAPES no JS (á). As chaves abaixo reproduzem a forma exata de cada
# lugar — por isso varias sao r"..." (string crua), para que o \u chegue
# literal ao arquivo em vez de virar o caractere.
# ==========================================================================
ESTATISTICAS = [

    # ------------------------------------------------------------------ <head>
    ("<title>MAPA-GR — Estatísticas da Graduação Brasileira</title>",
     "<title>MAPA-GR — Statistics of Brazilian Undergraduate Education</title>"),
    ('content="Estatísticas descritivas da graduação brasileira a partir dos indicadores '
     'SINAES/INEP (CPC, ENADE, IDD, IGC): distribuições por grande área, UF e organização '
     'acadêmica.">',
     'content="Descriptive statistics of Brazilian undergraduate education from the SINAES/INEP '
     'indicators (CPC, ENADE, IDD, IGC): distributions by broad field, state and academic '
     'organisation.">', 3),
    ('<meta property="og:title" content="MAPA-GR — Estatísticas da Graduação Brasileira">',
     '<meta property="og:title" content="MAPA-GR — Statistics of Brazilian Undergraduate '
     'Education">'),

    # --------------------------------------------------------------- cabecalho
    ('aria-label="Abrir filtros">&#9776;</button>', 'aria-label="Open filters">&#9776;</button>'),
    ("<h1><span>MAPA-GR</span> &#8212; Estat&#237;sticas da Gradua&#231;&#227;o Brasileira</h1>",
     "<h1><span>MAPA-GR</span> &#8212; Statistics of Brazilian Undergraduate Education</h1>"),
    ("            &#8592; Voltar\n", "            &#8592; Back\n"),

    # ------------------------------------------------------------ barra lateral
    ("<h3>&#128202; Filtros de Estat&#237;sticas</h3>", "<h3>&#128202; Statistics filters</h3>"),
    ("Selecione os filtros e clique <strong>Atualizar</strong> para gerar os gr&#225;ficos.</p>",
     "Choose the filters and click <strong>Update</strong> to build the charts.</p>"),
    ("<h3>Grande &#193;rea</h3>", "<h3>Broad field</h3>"),
    ("<h3>Ciclo ENADE</h3>", "<h3>ENADE cycle</h3>"),
    ("<h3>Regi&#227;o</h3>", "<h3>Region</h3>"),
    ('value="N" checked> Norte</label>', 'value="N" checked> North</label>'),
    ('value="NE" checked> Nordeste</label>', 'value="NE" checked> Northeast</label>'),
    ('value="CO" checked> Centro-Oeste</label>', 'value="CO" checked> Central-West</label>'),
    ('value="SE" checked> Sudeste</label>', 'value="SE" checked> Southeast</label>'),
    ('value="S" checked> Sul</label>', 'value="S" checked> South</label>'),
    ("<h3>Tipo de IES</h3>", "<h3>Institution type</h3>"),
    ('value="pub" checked> P&#250;blica</label>', 'value="pub" checked> Public</label>'),
    ('value="priv" checked> Privada</label>', 'value="priv" checked> Private</label>'),
    ("P&#250;blica = Federal/Estadual/Municipal. Privada = demais categorias (c/ e s/ fins, "
     "Comunit&#225;ria/Confessional, Especial).</p>",
     "Public = federal/state/municipal. Private = all other categories (for- and non-profit, "
     "community/confessional, special).</p>"),
    ("<h3>UF (Estado)</h3>", "<h3>State (UF)</h3>"),
    ('cursor:pointer;">Todos</button>', 'cursor:pointer;">All</button>'),
    ('cursor:pointer;">Nenhum</button>', 'cursor:pointer;">None</button>'),
    ("<h3>&#128269; Buscar por sigla da IES</h3>", "<h3>&#128269; Search by institution acronym</h3>"),
    ('<label><input type="checkbox" id="searchEnabled"> Filtrar por sigla</label>',
     '<label><input type="checkbox" id="searchEnabled"> Filter by acronym</label>'),
    ('placeholder="ex: UNB, UFRJ, USP"', 'placeholder="e.g.: UNB, UFRJ, USP"'),
    ('Busca parcial: "UF" encontra UFMT, UFRJ, etc.</p>',
     'Partial match: "UF" finds UFMT, UFRJ, and so on.</p>'),
    ('onclick="atualizar()">Atualizar Estat&#237;sticas</button>',
     'onclick="atualizar()">Update statistics</button>'),
    ('onclick="marcarTodos()">Marcar todos</button>', 'onclick="marcarTodos()">Select all</button>'),
    ('onclick="desmarcarTodos()">Desmarcar todos</button>',
     'onclick="desmarcarTodos()">Clear all</button>'),
    ("<h3>&#128230; Exportar</h3>", "<h3>&#128230; Export</h3>"),
    ('onclick="exportCSV()">Exportar CSV</button>', 'onclick="exportCSV()">Export CSV</button>'),
    ('onclick="exportReport()">Relat&#243;rio TXT</button>',
     'onclick="exportReport()">TXT report</button>'),
    ('margin-top:16px;">&#128200; Painel Principal</button>',
     'margin-top:16px;">&#128200; Main panel</button>'),
    ('margin-top:4px;">? Ajuda / Documenta&#231;&#227;o</button>',
     'margin-top:4px;">? Help / Documentation</button>'),
    ('title="Pedir um ajuste, apontar um dado errado ou sugerir uma melhoria">&#128161; '
     'Sugerir melhoria</button>',
     'title="Ask for a change, report wrong data or suggest an improvement">&#128161; '
     'Suggest an improvement</button>'),
    ('<p id="loadingMsg">Carregando todos os datasets...</p>',
     '<p id="loadingMsg">Loading all datasets...</p>'),

    # ------------------------------------------------------------ JS: estado
    ("'Carregando datasets...'", "'Loading datasets...'"),
    ("'Todos os datasets carregados'", "'All datasets loaded'"),
    ("'<div class=\"card\"><h2>Nenhum dado encontrado</h2><p>Ajuste os filtros na barra "
     "lateral.</p></div>'",
     "'<div class=\"card\"><h2>No data found</h2><p>Adjust the filters in the sidebar.</p></div>'"),
    ("setStatus('Filtro vazio')", "setStatus('No results')"),
    ("'Nada a exportar'", "'Nothing to export'", 2),

    # ------------------------------------------------------- JS: visao geral
    (r"""'<div class="card"><h2>Vis\u00e3o Geral</h2>'""", r"""'<div class="card"><h2>Overview</h2>'"""),
    ("'</div><div class=\"label\">Cursos</div></div>'",
     "'</div><div class=\"label\">Programmes</div></div>'"),
    ("'</div><div class=\"label\">UFs</div></div>'",
     "'</div><div class=\"label\">States</div></div>'"),
    ("'</div><div class=\"label\">Inscritos</div></div>'",
     "'</div><div class=\"label\">Registered</div></div>'"),
    ("'</div><div class=\"label\">Participantes</div></div>'",
     "'</div><div class=\"label\">Sat the exam</div></div>'"),
    (r"""'%</div><div class="label">Taxa Participa\u00e7\u00e3o</div></div>'""",
     r"""'%</div><div class="label">Turnout</div></div>'"""),

    # ------------------------------------------------------------- JS: abas
    (r"""onclick="switchSection(this)">Por \u00c1rea</div>""",
     r'onclick="switchSection(this)">By field</div>'),
    (r"""onclick="switchSection(this)">Por Regi\u00e3o / Estado</div>""",
     r'onclick="switchSection(this)">By region / state</div>'),
    (r'onclick="switchSection(this)">Por Ciclo</div>',
     r'onclick="switchSection(this)">By cycle</div>'),
    (r'onclick="switchSection(this)">Por IES</div>',
     r'onclick="switchSection(this)">By institution</div>'),

    # ------------------------------------------------------ JS: tipo de grafico
    (r"""\'pie\',this)">Pizza</button>""", r"""\'pie\',this)">Pie</button>""", 2),
    (r"""\'bar\',this)">Barras</button>""", r"""\'bar\',this)">Bars</button>""", 2),
    (r"""\'doughnut\',this)">Rosca</button>""", r"""\'doughnut\',this)">Doughnut</button>""", 2),

    # --------------------------------------------------- JS: titulos dos cartoes
    (r"<h2>Cursos por Grande \u00c1rea</h2>", r"<h2>Programmes by broad field</h2>"),
    (r"<h2>Alunos Inscritos por Grande \u00c1rea</h2>", r"<h2>Registered students by broad field</h2>"),
    (r"<h2>Participantes ENADE por Grande \u00c1rea</h2>", r"<h2>ENADE participants by broad field</h2>"),
    (r"<h2>Taxa de Participa\u00e7\u00e3o por Grande \u00c1rea (%)</h2>",
     r"<h2>Turnout by broad field (%)</h2>"),
    (r"<h2>Detalhamento por Grande \u00c1rea</h2>", r"<h2>Breakdown by broad field</h2>"),
    (r"<h2>Cursos por Regi\u00e3o</h2>", r"<h2>Programmes by region</h2>"),
    (r"<h2>Alunos Inscritos por Regi\u00e3o</h2>", r"<h2>Registered students by region</h2>"),
    (r"<h2>Cursos por Estado (UF)</h2>", r"<h2>Programmes by state</h2>"),
    (r"<h2>Alunos Inscritos por Estado (UF)</h2>", r"<h2>Registered students by state</h2>"),
    (r"<h2>Detalhamento por Regi\u00e3o</h2>", r"<h2>Breakdown by region</h2>"),
    (r"<h2>Detalhamento por Estado (UF)</h2>", r"<h2>Breakdown by state</h2>"),
    (r"<h2>Cursos por Ciclo ENADE</h2>", r"<h2>Programmes by ENADE cycle</h2>"),
    (r"<h2>Alunos por Ciclo ENADE</h2>", r"<h2>Students by ENADE cycle</h2>"),
    (r"<h2>Inscritos vs Participantes por Ciclo</h2>", r"<h2>Registered vs. sat, by cycle</h2>"),
    (r"<h2>Detalhamento por Ciclo</h2>", r"<h2>Breakdown by cycle</h2>"),
    (r"<h2>Top 30 IES por N\u00famero de Cursos</h2>", r"<h2>Top 30 institutions by number of programmes</h2>"),
    (r"<h2>Top 30 IES por Alunos Inscritos</h2>", r"<h2>Top 30 institutions by registered students</h2>"),
    (r"<h2>Detalhamento por IES (Top 50)</h2>", r"<h2>Breakdown by institution (top 50)</h2>"),

    # ------------------------------------------------------- JS: tabelas
    (r"<tr><th>Regi\u00e3o</th><th>Cursos</th><th>%</th><th>IES</th><th>Inscritos</th><th>%</th>"
     r"<th>Participantes</th><th>%</th></tr>",
     r"<tr><th>Region</th><th>Progr.</th><th>%</th><th>Inst.</th><th>Registered</th><th>%</th>"
     r"<th>Sat</th><th>%</th></tr>"),
    (r"<tr><th>UF</th><th>Regi\u00e3o</th><th>Cursos</th><th>%</th><th>IES</th><th>Inscritos</th>"
     r"<th>%</th><th>Participantes</th><th>%</th></tr>",
     r"<tr><th>State</th><th>Region</th><th>Progr.</th><th>%</th><th>Inst.</th><th>Registered</th>"
     r"<th>%</th><th>Sat</th><th>%</th></tr>"),
    (r"<tr><th>Ciclo</th><th>Cursos</th><th>IES</th><th>Inscritos</th><th>Participantes</th>"
     r"<th>Taxa Part.</th></tr>",
     r"<tr><th>Cycle</th><th>Progr.</th><th>Inst.</th><th>Registered</th><th>Sat</th>"
     r"<th>Turnout</th></tr>"),
    (r"<tr><th>#</th><th>Sigla</th><th>UFs</th><th>Cursos</th><th>Inscritos</th>"
     r"<th>Participantes</th><th>Taxa</th></tr>",
     r"<tr><th>#</th><th>Acronym</th><th>States</th><th>Progr.</th><th>Registered</th>"
     r"<th>Sat</th><th>Turnout</th></tr>"),

    # --------------------------------------------------- JS: rotulos de tooltip
    ("' cursos | '", "' programmes | '", 2),
    ("' inscritos'", "' registered'", 5),
    ("'Regi\\u00e3o: '", "'Region: '"),
    ("'Participantes: '", "'Sat the exam: '", 2),
    ("'Cursos: '", "'Programmes: '", 2),
    ("'IES: '", "'Institutions: '"),
    ("'UFs: '", "'States: '", 2),
]

# ------------------------------------------------------------------------
# estatisticas: o RELATORIO TXT exportado. Nao aparece na tela, mas e o que a
# pessoa leva embora — e nao tem palavra-funcao portuguesa que o detector de
# sobra pegue, entao so entra aqui se for listado a mao.
# ------------------------------------------------------------------------
ESTATISTICAS += [
    ("' \\u2014 Estat\\u00edsticas \\u2014 '", "' \\u2014 Statistics \\u2014 '"),
    ("' registros exportados em CSV'", "' records exported to CSV'"),
    ("' \\u2014 RELAT\\u00d3RIO DE ESTAT\\u00cdSTICAS'", "' \\u2014 STATISTICS REPORT'"),
    ("'  Gerado em: '", "'  Generated on: '"),
    ("'FILTROS APLICADOS:'", "'FILTERS APPLIED:'"),
    ("'  Grandes \\u00c1reas: '", "'  Broad fields: '"),
    ("'  Ciclos: '", "'  Cycles: '"),
    ("'  Regi\\u00f5es: '", "'  Regions: '"),
    ("' (todas)'", "' (all)'"),
    ("'  Tipo de IES: '", "'  Institution type: '"),
    # aqui o acento vem literal, nao escapado — o arquivo mistura as duas formas
    ("'Pública e Privada'", "'Public and private'"),
    ("t === 'pub' ? 'Pública' : 'Privada'", "t === 'pub' ? 'Public' : 'Private'"),
    ("'  Busca por sigla: \"'", "'  Acronym search: \"'"),
    ("'TOTAIS GERAIS:'", "'OVERALL TOTALS:'"),
    ("'  Cursos: '", "'  Programmes: '"),
    ("'  IES distintas: '", "'  Distinct institutions: '"),
    ("'  Alunos inscritos: '", "'  Students registered: '"),
    ("'  Participantes ENADE: '", "'  ENADE participants: '"),
    ("'  Taxa de participa\\u00e7\\u00e3o: '", "'  Turnout: '"),
    ("'POR GRANDE \\u00c1REA:'", "'BY BROAD FIELD:'"),
    ("'POR REGI\\u00c3O:'", "'BY REGION:'"),
    ("'TOP 10 ESTADOS POR CURSOS:'", "'TOP 10 STATES BY PROGRAMMES:'"),
    ("'TOP 10 IES POR CURSOS:'", "'TOP 10 INSTITUTIONS BY PROGRAMMES:'"),
    ("'POR CICLO ENADE:'", "'BY ENADE CYCLE:'"),
    ("'Fonte: INEP \\u2014 Indicadores de Qualidade da Educa\\u00e7\\u00e3o Superior'",
     "'Source: INEP \\u2014 Higher Education Quality Indicators'"),
    ("'Relat\\u00f3rio salvo: '", "'Report saved: '"),
]


# ==========================================================================
# censo.html — Censo da Educacao Superior.
# Mesma mistura de formas de acento da pagina de estatisticas: entidade no
# HTML, escape \u ou literal no JS. As chaves abaixo foram conferidas contra o
# arquivo uma a uma pela contagem.
# ==========================================================================
CENSO = [
    # ------------------------------------------------------------------ <head>
    ("<title>MAPA-GR — Censo da Educação Superior 2017-2023</title>",
     "<title>MAPA-GR — Higher Education Census 2017-2023</title>"),

    # --------------------------------------------------------------- cabecalho
    ('aria-label="Abrir filtros">&#9776;</button>', 'aria-label="Open filters">&#9776;</button>'),
    ("<h1><span>MAPA-GR</span> &#8212; Censo da Educa&#231;&#227;o Superior 2017-2023</h1>",
     "<h1><span>MAPA-GR</span> &#8212; Higher Education Census 2017-2023</h1>"),
    ("            &#8592; Voltar\n", "            &#8592; Back\n"),

    # ------------------------------------------------------------ barra lateral
    ("<h3>&#128196; Censo INEP</h3>", "<h3>&#128196; INEP Census</h3>"),
    ("Fonte: <strong>Portal INEP &#8212; Microdados do Censo da Educa&#231;&#227;o Superior</strong> "
     "(2017, 2021, 2022, 2023). Agregados nacionais, por regi&#227;o, UF, &#225;rea e IES.</p>",
     "Source: <strong>INEP portal &#8212; Higher Education Census microdata</strong> "
     "(2017, 2021, 2022, 2023). Aggregated nationally and by region, state, field and "
     "institution.</p>"),
    ("<h3>Ano de refer&#234;ncia</h3>", "<h3>Reference year</h3>"),
    ('value="2023" checked> 2023 (mais recente)</label>',
     'value="2023" checked> 2023 (most recent)</label>'),
    ("Na aba <em>Evolu&#231;&#227;o</em> todos os anos s&#227;o exibidos simultaneamente.</p>",
     "The <em>Trend</em> tab shows every year at once.</p>"),
    ("<h3>M&#233;trica principal</h3>", "<h3>Main metric</h3>"),
    ('<option value="mat" selected>Matr&#237;culas ativas</option>',
     '<option value="mat" selected>Active enrolments</option>'),
    ('<option value="ing">Ingressantes</option>', '<option value="ing">New entrants</option>'),
    ('<option value="con">Concluintes</option>', '<option value="con">Graduates</option>'),
    ('<option value="vg">Vagas ofertadas</option>', '<option value="vg">Places offered</option>'),
    ('<option value="insc">Inscritos no processo seletivo</option>',
     '<option value="insc">Applicants</option>'),
    ('<option value="mat_pcd">Matr&#237;culas &#8212; PCD</option>',
     '<option value="mat_pcd">Enrolments &#8212; students with disabilities</option>'),
    ('<option value="mat_fies">Matr&#237;culas &#8212; FIES</option>',
     '<option value="mat_fies">Enrolments &#8212; FIES student loan</option>'),
    ('<option value="mat_prouni_i">Matr&#237;culas &#8212; PROUNI Integral</option>',
     '<option value="mat_prouni_i">Enrolments &#8212; PROUNI full scholarship</option>'),
    ('<option value="mat_prouni_p">Matr&#237;culas &#8212; PROUNI Parcial</option>',
     '<option value="mat_prouni_p">Enrolments &#8212; PROUNI partial scholarship</option>'),
    ('<option value="mat_rv">Matr&#237;culas &#8212; Reserva de vagas (cotas)</option>',
     '<option value="mat_rv">Enrolments &#8212; affirmative-action quotas</option>'),
    ('<option value="sit_tra">Situa&#231;&#227;o &#8212; Trancada</option>',
     '<option value="sit_tra">Status &#8212; suspended</option>'),
    ('<option value="sit_des">Situa&#231;&#227;o &#8212; Desvinculada</option>',
     '<option value="sit_des">Status &#8212; dropped out</option>'),
    ("<h3>Grande &#193;rea</h3>", "<h3>Broad field</h3>"),
    ("<h3>Modalidade</h3>", "<h3>Delivery mode</h3>"),
    ('class="mod-chk" value="1" checked> Presencial</label>',
     'class="mod-chk" value="1" checked> On campus</label>'),
    ('class="mod-chk" value="2" checked> EAD</label>',
     'class="mod-chk" value="2" checked> Distance learning</label>'),
    ("<h3>Grau Acad&#234;mico</h3>", "<h3>Degree type</h3>"),
    ('class="grau-chk" value="1" checked> Bacharelado</label>',
     'class="grau-chk" value="1" checked> Bachelor</label>'),
    ('class="grau-chk" value="2" checked> Licenciatura</label>',
     'class="grau-chk" value="2" checked> Teaching degree</label>'),
    ('class="grau-chk" value="3" checked> Tecnol&#243;gico</label>',
     'class="grau-chk" value="3" checked> Technologist</label>'),
    ('class="grau-chk" value="4" checked> &#193;rea b&#225;sica</label>',
     'class="grau-chk" value="4" checked> Basic-cycle programme</label>'),
    ("<h3>Regi&#227;o</h3>", "<h3>Region</h3>"),
    ('class="reg-chk" value="N" checked> Norte</label>',
     'class="reg-chk" value="N" checked> North</label>'),
    ('class="reg-chk" value="NE" checked> Nordeste</label>',
     'class="reg-chk" value="NE" checked> Northeast</label>'),
    ('class="reg-chk" value="CO" checked> Centro-Oeste</label>',
     'class="reg-chk" value="CO" checked> Central-West</label>'),
    ('class="reg-chk" value="SE" checked> Sudeste</label>',
     'class="reg-chk" value="SE" checked> Southeast</label>'),
    ('class="reg-chk" value="S" checked> Sul</label>',
     'class="reg-chk" value="S" checked> South</label>'),
    ('cursor:pointer;">Todos</button>', 'cursor:pointer;">All</button>'),
    ('cursor:pointer;">Nenhum</button>', 'cursor:pointer;">None</button>'),
    ("<h3>Categoria Administrativa</h3>", "<h3>Administrative category</h3>"),
    ('class="cat-chk" value="1" checked> P&#250;blica Federal</label>',
     'class="cat-chk" value="1" checked> Federal public</label>'),
    ('class="cat-chk" value="2" checked> P&#250;blica Estadual</label>',
     'class="cat-chk" value="2" checked> State public</label>'),
    ('class="cat-chk" value="3" checked> P&#250;blica Municipal</label>',
     'class="cat-chk" value="3" checked> Municipal public</label>'),
    ('class="cat-chk" value="4" checked> Privada c/ fins</label>',
     'class="cat-chk" value="4" checked> Private for-profit</label>'),
    ('class="cat-chk" value="5" checked> Privada s/ fins</label>',
     'class="cat-chk" value="5" checked> Private non-profit</label>'),
    ('class="cat-chk" value="7" checked> Especial</label>',
     'class="cat-chk" value="7" checked> Special</label>'),
    ("<h3>&#128269; Buscar por sigla da IES</h3>", "<h3>&#128269; Search by institution acronym</h3>"),
    ('<label><input type="checkbox" id="searchEnabled"> Filtrar por sigla</label>',
     '<label><input type="checkbox" id="searchEnabled"> Filter by acronym</label>'),
    ('placeholder="ex: USP, UFRJ, UNB"', 'placeholder="e.g.: USP, UFRJ, UNB"'),
    ('onclick="atualizar()">Atualizar Estat&#237;sticas</button>',
     'onclick="atualizar()">Update statistics</button>'),
    ('onclick="marcarTodos()">Marcar todos</button>', 'onclick="marcarTodos()">Select all</button>'),
    ('onclick="desmarcarTodos()">Desmarcar todos</button>',
     'onclick="desmarcarTodos()">Clear all</button>'),
    ("<h3>&#128230; Exportar</h3>", "<h3>&#128230; Export</h3>"),
    ('onclick="exportCSV()">Exportar CSV</button>', 'onclick="exportCSV()">Export CSV</button>'),
    ('onclick="exportReport()">Relat&#243;rio TXT</button>',
     'onclick="exportReport()">TXT report</button>'),
    ('onclick="exportPNGs()" style="background:#FF9800;">Gr&#225;ficos PNG</button>',
     'onclick="exportPNGs()" style="background:#FF9800;">Charts as PNG</button>'),
    ('margin-top:16px;">&#128200; Painel Principal</button>',
     'margin-top:16px;">&#128200; Main panel</button>'),
    ('margin-top:4px;">? Ajuda / Documenta&#231;&#227;o</button>',
     'margin-top:4px;">? Help / Documentation</button>'),
    ('title="Pedir um ajuste, apontar um dado errado ou sugerir uma melhoria">&#128161; '
     'Sugerir melhoria</button>',
     'title="Ask for a change, report wrong data or suggest an improvement">&#128161; '
     'Suggest an improvement</button>'),
    ('<p id="loadingMsg">Carregando dados do Censo da Educa&#231;&#227;o Superior...</p>',
     '<p id="loadingMsg">Loading Higher Education Census data...</p>'),

    # -------------------------------------------------------- JS: metricas
    (r"'Matr\u00edculas ativas'", "'Active enrolments'"),
    ("'Vagas ofertadas'", "'Places offered'"),
    (r"'Matr\u00edculas \u2014 PCD'", "'Enrolments — with disabilities'"),
    (r"'Matr\u00edculas \u2014 FIES'", "'Enrolments — FIES'"),
    (r"'Matr\u00edculas \u2014 PROUNI Integral'", "'Enrolments — PROUNI full'"),
    (r"'Matr\u00edculas \u2014 PROUNI Parcial'", "'Enrolments — PROUNI partial'"),
    (r"'Matr\u00edculas \u2014 Reserva de vagas'", "'Enrolments — quotas'"),
    (r"'Situa\u00e7\u00e3o \u2014 Trancada'", "'Status — suspended'"),
    (r"'Situa\u00e7\u00e3o \u2014 Desvinculada'", "'Status — dropped out'"),
    (r"'Matr\u00edculas \u2014 60+ anos'", "'Enrolments — aged 60+'"),
    (r"'\u00c1rea b\u00e1sica'", "'Basic-cycle programme'"),
    (r"'P\u00fablica Federal'", "'Federal public'"),
    (r"'P\u00fablica Estadual'", "'State public'"),
    (r"'P\u00fablica Municipal'", "'Municipal public'"),
    ("'Privada c/ fins lucrativos'", "'Private for-profit'"),
    ("'Privada s/ fins lucrativos'", "'Private non-profit'"),

    # -------------------------------------------------------- JS: telas e abas
    ('<div class="card"><h2>Nenhum dado encontrado</h2><p>Ajuste os filtros na barra lateral.</p></div>',
     '<div class="card"><h2>No data found</h2><p>Adjust the filters in the sidebar.</p></div>'),
    ("'Filtro vazio'", "'No results'"),
    (r'<div class="card"><h2>Vis\u00e3o Geral &#8212; Censo ',
     '<div class="card"><h2>Overview &#8212; Census '),
    (r'</div><div class="label">Matr\u00edculas</div></div>',
     '</div><div class="label">Enrolments</div></div>'),
    ('</div><div class="label">Ingressantes</div></div>',
     '</div><div class="label">New entrants</div></div>'),
    ('</div><div class="label">Concluintes</div></div>',
     '</div><div class="label">Graduates</div></div>'),
    ('</div><div class="label">Vagas</div></div>', '</div><div class="label">Places</div></div>'),
    ('</div><div class="label">Inscritos</div></div>',
     '</div><div class="label">Applicants</div></div>'),
    ("' (filtro)</div></div>'", "' (filtered)</div></div>'"),
    (r"'. Ano de refer\u00eancia: <strong>'", "'. Reference year: <strong>'"),
    (r'onclick="switchSection(this)">&#128200; Evolu\u00e7\u00e3o 2017-2023</div>',
     'onclick="switchSection(this)">&#128200; Trend 2017-2023</div>'),
    (r'onclick="switchSection(this)">Por \u00c1rea</div>', 'onclick="switchSection(this)">By field</div>'),
    (r'onclick="switchSection(this)">Por Regi\u00e3o / UF</div>',
     'onclick="switchSection(this)">By region / state</div>'),
    ('onclick="switchSection(this)">Grau / Modalidade</div>',
     'onclick="switchSection(this)">Degree / mode</div>'),
    ('onclick="switchSection(this)">Demografia</div>',
     'onclick="switchSection(this)">Demographics</div>'),
    (r'onclick="switchSection(this)">Inclus\u00e3o / Financiamento</div>',
     'onclick="switchSection(this)">Inclusion / funding</div>'),
    ('onclick="switchSection(this)">Cat. Administrativa</div>',
     'onclick="switchSection(this)">Admin. category</div>'),

    # -------------------------------------------------------- JS: cartoes
    (r'<div class="card"><h2>Evolu\u00e7\u00e3o nacional &#8212; ',
     '<div class="card"><h2>National trend &#8212; '),
    (r"<h2>Crescimento total 2017\u21922023 (principais m\u00e9tricas)</h2>",
     '<h2>Total growth 2017→2023 (main metrics)</h2>'),
    (r"<h2>CAGR 2017\u21922023 (principais m\u00e9tricas)</h2>", '<h2>CAGR 2017→2023 (main metrics)</h2>'),
    ('<div class="card"><h2>Totais nacionais por ano</h2>',
     '<div class="card"><h2>National totals by year</h2>'),
    (r"""setChartType(\'pie\', this)">Pizza</button>""", r"""setChartType(\'pie\', this)">Pie</button>"""),
    (r"""setChartType(\'bar\', this)">Barras</button>""", r"""setChartType(\'bar\', this)">Bars</button>"""),
    (r"""setChartType(\'doughnut\', this)">Rosca</button>""",
     r"""setChartType(\'doughnut\', this)">Doughnut</button>"""),
    (r"' por Grande \u00c1rea</h2>'", "' by broad field</h2>'"),
    (r"<h2>Crescimento 2017\u21922023 por Grande \u00c1rea (matr\u00edculas)</h2>",
     '<h2>Growth 2017→2023 by broad field (enrolments)</h2>'),
    (r'<div class="card"><h2>Detalhamento por Grande \u00c1rea &#8212; ',
     '<div class="card"><h2>Breakdown by broad field &#8212; '),
    (r"' por Regi\u00e3o</h2>'", "' by region</h2>'"),
    ("' por UF</h2>'", "' by state</h2>'"),
    (r'<div class="card"><h2>Detalhamento por Regi\u00e3o &#8212; ',
     '<div class="card"><h2>Breakdown by region &#8212; '),
    ('<div class="card"><h2>Detalhamento por UF &#8212; ',
     '<div class="card"><h2>Breakdown by state &#8212; '),
    ("' por Modalidade</h2>'", "' by delivery mode</h2>'"),
    ("' por Grau</h2>'", "' by degree type</h2>'"),
    (r'<div class="card"><h2>Evolu\u00e7\u00e3o Presencial vs EAD (matr\u00edculas)</h2>',
     '<div class="card"><h2>On campus vs. distance learning (enrolments)</h2>'),
    (r'<div class="card"><h2>Grau \u00d7 Modalidade &#8212; ',
     '<div class="card"><h2>Degree × mode &#8212; '),
    (r"<h2>G\u00eanero (matr\u00edculas ativas)</h2>", '<h2>Gender (active enrolments)</h2>'),
    (r"<h2>Cor / Ra\u00e7a (matr\u00edculas ativas)</h2>", '<h2>Colour / race (active enrolments)</h2>'),
    (r'<div class="card"><h2>Faixa et\u00e1ria das matr\u00edculas ativas</h2>',
     '<div class="card"><h2>Age range of active enrolments</h2>'),
    (r'<div class="card"><h2>Matr\u00edculas por turno (presencial)</h2>',
     '<div class="card"><h2>Enrolments by time of day (on campus)</h2>'),
    (r"<h2>Evolu\u00e7\u00e3o FIES &#8212; matr\u00edculas 2017\u21922023</h2>",
     '<h2>FIES trend &#8212; enrolments 2017→2023</h2>'),
    (r"<h2>Evolu\u00e7\u00e3o PROUNI &#8212; matr\u00edculas 2017\u21922023</h2>",
     '<h2>PROUNI trend &#8212; enrolments 2017→2023</h2>'),
    ('<h2>Reserva de vagas (cotas) por tipo &#8212; ',
     '<h2>Affirmative-action quotas by type &#8212; '),
    (r"<h2>Matr\u00edculas PCD 2017\u21922023</h2>", '<h2>Enrolments of students with disabilities 2017→2023</h2>'),
    (r'<div class="card"><h2>Top 30 IES por matr\u00edculas &#8212; ',
     '<div class="card"><h2>Top 30 institutions by enrolments &#8212; '),
    ('<div class="card"><h2>Detalhamento Top 50 IES</h2>',
     '<div class="card"><h2>Breakdown of the top 50 institutions</h2>'),
    (r"<h2>Matr\u00edculas por Categoria Administrativa</h2>",
     '<h2>Enrolments by administrative category</h2>'),
    (r"<h2>Evolu\u00e7\u00e3o P\u00fablica vs Privada 2017\u21922023</h2>",
     '<h2>Public vs. private 2017→2023</h2>'),
    ('<div class="card"><h2>Detalhamento por Categoria &#8212; ',
     '<div class="card"><h2>Breakdown by category &#8212; '),

    # -------------------------------------------------------- JS: rotulos
    (r"' matr\u00edculas | '", "' enrolments | '"),
    ("' ingress. | '", "' entrants | '"),
    ("' concl.'", "' graduates'"),
    (r"'Varia\u00e7\u00e3o total (%)'", "'Total change (%)'"),
    ("'CAGR (% a.a.)'", "'CAGR (% p.a.)'"),
    ("'PROUNI Integral'", "'PROUNI full'"),
    ("'PROUNI Parcial'", "'PROUNI partial'"),
    (r"'Cotas \u00c9tnico-raciais'", "'Ethnic/racial quotas'"),
    (r"'Escola P\u00fablica'", "'State-school quota'"),
    ("'Social / Renda'", "'Social / income quota'"),
    (r"'Matr\u00edculas PCD'", "'Enrolments with disabilities'"),
    ("'Ingressantes: '", "'New entrants: '"),
    ("'Concluintes: '", "'Graduates: '"),
    ("'Nada a exportar'", "'Nothing to export'", 2),
    ("' linhas exportadas'", "' rows exported'"),
    ("'Relatório TXT salvo'", "'TXT report saved'"),
    ("'Nenhum gráfico para exportar'", "'No chart to export'"),
    ("' gráficos exportados'", "' charts exported'"),

    # -------------------------------------------------------- JS: relatorio TXT
    ("'  MAPA-GR — CENSO DA EDUCAÇÃO SUPERIOR'", "'  MAPA-GR — HIGHER EDUCATION CENSUS'"),
    ("'  Gerado em: '", "'  Generated on: '"),
    ("'  Fonte: INEP — Microdados (download.inep.gov.br)'",
     "'  Source: INEP — microdata (download.inep.gov.br)'"),
    ("'FILTROS APLICADOS:'", "'FILTERS APPLIED:'"),
    ("'  Ano: '", "'  Year: '"),
    ("'  Métrica principal: '", "'  Main metric: '"),
    ("'  Grandes áreas: '", "'  Broad fields: '"),
    ("'  Modalidades: '", "'  Delivery modes: '"),
    ("'  Graus: '", "'  Degree types: '"),
    ("'  Regiões: '", "'  Regions: '"),
    ("' selecionada(s)'", "' selected'"),
    ("'  Categorias administrativas: '", "'  Administrative categories: '"),
    ("'  Busca IES: \"'", "'  Institution search: \"'"),
    ("'TOTAIS (FILTRO):'", "'TOTALS (FILTERED):'"),
    ("'  Matrículas: '", "'  Enrolments: '"),
    ("'  Ingressantes: '", "'  New entrants: '"),
    ("'  Concluintes: '", "'  Graduates: '"),
    ("'  Vagas ofertadas: '", "'  Places offered: '"),
    ("'  Inscritos: '", "'  Applicants: '"),
    ("'TOTAIS NACIONAIS POR ANO (sem filtros):'", "'NATIONAL TOTALS BY YEAR (unfiltered):'"),
    ("'CRESCIMENTO 2017 → 2023 (totais nacionais):'", "'GROWTH 2017 → 2023 (national totals):'"),
    ("' a.a.'", "' p.a.'"),
    ("'POR GRANDE ÁREA ('", "'BY BROAD FIELD ('"),
    ("'POR REGIÃO ('", "'BY REGION ('"),
    ("'TOP 10 UFs POR MATRÍCULAS ('", "'TOP 10 STATES BY ENROLMENTS ('"),
    ("'DEMOGRAFIA ('", "'DEMOGRAPHICS ('"),
    ("'  Gênero — F: '", "'  Gender — F: '"),
    ("'  Cor/Raça:'", "'  Colour/race:'"),
    ("'    Branca:    '", "'    White:     '"),
    ("'    Preta:     '", "'    Black:     '"),
    ("'    Parda:     '", "'    Mixed:     '"),
    ("'    Amarela:   '", "'    Asian:     '"),
    ("'    Indígena:  '", "'    Indigenous:'"),
    ("'  Reserva de vagas (cotas): '", "'  Affirmative-action quotas: '"),
    ("'Fonte: INEP — Portal de Dados Abertos'", "'Source: INEP — Open Data Portal'"),
]


# ==========================================================================
# help-doc.html — so o cabecalho e a navegacao entram aqui.
# O CORPO do documento nao e traduzido por esta tabela: e texto longo, tratado
# secao a secao pelos arquivos de i18n/doc_en/ (ver secoes_de_documento no
# gerador). Fatiar prosa em centenas de pares seria ilegivel e quebradico.
# ==========================================================================
HELP_DOC = [
    ("<title>MAPA-GR v2.8.2 — Documentação e Fontes de Dados</title>",
     "<title>MAPA-GR v2.8.2 — Documentation and Data Sources</title>"),
    ('content="Documentação do MAPA-GR: metodologia, glossário dos indicadores do SINAES '
     '(CPC, ENADE, IDD, IGC) e fontes de dados públicas do INEP.">',
     'content="MAPA-GR documentation: methodology, a glossary of the SINAES indicators '
     '(CPC, ENADE, IDD, IGC) and INEP public data sources.">', 3),
    ('<meta property="og:title" content="MAPA-GR — Documentação e Fontes de Dados">',
     '<meta property="og:title" content="MAPA-GR — Documentation and Data Sources">'),
    ("<h1><em>MAPA-GR</em> — Documentação v2.8.2</h1>",
     "<h1><em>MAPA-GR</em> — Documentation v2.8.2</h1>"),
    ("<div>v2.8.2 — Agosto 2026</div>", "<div>v2.8.2 — August 2026</div>"),
    ("            ← Voltar\n", "            ← Back\n"),
    ('id="nav-sobre">Sobre</a>', 'id="nav-sobre">About</a>'),
    ('id="nav-areas">Grandes Áreas</a>', 'id="nav-areas">Broad fields</a>'),
    ('id="nav-uso">Como Usar</a>', 'id="nav-uso">How to use</a>'),
    ('id="nav-indicadores">Indicadores SINAES</a>', 'id="nav-indicadores">SINAES indicators</a>'),
    ('id="nav-cpc-censo">CPC × Censo</a>', 'id="nav-cpc-censo">CPC × Census</a>'),
    ('id="nav-fontes">Fontes de Dados</a>', 'id="nav-fontes">Data sources</a>'),
    ('id="nav-stats">Estatísticas</a>', 'id="nav-stats">Statistics</a>'),
    ('id="nav-versoes">Versões</a>', 'id="nav-versoes">Versions</a>'),
]
