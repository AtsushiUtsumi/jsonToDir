# -*- coding: utf-8 -*-
import codecs
import json
import os
# ブレースがディレクトリ
def list_parser(level, list):
    for i in list:
        if type(i) is dict:
            dict_parser(level + 1, i)
        else:
            print("エラー:リストの中身は辞書型である必要があります")

def dict_parser(level, dict):
    directory_name = dict["name"]
    os.mkdir(directory_name)
    os.chdir(directory_name)
    file_name_list = dict["files"]
    for file_name in file_name_list:
        output_file = codecs.open(file_name, 'w', 'utf8')
        output_file.close()        
    directory_list = dict["directories"]
    list_parser(level + 1, directory_list)
    os.chdir('..')
    
input_file = codecs.open('onion.json', 'r', "utf8")
json_dict = json.load(input_file)

output_directory_name = 'output'
import shutil
if os.path.isdir(output_directory_name):
    shutil.rmtree(output_directory_name)
os.mkdir(output_directory_name)
os.chdir(output_directory_name)
dict_parser(0, json_dict)
os.chdir('..')