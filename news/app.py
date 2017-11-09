#! /usr/bin/env pyhton3
# -*- coding:utf-8 -*-

import os, json
from flask import Flask, render_template

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

filepath = "/home/shiyanlou/files"

def loadfiles(filepath):
    dict = {}
    for path,subdirs,files in os.walk(filepath):
        for name in files:
            new_path = os.path.join(path,name)
            new_name = name.split('.')
            new_content = json.load(open(new_path, 'r'))
            dict[new_name[0]] =  new_content 
    return dict

result = loadfiles(filepath)

@app.route('/')

def index():
    
    return render_template('index.html', course=result)

@app.route('/files/<filename>')

def file(filename):
    if filename in result:
        return render_template('file.html', course=result[filename])

@app.errorhandler(404)

def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(host='127.0.0.1',port=3000, debug=True)
