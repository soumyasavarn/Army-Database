import mysql.connector
import pandas as pd
import random


#commit function
def add_officer(uid, officer_name, officer_rank, officer_unit, married, accomadation, mess_member, guest):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",
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

#fixed charges
def get_fixed_charges():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        select_query = "SELECT SUB_NAME,RANK_1,RANK_2,RANK_3,RANK_4 FROM FIXED_CHARGES limit 15"
        cursor.execute(select_query)
        split_list = [list([str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4])]) for row in cursor.fetchall()] 
        connection.close()
        return list(split_list)
    except mysql.connector.Error as err:
        return f"Error: {err}"       
    
def get_fixed_charges_name():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        select_query = "SELECT SUB_NAME,RANK_1,RANK_2,RANK_3,RANK_4 FROM FIXED_CHARGES limit 15"
        cursor.execute(select_query)
        split_list = [str(row[0]) for row in cursor.fetchall()] 
        connection.close()
        return list(split_list)
    except mysql.connector.Error as err:
        return f"Error: {err}"       
    
def modify_fixed_charge(name,rank,amount):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",
            database="ARMY_CAMP"
        )
        rank = rank.upper()
        rank = rank.replace(" ","_")
        cursor = connection.cursor()
        select_query = "UPDATE FIXED_CHARGES SET "+ rank + " = %s where SUB_NAME = %s;"
        cursor.execute(select_query,(amount, name))

        connection.commit()
        connection.close()
        return "Fixed Charge modified successfully."

    except mysql.connector.Error as err:
        return f"Error: {err}"       

def addto_current_split(name, amount):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",
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
    
def addto_fixed_charges(rank_applicable, name, amount):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        insert_query = """INSERT INTO FIXED_CHARGES (SUB_NAME,RANK_1, RANK_2, RANK_3, RANK_4)
                          VALUES (%s, %s, %s, %s, %s)"""
        for i in range(0,len(rank_applicable)):
            rank_applicable[i]=int(rank_applicable[i])
            print(rank_applicable)
        cursor.execute(insert_query, (name, float(amount)*rank_applicable[0],float(amount)*rank_applicable[1],float(amount)*rank_applicable[2],float(amount)*rank_applicable[3]))
        connection.commit()
        return "Fixed charge added successfully."
        connection.close()
    except mysql.connector.Error as err:
        return f"Error: {err}"
        
def get_current_split():
    split_list = []
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",
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
        

def add_mess_entry(charge_type, description, remarks, amount, officer, date):
     try:
         connection = mysql.connector.connect(
             host="localhost",
             user="root",
             password="root@123",
             database="ARMY_CAMP"
         )
         cursor = connection.cursor()
         if (charge_type == "Normal"):
             insert_query = """INSERT INTO MESS_LEDGER (TYPE, DESCRIPTION, REMARKS, AMOUNT, DATE)
                           VALUES (%s, %s, %s, %s, %s)"""
             cursor.execute(insert_query, (charge_type, description, remarks, amount, date))   
         else:
             insert_query = """INSERT INTO MESS_LEDGER (TYPE, DESCRIPTION, REMARKS, AMOUNT, OFFICER, DATE)
                           VALUES (%s, %s, %s, %s, %s, %s)"""
             cursor.execute(insert_query, (charge_type, description, remarks, amount, officer, date))   
             
         connection.commit()
         return "Added successfully."
         connection.close()
     except mysql.connector.Error as err:
         return err

def get_mess_entry():
    mess_list=[]
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        select_query = "SELECT TYPE,DESCRIPTION,AMOUNT FROM MESS_LEDGER limit 10"
        cursor.execute(select_query)
        mess_list = [list([str(row[0]),str(row[1]),str(row[2])]) for row in cursor.fetchall()] 
        connection.close()
        return list(mess_list)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
      

#commit function
def add_charge(charge_type, uid, description, amount, charge_date, charge_remarks, officers_split):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root@123",
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
            password="root@123",
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
            password="root@123",
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
            password="root@123",
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
            password="root@123",
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
            password="root@123",
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
            password="root@123",
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
            password="root@123",
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
