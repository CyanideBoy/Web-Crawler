# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 11:51:31 2018

@author: SONU
"""

import os

def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating new project "+directory)
        os.makedirs(directory)
        
# create queue and crawled files
def create_data_files(project_name,base_url):
    queue = project_name + '/queue.txt'
    crawled = project_name + '/crawled.txt'
    emails = project_name + '/emails.txt'
    
    if not os.path.isfile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')
    if not os.path.isfile(emails):
        write_file(emails,'')
        
# create a new file
def write_file(path,data):
    f = open(path,'w')
    f.write(data)
    f.close()
    
# Adds data to existing file

def append_to_file(path,data):
    with open(path,'a') as file:
        file.write(data+'\n')
        
#delete everything inside
def delete_file_contents(path):
    with open(path,'w'):
        pass


#File to set & reverse
        
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

def set_to_file(links,file):
    delete_file_contents(file)
    for link in sorted(links):
        append_to_file(file,link)

    
    
    


        




    
        
    
        

