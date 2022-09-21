from fileinput import filename
from app import app
from flask import request, render_template
import os
from skimage.metrics import structural_similarity
import imutils
import cv2
from PIL import Image
import requests



app.config['INITIAL_FILE_UPLOADS']='app/statics/uploads'
app.config['EXISTING_FILE']='app/statics/original'
app.config['GENERATED_FILE']='app/statics/generated'



@app.route("/", methods=["GET","POST"])

def index():
    if request.method=="GET":
        return render_tempalte("index.html")
    id request.method=="POST":
    file_upload=request.files['file_upload']
    filename=file_upload.filename
    