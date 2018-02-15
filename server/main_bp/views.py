# -*- coding:utf-8 -*-

import os
import time 
from flask import *
from werkzeug import secure_filename
from server.main_bp import main_bp
import constant
from generate import generate_midi,get_generatefile, wav2midi

# 规定文件格式只为midi文件
ALLOWED_EXTENSIONS = set(['midi', 'mid'])

def allowed_file(filename):
	return '.' in filename and filename.split('.', 1)[1] in ALLOWED_EXTENSIONS
	
def save_uploadfile(file, file_dir):
	securename = secure_filename(file.filename)
	filepath = os.path.join(file_dir, securename)
	file.save(filepath)
	# 返回文件路径供生成旋律函数调用
	return filepath

@main_bp.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		# 通过request对象的files属性来获取表单上传的文件
		file = request.files['file']
		if file and allowed_file(file.filename):
			filepath = save_uploadfile(file, constant.MIDI_UPLOAD_FOLDER)
			generate_midi(filepath)
			generate_file = get_generatefile()
			return u'Uploaded Successfully！ 文件保存在' + generate_file
		else:
			return 'Uploaded Failed'
	else:
		return render_template('index.html')


@main_bp.route('/api/audio', methods=['POST'])
@main_bp.route('/api/audio/<filename>', methods=['GET'])
def api_receivefile(filename=None):
	if request.method == 'POST':
		# files[] 的索引就是上传文件的name参数，如curl命令：-F "filename=@test.txt" filename就是name参数
		file = request.files['filename']
		filepath = save_uploadfile(file, constant.WAV_UPLOAD_FOLDER)
		data = {
			'upload_file' : filepath,
			'upload_state' : 'successed',
			'file_num' : 1
		}
		js = json.dumps(data)
		resp = Response(js, status=200, mimetype='application/json')
		
		return resp
	else:
	# 先通过api将文件转换成midi文件，
		upload_path = constant.WAV_UPLOAD_FOLDER + filename
		midiname = wav2midi(filename)
		generate_midi(constant.MIDI_UPLOAD_FOLDER + '/' + midiname)
		gen_file = get_generatefile()
		return send_from_directory(constant.GENERATE_DIR, midiname)
	
	
@main_bp.route('/hello')
def hello():
	return 'hello'
	

	