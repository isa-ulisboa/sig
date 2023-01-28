

################################################ create "clean" project
# It supposes there is a myproject variable
# clear layer tree and canvas
def my_clean_project():
    # project and canvas
    myproject = QgsProject.instance() # does not write to file
    mycanvas = iface.mapCanvas()
    # clear layers in project
    myproject.removeAllMapLayers()
    # refresh canvas
    mycanvas.refreshAllLayers()
    return myproject,mycanvas


###################### my_processing_run
# operation: string that defines the operation to apply from Processing Toolbox
# ln_input: string: layer name of the input layer
# dict_params: dictionary with operation parameters except 'INPUT' and 'OUTPUT'
# layer_name: name of the output layer
# output: output layer
def my_processing_run(operation,ln_input,dict_params,layer_name):
    dict_params['INPUT']=ln_input
    dict_params['OUTPUT']=QgsProcessing.TEMPORARY_OUTPUT
    mylayer=processing.run(operation,dict_params)['OUTPUT']
    # if mylayer is a string
    if isinstance(mylayer,str):
        if 'tif' in mylayer:
            mylayer=my_add_raster_layer(mylayer,layer_name)
        else:
            mylayer=my_add_vector_layer(mylayer,layer_name)
    else:
        myproject.addMapLayer(mylayer)
    mylayer.setName(layer_name)
    return mylayer

################################### add, name, remove layers

# It supposes there is a myproject variable
# add and name vector layer from file
# fn: string: path_to_file
# ln: string: output layer name
# output: output layer
def my_add_vector_layer(fn,ln):
    mylayer=QgsVectorLayer(fn,"", "ogr")
    mylayer.setName(ln)
    myproject.addMapLayer(mylayer)
    return mylayer

def my_add_raster_layer(fn,ln):
    mylayer=QgsRasterLayer(fn,"", "gdal")
    mylayer.setName(ln)
    myproject.addMapLayer(mylayer)
    return mylayer

# It supposes there is a myproject variable
# remove layer with name "ln"
def my_remove_layer(ln):
    to_be_deleted = myproject.mapLayersByName(ln)[0]
    myproject.removeMapLayer(to_be_deleted.id())
