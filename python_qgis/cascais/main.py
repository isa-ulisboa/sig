# Exercício análise espacial (Secção 3 do Caderno das Aulas Práticas ISA ULisboa). 
# Dados para Cascais: COS2018, OSM, Carta de Solos
# Copyright Manuel Campagnolo 2023

import qgis # already loaded
from qgis.core import QgsProject
import processing # idem
import os # file management
import sys # to get sys.path

# opção para retirar as layers desnecessárias após serem usadas
REMOVE_LAYERS=True

# where data and the auxiliary functions python file is:
myfolder=r'C:\Users\mlc\OneDrive - Universidade de Lisboa\Documents\temp'

# load auxiliary functions
exec(open(os.path.join(myfolder,'cascais_COS_OSM_funcoes_auxiliares.py').encode('utf-8')).read())

####################################depois de carregar funções auxiliares

# project and data set CRS
my_crs=3763
# Create project
myproject,mycanvas= my_clean_project()
# set project CRS
myproject.setCrs(QgsCoordinateReferenceSystem(my_crs))

# street maps
uri_StreetMap = 'type=xyz&url=https://a.tile.openstreetmap.org/%7Bz%7D/%7Bx%7D/%7By%7D.png&zmax=19&zmin=0&crs=EPSG3857'
iface.addRasterLayer(uri_StreetMap, "OpenStreetMap", "wms")


#########################################################################  ler dados

# Limite Concelho
fn=os.path.join(myfolder,'LimConc.shp')
mylayer=my_processing_run("native:fixgeometries",fn,{},'LimConc')
# CartaSolos
fn=os.path.join(myfolder,'CartaSolos.shp')
mylayer=my_processing_run("native:fixgeometries",fn,{},'CartaSolos')
# UsoSolo
fn=os.path.join(myfolder,'UsoSolo.shp')
mylayer=my_processing_run("native:fixgeometries",fn,{},'UsoSolo') 
# Rede Viária
fn=os.path.join(myfolder,'RedeViaria.shp')
mylayer=my_processing_run("native:fixgeometries",fn,{},'RedeViaria')
# LAgua
fn=os.path.join(myfolder,'LAgua.shp')
mylayer=my_processing_run("native:fixgeometries",fn,{},'LAgua')

# ler ficheiros csv com pyqgis
fn='ProtRV.csv' # delimiter=;
ln='ProtRV'
uri = "file:///"+os.path.join(myfolder,fn)+"?encoding=System&type=csv&delimiter=;&maxFields=10000&detectTypes=yes&geomType=none&subsetIndex=no&watchFile=no"
mylayer = QgsVectorLayer(uri, ln, "delimitedtext")
myproject.addMapLayer(mylayer)

fn='ProdS.csv' # delimiter=;
ln='ProdS'
uri = "file:///"+os.path.join(myfolder,fn)+"?encoding=System&type=csv&delimiter=;&maxFields=10000&detectTypes=yes&geomType=none&subsetIndex=no&watchFile=no"
mylayer = QgsVectorLayer(uri, ln, "delimitedtext")
myproject.addMapLayer(mylayer)

# keys for joins
key_UsoSolo='COS18n1_L'
key_ProtRV='Tipo'
atrib_ProtRV='protM'
key_RedeViaria='fclass'
key_CartaSolos='COD1_solos'
key_ProdS='COD1'
atrib_ProdS='produtividade'
atrib_LAgua='fclass'

# some expressions 
exp_CartaSolos=' "produtividade" = \'Baixa produtividade\' OR  "produtividade" = \'Media produtividade\' ' 
exp_LAgua = ' "fclass" = \'stream\' OR "fclass" = \'river\' ' # table Streams
exp_area = ' \"area\" >300000 '  
exp_UsoSolo='"COS18n1_L" =  \'Florestas\' OR \
"COS18n1_L" =  \'Superfícies agroflorestais (SAF)\' OR \
"COS18n1_L" =  \'Matos\' '

# attribute in 'RoadProtection' for buffers
property_distance=QgsProperty.fromExpression('"protM"')

################################################# Spatial Analysis

# clip to Cascais Municipality
dict_params={'OVERLAY':'LimConc'}
mylayer=my_processing_run("native:clip",'UsoSolo',dict_params,'UsoSolo_')
if REMOVE_LAYERS: my_remove_layer('UsoSolo')

# select suitable land use
dict_params={'EXPRESSION': exp_UsoSolo}
mylayer=my_processing_run("native:extractbyexpression",'UsoSolo_',dict_params,'UsoAdeq')
if REMOVE_LAYERS: my_remove_layer('UsoSolo_')

# join layers CartaSolos
dict_params={'FIELD': key_CartaSolos,'INPUT_2': 'ProdS', 'FIELD_2':key_ProdS}
mylayer=my_processing_run("native:joinattributestable",'CartaSolos',dict_params,'CartaSolos_')
if REMOVE_LAYERS: my_remove_layer('CartaSolos')
if REMOVE_LAYERS: my_remove_layer('ProdS')

# select suitable soil type 
dict_params={'EXPRESSION': exp_CartaSolos}
mylayer=my_processing_run("native:extractbyexpression",'CartaSolos_',dict_params,'SolosAdeq')
if REMOVE_LAYERS: my_remove_layer('CartaSolos_')

# clip suitable Land Use with suitable Soil Type
dict_params={'OVERLAY':'SolosAdeq'}
mylayer=my_processing_run("native:clip",'UsoAdeq',dict_params,'UsoSolosAdeq')
if REMOVE_LAYERS: my_remove_layer('UsoAdeq')
if REMOVE_LAYERS: my_remove_layer('SolosAdeq')

# join layers about Roads
dict_params={'FIELD': key_RedeViaria,'INPUT_2': 'ProtRV', 'FIELD_2':key_ProtRV}
mylayer=my_processing_run("native:joinattributestable",'RedeViaria',dict_params,'RedeViaria_')
if REMOVE_LAYERS: my_remove_layer('ProtRV')
if REMOVE_LAYERS: my_remove_layer('RedeViaria')

# Create buffer around Roads
dict_params={'DISTANCE':property_distance,'DISSOLVE':True}
mylayer=my_processing_run("native:buffer",'RedeViaria_',dict_params,'BuffersRV')
if REMOVE_LAYERS: my_remove_layer('RedeViaria_')

# Remove roads buffer from suitable areas # demora porque há muitos buffers de estrada
dict_params={'OVERLAY':'BuffersRV'}
mylayer=my_processing_run("native:difference",'UsoSolosAdeq',dict_params,'UsoSolosRV')
if REMOVE_LAYERS: my_remove_layer('UsoSolosAdeq')
if REMOVE_LAYERS: my_remove_layer('BuffersRV')

# Dissolve suitable areas
dict_params={}
mylayer=my_processing_run("native:dissolve",'UsoSolosRV',dict_params,'AdeqDiss_')
if REMOVE_LAYERS: my_remove_layer('UsoSolosRV')

# Remove all fields except 'fid' after dissolve
FirstField=mylayer.fields().names()[0]
dict_params={'FIELDS':[FirstField]}
mylayer=my_processing_run("native:retainfields",'AdeqDiss_',dict_params,'AdeqDiss')
if REMOVE_LAYERS: my_remove_layer('AdeqDiss_')

# Convert to singlepart (spatially connected)
dict_params={}
mylayer=my_processing_run("native:multiparttosingleparts",'AdeqDiss',dict_params,'AdeqSingle')
if REMOVE_LAYERS: my_remove_layer('AdeqDiss')

# Select main streams 
dict_params={'EXPRESSION': exp_LAgua}
mylayer=my_processing_run("native:extractbyexpression",'LAgua',dict_params,'RiverStream')
if REMOVE_LAYERS: my_remove_layer('LAgua')

# Select by location suitable areas that are intersected by main streams
dict_params={'PREDICATE':[0], 'INTERSECT':'RiverStream'}
mylayer=my_processing_run("native:extractbylocation",'AdeqSingle',dict_params,'AdeqLAgua')
if REMOVE_LAYERS: my_remove_layer('AdeqSingle')

# Calculate areas
dict_params={'CALC_METHOD':2}
mylayer=my_processing_run("qgis:exportaddgeometrycolumns",'AdeqLAgua',dict_params,'AdeqLAgua_')
if REMOVE_LAYERS: my_remove_layer('AdeqLAgua')

# Select  areas with more than a given value (e.g. 300000, in square meters), defined by exp_area
dict_params={'EXPRESSION': exp_area}
mylayer=my_processing_run("native:extractbyexpression",'AdeqLAgua_',dict_params,'final')

# export layer as geopackage
options = QgsVectorFileWriter.SaveVectorOptions()
transform_context = QgsProject.instance().transformContext()
options.actionOnExistingFile = QgsVectorFileWriter.CreateOrOverwriteLayer # overwrite
QgsVectorFileWriter.writeAsVectorFormatV3(mylayer, os.path.join(myfolder,'final.gpkg'),transform_context,options)
# to save as shapefile
# options.driverName = "ESRI Shapefile"
