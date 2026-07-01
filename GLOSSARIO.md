Glossario do dataset - mapa-gr (dados_inep.json)

Fonte: INEP - Dados Abertos (Indicadores de Qualidade da Educacao Superior).

Cada campo de cursos e uma chave abreviada; o proprio JSON traz o dicionario no bloco legend. Granularidade da linha = um curso em um ciclo (curso x ano).


Estrutura de topo (4 blocos)

metadata    Cabecalho de geracao (fonte, area, ciclos, contagens, data).
legend      Dicionario chave-significado (o glossario embutido).
ies_list    Lista de IES presentes (apoio aos filtros do app).
cursos      Array de registros curso x ciclo; cada registro tem os campos abaixo.


metadata - campos

fonte       Origem dos dados (INEP - Dados Abertos).
portal      URL do portal de dados abertos do INEP.
area        Areas de avaliacao cobertas (ex.: FISICA LICENCIATURA + BACHARELADO).
ciclos      Anos dos ciclos ENADE incluidos (ex.: 2017, 2021).
n_cursos    Total de registros curso x ciclo no arquivo.
n_ies       Total de IES distintas.
ufs         Lista de UFs presentes.
gerado_em   Data e hora de geracao do dataset.


cursos - identificacao do curso e IES

y     ano do ciclo ENADE (ex.: 2017, 2021)
ar    area de avaliacao (ex.: FISICA BACHARELADO)
g     grau academico (Bacharelado, Licenciatura, Tecnologico)
ci    codigo da IES (INEP)
ie    nome da IES
sg    sigla da IES
o     organizacao academica (Universidade, Centro Universitario, Faculdade)
ct    categoria administrativa (Publica Federal, Privada, Estadual)
cc    codigo do curso no e-MEC
m     modalidade de ensino (Presencial, EaD)
mu    municipio do curso
u     UF (sigla da unidade federativa)


cursos - participacao na prova

ni    numero de concluintes inscritos no ENADE
np    numero de concluintes participantes (efetivamente avaliados)


cursos - desempenho na prova (compoem o Conceito ENADE)

fg    nota bruta de Formacao Geral (FG) - peso 25 por cento no ENADE
ce    nota bruta de Componente Especifico (CE) - peso 75 por cento no ENADE
e     Conceito ENADE continuo - resultante de FG mais CE

O Conceito ENADE nao inclui questionario; e so prova.


cursos - IDD (Indicador de Diferenca entre Desempenhos Observado e Esperado)

ib    IDD - nota bruta
ip    IDD - nota padronizada (z-score por area; entra no CPC)


cursos - componentes do Questionario do Estudante (percepcao dos concluintes)

Estes 3 campos vem do questionario do ENADE.

op    Organizacao Didatico-Pedagogica (padronizada) - percepcao do estudante
nf    Infraestrutura e Instalacoes Fisicas (padronizada) - percepcao do estudante
of    Oportunidade de Ampliacao da Formacao (padronizada) - percepcao do estudante


cursos - corpo docente (insumos do CPC)

nd    numero de docentes
ms    proporcao de mestres (padronizada)
dr    proporcao de doutores (padronizada)
rg    regime de trabalho (padronizada)


cursos - indicadores consolidados

pc    CPC - Conceito Preliminar de Curso (continuo)
pf    CPC - faixa (1 a 5) - nota oficial divulgada do curso
igc_f IGC da IES - faixa (1 a 5) - indice da instituicao, nao do curso


Previstos no legend mas nao materializados nos registros

igc_c IGC da IES (continuo) - chave prevista pelo gerador, mas nenhum curso do arquivo atual a possui


Notas de interpretacao

padronizada = valor convertido em z-score dentro da area de avaliacao (media 0, desvio 1); e a forma como o componente entra no calculo do CPC.

Composicao do CPC = desempenho na prova (fg, ce), IDD (ip), corpo docente (ms, dr, rg) e os 3 itens do questionario do estudante (op, nf, of).

Conceito ENADE (e) nao e igual ao CPC (pc, pf): o primeiro e so prova; o segundo agrega prova mais docentes mais questionario.

Fontes brutas dos campos estao em mapa-gr/dados_inep/ (conceito_enade_AAAA, CPC_AAAA, IDD_AAAA, IGC_AAAA em xlsx); o dados_inep.json e gerado por gerar_mapa_gr.py e gerar_mapa_gr_multi.py.
