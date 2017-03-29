# -*- coding: utf-8 -*-


from __future__ import unicode_literals

import json
import os
from os import listdir
from os.path import isfile, join
import sys
import time
import random
from bs4 import BeautifulSoup

import shutil
i = 0
category_files = ['pol', 'sport', 'ent', 'tech', 'misc']
html_titles = ['politics', 'sport', 'entertainment', 'technology', 'other']
html_files = [x for x in listdir('html_files')]
for file_name in category_files:
    html_file_name = file_name + '.html'
    html_file = open(join('html_files', html_file_name), 'w')
    img_urls = []
    titles = []
    html_str = """
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <title>"""
    html_file.write(html_str.encode('utf8'))
    html_str = str(html_titles[i])
    html_file.write(html_str.encode('utf8'))
    html_str = """</title>
    <script id="twitter-wjs" type="text/javascript" async defer src="http://platform.twitter.com/widgets.js"></script>
    <link rel= "stylesheet" type ="text/css" href="style.css">
    <link rel="shortcut icon" href="inkpot.ico" type="image/x-icon">
    <body>


    <div class="container">

    <header>
       <h1>INKBOT</h1>
    <div class="btn-group">
      <a href = "misc.html"><button class="button">Miscellaneous</button></a>
      <a href = "tech.html"><button class="button">Technology</button></a>
      <a href = "ent.html"><button class="button">Entertainment</button></a>
      <a href = "sport.html"><button class="button">Sports</button></a>
      <a href = "pol.html"><button class="button">Politics</button></a>
      <a href = "index.html"><button class="button">Home</button></a>

    </div></header>
    <body>
    <div id="body">
    <!-- BEGIN content -->
    <div id="content">
    """
    html_file.write(html_str.encode('utf8'))
    sub_html_files = [x for x in html_files if x.startswith(html_titles[i])]
    for sub_file_name in sub_html_files:
        print(sub_file_name)
    for sub_file_name in sub_html_files:
        sub_file = open(join('html_files', sub_file_name), 'r')
        soup = BeautifulSoup(sub_file, "lxml")
        title = soup.title.string
        titles.append(title)
        imgs = soup.findAll("img")
        for img in imgs:
            img_url = img["src"]
            img_urls.append(str(img_url))
    for j in range(len(sub_html_files)):
        print(sub_html_files[j])
        html_str = """
        <div class="f post"> <a href=" """
        html_file.write(html_str.encode('utf8'))
        html_str = str(sub_html_files[j])
        html_file.write(html_str.encode('utf8'))
        html_str = """
    "><img src="
        """
        html_file.write(html_str.encode('utf8'))
        html_str = img_urls[j]
        html_file.write(html_str.encode('utf8'))
        html_str = """
        " alt="" />
            <p>"""
        html_file.write(html_str.encode('utf8'))
        html_str = titles[j]
        html_file.write(html_str.encode('utf8'))
        html_str = """</p></a>
        </div>
        <hr>
        """
        html_file.write(html_str.encode('utf8'))
    

    

    
    html_str = """</div>
    </div>
    </body>
    </html>
    """
    i+=1

    html_file.write(html_str.encode('utf8'))

    html_file.close()
    
