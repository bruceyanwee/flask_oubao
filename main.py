# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
from flask import Flask,jsonify,request,render_template
from flask_cors import CORS,cross_origin
app = Flask(__name__)
CORS(app, supports_credentials=True)

import gensim
import jieba
from scipy.linalg import norm
import pandas as pd
import numpy as np
model_file3 = './data/Tencent_AILab_ChineseEmbedding_Min.txt'
model3 = gensim.models.KeyedVectors.load_word2vec_format(model_file3,binary=False)
df_qa_set = pd.read_csv('./data/qa_set_all.csv')
# 相似度计算函数
def vector_similarity_Tencent(s1, s2):
    def is_not_found_w(w):
        return True if w not in model3.key_to_index else False
    def sentence_vector(s):
        words = jieba.lcut(s)
        v = np.zeros(200)
        for word in words:
            if not is_not_found_w(word):            
                v += model3[word]            
        v /= len(words)
        return v    
    v1, v2 = sentence_vector(s1), sentence_vector(s2)
    return np.dot(v1, v2) / (norm(v1) * norm(v2))
# 匹配最相似的top-n
def match_top_n(qa_set,query,sim_func,n):
    df = qa_set.copy()
    df['q_new'] = query
    df['sim'] = df.apply(lambda row:sim_func(row['questions'],row['q_new']),axis=1)
    return df.sort_values(by='sim',ascending=False).head(n)['answers'].tolist()


@app.route("/test",methods=['GET', 'POST'])
def test():
    print('ok')
    f = request.files['file']
    return 'upfile ok'

@app.route("/query",methods=['POST'])
def query():
    question = request.form.get('query')
    ans = match_top_n(df_qa_set,question,vector_similarity_Tencent,1)
    response_data = {
        'query':question,
        'answer':ans
        }
    return jsonify(response_data)


# 上传文件的
# 存放路径
file_base_path = '/root/home/wwj/'
file_paths = {
    'test':'test/',
    'hot_video':'hot_video/',
    'hot_img':'hot_img/'
}
@app.route('/upload/',methods=['GET', 'POST'])
def upload_res():
    if request.method == 'GET':
        return render_template('upload_file.html')
    else:
        f = request.files['up_file']
        path = file_base_path+file_paths['test']+f.filename
        f.save(path)
        return 'upload sucess'

# 关于育儿知识智能问答函数功能
# Tencent 发布的800w的词向量，但是太大，只截取了1w个高频的词

app.run(host="0.0.0.0",port=5000)