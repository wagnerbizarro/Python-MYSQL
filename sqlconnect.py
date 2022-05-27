#!/bin/python3
import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="python",
    password="python",
    database="cars"
)
#print(mydb)

cursor = db.cursor()
