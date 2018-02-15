# -*- coding:utf-8 -*-

import os 
import shutil
import time
import re
import constant

# 模型参数
MODULE_NAME = 'melody_rnn_generate'
BUNDLE_CONFIG = 'basic_rnn'
BUNDLE_FILE = '/tmp/MagenServer/server/magenta_modules/basic_rnn.mag'
OUTPUT_DIR = '/tmp/t/MagenServer/server/generate'
NUM_OUTPUT = 1
NUM_STEPS = 256
PRIMER_MIDI = ''

# 转换格式参数
TRANS_NAME = 'sonic-annotator'
PLUGIN_NAME = 'vamp:silvet:silvet:notes'
TRANS_TO = 'midi'

def generate_midi(filepath):
	command = MODULE_NAME + ' --config=' + BUNDLE_CONFIG + \
							' --bundle_file=' + BUNDLE_FILE + \
							' --output_dir=' + OUTPUT_DIR + \
							' --num_outputs=' + str(NUM_OUTPUT) + \
							' --num_steps=' + str(NUM_STEPS) + \
							' --primer_midi=' + filepath
	os.system(command)
	
def get_generatefile():
	currenttime = time.strftime('%Y-%m-%d_%H%M',time.localtime(time.time()))
	# 通过re.compile()函数生成一个正则表达式对象，找出生成的音乐文件
	pattern = re.compile(currenttime+r'[0-9_]*\.mid$')
	filelist = os.listdir(OUTPUT_DIR)
	for index,f in enumerate(filelist): # 通过enumerate()函数来获取循环时迭代器当前的索引，判断是否到了最后一个文件
		if pattern.match(f): # 如果找到匹配文件，就返回（一般只有一个文件，所以找到就返回）
			return f
		elif(index == len(filelist)):
			return 'No match file'
			
def wav2midi(filename):
	os.chdir(constant.WAV_UPLOAD_FOLDER)
	command = TRANS_NAME + ' ' + filename + ' -d ' + PLUGIN_NAME + ' -w ' + TRANS_TO
	os.system(command)
	midiname = re.sub(r'wav$', 'mid', filename)
	shutil.move(constant.WAV_UPLOAD_FOLDER + '/' + midiname, constant.MIDI_UPLOAD_FOLDER + '/' + midiname)
	os.chdir(constant.SERVER_ROOT_DIR)
	
	return midiname











