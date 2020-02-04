#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
import os
import struct_bit
import struct_all
def __get_input_dir_name(dir_name):
    dir_list = []
    try:
        file_dir = os.getcwd() + '\\' + dir_name
        for root, dirs, files in os.walk(file_dir):
            root = root.split('\\')
            dir_list.append(root[-1])
        return dir_list
    except:
        print('file not exist or corupted')
        sys.exit()
        
def dir_process(dir_name):
    file_list = []
    dir_list = __get_input_dir_name(dir_name) 
    try:
        for sub_dir in dir_list[1:]:
            struct_bit.get_struct_bit(dir_name,sub_dir)
            struct_all.get_struct_all(dir_name,sub_dir)              
        return file_list
    except:
        print('file not exist or corupted')
        sys.exit()
                   
def main(argv=None):
    if argv is None:
        argv = sys.argv
        if len(argv) < 2:
            print('please set argv as log file')
        else:   
            dir_process(argv[1])                       
            print('generate file end!');            

if __name__ == "__main__":
    sys.exit(main())
 