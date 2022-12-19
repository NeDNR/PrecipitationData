import urllib.request
import tarfile
import os
import shutil

url = "http://www.srh.noaa.gov/ridge2/Precip/qpehourlyshape/latest/last_24_hours.tar.gz"

BaseOutput = "\\\\server23\\Tasks\\NightlyWeatherShapefile\\"
outputPath = BaseOutput+"nws_precip.tar.gz"


print("Deleting " + outputPath)
if os.path.exists(outputPath):
	os.remove(outputPath)

print("Deleting " + BaseOutput + "Shapefile\\precipitation")
if os.path.isdir(BaseOutput + "Shapefile\\precipitation"):
	for f in os.listdir(BaseOutput + "Shapefile\precipitation"):
		os.remove(BaseOutput + "Shapefile\\precipitation\\"+f)
#os.remove(BaseOutput + "Shapefile\\precipitation")

print("Deleting	" + BaseOutput + "Shapefile")
if os.path.isdir(BaseOutput + "Shapefile"):
	for f in os.listdir(BaseOutput + "Shapefile"):
		if not os.path.isdir(BaseOutput + "Shapefile\\"+f):
			os.remove(BaseOutput + "Shapefile\\"+f)




print("Downloading NWS Data")
response = urllib.request.urlopen(url)
data = response.read()
print("Downloaded: " + str(len(data)))

print("Saving " + outputPath)
with open(outputPath,"wb") as file:
    file.write(data)

print("Extracting tar to " + BaseOutput)
with tarfile.open(outputPath,"r") as tar: #Use this line for tar only
#with tarfile.open(outputPath,"r:gz") as tar: #Use this line for tar and gz file
    def is_within_directory(directory, target):
        
        abs_directory = os.path.abspath(directory)
        abs_target = os.path.abspath(target)
    
        prefix = os.path.commonprefix([abs_directory, abs_target])
        
        return prefix == abs_directory
    
    def safe_extract(tar, path=".", members=None, *, numeric_owner=False):
    
        for member in tar.getmembers():
            member_path = os.path.join(path, member.name)
            if not is_within_directory(path, member_path):
                raise Exception("Attempted Path Traversal in Tar File")
    
        tar.extractall(path, members, numeric_owner=numeric_owner) 
        
    
    safe_extract(tar, BaseOutput)

print("Creating " + BaseOutput + "Shapfile")
if not os.path.isdir(BaseOutput+"Shapefile"):
    os.mkdir(BaseOutput+"Shapefile")
	

for file in os.listdir(BaseOutput+"latest"):
	print("Coping file " + BaseOutput+"latest\\"+file + " to " + BaseOutput+"Shapefile\\"+file.replace("last_24_hours","nws_precip"))
	
	shutil.copy(BaseOutput+"latest\\"+file,BaseOutput+"Shapefile\\"+file.replace("last_24_hours","nws_precip"))

    

