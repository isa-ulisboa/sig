# QGIS 3 em português
# Manuel Campagnolo
# Instituto Superior de Agronomia, Universidade de Lisboa
# Janeiro 2023
#########################################################
# Criar uma legenda usando uma variável quantitativa; Gerar cores aleatórias usando random.randint()

# criar uma variável para o projecto
myproject = QgsProject.instance()

# determinar qual é a layer que tem nome Conc2016 no projecto
mylayer=myproject.mapLayersByName('Conc2016')[0]

# lista de atributos de mylayer
mylayeratribs= mylayer.dataProvider().fields().names()

# atributos a usar para a legenda e para as etiquetas
my_legend_atrib='áreaHa'
if my_legend_atrib not in mylayeratribs: stop
my_labels_atrib='Concelho'
if my_labels_atrib not in mylayeratribs: stop

############################################# LEGENDA QUANTITATIVA
# definir classes da legenda

# classe 1
myMin = 0
myMax = 10000
myLabel = 'freguesias pequenas'
myColor = QColor('red')  # ou QColor('#ff0000')  #hexadecimal
myOpacity = 1
mySymbol = QgsSymbol.defaultSymbol(mylayer.geometryType())
mySymbol.setColor(myColor)
mySymbol.setOpacity(myOpacity)
myRange1 = QgsRendererRange(myMin, myMax, mySymbol, myLabel)

# classe 2
myMin = myMax
myMax = 25000
myLabel = 'freguesias médias'
myColor = QColor('orange') #
myOpacity = 1
mySymbol = QgsSymbol.defaultSymbol(mylayer.geometryType())
mySymbol.setColor(myColor)
mySymbol.setOpacity(myOpacity)
myRange2 = QgsRendererRange(myMin, myMax, mySymbol, myLabel)

# classe 3
myMin = myMax
myMax = 100000
myLabel = 'freguesias grandes'
myColor = QColor('green')
mySymbol = QgsSymbol.defaultSymbol(mylayer.geometryType())
mySymbol.setColor(myColor)
mySymbol.setOpacity(myOpacity)
myOpacity = 1
myRange3 = QgsRendererRange(myMin, myMax, mySymbol, myLabel)

# classe 4
myMin = myMax
myMax = 200000
myLabel = 'freguesias muito grandes'
myColor = QColor('blue')
myOpacity = 1
mySymbol = QgsSymbol.defaultSymbol(mylayer.geometryType())
mySymbol.setColor(myColor)
mySymbol.setOpacity(myOpacity)
# dir(mySymbol.symbolLayer(0)) # access individual symbol layers inside
mySymbol.symbolLayer(0).setStrokeWidth(.5)
myRange4 = QgsRendererRange(myMin, myMax, mySymbol, myLabel)

# Lista de objectos QgsRendererRange
myRangeList=[myRange1,myRange2,myRange3,myRange4]

# definir legenda (que é do tipo GraduatedSymbol)
# apenas precisa de indicar qual o atributo e quais são as classes
renderer = QgsGraduatedSymbolRenderer(my_legend_atrib, myRangeList)

# alterar simbologia da layer
# aplica o "renderer" à nossa layer
mylayer.setRenderer(renderer)
# Refresh layer: necessário para fazer o "refresh"
mylayer.triggerRepaint()

############################################## ETIQUETAS
# definir QgsVectorLayerSimpleLabeling
layer_settings  = QgsPalLayerSettings()
text_format = QgsTextFormat()
text_format.setFont(QFont("Arial"))
text_format.setSize(12)
buffer_settings = QgsTextBufferSettings()
buffer_settings.setEnabled(True)
buffer_settings.setSize(0.5)
buffer_settings.setColor(QColor("white"))
text_format.setBuffer(buffer_settings)
layer_settings.setFormat(text_format)
layer_settings.fieldName = my_labels_atrib
layer_settings.placement = 1
layer_settings.enabled = True
my_layer_settings = QgsVectorLayerSimpleLabeling(layer_settings)

# alterar etiquetas de mylayer
mylayer.setLabelsEnabled(True)
mylayer.setLabeling(my_layer_settings)
mylayer.triggerRepaint()
