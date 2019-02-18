#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import gensim

from flask import Flask,render_template, request,json,jsonify

#this part to get the absloute path to our model file
import sys
from imp import reload
reload(sys)

#type here the model name you have during kaggle's tutorial.

# my_dir = os.path.dirname(__file__)
# model_file_path = os.path.join(my_dir, model_name)
model = gensim.models.word2vec.Word2Vec.load_word2vec_format("GoogleNews-vectors-negative300.bin.gz", binary=True)
# model = gensim.models.keyedvectors.KeyedVectors.load_word2vec_format("GoogleNews-vectors-negative300.bin.gz", binary=True, limit = 2000)

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

@app.route('/ajaxhandlerForm1', methods=['POST'])
def ajax_handler_form1():
    first =  request.form.get('first', None)
    second = request.form.get('second', None)
    third= request.form.get('third', None)
    fourth =request.form.get('fourth', None)
    result1 = 'Remplir le formulaire'
    if (first and second and third and fourth) :
        # result = model.doesnt_match (("%s %s %s %s"%(a_first,a_second,a_third,a_fourth)).split())
        result1 = model.doesnt_match (("%s %s %s %s"%(first,second,third,fourth)).split())
    else:
        result1 = 'Remplir le formulaire'

    return jsonify({'result1':result1})


@app.route('/ajaxhandlerForm2', methods=['POST'])
def ajax_handler_form2():
    first =  request.form.get('first', None)
    second = request.form.get('second', None)
    third= request.form.get('third', None)

    result2 = 'Remplir le formulaire'
    if (first and second and third) :
        result2 = model.most_similar(positive = [second, third], negative=[first], topn = 1)[0]
    else:
        result2 = 'Remplir le formulaire'

    return jsonify({'result2':result2})


if __name__=="__main__":
    app.run(debug=True)
