import mysql.connector
import pymysql
import pandas as pd
import random
from datetime import datetime

host_name = "army-database-army-database.j.aivencloud.com"
user_name = "avnadmin"
user_password = "AVNS__umkEfKeGkBKQ4UL31v" 
db_name = "defaultdb"
timeout=10

#commit function
def add_officer(uid, officer_name, officer_rank, officer_unit, married, accomodation, mess_member, guest):
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        if (guest):
            uid = "Guest" + str(random.randint(1, 10000))
            insert_query = """INSERT INTO OFFICERS (UID, NAME, IS_GUEST)
                          VALUES (%s, %s,%s)"""
            cursor.execute(insert_query, (uid, officer_name, guest))
        else:
            insert_query = """INSERT INTO OFFICERS (UID, NAME, OFFICER_RANK, UNIT, IS_MESS_MEMBER, IS_MARRIED, ACCOMODATION_AVAILED, IS_GUEST)
                          VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
            cursor.execute(insert_query, (uid, officer_name, officer_rank, officer_unit, mess_member, married, accomodation, guest))
            
        connection.commit()
        connection.close()
        return "Added successfully."
    except mysql.connector.Error as err:
        return err

#fixed charges
def get_fixed_charges():
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        select_query = "SELECT SUB_NAME,RANK_1,RANK_2,RANK_3,RANK_4 FROM FIXED_CHARGES limit 15"
        cursor.execute(select_query)
        split_list = [list([str(row['SUB_NAME']),str(row['RANK_1']),str(row['RANK_2']),str(row['RANK_3']),str(row['RANK_4'])]) for row in cursor.fetchall()] 
        connection.close()
        return list(split_list)
    except mysql.connector.Error as err:
        return f"Error: {err}"       
    
def get_fixed_charges_name():
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        select_query = "SELECT SUB_NAME,RANK_1,RANK_2,RANK_3,RANK_4 FROM FIXED_CHARGES limit 15"
        cursor.execute(select_query)
        split_list = [str(row['SUB_NAME']) for row in cursor.fetchall()] 
        connection.close()
        return list(split_list)
    except mysql.connector.Error as err:
        return f"Error: {err}"       
    
def modify_fixed_charge(name,rank,amount):
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
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
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        insert_query = """INSERT INTO CURRENT_SPLIT (NAME, AMOUNT)
                          VALUES (%s, %s)"""
        cursor.execute(insert_query, (name, amount))
        connection.commit()
        connection.close()
        return "Split added successfully."
    except mysql.connector.Error as err:
        return f"Error: {err}"

def empty_current_split():
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        query = """TRUNCATE TABLE CURRENT_SPLIT;"""
        cursor.execute(query)
        connection.commit()
        connection.close()
        return "Split cleared."
    
    except mysql.connector.Error as err:
        return f"Error: {err}"
    
def addto_fixed_charges(rank_applicable, name, amount):
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
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
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        ) 
        cursor = connection.cursor()
        select_query = "SELECT NAME,AMOUNT FROM CURRENT_SPLIT limit 10"
        cursor.execute(select_query)
        split_list = [list([str(row['NAME']),str(row['AMOUNT'])]) for row in cursor.fetchall()] 
        connection.close()
        return list(split_list)
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

def add_mess_entry(charge_type, description, remarks, amount, officer, date):
     try:
         connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
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
         connection.close()
         return "Added successfully."
     except mysql.connector.Error as err:
         return err

def get_mess_entry():
    mess_list=[]
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        select_query = "SELECT TYPE,DESCRIPTION,AMOUNT FROM MESS_LEDGER limit 10"
        cursor.execute(select_query)
        mess_list = [list([str(row['TYPE']),str(row['DESCRIPTION']),str(row['AMOUNT'])]) for row in cursor.fetchall()] 
        connection.close()
        return list(mess_list)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
      

#commit function
def add_charge(charge_type, uid, description, amount, charge_date, charge_remarks, officers_split):
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        
        if charge_type == "Individual":    
            insert_query = """INSERT INTO TOTAL_CHARGES (UID, DESCRIPTION, AMOUNT, DATE, TYPE_OF_CHARGE, REMARKS)
                              VALUES (%s, %s, %s, %s, %s, %s)"""                      
            print ("OK 1")
            cursor.execute(insert_query, (uid, description, amount, charge_date, charge_type, charge_remarks))
            connection.commit()
            print ("OK 2")
        else:
            #Split logic here
            if len(officers_split)==0:
                return "Please enter officers' name"
            print ("officers_split",officers_split)
            amount=float(amount)
            for i in range(0,len(officers_split)):
                insert_query = """INSERT INTO TOTAL_CHARGES (UID, DESCRIPTION, AMOUNT, DATE, TYPE_OF_CHARGE, REMARKS)
                              VALUES (%s, %s, %s, %s, %s, %s)"""  
                tot = 0 
                for ii in range(0,len(officers_split)):     
                    officers_split[ii][1] = float(officers_split[ii][1])  
                    tot += float(officers_split[ii][1])              
                cursor.execute(insert_query, (officers_split[i][0], description, amount*float(officers_split[i][1])/tot, charge_date, charge_type, charge_remarks))
                connection.commit()
        connection.close()
        return "Charge added successfully."
    except mysql.connector.Error as err:
        return f"Error: {err}"
        
def get_charges():
    charge_data = []
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        select_query = "SELECT UID, DESCRIPTION, AMOUNT, DATE FROM TOTAL_CHARGES"
        cursor.execute(select_query)
        charge_data = [list([str(row['UID']),str(row['DESCRIPTION']),str(row['AMOUNT']),str(row['DATE'])]) for row in cursor.fetchall()]      
        connection.close()
        return charge_data
    except mysql.connector.Error as err:
        print(f"Error: {err}")
       

#display funtion
def existing_officers_uid():
    uid_list=[]
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        global cursor
        cursor = connection.cursor()
        select_query = "SELECT UID FROM OFFICERS"
        cursor.execute(select_query)
        uid_list = [row['UID'] for row in cursor.fetchall()]  
        connection.close()
        return uid_list
    except mysql.connector.Error as err:
        print(f"Error: {err}")

#display funtion
def existing_officers_uid_mess():
    uid_list=[]
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        global cursor
        cursor = connection.cursor()
        select_query = "SELECT UID FROM OFFICERS WHERE IS_MESS_MEMBER=1"
        cursor.execute(select_query)
        uid_list = [row['UID'] for row in cursor.fetchall()]  
        connection.close()
        return uid_list
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        

#display function
def existing_officers_name():
    officers_name_list=[]
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        select_query = "SELECT NAME FROM OFFICERS"
        cursor.execute(select_query)
        officers_name_list = [row['NAME'] for row in cursor.fetchall()]      
        connection.close()
        return officers_name_list

    except mysql.connector.Error as err:
        print(f"Error: {err}")

#display function
def existing_officers_name_mess():
    officers_name_list=[]
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        select_query = "SELECT NAME FROM OFFICERS WHERE IS_MESS_MEMBER=1"
        cursor.execute(select_query)
        officers_name_list = [row['NAME'] for row in cursor.fetchall()]      
        connection.close()
        return officers_name_list

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
def get_name_rank():
    officers_name_rank_list=[]
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        select_query = "SELECT NAME,OFFICER_RANK FROM OFFICERS limit 10"
        cursor.execute(select_query)
        officers_name_rank_list = [list([str(row['NAME']),str(row['OFFICER_RANK'])]) for row in cursor.fetchall()] 
        connection.close()
        return list(officers_name_rank_list)
    except mysql.connector.Error as err:
        print(f"Error: {err}")

def get_unit(uid):
    unit=""
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        select_query = "SELECT UNIT FROM OFFICERS WHERE UID=%s"
        cursor.execute(select_query,(uid,))
        unit = [str(row['UNIT']) for row in cursor.fetchall()]
        unit = str(uid [0])      
        connection.close()
        return unit       
    except mysql.connector.Error as err:
        print(f"Error: {err}")


#utility function for fetching name from uid    
def get_name_from_uid(uid):
    name=""
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        select_query = "SELECT NAME FROM OFFICERS WHERE UID=%s"
        cursor.execute(select_query,(uid,))
        name = [str(row['NAME']) for row in cursor.fetchall()]
        name = str(name [0])      
        connection.close()
        return name

    except mysql.connector.Error as err:
        print(f"Error: {err}")

    
        
def get_name_uid():
    l1=existing_officers_uid()
    l2=existing_officers_name()
    l3=[]
    for i in range(0,len(l1)):
        l3.append(l1[i]+" : "+l2[i])
    return l3

def get_name_uid_mess_member():
    l1=existing_officers_uid_mess()
    l2=existing_officers_name_mess()
    l3=[]
    for i in range(0,len(l1)):
        l3.append(l1[i]+" : "+l2[i])
    return l3

#Groups all possible charges of an officer and returns a list of tuple/list
def get_total_bill(officer,arrears,month,year):
    #[ser,desc,amount,remarks]
    final_list=[]
    #This is the list to be returned (initialised here as global variable)
    ind = 0
    for i in range(0,len(officer)):
        if officer[i]==':':
            ind=i
            break

    month=int(month)
    # print(month)
    # import datetime
    # year = datetime.datetime.now().year

    name=officer[i+2:]
    uid=officer[:i-1]
    rank=[]
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        select_query = "SELECT OFFICER_RANK FROM OFFICERS WHERE UID=%s"
        cursor.execute(select_query,(uid,))
        rank = [str(row['OFFICER_RANK']) for row in cursor.fetchall()]
        rank=str(rank[0])
        connection.close()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    rank = rank.upper()
    rank=rank.replace(" ","_")
    # print(rank)
    # print(name,uid)
    charges=None
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        select_query = "SELECT IS_MARRIED,ACCOMODATION_AVAILED FROM OFFICERS WHERE UID = %s"
        cursor.execute(select_query,(uid,))
        charges = [[bool(row['IS_MARRIED']),bool(row['ACCOMODATION_AVAILED'])] for row in cursor.fetchall()]
        # print(charges)
        connection.close()
        # print (charges)    
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    # 1. messing charges
    messing_charge_list=[]
    mess=[]
    daily=0.00
    extra=0.00
    
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        Daily_Messing = "Daily Messing"
        Extra_Messing = "Extra Messing"

        # Assuming date1 and date2 are properly formatted strings in YYYY-MM-DD format
        select_query = "SELECT AMOUNT FROM MESS_LEDGER WHERE MONTH(DATE) = {} AND YEAR(DATE) = {} AND TYPE = %s AND OFFICER = %s".format(month,year)
        cursor.execute(select_query, (Daily_Messing, officer,))
        mess = [float(row['AMOUNT']) for row in cursor.fetchall()]
        daily = sum(mess)

        select_query = "SELECT AMOUNT FROM MESS_LEDGER WHERE MONTH(DATE) = {} AND YEAR(DATE) = {} AND TYPE = %s AND OFFICER = %s".format(month,year)
        cursor.execute(select_query, (Extra_Messing, officer,))
        mess = [float(row['AMOUNT']) for row in cursor.fetchall()]
        extra = sum(mess)

        connection.close()
        # print (daily, extra)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        
    messing_charge_list.append([1,"Daily Messing",daily,""])
    messing_charge_list.append([2,"Extra Messing",extra,""])
    # print(messing_charge_list)

    # 2. fixed charges list
    fixed_charge_list=[]
    fix=[]
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()
        select_query = "SELECT SUB_NAME,"+rank+" FROM FIXED_CHARGES WHERE SUB_NAME='Spouse Memento Fund'"
        cursor.execute(select_query)
        fix = [list(row) for row in cursor.fetchall()]
        fixed_charge_list.append([3,fix[0][0],float(fix[0][1])*int(charges[0][0]),""])

        select_query = "SELECT SUB_NAME,"+rank+" FROM FIXED_CHARGES WHERE SUB_NAME='Accomodation'"
        cursor.execute(select_query)
        fix = [list(row) for row in cursor.fetchall()]
        fixed_charge_list.append([4,fix[0][0],float(fix[0][1])*int(charges[0][1]),""])

        select_query = "SELECT SUB_NAME,"+rank+" FROM FIXED_CHARGES WHERE SUB_NAME!='Accomodation' AND SUB_NAME!='Spouse Memento Fund'"
        cursor.execute(select_query)
        fix = [list(row) for row in cursor.fetchall()]
        connection.close()
        
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    for i in range (5,len(fix)+5):
        fixed_charge_list.append([i,fix[i-5][0],fix[i-5][1],""])
    # print(fixed_charge_list)

    # 3. misc charges list
    misc_charge_list=[]
    misc=[]
    try:
        connection = pymysql.connect(
          charset="utf8mb4",
          connect_timeout=timeout,
          cursorclass=pymysql.cursors.DictCursor,
          db="defaultdb",
          host="army-database-army-database.j.aivencloud.com",
          password="AVNS__umkEfKeGkBKQ4UL31v",
          read_timeout=timeout,
          port=21565,
          user="avnadmin",
          write_timeout=timeout,
        )
        cursor = connection.cursor()

        # Assuming date1 and date2 are properly formatted strings in YYYY-MM-DD format
        select_query = """SELECT DESCRIPTION, SUM(AMOUNT) AS TOTAL_AMOUNT
        FROM TOTAL_CHARGES
        WHERE MONTH(DATE) = %s AND YEAR(DATE) = %s AND UID = %s
        GROUP BY DESCRIPTION"""
        
        cursor.execute(select_query, (month, year, officer))

        misc = [list(row) for row in cursor.fetchall()]
        # print(misc)
        connection.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    for i in range (0,len(misc)):
        connection = mysql.connector.connect(
            host=host_name,
        user=user_name,
        password=user_password,database=db_name
        )
        cursor = connection.cursor()
        select_query = """SELECT REMARKS
        FROM TOTAL_CHARGES
        WHERE MONTH(DATE) = %s AND YEAR(DATE) = %s AND UID = %s AND DESCRIPTION = %s
        """
        cursor.execute(select_query, (month, year, officer,misc[i][0]))
        remark_received = [list(row) for row in cursor.fetchall()]
        connection.close()
        remark_rec = ""
        print (remark_received)
        try:
            remark_rec = remark_received[0][0]
        except:
            print ("Empty remark")
        print (remark_rec)
        misc_charge_list.append([i+5+len(fix),misc[i][0],misc[i][1],remark_rec])
    # print(misc_charge_list)

    for i in messing_charge_list:
        final_list.append(i)
    for i in fixed_charge_list:
        final_list.append(i)
    for i in misc_charge_list:
        final_list.append(i)
    total_sum=0.0
    for i in final_list:
        total_sum+=float(i[2])
    final_list.append(["","----------","----------"])
    final_list.append(["","    Total: ",round(total_sum, 2),""])
    final_list.append(["","    Arrears: ",round(arrears, 2),""])
    final_list.append(["","    G/Total: ",round(total_sum+float(arrears),2),""])
    final_list.append(["","    R/Off: ",round(int(total_sum)+int(arrears)-total_sum-float(arrears),2),""])
    final_list.append(["","    Amount Payable: ",round(float(int(total_sum)+int(arrears)),2),""])

    # print (final_list)
    return final_list
