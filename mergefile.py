import os ,ogr
import psycopg2
import osgeo.ogr  

print("merge file ==================================")


def combine():
    path = os.getcwd()
    directory = os.path.join(path, 'uploads')
    output = os.path.join(path, 'merge')
    # output = "/home/bisag/Documents/wfh/1WFH/QFIELD/flaskApp/merge/"
    # directory = "/home/bisag/Documents/wfh/1WFH/QFIELD/flaskApp/uploads/"

    fileEndsWith = '.gpkg'
    fileEndsWith1 = '.shp'
    outputMergefn = output+'/mergefile.gpkg'
    fileList = os.listdir(directory)

    #merge gpkg file
    first = True
    command = ''
    for file in fileList:
        if file.endswith(fileEndsWith) or file.endswith(fileEndsWith1):

            file1 = directory +"/"+ file

            if first:
                command = 'ogr2ogr ' + outputMergefn + ' ' + file1+' -nln mergefile'
                first = False
            else:
                command = 'ogr2ogr -update -append ' + outputMergefn + ' '  + file1+' -nln mergefile' 

            os.system(command)

    #gpkg to postgresql

    connection1 = r"host=localhost port=5432 dbname=postgres user=postgres password=postgres"
    schema = "public"
    command = 'ogr2ogr -f "PostgreSQL" PG:"%s" -lco SCHEMA=%s "%s" -overwrite -progress -lco OVERWRITE=YES' % (connection1, schema, outputMergefn)

    os.system(command)
    print("upload postgres succss:")

if __name__ == "__main__":
    combine()
