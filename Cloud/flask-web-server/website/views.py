import os
from flask import Blueprint, render_template, request, flash, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return redirect('/get_prediction', code=302)

@views.route('/about')
def about():
    return render_template('about.html')

    
@views.route('/dummy_images/Apple.png')
def imagefile():
    imagefile = send_from_directory('dummy_images', 'Apple.png')
    return imagefile

@views.route('/model.json')
def model():
    modelfile = send_from_directory('templates', 'model.json')
    return modelfile

@views.route('/dict.txt')
def dicttxt():
    dictfile = send_from_directory('templates', 'dict.txt')
    return dictfile
    
@views.route('/group1-shard1of1.bin')
def weight():
    weightfile = send_from_directory('templates', 'group1-shard1of1.bin')
    return weightfile