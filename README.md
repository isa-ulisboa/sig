# Elementos de apoio às UC da área dos SIG (Geomática e SIGDR) elaborados no quadro do ensino nas licenciaturas do ISA/ULisboa

---

## Projeções de apoio às aulas teóricas

[Projeções](slides_uc_sig_2023.pdf) (versão provisória de 23 de janeiro de 2023)

---

## Caderno de apoio às aulas práticas de Sistemas de Informação Geográfica

[Caderno de apoio](Caderno-aulas-praticas-qgis3_SIG.pdf) (versão provisória de 23 de janeiro de 2023)

---

## Link para canal youtube com as resoluções dos exercícios do caderno de apoio às aulas práticas

[Canal Youtube](https://www.youtube.com/@qgis3emportugues)

<!--  comments
### Script python para Seccao 1.B.1: Primeiro exemplo de script de Python em QGIS, 'processing.run' e 'History'

### Script python para Seccao 1.B.2: Script Python para criar legenda quantivativa e colocar de etiquetas na layer em QGIS 3

### Script python para Seccao 1.B.3: Script Python para criar legenda qualitativa com cores aleatórias ("random colors")
-->

---

## Dados para os exercícios

### Secção 1: Introdução a QGIS3
### Secção 2: Acesso a dados e criação de dados geográficos
### Secção 3: Análise espacial para dados vetoriais

Descarregar os dados para o exercício dos repositórios seguintes:
- Tabelas simples [ProtRV e ProdS](analise_espacial_cascais/tabelas_simples_cascais.zip) 
- [Carta dos Solos](https://snisolos.dgadr.gov.pt/downloads) no site da DGADR
- Rede estradas (roads), linhas de água (waterways), uso do solo (landuse), etc [Dados OpenStreetMap para Portugal](https://download.geofabrik.de/europe/portugal.html)
- CAOP: Carta Administrativa Oficial de Portugal no [Registo Nacional de dados geográficos/SNIG](https://snig.dgterritorio.gov.pt/rndg/srv/por/catalog.search#/home)
- COS: Carta de Uso e Ocupação do Solo no [Registo Nacional de dados geográficos/SNIG](https://snig.dgterritorio.gov.pt/rndg/srv/por/catalog.search#/home)

Caso não seja possível obter os dados geográficos nos links acima:
- [LAgua, RedeViaria, CartaSolos, UsoSolos, LimConc](analise_espacial_cascais/dados_geog_input_cascais.zip) já pré-processados.

### Secção 4: Análise de dados "raster" e conversão vetorial/matricial

Dados vetoriais e "raster" para a região de Esposende:
- [Freguesias, uso do solo, tipo de solo, limites do aquífero, medições pontuais de concentrações de nitratos](Dados_Esposende_3763.zip)

### Secção 6: Representação cartográfica do relevo

Dados de levantamento topográfico: 
- (Secção 6.2) Portalegre: [Curvas de nível, pontos cotados, linhas de água, linhas de festo, EPSG:20790](Representacao_terreno_portalegre_20790.zip)
- (Secção 6.4) Paisagem Protegida da Serra de Montejunto: [Curvas de nível, pontos cotados, linhas de água, EPSG:3763](representacao_terreno_montejunto_3763.zip)

Descarregar o modelo digital de elevações para Portugal Continental (Secção 6.4):
- [SRTM-DEM EPSG:3763, GSD=25m](https://www.fc.up.pt/pessoas/jagoncal/dems/); ou
- [ALOS-AW3D30 EPSG:3763, GSD=25m](https://www.fc.up.pt/pessoas/jagoncal/dems/), com algumas falhas.
