#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 10:57:46 2018

@author: Ygor Pitombeira
"""
from lib import schedule
from lib.task import taskModel
from lib.database import dbsql, table
from lib.sap import sapvbs
from lib.regex import RegExec

from lib.report import PlotLine

class task(taskModel):
        
<<<<<<< HEAD
    def scheduleJob(self):
        self.scheduleJob = schedule.every(10).seconds.tag('t0001','tasks')
        return self.scheduleJob
=======
    def execute(self):
>>>>>>> parent of 1a2c80d... shedule task periodic complete
        
        if not super().dispatcher():
            return 0      
        super().execute()
                    
         # 1) Criando e conectando estrutura de dados e DB
        
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
        tb.db.script_file("t0001_sqlcreaper.txt")
#        
#        
#        # 2) Vbscript - Extraindo dados do SAP
#        
#        sap1 = sapvbs("t0001_medncon.vbs","t0001_medncon.txt")       
#        sap1.execute()
#
#        sap2 = sapvbs("t0001_medconc.vbs","t0001_medconc.txt")   
#        
#        subs = [('#DTSTART#','01.01.2013'),
#                ('#DTEND#','09.10.2018'),]
#        
#        sap2.subs(subs)
#        sap2.execute()
#        
#        # 3) Aplicar regex para extracao das informacoes
#        
#        Patern = '\|\w?\s*(?P<Item>\d+)\s*\|\s*(?P<Medida>\d+)\s*\|\s*(?P<Nota>\d+)\s*\|\s*(?P<Ordem>\d*)\s*\|(?P<Prioridade>\d*)\|(?P<TextoMedida>[^\|]+)\s*\|(?P<TextoItem>[^\|]*)\|(?P<CenTrabRes>[^\|\s]*)\s*\|(?P<StatusUsu>[^\|]+)\s*\|(?P<StatusSis>[^\|]+)\|(?P<LocalInst>[^\|]+)\s*\|(?P<CenTrabExe>[^\|\s]*)\s*\|[^\|]*\|[^\|]*\|[^\|]*\|(?P<DataNota>[^\|]+)\|(?P<DataConc>[^\|]*)\|\s*(?P<ArO>[^\|]+)\s*\|\s*(?P<CodMed>\w*)'
#        data1 = RegExec(Patern, sap1.outputFilePath)
#        data2 = RegExec(Patern, sap2.outputFilePath)
#        
#        # 4) Salva informacoes no banco de dados
#        
#        tb.insert(data1)
#        tb.insert(data2)
#        
        PlotLine(tb.db.output_file("t0001_sqlcalcmed.txt"))
        
<<<<<<< HEAD
        schedule.cancel_job(self.scheduleJob)       
=======
        return schedule.CancelJob         
>>>>>>> parent of 1a2c80d... shedule task periodic complete
        
t0001 = task()
