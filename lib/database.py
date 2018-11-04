# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 13:48:23 2018

@author: wu3y
"""

import sqlite3
import os

class db:
     
    def __init__(self, Path=None, PathSec=None, File=None):
        
        if Path:
            self.Path = Path
        else:
            self.Path = os.getcwd()
            
        if PathSec:
            self.PathSec = PathSec
        else:
            self.PathSec = os.path.join(self.Path, 'data')
        
        if File:
            self.File = os.path.join(self.Path,File)
        else:
            self.File = os.path.join(self.Path,'data.db')
 
        
class sql:
    
    def __init__(self, db, SQL = '', File = '', DataIn = []):
        self.db = db
        self.File = File
        self.SQL = SQL
        self.DataIn = DataIn
        self.ScriptProp = False
        self.OutProp = True
        self.columns = None
        self.result = None
        self.axis = None
        self.legends = None
        
    @property
    def script(self):
        self.ScriptProp = True
        return self
    
    @property
    def nout(self):
        self.OutProp = False
        return self

    def execute(self):
        if self.SQL or self.File:
            conn = sqlite3.connect(self.db.File)
            cursor = conn.cursor()
            SQL = self.SQL
            
            if self.File:
                File = os.path.join(self.db.PathSec,self.File)
                SQL = open(File,"r").read()
                
            if self.DataIn:
                cursor.executemany(SQL, self.DataIn)
            else:
                if self.ScriptProp:
                    cursor.executescript(SQL)
                else:
                    cursor.execute(SQL)
                    
            if self.OutProp:
                self.result = cursor.fetchall()
                self.axis = list(zip(*self.resrows))
                self.columns = list(zip(*cursor.description))[0]
                # Legenda para ser utilizada nas plotagens
                self.legends = self.columns[1:]
            
            conn.commit()  
            conn.close()
            
        return self
            

class table:
 
    def __init__(self, db, tbname, columns):
        
        self.db = db
        columns.append(('id','INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT'))
        self.qtdcols = len(columns)
        self.qtdcolsD = self.qtdcols - 1 
        self.columns = ",".join([c[0] for c in columns])
        self.columnsD = ",".join([c[0] for c in columns if c[0].upper() != 'ID'])
        self.columnstr_create = ",".join(["%s %s"%(c[0],c[1]) for c in columns])
        self.tbname = tbname
        
        sql(db=self.db, SQL="CREATE TABLE IF NOT EXISTS %s (%s)"%(self.tbname, self.columnstr_create)).nout.execute()
        
    def insert(self, DataList):
        fieldsRep = ",".join(["?" for x in range(0, self.qtdcolsD)])
        sql(db=self.db, SQL="INSERT INTO %s (%s) VALUES (%s)"%(self.tbname,self.columnsD,fieldsRep), DataIn=DataList).nout.execute()
        
    def select(self, SQL):
        sqlsel = sql(db=self.db, SQL="SELECT %s FROM %s"%(SQL, self.tbname)).execute()
        return sqlsel.resrows
    
    def clear(self):
        sql(db=self.db, SQL="DELETE FROM %s"%(self.tbname)).nout.execute()

    def drop(self):
        sql(db=self.db, sSQL="DROP TABLE %s"%(self.tbname)).nout.execute()    