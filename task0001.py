#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 10:57:46 2018

@author: Ygor Pitombeira
"""
from lib import schedule
from lib.database import dbsql, table
from lib.sap import sapvbs
from lib.regex import RegExec
from lib.report import PlotLine
from datetime import datetime, date

class taskModel:

    def scheduleJob(self):
        dtStart = datetime(2018, 10, 15, 14, 44)
        self.scheduleJob = schedule.every().second.start(dtStart).tag('t0001','tasks')
        return self.scheduleJob

    def job(self):
     
       
        #1) Criando e conectando estrutura de dados e DB

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


        # 2) Vbscript - Extraindo dados do SAP
        
        # 2.1) medidas nao concluidas
        sapmnc = sapvbs("t0001_medncon.vbs","t0001_medncon.txt")
        sapmnc.openSAP("txt.sap")               
        sapmnc.execute()

        # 2.2) medidas concluidas
        sapmco = sapvbs("t0001_medconc.vbs","t0001_medconc.txt")
        
        DtStart = '06.10.2018' # Falta implementar lógica de ultima pesquisa
        DtEnd = date.today().strftime("%d.%m.%y")
        subs = [('#DTSTART#',DtStart),
                ('#DTEND#',DtEnd),]

        sapmco.subs(subs)
        sapmco.execute()

        # 3) Aplicar regex para extracao das informacoes

        Patern = '\|\w?\s*(?P<Item>\d+)\s*\|\s*(?P<Medida>\d+)\s*\|\s*(?P<Nota>\d+)\s*\|\s*(?P<Ordem>\d*)\s*\|(?P<Prioridade>\d*)\|(?P<TextoMedida>[^\|]+)\s*\|(?P<TextoItem>[^\|]*)\|(?P<CenTrabRes>[^\|\s]*)\s*\|(?P<StatusUsu>[^\|]+)\s*\|(?P<StatusSis>[^\|]+)\|(?P<LocalInst>[^\|]+)\s*\|(?P<CenTrabExe>[^\|\s]*)\s*\|[^\|]*\|[^\|]*\|[^\|]*\|(?P<DataNota>[^\|]+)\|(?P<DataConc>[^\|]*)\|\s*(?P<ArO>[^\|]+)\s*\|\s*(?P<CodMed>\w*)'
        datamnc = RegExec(Patern, sapmnc.outputFilePath)
        datamco = RegExec(Patern, sapmco.outputFilePath)

        # 4) Salva informacoes no banco de dados
        tb.db.script("DELETE FROM " + tb.tbname + " WHERE status_sis NOT LIKE '%MSUC%'")
        tb.insert(datamnc)
        tb.insert(datamco)

        # 4.1) Consulta banco de dados e exibe resultado

        data3 = tb.db.output_file("t0001_sqlcalcmed.txt")

        PlotLine(data3)
        
        schedule.cancel_job(self.scheduleJob)