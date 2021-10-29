from flask import Flask, flash, request, redirect, render_template, url_for, send_file, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS
import ogr ,os, sys
import psycopg2
import osgeo.ogr  
import pandas as pd

from mergefile import combine

app=Flask(__name__)
CORS(app)

#file upload 
app.secret_key = "secretiskey" 
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
path = os.getcwd()
print(path)
UPLOAD_FOLDER = os.path.join(path, 'uploads')
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['gpkg','shp'])
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html', title="well come to bisag-n")

@app.route('/upload_form')
def upload_form():
    return render_template('upload2.html', title="Select file(s) to upload")


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('File(s) successfully uploaded')
        return redirect('/upload_form')

@app.route('/merge')
def merge():
    combine()
    flash('files merge successfully')
    flash('merge file store in database successfully')

    return redirect(url_for('merge_file'))

@app.route('/merge_file')
def merge_file():

    # connection = psycopg2.connect(user="postgres", password="postgres", host="localhost", database="postgres")
    # cursor = connection.cursor()
    # cursor.execute("SELECT * FROM mergefile")
    # list11 = cursor.fetchall()

    # row =[]
    # for i in list11:
    #     r = str(i)
    #     r = r.replace("("," ")
    #     r = r.replace(")"," ")
    #     r = r.replace("'"," ")
    #     r = r.replace(","," ")
    #     row.append(r)
    # #print(r)

    # cursor.close()
    # connection.close()

    # df = pd.DataFrame(row)
    # html = df.to_html()

    return render_template('combile.html',  title="merge youre uploaded files")



@app.route('/download')
def download_file():
    path = os.getcwd()
    output = os.path.join(path, 'merge') +"/mergefile.gpkg"

    return send_file(output, as_attachment=True)



if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5389)
    
