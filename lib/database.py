# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:48:23 2018

@author: wu3y
"""

import sqlite3
import os


class dbsql:
     
    def __init__(self):
        self.Path = os.getcwd()
        self.PathDat  = os.path.join(self.Path,'data')
        self.DbFileName = os.path.join(os.getcwd(),'data.db')
        self.conn = sqlite3.connect(self.DbFileName)
        self.cursor = self.conn.cursor()
    
    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def script(self,SQL):
        self.cursor.executescript(SQL)
        return None

    def script_file(self,FileSQL):
        FileSQLPath = os.path.join(self.PathDat,FileSQL)
        self.cursor.executescript(open(FileSQLPath,"r").read())
        return None

    def output(self,SQL):
        self.cursor.execute(SQL)
        return self.cursor.fetchall()
    
    def output_file(self,FileSQL):
        FileSQLPath = os.path.join(self.PathDat,FileSQL)
        self.cursor.execute(open(FileSQLPath,"r").read())
        return self.cursor.fetchall()
    
    def inputs(self,SQL,DataList):
        self.cursor.executemany(SQL, DataList)
        self.conn.commit() 
        return None

    def inputs_file(self,FileSQL,DataList):
        FileSQLPath = os.path.join(self.PathDat,FileSQL)
        self.cursor.executemany(open(FileSQLPath,"r").read(), DataList)
        self.conn.commit() 
        return None


class table:
 
    def __init__(self, db, tbname, columns):
        
        self.db = db
        self.qtdcols = len(columns)
        self.qtdcolsD = self.qtdcols - 1 
        self.columns = ",".join([c[0] for c in columns])
        self.columnsD = ",".join([c[0] for c in columns if c[0].upper() != 'ID'])
        self.columnstr_create = ",".join(["%s %s"%(c[0],c[1]) for c in columns])
        self.tbname = tbname
 
        self.db.script("CREATE TABLE IF NOT EXISTS %s (%s)"%(self.tbname, self.columnstr_create))
        
    def insert(self, DataList):
        fieldsRep = ",".join(["?" for x in range(0, self.qtdcolsD)])
        self.db.inputs("INSERT INTO %s (%s) VALUES (%s)"%(self.tbname,self.columnsD,fieldsRep), DataList)
        
    def select(self, SQL):
        return self.db.output("SELECT %s FROM %s"%(SQL, self.tbname))
    
    def clear(self):
        self.db.script("DELETE FROM %s"%(self.tbname))

    def drop(self):
        self.db.script("DROP TABLE %s"%(self.tbname))    