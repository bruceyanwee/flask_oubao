# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import json
from flask import Flask,jsonify,request,render_template
from flask_cors import CORS,cross_origin
app = Flask(__name__)
CORS(app, supports_credentials=True)

@app.route("/test",methods=['GET', 'POST'])
def test():
    print('ok')
    f = request.files['file']
    return 'upfile ok'

@app.route("/query",methods=['POST'])
def query():
    question = request.form.get('query')
    response_data = {
        'query':question,
        'answer':'api test ok'
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

app.run(host="0.0.0.0",port=5000)