# Elementos de apoio à UC de Sistemas de Informação Geográfica para as licenciaturas do ISA/ULisboa

---

## Projeções de apoio às aulas teóricas

[Manuel Campagnolo - Projeções](slides_uc_sig_2024.pdf) (versão de 22 de abril de 2024) - material para estudo

[Alguns elementos sobre o Sistema Nacional de Informação Cadastral](Cadastro_Predial.pdf) (aula de 18 de março de 2024)

**Slides das aulas teóricas 2024/2025**
- [aula 01](https://docs.google.com/presentation/d/12nqBlxaVKIH8I5izmX9HmGn6AFykuouYn_f5h_ZtUGw/edit?usp=sharing)
- [aula 02](https://docs.google.com/presentation/d/1PAbYxN4jOoz--GHemJlzzeqEad6biOa2GxEFbExQKaU/edit?usp=sharing)
- [aula 03](https://docs.google.com/presentation/d/1SiunqJfpeGt-GMZMFMWoFK7y-D-lGBWJFaF5yMfxQVg/edit?usp=sharing)
- [aula 04](https://docs.google.com/presentation/d/1ot364ImHwTwvtW7IEpjMAPV5K-l9P7LCBHBkNeCzhFw/edit?usp=sharing)
- [aula 05](https://docs.google.com/presentation/d/1c60zINYuNSMNlhSHsssKo89qrVf03fZDuotSHFxeSBw/edit?usp=sharing)
- [aula 06](https://docs.google.com/presentation/d/1FIYiQFKzUG5YW5BV0sg59eAPDS4u6g8I83nYyFlYty4/edit?usp=sharing)
- [aula 07](https://docs.google.com/presentation/d/1cZnN4tMANhwVaTZJpXXofbImw2GZIOgiAZmvoSg2piA/edit?usp=sharing)

---

## Caderno de apoio às aulas práticas de Sistemas de Informação Geográfica

[Caderno de apoio](Caderno-aulas-praticas-qgis3_SIG.pdf) (versão de 13 de fevereiro de 2025)

---

## Canal youtube com as resoluções dos exercícios do caderno de apoio às aulas práticas

[Canal Youtube](https://www.youtube.com/@qgis3emportugues)

<!--  comments
### Script python para Seccao 1.B.1: Primeiro exemplo de script de Python em QGIS, 'processing.run' e 'History'

### Script python para Seccao 1.B.2: Script Python para criar legenda quantivativa e colocar de etiquetas na layer em QGIS 3

### Script python para Seccao 1.B.3: Script Python para criar legenda qualitativa com cores aleatórias ("random colors")
-->

---

## Dados para os exercícios do caderno de apoio às aulas práticas

*Nota: Os links para scripts em Python indicados são extra programa da UC; são elementos de apoio adicional para os eventuais interessados.*

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
- Rede estradas (roads), linhas de água (waterways), etc [Dados OpenStreetMap para Portugal](https://download.geofabrik.de/europe/portugal.html)
- CAOP: Carta Administrativa Oficial de Portugal no [Link: Registo Nacional de dados geográficos/SNIG](https://snig.dgterritorio.gov.pt/rndg/srv/por/catalog.search#/home)
- COS: Carta de Uso e Ocupação do Solo no [Link: Registo Nacional de dados geográficos/SNIG](https://snig.dgterritorio.gov.pt/rndg/srv/por/catalog.search#/home)

Caso não seja possível obter os dados geográficos nos links acima, pode usar unicamente as tabelas simples e os 5 conjuntos de dados geográficos que pode obter nos links abaixo:
- Tabelas simples [Download zip file: ProtRV e ProdS](analise_espacial_cascais/tabelas_simples_cascais.zip) 
- [Download zip file: LAgua, RedeViaria, CartaSolos, UsoSolos, LimConc](analise_espacial_cascais/dados_geog_input_cascais.zip) já pré-processados.

Scripts em Python para QGIS:
- [Download script: main.py](python_qgis/cascais/main.py)
- [Download script: cascais_COS_OSM_funcoes_auxiliares.py](python_qgis/cascais/cascais_COS_OSM_funcoes_auxiliares.py)

### Secção 4: Análise de dados "raster" e conversão vetorial/matricial

Dados vetoriais e "raster" para a região de Esposende:
- [Download zip file: Freguesias, uso do solo, tipo de solo, limites do aquífero, medições pontuais de concentrações de nitratos](Dados_Esposende_3763.zip)

### Secção 5: Sistemas de coordenadas de referência e projeções

- [Download zip file: Vertice geodésico de Sesimbra, estradas Sesimbra HGLx](SistCoordReferenciaProjecoes.zip)

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

- [Download zip file: Imagem de 15 de maio 2014 (MacOS: float32)](LC82030332014151_float32.zip)
- [Download zip file: Imagem de 1 de junho 2014 (MacOS: float32)](LC82030332014167_float32.zip)
