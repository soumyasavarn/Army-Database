import mysql.connector
import pandas as pd
import random


#commit function
def add_officer(uid, officer_name, officer_rank, officer_unit, married, accomadation, mess_member, guest):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        if (guest):
            uid = "Guest" + str(random.randint(1, 10000))
            insert_query = """INSERT INTO OFFICERS (UID, NAME, IS_GUEST)
                          VALUES (%s, %s,%s)"""
            cursor.execute(insert_query, (uid, officer_name, guest))
        else:
            insert_query = """INSERT INTO OFFICERS (UID, NAME, OFFICER_RANK, UNIT, IS_MESS_MEMBER, IS_MARRIED, ACCOMADATION_AVAILED, IS_GUEST)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(insert_query, (uid, officer_name, officer_rank, officer_unit, mess_member, married, accomadation, guest))
            
        connection.commit()
        return "Added successfully."
        connection.close()
    except mysql.connector.Error as err:
        return err
        

def addto_current_split(name, amount):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        insert_query = """INSERT INTO CURRENT_SPLIT (NAME, AMOUNT)
                          VALUES (%s, %s)"""
        cursor.execute(insert_query, (name, amount))
        connection.commit()
        return "Split added successfully."
        connection.close()
    except mysql.connector.Error as err:
        return f"Error: {err}"
        
def get_current_split():
    split_list = []
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ARMY_CAMP"
        )   
        cursor = connection.cursor()
        select_query = "SELECT NAME,AMOUNT FROM CURRENT_SPLIT limit 10"
        cursor.execute(select_query)
        split_list = [list([str(row[0]),str(row[1])]) for row in cursor.fetchall()] 
        connection.close()
        return list(split_list)
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

    

#commit function
def add_charge(charge_type, uid, description, amount, charge_date, charge_remarks, officers_split):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        slice_index=0
        for i in range(0,len(uid)):
            if uid[i]==":":
                slice_index=i
                break
            
        if charge_type == "Individual":    
            insert_query = """INSERT INTO TOTAL_CHARGES (UID, DESCRIPTION, AMOUNT, DATE, TYPE_OF_CHARGE, REMARKS)
                              VALUES (%s, %s, %s, %s, %s, %s)"""                      
            cursor.execute(insert_query, (uid, description, amount, charge_date, charge_type, charge_remarks))
            connection.commit()
            
        return "Charge added successfully."
        connection.close()
    except mysql.connector.Error as err:
        return f"Error: {err}"
        
def get_charges():
    
    charge_data = []
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        select_query = "SELECT UID, DESCRIPTION, AMOUNT, DATE FROM TOTAL_CHARGES"
        cursor.execute(select_query)
        charge_data = [list([str(row[0]),str(row[1]),str(row[2]),str(row[3])]) for row in cursor.fetchall()]      
        connection.close()
        return charge_data
    except mysql.connector.Error as err:
        print(f"Error: {err}")
       

#display funtion
def existing_officers_uid():
    uid_list=[]
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="ARMY_CAMP"
        )
        global cursor
        cursor = connection.cursor()
        select_query = "SELECT UID FROM OFFICERS"
        cursor.execute(select_query)
        uid_list = [row[0] for row in cursor.fetchall()]  
        connection.close()
        return uid_list
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

#display function
def existing_officers_name():
    officers_name_list=[]
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        select_query = "SELECT NAME FROM OFFICERS"
        cursor.execute(select_query)
        officers_name_list = [row[0] for row in cursor.fetchall()]      
        connection.close()
        return officers_name_list

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
def get_name_rank():
    officers_name_rank_list=[]
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        select_query = "SELECT NAME,OFFICER_RANK FROM OFFICERS limit 10"
        cursor.execute(select_query)
        officers_name_rank_list = [list([str(row[0]),str(row[1])]) for row in cursor.fetchall()] 
        connection.close()
        return list(officers_name_rank_list)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

#utility function for fetching name from uid    
def get_name_from_uid(uid):
    name=""
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        select_query = "SELECT NAME FROM OFFICERS WHERE UID=%s"
        cursor.execute(select_query,(uid,))
        name = [str(row[0]) for row in cursor.fetchall()]
        name = str(name [0])      
        connection.close()
        return name

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def get_total_charges(uid):
    
    li=[]
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        select_query = "SELECT AMOUNT FROM TOTAL_CHARGES WHERE UID=%s"
        cursor.execute(select_query,(uid,))
        li = [float(row[0]) for row in cursor.fetchall()]      
        connection.close()
        return sum(li)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
        
def get_name_uid():
    l1=existing_officers_uid()
    l2=existing_officers_name()
    l3=[]
    for i in range(0,len(l1)):
        l3.append(l1[i]+": "+l2[i])
    return l3
#---------------------------UNDER CONSTRUCTION BELOW----------------------------------
def get_name_charges():
    officers_name_charges=[]
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        select_query = "SELECT NAME,OFFICER_RANK FROM OFFICERS"
        cursor.execute(select_query)
        officers_name_charges = [row[0] for row in cursor.fetchall()]      
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
       # cursor.close()
        connection.close()
        return officers_name_charges
