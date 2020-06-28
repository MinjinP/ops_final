#!/usr/bin/python3
#-*- coding: utf-8 -*-

import re
import sys
import requests
from bs4 import BeautifulSoup
from elasticsearch import Elasticsearch
import json
import io
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('final.html')

@app.route('/final', methods=['POST'])   
def post(num=None):

    if request.method == 'POST':
        pass
    elif request.method == 'GET':

        htm = request.args.get('ht')

        res = requests.get(htm)

        html = BeautifulSoup(res.content, 'html.parser')

  
        data_r = []

        datah1 = html.find_all('h1') #'h1' tag
        datah2 = html.find_all('h2') #'h2' tag
        datah3 = html.find_all('h3') #'h3' tag
        datah4 = html.find_all('h4') #'h4' tag
        datap = html.find_all('p') #'p' tag
        datali = html.find_all('li') #'li' tag

        result = []

        for n in range(len(datah1)):
            data_r.extend(datah1[n].get_text().lower().split())
        for n in range(len(datah2)):
            data_r.extend(datah2[n].get_text().lower().split())
        for n in range(len(datah3)):
            data_r.extend(datah3[n].get_text().lower().split())
        for n in range(len(datah4)):
            data_r.extend(datah4[n].get_text().lower().split())
        for n in range(len(datap)):
            data_r.extend(datap[n].get_text().lower().split())
        for n in range(len(datali)):
            data_r.extend(datali[n].get_text().lower().split())

    
        text =" ".join(data_r)

        line = re.sub('[-=+,#/\?:^$.@©*;\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', text)
    
        freq = []
        result.extend(line.split())

        for i in range(len(result)):
            freq.append(result.count(result[i]))

        dic = {}
        for k in range(len(result)):
            dic[result[k]] = freq[k]
        
        return htm


if __name__ == '__main__':
    app.debug = True
    app.run()
