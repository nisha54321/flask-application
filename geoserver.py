
#pip install geoserver-rest
from geo.Geoserver import Geoserver

# Initialize the library
geo = Geoserver('http://localhost:8080/geoserver', username='admin', password='geoserver')

# For creating workspace
geo.create_workspace(workspace='demo')

# For uploading raster data to the geoserver
#geo.create_coveragestore(layer_name='alayer1', path="/home/bisag/Documents/1DEM/publish_folder/polygon.shp", workspace='demo')

# For creating postGIS connection and publish postGIS table
geo.create_featurestore(store_name='mergefile', workspace='demo', db='postgres', host='localhost', pg_user='postgres',
                        pg_password='postgres')
geo.publish_featurestore(workspace='demo', store_name='mergefile', pg_table='mergefile')



# # For uploading SLD file and connect it with layer
# geo.upload_style(path=r'path\to\sld\file.sld', workspace='demo')
# geo.publish_style(layer_name='geoserver_layer_name', style_name='sld_file_name', workspace='demo', sld_version='1.0.0')

# # For creating the style file for raster data dynamically and connect it with layer
# geo.create_coveragestyle(raster_path=r'path\to\raster\file.tiff', style_name='style_1', workspace='demo',
#                          color_ramp='RdYiGn')
# geo.publish_style(layer_name='geoserver_layer_name', style_name='raster_file_name', workspace='demo')

# # delete workspace
# geo.delete_workspace(workspace='demo')

# # delete layer
# geo.delete_layer(layer_name='agri_final_proj', workspace='demo')

# # delete style file
# geo.delete_style(style_name='kamal2', workspace='demo')
