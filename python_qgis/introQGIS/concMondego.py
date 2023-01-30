import processing

processing.run("native:extractbyexpression", 
{'INPUT':'C:/Users/mlc/OneDrive - Universidade de Lisboa/Documents/temp/linhasAgua.shp',
'EXPRESSION':' "DESIGNACAO" =  \'Rio Mondego\' OR "DESIGNACAO" =  \'Albufeira Aguieira\' OR "DESIGNACAO" =  \'Albufeira Raiva\' OR "DESIGNACAO" =  \'Albufeira Ponte de Coimbra\' ',
'OUTPUT':'C:/Users/mlc/OneDrive - Universidade de Lisboa/Documents/temp/RioMondego.gpkg'})


processing.run("native:extractbylocation", 
{'INPUT':'C:/Users/mlc/OneDrive - Universidade de Lisboa/Documents/temp/Conc2016.shp',
'PREDICATE':[0],
'INTERSECT':'C:/Users/mlc/OneDrive - Universidade de Lisboa/Documents/temp/RioMondego.gpkg',
'OUTPUT':'C:/Users/mlc/OneDrive - Universidade de Lisboa/Documents/temp/ConcMondego.gpkg'})
