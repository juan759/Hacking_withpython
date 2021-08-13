#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 13 11:53:45 2021

@author: juan
"""

from cryptography.fernet import Fernet
import os

def load_key():
    return open('key.key','rb')

def de_encrypt(items,key):
    f = Fernet(key)
    for item in items:
        with open(item,'rb') as file:
            encrypted_data = file.read()
        decrypted_data = f.decrypt(encrypted_data)
        with open(item,'wb') as file:
            file.write(decrypted_data)
            
if __name__ == '__main__':
    path_to_encrypt = '//home//juan//PythonUdemy//security//victima'
    os.remove(path_to_encrypt+'\\'+'rescate.txt')
    
    items = os.listdir(path_to_encrypt)
    full_path = [path_to_encrypt+'\\'+item for item in items]
    
    key = load_key()
    
    de_encrypt(full_path,key)
    