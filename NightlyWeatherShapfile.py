import arcpy
import arcgisscripting

gp = arcgisscripting.create()
arcpy.CheckOutExtension("3D")
gp.workspace = r"\\server23\Tasks\NightlyWeatherShapefile\Shapefile"

#Project Points From HRAP to State Plane
arcpy.Project_management(in_dataset="/nws_precip.shp",out_dataset="/nws_precip_projected.shp",out_coor_system="GEOGCS['HRAP_Sphere',DATUM['<custom>',SPHEROID['<custom>',6371200.0,0.0]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]",transform_method="#",in_coor_system="GEOGCS['HRAP_Sphere',DATUM['<custom>',SPHEROID['<custom>',6371200.0,0.0]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]]")
print"Projecting Points Completed"

#Create Tin from Points
arcpy.CreateTin_3d("E:/Tasks/NightlyWeatherShapefile/Shapefile/precipitation","PROJCS['NAD_1983_StatePlane_Nebraska_FIPS_2600_Feet',GEOGCS['GCS_North_American_1983',DATUM['D_North_American_1983',SPHEROID['GRS_1980',6378137.0,298.257222101]],PRIMEM['Greenwich',0.0],UNIT['Degree',0.0174532925199433]],PROJECTION['Lambert_Conformal_Conic'],PARAMETER['False_Easting',1640416.666666667],PARAMETER['False_Northing',0.0],PARAMETER['Central_Meridian',-100.0],PARAMETER['Standard_Parallel_1',40.0],PARAMETER['Standard_Parallel_2',43.0],PARAMETER['Latitude_Of_Origin',39.83333333333334],UNIT['Foot_US',0.3048006096012192]]","C:/Tasks/NightlyWeatherShapefile/Shapefile/nws_precip_projected.shp Globvalue masspoints <None>","DELAUNAY")
print"Creating Tin from Points Completed"

#Create Contours from Tin
arcpy.SurfaceContour_3d(in_surface="/precipitation",out_feature_class="/Contours.shp",interval="1",base_contour="0",contour_field="Contour",contour_field_precision="0",index_interval="#",index_interval_field="Index_Cont",z_factor="1",pyramid_level_resolution="0")
print"Creating Contours Completed"

#Convert contour lines to polygons
arcpy.FeatureToPolygon_management(in_features="/Contours.shp",out_feature_class="/ContoursPoly.shp",cluster_tolerance="#",attributes="ATTRIBUTES",label_features="#")
print"Converting Contour Lines to Polygons Completed"
print"****Precipitation Data Processing Completed****"


arcpy.CheckInExtension("3D")
