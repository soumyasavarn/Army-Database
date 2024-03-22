import mysql.connector

#commit function
def add_officer(uid, officer_name, officer_rank, officer_unit):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        insert_query = """INSERT INTO OFFICERS (UID, NAME, OFFICER_RANK, UNIT)
                          VALUES (%s, %s, %s, %s)"""
        cursor.execute(insert_query, (uid, officer_name, officer_rank, officer_unit))
        connection.commit()
        return "Officer added successfully."
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        connection.close()

#commit function
def add_charge(uid, description, amount, charge_date, charge_type):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password",
            database="ARMY_CAMP"
        )
        cursor = connection.cursor()
        insert_query = """INSERT INTO TOTAL_CHARGES (UID, DESCRIPTION, AMOUNT, DATE, TYPE_OF_CHARGE)
                          VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (uid, description, amount, charge_date, charge_type))
        connection.commit()
        return "Charge added successfully."
    except mysql.connector.Error as err:
        return f"Error: {err}"
    finally:
        cursor.close()
        connection.close()

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
        cursor = connection.cursor()
        select_query = "SELECT UID FROM OFFICERS"
        cursor.execute(select_query)
        uid_list = [row[0] for row in cursor.fetchall()]      
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
        return uid_list

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
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
        return officers_name_list

def get_name_rank():
    officers_name_rank_list=[]
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
        officers_name_rank_list = [[row[0],row[1]] for row in cursor.fetchall()]      
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
        return officers_name_rank_list

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
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
        return sum(li)

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
        cursor.close()
        connection.close()
        return officers_name_charges
