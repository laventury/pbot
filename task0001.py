#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 10:57:46 2018

@author: ygor
"""

from lib.task import taskModel
from lib.database import dbsql, table
from lib.sap import sapvbs
import os

class task(taskModel):

    def execute(self):
        
        super(task, self).execute()

        # Criando e conectando estrutura de dados e DB
        
        db = dbsql()
        
        columns = [
        	('id','INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'),
        	('item','INTEGER'),
        	('medida','INTEGER'),
        	('nota','VARCHAR(20)'),
        	('ordem','VARCHAR(20)'),
        	('prioridade','integer'),
        	('texto_medida','TEXT'),
        	('texto_item','TEXT'),
        	('centrabres','VARCHAR(12)'),
        	('status_usu','VARCHAR(30)'),
        	('status_sis','VARCHAR(30)'),
        	('local','varchar(50)'),
        	('centrabexe','VARCHAR(12)'),
        	('datanota','varchar(20)'),
        	('dataconc','varchar(20)'),
        	('ArO','varchar(10)'),
        	('CodMed','varchar(3)')
            ]
        
        tb = table(db, "t0001_medidas", columns)
        
        # Vbscript 
        
        sap = sapvbs("t0001_medidas.vbs","t0001_output.txt")
        
        #   Vbs - Substituindo template
        
        fileInput = "t0001_notas.txt"
        
        values = [("#FILEINPUT#", fileInput)]
        sap.subs(values)
        
        # Consulta notas atuais abertas e salva no arquivo de entradas 
        
        selNotes = tb.db.output("SELECT DISTINCT nota FROM t0001_medidas WHERE status_sis NOT LIKE '%MSUC%'")
        
        strNotes = "\n".join([x[0] for x in selNotes])
        
        fileInputPath = os.path.join(sap.path,fileInput)
        file = open(fileInputPath,"w+")
        file.write(strNotes)
        
        #sap.execute()
        
        
task_X = task()