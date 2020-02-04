#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import re
import os

def __read_file_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = (file.read())
            lines = lines.split('\n')        
    except:
        print('file not exist or corupted')
        sys.exit()
    return lines  
       
def __get_input_file_name(dir_name,sub_dir):
    file_list = []
    try:
        file_dir = os.getcwd() + '\\' + dir_name + '\\' + sub_dir
        for root, dirs, files in os.walk(file_dir):
            for file in files:
                if os.path.splitext(file)[1] == '.h':                                      
                    file_list.append(os.path.join(root,file))
        return file_list
    except:
        print('file not exist or corupted')
        sys.exit()
    
def __mkdir_out_filefolder():
    try:
        myfile = os.getcwd()+'\\out_dir'
        if not os.path.exists(myfile):
            os.mkdir(myfile)
    except:
        print('file not exist or corupted')
        sys.exit()
        
def __demo_file_line_process_module(line,demo_lines,oldstr):
    demo_lines_out = [] 
    try:
        modulestr = line.split('\"')[1]
        modulestr = modulestr.split('[')[0]
        modulestr = modulestr.upper()
        for demo_line in demo_lines: 
            demo_line = demo_line.replace(oldstr,modulestr) 
            demo_lines_out.append(demo_line)                                
    except:
        print('len of line is 1 ')
        sys.exit() 
    return demo_lines_out  

def __demo_file_line_process_bit(line,demo_lines,oldstr):
    demo_lines_out = [] 
    modulestr = line.split(' ')
    modulestr = modulestr[0]
    modulestr = modulestr.upper()
    try:
        for demo_line in demo_lines: 
            demo_line = demo_line.replace(oldstr,modulestr)
            demo_lines_out.append(demo_line)                                
    except:
        print('len of line is 1 ')
        sys.exit() 
    return demo_lines_out  

def __get_output_file_name(out_file_name):
    try:       
        out_file_name = out_file_name.lower()
        out_file_name = 'out_dir\\' + out_file_name + '_'+ 'struct_interface_bit.h'    
        return out_file_name     
    except:
        print('len of line is 1 ')
        sys.exit() 
             
def __file_line_process(lines,demo_lines): 
    demo_lines_out = demo_lines
    try: 
        demo_lines_out = __demo_file_line_process_module(lines[0],demo_lines_out,'AAAAA')
        demo_lines_out = __demo_file_line_process_module(lines[1],demo_lines_out,'BBBBB')
        oldstr = 'NULL'
        counter = 0
        for line in lines[2:]: 
            line_check = line[0:1]             
            if line_check !='' and line_check !='\n' and line_check !=' ' :        
                oldstr1 = oldstr + str(counter)
                demo_lines_out = __demo_file_line_process_bit(line,demo_lines_out,oldstr1) 
                counter = counter+1 
        return demo_lines_out     
    except:
        print('len of line is 22 ')
        sys.exit()  
         
def __wirte_list_to_file(list_out,file_name):
    try:
        with open(file_name, 'w+') as file:
            file_name = file_name.split('\\')
            file_name = file_name[-1]
            file_name = file_name.replace('.','_')
            file_name1 = '#ifndef ' + file_name.upper()+'\n'
            file_name2 = '#define ' + file_name.upper()+'\n'
            file.write(file_name1)
            file.write(file_name2)
            file.write('\n'.join(list_out)) 
            file.write('\n#endif\n')
    except:
        print('file not exist or corupted')
        sys.exit()
 
def __file_read_process(file_all,demo_lines,sub_dir):
    demo_lines_out_all = []
    for file_name in file_all:      
        lines = __read_file_lines(file_name)
        demo_lines_out = __file_line_process(lines,demo_lines)
        demo_lines_out_all = demo_lines_out_all + demo_lines_out
    out_file_name = __get_output_file_name(sub_dir)
    __wirte_list_to_file(demo_lines_out_all,out_file_name)
    
    
def  get_struct_bit(dir_name,sub_dir):
    file_list = __get_input_file_name(dir_name,sub_dir)
    demo_lines = __read_file_lines('demo.h')
    __mkdir_out_filefolder()     
    __file_read_process(file_list,demo_lines,sub_dir)
                          
def main(argv=None):
    if argv is None:
        argv = sys.argv
        if len(argv) < 2:
            print('please set argv as log file')
        else:                                           
            get_struct_bit(argv[1])            
            print('generate file end');            

if __name__ == "__main__":
    sys.exit(main())
 