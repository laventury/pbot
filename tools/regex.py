# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 21:42:51 2018

@author: ygor Pitombeira

    Ler arquivo de dados em formato de texto,
    aplica regex a partir de um arquivo pattern 
    
    Entrada : Arquivo de texto
    Saida : [('AAA','bbb'),('ddd','www')]
"""

import re
import os

class regex:
     
    def __init__(self, data, path=None, pathsec=None, regex=None, file=None):

        if path:
            self.path = path
        else:
            self.path = os.getcwd()
            
        if pathsec:
            self.pathsec = pathsec
        else:
            self.pathsec = os.path.join(self.path, 'data')
        
        self.file = file
        if file:
            self.file = os.path.join(self.pathsec,file)
  
        self.data = data
        if data:
            self.data = os.path.join(self.pathsec,data)

        self.regex = regex
        self.pattern = None    
        
        pattern = None
        
        if self.regex:
            pattern = self.regex
        else:
            if self.file:
                pattern = open(self.file,"r").read()
        
        if pattern:
            self.pattern = re.compile(pattern)
        
        columnsrow = list(self.pattern.groupindex.keys())
        columns = []
        
        for col in columnsrow:
            colnt = col.split('__')
            columns.append((colnt[0],colnt[1].upper()))
            
        self.columns = columns
        self.result = None
        
    def execute(self):
        datafile = open(self.data,"r").read()
        #Convertendo datas de padrão SAP para padrao SQL
        #datafile = re.sub('(\d{2}).(\d{2}).(\d{4})','\g<3>-\g<2>-\g<1>',datafile)
        #Aplicando regex no arquivo de dados
        if self.pattern:        
            self.result = self.pattern.findall(datafile)
        return self
