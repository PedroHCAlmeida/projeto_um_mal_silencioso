# Projeto Um Mal Silencioso🧫
[![Made withJupyter](https://img.shields.io/badge/Made%20with-Jupyter-orange?style=flat-square&logo=Jupyter)](https://jupyter.org/try) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg?style=flat-square)](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/edit/main/LICENSE)
![Alt text](https://veja.abril.com.br/wp-content/uploads/2017/02/hepatite-c-virus-ilustracao.jpg)
# Introdução 📜

Olá, meu nome é Pedro Henrique, e esse é meu repositório referente ao projeto final do módulo 2 do [Bootcamp De Data Science Aplicada](https://www.alura.com.br/bootcamp/data-science-aplicada/matriculas-abertas) promovido pela [Alura](https://www.alura.com.br/) sobre Visualização de dados com Seaborn e Matplotlib.O objetivo desse projeto foi utilizar dados do [Projeto Nacional de Imunização(PNI)](http://tabnet.datasus.gov.br/cgi/tabcgi.exe?pni/cnv/cpniuf.def) em conjunto com outras bases de dados a fim de contar uma história com esses dados, eu optei por explorar os dados sobre a vacinação contra a hepatite e analisar os casos e óbitos no Brasil a partir de [dados do SUS](https://datasus.saude.gov.br/informacoes-de-saude-tabnet/)(Sistema Único de Saúde).

# Hepatites🦠

## O que são as Hepatites 💭

A palavra hepatite vem do Grego “HEPAR”, que significa “fígado”, e a terminação “ITIS” foi adotada pelo linguajar médico para designar _**“doença inflamatória”**_, ou seja, uma hepatite é uma doença inflamatória que ataca o fígado e podem ser causadas por alguns remédios, álcool e outras drogas, doenças autoimunes, metabólicas e genéticas, porém nesse projeto o foco são as hepatites virais, que são aquelas infecções causadas por vírus.

## Qual a importância do fígado 📑

O fígado é é considerado um dos maiores órgãos do corpo humano, ele é responsável por diversas funções cruciais para o corpo humano, tais como a síntese da maioria das proteínas produzidas no corpo, armazenamento de vitaminas e minerais, degradação de hormônios, armazenamento de substâncias, como o glicogênio, além disso ele produz a bile, que desempenha, principalmente, um papel na excreção de substâncias tóxicas e na absorção de gorduras e vitaminas lipossolúveis, quebrando as moléculas de gorduras em ácidos graxos, que são mais facilmente absorvidos no intestino delgado.

## Hepatites Virais 🧫

Vários vírus podem causar quadros de inflamação do fígado, ou seja, hepatite. Porém, as chamadas hepatites virais são apenas aquelas causadas por _**vírus que atacam preferencialmente o fígado**_, portanto, até hoje foram descobertas 5 hepatites virais causadas por diferentes vírus, sendo elas a Hepatite A, B, C, D e E, porém as duas últimas(D e E) não são tão comuns no Brasil e portanto nesse projeto o foco será na _**hepatite A, B e C**_.

## Hepatite A 🅰️

Causada pelo vírus A (HAV) da hepatite, a hepatite A ,na maioria dos casos, é uma doença de caráter benigno e raramente provoca hepatite crônica, contudo sua letalidade aumenta com a idade podendo provocar sintomas de hepatite aguda em pessoas mais velhas. Sua transmissão é fecal-oral, por contato entre indivíduos ou por meio de água ou alimentos contaminados pelo vírus.
A hepatite A possui _**cura**_ e existe _**vacina**_, a mesma é eficaz em cerca de 95% dos casos, dura pelo menos quinze anos e, possivelmente, a vida inteira da pessoa.

## Hepatite B 🅱️

A hepatite B, transmitida pelo vírus B(HBV), tem um risco maior que a hepatite A de desenvolver a _**hepatite crônica**_ , que a longo prazo pode acarretar diversos problemas como cirrose, falência hepática e câncer hepático, esse risco aumenta ainda mais em pessoas com a idade mais avançada, alto consumo de álcool, tabagismo e imunossupressão.A hepatite B é transmitida habitualmente por contato sexual, transfusão sanguínea ou por agulhas contaminadas, podendo ocorrer até em tatuagens, piercings e acupuntura.

O maior problema da hepatite B é que 5 a 10% das pessoas nunca se curam pois desenvolvem a doença crônica, e outro fator que agrava mais a situação é que por nem sempre apresentarem sintomas, grande parte das pessoas _**desconhecem ter a infecção**_. Isso faz com que a doença possa evoluir por décadas sem o devido diagnóstico.Além disso por mais que a hepatite B possua esses riscos, atualmente existe a _**vacina**_ e faz parte do calendário básico do Projeto Nacional de Imunização(PNI) oferecido pelo Sistema Único de Saúde(SUS), e portanto é de extrema importância essa vacinação desde criança. 

## Hepatite C 👀

A hepatite C, causada pelo vírus C(HCV), é a _**maior causa de doença crônica do fígado**_, sua transmissão ocorre por meio de compartilhamento de agulhas, objetos cortantes(podendo ser equipamentos médicos, tatuagem, piercing e até alicate de unha), além da transmissão na gestação da mãe para o filho. A grande tragédia da hepatite C é que seu vírus só foi reconhecido no início da década de 1990 e por mais que exista tratamento,  até os dias atuais _**não existe uma vacina**_ contra esse vírus, ou seja, ninguém está livre de contrair o vírus.

Além disso o maior problema da hepatite C é que como ela evolui muito facilmente para fase crônica e ela não costuma apresentar sintomas agressivos, _**a maior parte das pessoas desconhecem sua infecção**_ e demoram para descobrir-la ,logo esse vírus permanece atacando o fígado da pessoa podendo evoluir para cirrose hepática, carcinoma hepatocelular (CHC), descompensação hepática, podendo ser fatal.

## Mal Silencioso 🐱‍👤

Por todas essas razões citadas as hepatites atacam o fígado muitas vezes silenciosamente, o que reitera a importância das pessoas tomarem os devidos cuidados e sempre estarem atentos à uma possível infecção, testes rápidos das doenças são oferecidos gratuitamento pelo SUS e se positivar a pessoa pode ser encaminhada para o tratamento, que também é oferecido gratuitamente pelo SUS, com medicamentos capazes de curar a infecção e impedir a progressão da doença.
 
# Perguntas a serem respondidas 🤔

O intuito do projeto será relizar análises a fim de responder certas perguntas relacionadas a Hepatite no Brasil, são elas:

* Qual a Hepatite Viral mais comum no Brasil atualmente?
* Qual a Hepatite que mais mata pessoas por ano?
* Qual a letalidade média de cada Hepatite?
* Quando começou a vacinação ampla contra a Hepatite B?
* Existe uma relação entre as doses aplicadas das vacinas contra a Hepatite B e as taxas de incidência e óbitos?
* Quando começou a vacinação ampla contra a Hepatite A?
* Existe uma relação entre as doses aplicadas da vacina contra a Hepatite A e as taxas de incidência e óbitos?
* Como se comporta a taxa de incidência, relativa à população, de cada Hepatite nos últimos anos?
* Como se comporta a taxa de óbitos, relativa à população, de cada Hepatite nos últimos anos?
* Qual região brasileira mais apresenta casos e óbitos de Hepatite por ano?
* Como se comporta a taxa de incidência, relativa à população, de cada Hepatite em cada região nos últimos anos?
* Como se comporta a taxa de óbitos, relativa à população, de cada Hepatite em cada região nos últimos anos?
* Qual região brasileira apresenta maior taxa de incidência e maior taxa de óbitos médias das Hepatites?
* Qual região brasileira apresenta maior taxa de incidência e maior taxa de óbitos médias para cada Hepatite?

# Estrutura do projeto 🧱
## [Dados Brutos](https://github.com/Pedro-correa-almeida/projeto_um_mal_silencioso/tree/main/dados_brutos)🗃️
Nesta pasta estão os arquivos relacionados aos dados brutos, esses consistem em 13 arquivos, 6 .csv e 7 .xls, obtidos de 3 fontes de dados, são eles:

* arquivo .csv obtido do [DATASUS](http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinanwin/cnv/hepabr.def) sobre os casos e óbitos de hepatite no Brasil todo:
[casos_hepatite_2001-2006_brasil.csv](https://github.com/Pedro-correa-almeida/projeto_um_mal_silencioso/blob/main/dados_brutos/casos_hepatite_2001-2006_brasil.csv) : arquivo csv com dados de casos de Hepatite entre 2001 e 2006<br>
* 3 arquivos .csv obtidos do [DATASUS](http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinanwin/cnv/hepabr.def) sobre os casos e óbitos de hepatite por região:<br>
[casos_hepA_por_regiao.csv](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/dados_brutos/casos_hepA_por_regiao.csv) : arquivo csv com os dados de casos e óbitos de hepatite A por região entre 2001 e 2006<br>
[casos_hepB_por_regiao.csv](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/dados_brutos/casos_hepB_por_regiao.csv) : arquivo csv com os dados de casos e óbitos de hepatite B por região entre 2001 e 2006<br>
[casos_hepC_por_regiao.csv](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/dados_brutos/casos_hepC_por_regiao.csv) : arquivo csv com os dados de casos e óbitos de hepatite C por região entre 2001 e 2006<br>
* 2 arquivos .csv obtidos do [DATASUS](http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinanwin/cnv/hepabr.def) sobre cobertura de vacinação e doses aplicadas das vacinas contra hepatite B e hepatite A:<br>
[cobertura_vacina_hep.csv](https://github.com/Pedro-correa-almeida/projeto_um_mal_silencioso/blob/main/dados_brutos/cobertura_vacina_hep.csv) : dados relacionados à cobertura das vacinas contra hepatite B e hepatite A, a fórmula de cálculo da cobertura é o número de doses aplicadas da dose indicada (1ª, 2ª, 3ª dose ou dose única, conforme a vacina) dividida pela população alvo, multiplicado por 100<br>
[vacinas_hepatite.csv](https://github.com/Pedro-correa-almeida/projeto_um_mal_silencioso/blob/main/dados_brutos/vacinas_hepatite.csv) : dados relacionados aos totais de doses aplicadas das vacinas contra hepatite B e da vacina contra a hepatite A<br>
* arquivo .xls com dados de casos e óbitos de hepatite dos [indicadores de Hepatite do governo](http://indicadoreshepatites.aids.gov.br/) no Brasil todo:<br>
[MonitoramentoHepatites-Brasil.xls](https://github.com/Pedro-correa-almeida/projeto_um_mal_silencioso/blob/main/dados_brutos/MonitoramentoHepatites-Brasil.xls) : arquivo xls com diversas tabelas relacionados aos dados de casos e óbitos de hepatite no Brasil entre 2007 e 2019<br>
* 5 arquivos .xls com dados de casos e óbitos dos [indicadores de Hepatite do governo](http://indicadoreshepatites.aids.gov.br/) em cada região:<br>
[MonitoramentoHepatites-Norte.xls](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/dados_brutos/MonitoramentoHepatites-Norte.xls) : arquivo xls com várias tabelas relacionadas aos casos e óbitos de Hepatites da região Norte entre 2007 e 2019<br>
[MonitoramentoHepatites-Nordeste.xls](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/dados_brutos/MonitoramentoHepatites-Nordeste.xls) : arquivo xls com várias tabelas relacionadas aos casos e óbitos de hepatites da região Nordeste entre 2007 e 2019<br>
[MonitoramentoHepatites-Sul.xls](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/dados_brutos/MonitoramentoHepatites-Sul.xls) : arquivo xls com várias tabelas relacionadas aos casos e óbitos de hepatites da região Sul entre 2007 e 2019<br>
[MonitoramentoHepatites-Sudeste.xls](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/dados_brutos/MonitoramentoHepatites-Sudeste.xls) : arquivo xls com várias tabelas relacionadas aos casos e óbitos de hepatites da região Sudeste entre 2007 e 2019<br>
[MonitoramentoHepatites-Centro-Oeste.xls](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/dados_brutos/MonitoramentoHepatites-Centro-Oeste.xls) : arquivo xls com várias tabelas relacionadas aos casos e óbitos de hepatites da região Centro-Oeste entre 2007 e 2019<br>
* arquivo .xls com estimativas populacionais realizadas pelo [IBGE](https://www.ibge.gov.br/estatisticas/sociais/populacao.html) entre 2001 e 2020 por unidade federativa:
[serie_2001_2020_TCU_populacao.xls](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/dados_brutos/serie_2001_2020_TCU_populacao.xls) : arquivo xls com dados com dados da estimativa da população brasileira feita pelo IBGE entre 2001 e 2020<br>

## [Dados Tratados](https://github.com/Pedro-correa-almeida/projeto_um_mal_silencioso/tree/main/dados_tratados):🗂️
Aqui se encontram os dados que foram tratados para realizar a [análise final](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/notebooks/Analise_final.ipynb), esses dados se encontram em 3 arquivos .csv, são eles:<br>
* [casos_obitos_hep](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/dados_tratados/casos_obitos_hep): dados sobre o número de casos e óbitos das hepatite A, B e C por ano, além disso com dados de taxas de incidência e de óbitos a cada 100 mil habitantes.<br>
* [casos_obitos_por_regiao](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/dados_tratados/casos_obitos_por_regiao): dados sobre o número de casos e óbitos das hepatites A, B e C por ano e por região, além disso com dados de taxas de incidência e de óbitos a cada 100 mil habitantes.<br>
* [vacinas_hep](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/dados_tratados/vacinas_hep): dados sobre a cobertura de vacinação contra a hepatite A e B, e a soma das doses aplicadas das vacinas contra hepatite B(HB, pentavalente e hexavalente) e da vacina contra a hepatite A <br>
## [Notebooks](https://github.com/Pedro-correa-almeida/projeto_um_mal_silencioso/tree/main/notebooks):📓

Nesta pasta se encontram os notebooks desenvolvidos no jupyter, esses notebooks foram divididos em dois tipos, 3 deles destinados ao tratamento dos dados brutos:<br>
* [tratamento_casos_obitos_hep_brasil](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/notebooks/tratamento_casos_obitos_hep_brasil.ipynb): notebook destinado a realizar todas as transformações necessárias nos conjuntos de dados relacionados aos casos e óbitos de hepatite no Brasil.<br>
* [tratamento_casos_por_regiao](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/notebooks/tratamento_casos_obitos_hep_brasil.ipynb): notebook destinado a realizar todas as transformações necessárias nos conjuntos de dados relacionados aos casos e óbitos de hepatite no Brasil por região.<br>
* [tratamento_vacina](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/notebooks/tratamento_casos_obitos_hep_brasil.ipynb): notebook destinado a realizar todas as transformações necessárias nos conjuntos de dados relacionados aos as vacinas contra as hepatites no Brasil.<br>
<br>
O outro notebook foi destinado à análise dos dados e as visualizações:<br>

* [Analise_final](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/notebooks/Analise_final.ipynb): notebook destinado à análise dos dados de hepatite A, B e C<br>

Além dos notebooks nessa pasta se encontra o arquivo [requirements.txt](https://github.com/PedroHCAlmeida/projeto_um_mal_silencioso/blob/main/notebooks/requirements.txt) , com a lista de todos os pacotes usados no projeto, afim de facilitar a reprodutibilidade.
## [Imagens](https://github.com/Pedro-correa-almeida/projeto_um_mal_silencioso/tree/main/images):📊

Nessa pasta estão as imagens utilizadas no projeto, tanto no README e nos notebooks, e todos os gráficos criados no projeto.

# Conclusões 💡

Após a análise foi possível tirar diversas informação dos dados e criar algumas hipóteses, foram elas:
* O vírus HCV é a responsável pela maior quantidade de casos de hepatite desde 2008 no Brasil
* O vírus HAV da hepatite A vem baixando ao longo do tempo desde 2006 no Brasil, o que pode ser advindo de um investimento melhor em saneamento básico
* A hepatite C é a hepatite que _**mais matou**_ no Brasil em todo o período de 2007 e 2018 
* A hepatite C é a hepatite mais _**letal**_, em que _**8,13%**_ das pessoas infectadas morrem
* A vacina da hepatite B teve seu pico de imunização no final dos anos 1990 e início dos anos 2000
* No ano onde mais foram aplicadas doses de vacinas contra a Hepatite B foi o ano que a taxa de incidência por 100 mil habitantes obteve o menor valor entre 2001 e 2019
* A vacinação ampla da hepatite A começou a partir do ano de 2014, e os anos seguintes foram os anos onde menos se teve casos de infecção do vírus e menos teve mortes relacionadas a essa infecção
* A região _**Sul**_ é a que apresentou maior média de casos(entre 2001 e 2019) e óbitos(entre 2007 e 2018) de hepatite 
* A hepatite C teve a maior taxa de incidência na maior parte do período(entre 2001 e 2019) nas regiões Sul e Sudeste
* A hepatite C teve a maior taxa de incidência na maior parte do período(entre 2001 e 2019) nas regiões Norte e Nordeste
* A hepatite B teve a maior taxa de incidência na maior parte do período(entre 2001 e 2019) na região Centro-Oeste
* A _**hepatite C**_ foi a que teve _**maior taxa de óbitos em todas as regiões**_ em todo o período de 2007 até 2018
* A região Sul é a região que apresenta a maior taxa de incidência e de óbitos médios de todas as hepatites durante o período analisado 
* A região Norte é a região que apresenta a maior taxa de incidência de hepatite A durante o período analisado 
* A região Sul é a região que apresenta a maior taxa de óbitos de hepatite A, B e C durante o período analisado, tendo uma taxa de óbitos por hepatite C de _**3,79**_ a cada 100 mil habitantes 
* A região Sul é a região que apresenta a maior taxa de incidência de hepatite B e C durante o período analisado

# Tecnologias utilizadas 💻
Esse projeto foi realizado utilizando a lingaugem Python versão 3.7.6 através do jupyter lab versão 1.2.6, as bibliotecas usadas foram:
* Pandas versão 1.0.1 : biblioteca rápida e poderosa usada para manipulação de dados
* Matplotlib versão 3.1.3 : biblioteca usada para visualização de dados
* Seaborn versão 0.10.0 : biblioteca baseada no Matplotlib para visualização de gráficos estatísticos mais complexos
* Re versão 2.2.1 : biblioteca usada para manipulação de strings usando 'regular expressions'
* Para mais informações de todas as versões utilizadas para replicação do projeto acesse o [requirements.txt](https://github.com/Pedro-correa-almeida/projeto_um_mal_silencioso/tree/main/notebooks/requirements.txt)
# Agradecimentos 😀

Queria agradecer a todos da alura, aos professores Thiago Gonçalves e Guilherme Silveira, a todo pessoal do discord do bootcamp de Data Science Aplicada e aos projetos dos outros alunos que todos eles ajudam a melhorar e dão diversas inspirações. 

# Referências 📚

https://mundoeducacao.uol.com.br/biologia/figado.htm<br>
https://hepatogastro.com.br/importancia-da-saude-do-figado/<br>
https://www.tuasaude.com/funcao-do-figado/<br>
https://brasilescola.uol.com.br/biologia/o-figado.htm<br>
https://www.mdsaude.com/gastroenterologia/hepatites/<br>
https://www.megaimagem.com.br/blog/hepatites-virais-causas-e-diagnosticos/<br>
http://giv.org.br/Hepatites-Virais/Hepatite-C/index.html<br>
http://www.aids.gov.br/pt-br/publico-geral/hv/o-que-sao-hepatites-virais<br>
https://www.saude.pr.gov.br/Pagina/Hepatites-virais<br>
https://www.gov.br/saude/pt-br/assuntos/noticias/sus-disponibiliza-18-vacinas-para-criancas-e-adolescentes<br>
http://www.planassiste.mpu.mp.br/news/governo-inclui-vacina-contra-hepatite-a-no-calendario-do-sus<br>
https://portalarquivos.saude.gov.br/campanhas/vivamaissus/hepatite_interna.html<br>
https://www.scielo.br/j/sausoc/a/gn7vpPFZYBHq6s6JVtHCHbw/?lang=pt#<br>
http://tabnet.datasus.gov.br/cgi/pni/Imun_cobertura_desde_1994.pdf<br>
https://www.storytellingwithdata.com/<br>
https://github.com/diascarolina/healthcare-analysis<br>
https://jtemporal.com/requirements-txt/

# Contato ☎️

[<img src="https://img.shields.io/badge/pedrocorrea-0A66C2?style=flat-square&logo=linkedin&logoColor=white" />](https://www.linkedin.com/in/pedro-henrique-corrêa-de-almeida/)<br>
[<img src="https://img.shields.io/badge/GitHub-PedroHCAlmeida-DCDCDC?style=flat-square" />](https://github.com/PedroHCAlmeida)<br>
