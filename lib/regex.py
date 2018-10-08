# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:42:51 2018

@author: ygor Pitombeira

    Ler arquivo de dados em formato de texto,
    aplica regex a partir de um arquivo Pattern 
    
    Entrada : Arquivo de texto
    Saida : [('AAA','bbb'),('ddd','www')]
"""

import re

def RegexFile(FileRgx, DataFileIn):
    DataFile = open(DataFileIn,"r").read()
    DataFile = re.sub('(\d{2}).(\d{2}).(\d{4})','\g<3>-\g<2>-\g<1>',DataFile)

    Patern = open(FileRgx,"r").read()
    Data = re.findall(Patern, DataFile)    
       
    return Data