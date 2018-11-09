#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 17 10:57:46 2018

@author: Ygor Pitombeira
"""

from datetime import datetime
from datetime import date

from lib.task import taskModel
from tools.database import db,sql,table
from tools.sap import sap
from tools.regex import regex
from tools.panels import plot

class taskChild(taskModel):

    def __init__(self, id):
        super().__init__(id)
        self.scheduleJob.interval = 3
        self.scheduleJob.unit = 'minutes'
        self.scheduleJob.start(datetime(2018,10,19,12,00))

    def job(self):

        print("rodando task 1 : ",datetime.now())

#        # 1) Vbscript - Extraindo dados do SAP
#
#        # 1.1) medidas nao concluidas
#        sapmnc = sap(File="t0001_medncon.vbs",Output="t0001_medncon.txt")
#        sapmnc.connect("txt.sap")
#        sapmnc.execute()
#
#        # 1.2) medidas concluidas
#        sapmco = sap(File="t0001_medconc.vbs",Output="t0001_medconc.txt")
#
#        DtStart = '06.10.2018' # Falta implementar lógica de ultima pesquisa
#        DtEnd = date.today().strftime("%d.%m.%y")
#        subs = [('#DTSTART#',DtStart),
#                ('#DTEND#',DtEnd),]
#
#        sapmco.subs(subs)
#        sapmco.execute()

        # 2) Aplicar regex para extracao das informacoes

        Pattern = r'\|\w?\s*(?P<Item__integer>\d+)\s*\|\s*(?P<Medida__integer>\d+)\s*\|\s*(?P<Nota__text>\d+)\s*\|\s*(?P<Ordem__text>\d*)\s*\|(?P<Prioridade__integer>\d*)\|(?P<Texto_Medida__text>[^\|]+)\s*\|(?P<Texto_Item__text>[^\|]*)\|(?P<CenTrabRes__text>[^\|\s]*)\s*\|(?P<Status_Usu__text>[^\|]+)\s*\|(?P<Status_Sis__text>[^\|]+)\|(?P<LocalInst__text>[^\|]+)\s*\|(?P<CenTrabExe__text>[^\|\s]*)\s*\|[^\|]*\|[^\|]*\|[^\|]*\|(?P<DataNota__text>[^\|]+)\|(?P<DataConc__text>[^\|]*)\|\s*(?P<ArO__text>[^\|]+)\s*\|\s*(?P<CodMed__text>\w*)'
 
#        datamnc = regex(regex=Pattern, data=sapmnc.Output).execute()
#        datamco = regex(regex=Pattern, data=sapmco.Output).execute()
        datamnc = regex(regex=Pattern, data="t0001_medconc.txt").execute()
        datamco = regex(regex=Pattern, data="t0001_medconc.txt").execute()


         #3) Criando e conectando estrutura de dados e DB

        db1 = db()
        tb = table(db1,name="t0001_medidas", columns=datamnc.columns)
        sql(db1,File="t0001_sqlcreaper.txt").script.nout.execute()


        # 4) Salva informacoes no banco de dados
        sql(db1,SQL="DELETE FROM " + tb.tbname + " WHERE status_sis NOT LIKE '%MSUC%'").nout.execute()
        tb.insert(datamnc.result)
        tb.insert(datamco.result)

        # 4.1) Consulta banco de dados e exibe resultado

        DataPlot = sql(db1,File="t0001_sqlcalcmed.txt").execute()

        plot(title="Medidas",data=DataPlot.result,legends=DataPlot.legends).dt.my.show()


task = taskChild('t0001')
task.job()
