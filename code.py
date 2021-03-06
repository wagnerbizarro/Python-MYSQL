#!/bin/python3
import mysql.connector

# Connection MYSQL
#--------------------------#
db = mysql.connector.connect(
    host="localhost",
    user="python",
    password="python",
    database="cars"
)

#print(mydb)

cursor = db.cursor()
#-----------------------#

#Functions Query
#------------------------#
def insert (brand,model,year):
    sql_query_insert = "INSERT INTO mycars(brand, model, year) VALUES(%s,%s,%s)"
    values = (brand,model,year)
    cursor.execute(sql_query_insert, values)
    db.commit()
    print(cursor.rowcount, "record inserted")

def delete (id):
    sql_query_delete = "DELETE FROM mycars WHERE id = %s"
    sql_data = id
    cursor.execute(sql_query_delete, (sql_data,))
    db.commit()
    print(cursor.rowcount, "record deleted")

def select_brand(brand):
    sql_query_select = "SELECT * FROM mycars WHERE brand = %s"
    sql_data = brand
    cursor.execute(sql_query_select, (sql_data,))
    result = cursor.fetchall()
    for x in result:
        print(x)

def select_model(model):
    sql_query_select = "SELECT * FROM mycars WHERE model= %s"
    sql_data = model
    cursor.execute(sql_query_select, (sql_data,))
    result = cursor.fetchall()
    for x in result:
        print(x)

def select_all():
    sql_query_select = "SELECT * FROM mycars"
    cursor.execute(sql_query_select)
    result = cursor.fetchall()
    for x in result:
        print(x)
#------------------------------------#

#Menu
#-------------------------------------#
menu = 50
submenu = 50
while menu != '0':
    menu = input("0-Exit\n1-Show\n2-Insert\n3-Delete\n:")

    if menu == '0':
        break

    elif menu == '1':
        print("\n" *10)
        print("Show")
        while submenu != '0':
            submenu = input("0-Exit\n1-All\n2-Model\n3-Brand\n:")

            if submenu == '0':
                break

            elif submenu == "1":
                select_all()
                input("\nPress ENTER to Go Back")
            
            elif submenu == "2":
                model = input("Model:")
                select_model(model)
                input("\nPress ENTER to Go Back")
            
            elif submenu == "3":
                brand = input("Brand:")
                select_brand(brand)
                input("\nPress ENTER to Go Back")

    elif menu == '2':
        print("\n" *10)
        print("Insert")
        brand = input("\nBrand:")
        model = input("\nModel:")
        year = input("\nYear:")
        insert(brand,model,year)
        input("\nPress ENTER to Go Back")

    elif menu == '3':
        print("\n" *10)
        print("Delete")
        id = input("ID:")
        delete(id)
        input("\nPress ENTER to Go Back")
