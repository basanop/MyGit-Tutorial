# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 14:41:05 2016

@author: Isaiahellad
"""
import sqlite3
conn = sqlite3.connect('C:/Pytutorials/Section2/Source Code/tutorial.db')
c = conn.cursor()

def create_table():
    c.execute("CREATE TABLE example(Language VARCHAR, Version REAL, Skill TEXT)")
#conn.close()
def enter_data():
    c.execute("INSERT INTO example VALUES('R',3.8,'Expert')")
    conn.commit()
    
#enter_data()
#conn.close()

def createCarsTB():
    
    with conn:
        
        cur = conn.cursor()    
        cur.execute("CREATE TABLE Cars(Id INT, Name TEXT, Price INT)")
        cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
        cur.execute("INSERT INTO Cars VALUES(2,'Mercedes',57127)")
        cur.execute("INSERT INTO Cars VALUES(3,'Skoda',9000)")
        cur.execute("INSERT INTO Cars VALUES(4,'Volvo',29000)")
        cur.execute("INSERT INTO Cars VALUES(5,'Bentley',350000)")
        cur.execute("INSERT INTO Cars VALUES(6,'Citroen',21000)")
        cur.execute("INSERT INTO Cars VALUES(7,'Hummer',41400)")
        cur.execute("INSERT INTO Cars VALUES(8,'Volkswagen',21600)")
        

createCarsTB()
conn.close()