# Elementos de apoio às UC sobre Sistemas de Informação Geográfica (Geomática e SIGDR) para as licenciaturas do ISA/ULisboa

---

## Projeções de apoio às aulas teóricas

[Projeções](slides_uc_sig_2023.pdf) (versão de 23 de fevereiro de 2023)

---

## Caderno de apoio às aulas práticas de Sistemas de Informação Geográfica

[Caderno de apoio](Caderno-aulas-praticas-qgis3_SIG.pdf) (versão de 11 de fevereiro de 2023)

---

## Canal youtube com as resoluções dos exercícios do caderno de apoio às aulas práticas

[Canal Youtube](https://www.youtube.com/@qgis3emportugues)

<!--  comments
### Script python para Seccao 1.B.1: Primeiro exemplo de script de Python em QGIS, 'processing.run' e 'History'

### Script python para Seccao 1.B.2: Script Python para criar legenda quantivativa e colocar de etiquetas na layer em QGIS 3

### Script python para Seccao 1.B.3: Script Python para criar legenda qualitativa com cores aleatórias ("random colors")
-->

---

## Dados para os exercícios do caderno de apoio às aulas práticas, e alguns scripts em Python

### Secção 1: Introdução a QGIS3

Dados vetoriais (concelhos de Portugal Continental, linhas de água) e tabela simples:
- [Download zip file: Conc2016, linhasAgua, VACc](IntroQGIS.zip)

Descarregar o modelo digital de elevações para Portugal Continental (25 m)
- [Link: SRTM-DEM EPSG:3763, GSD=25m](https://www.fc.up.pt/pessoas/jagoncal/dems/); ou
- [Link: ALOS-AW3D30 EPSG:3763, GSD=25m](https://www.fc.up.pt/pessoas/jagoncal/dems/), com algumas falhas.

Scripts em Python para QGIS:
- Secção 1.4.7 [Download script: Criar legenda qualitativa e usar random.randint() para criar cores aleatórias](python_qgis/introQGIS/legenda_qualitativa_random_mylayer.py)
- Secção 1.4.8 [Download script: Criar legenda quantitativa para layer vetorial e colocar etiquetas](python_qgis/introQGIS/legenda_quantitativa_mylayer.py)
- Secção 1.5.2 [Download script: Seleção por atributos e por localização](python_qgis/introQGIS/concMondego.py)

### Secção 3: Análise espacial para dados vetoriais

Descarregar os dados para o exercício dos repositórios seguintes:
- Tabelas simples [Download zip file: ProtRV e ProdS](analise_espacial_cascais/tabelas_simples_cascais.zip) 
- [Link: Carta dos Solos](https://snisolos.dgadr.gov.pt/downloads) no site da DGADR
- Rede estradas (roads), linhas de água (waterways), uso do solo (landuse), etc [Dados OpenStreetMap para Portugal](https://download.geofabrik.de/europe/portugal.html)
- CAOP: Carta Administrativa Oficial de Portugal no [Link: Registo Nacional de dados geográficos/SNIG](https://snig.dgterritorio.gov.pt/rndg/srv/por/catalog.search#/home)
- COS: Carta de Uso e Ocupação do Solo no [Link: Registo Nacional de dados geográficos/SNIG](https://snig.dgterritorio.gov.pt/rndg/srv/por/catalog.search#/home)

Caso não seja possível obter os dados geográficos nos links acima:
- [Download zip file: LAgua, RedeViaria, CartaSolos, UsoSolos, LimConc](analise_espacial_cascais/dados_geog_input_cascais.zip) já pré-processados.

Scripts em Python para QGIS:
- [Download script: main.py](python_qgis/cascais/main.py)
- [Download script: cascais_COS_OSM_funcoes_auxiliares.py](python_qgis/cascais/cascais_COS_OSM_funcoes_auxiliares.py)

### Secção 4: Análise de dados "raster" e conversão vetorial/matricial

Dados vetoriais e "raster" para a região de Esposende:
- [Download zip file: Freguesias, uso do solo, tipo de solo, limites do aquífero, medições pontuais de concentrações de nitratos](Dados_Esposende_3763.zip)

### Secção 6: Representação cartográfica do relevo

Dados de levantamento topográfico: 
- (Secção 6.2) Portalegre: [Download zip file: Curvas de nível, pontos cotados, linhas de água, linhas de festo, EPSG:20790](Representacao_terreno_portalegre_20790.zip)
- (Secção 6.4) Paisagem Protegida da Serra de Montejunto: [Download zip file: Curvas de nível, pontos cotados, linhas de água, EPSG:3763](representacao_terreno_montejunto_3763.zip)

Descarregar o modelo digital de elevações para Portugal Continental (Secção 6.4):
- [Link: SRTM-DEM EPSG:3763, GSD=25m](https://www.fc.up.pt/pessoas/jagoncal/dems/); ou
- [Link: ALOS-AW3D30 EPSG:3763, GSD=25m](https://www.fc.up.pt/pessoas/jagoncal/dems/), com algumas falhas.

### Secção 7: Imagens multiespectrais

Imagens multiespectrais (7 bandas) Landsat-8 OLI para a zona do Alqueva:
- [Download zip file: Imagem de 15 de maio 2014](LC82030332014151.zip)
- [Download zip file: Imagem de 1 de junho 2014](LC82030332014167.zip)
