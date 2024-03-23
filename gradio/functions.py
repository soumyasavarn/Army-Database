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
        slice_index=0
        for i in range(0,len(uid)):
            if uid[i]==":":
                slice_index=i
                break
        
        insert_query = """INSERT INTO TOTAL_CHARGES (UID, DESCRIPTION, AMOUNT, DATE, TYPE_OF_CHARGE)
                          VALUES (%s, %s, %s, %s, %s)"""
        cursor.execute(insert_query, (uid[:slice_index], description, amount, charge_date, charge_type))
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
        officers_name_rank_list = [list([str(row[0]),str(row[1])]) for row in cursor.fetchall()]      
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
        return list(officers_name_rank_list)

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
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        connection.close()
        return name

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
        cursor.close()
        connection.close()
        return officers_name_charges
