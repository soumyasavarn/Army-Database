import mysql.connector
import pymysql

host_name = "army-database-army-database.j.aivencloud.com"
user_name = "avnadmin"
user_password = "AVNS__umkEfKeGkBKQ4UL31v" 
db_name = "defaultdb"
timeout=10

def set_database():
    # Connect to MySQL server
    print ("Starting connection")
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
    print ("database connnected successfully")
    # Create database if not exists
    create_db_query = "CREATE DATABASE IF NOT EXISTS " + db_name
    create_db_cursor = connection.cursor()
    create_db_cursor.execute(create_db_query)

    # Use ARMY_CAMP database
    use_db_query = "USE " + db_name
    use_db_cursor = connection.cursor()
    use_db_cursor.execute(use_db_query)

    # Create OFFICERS table
    create_officers_table_query = """
    CREATE TABLE IF NOT EXISTS OFFICERS (
        UID VARCHAR(50) PRIMARY KEY NOT NULL,
        NAME VARCHAR(100) NOT NULL,
        OFFICER_RANK VARCHAR(100),
        UNIT VARCHAR(100),
        IS_MESS_MEMBER BOOLEAN,
        IS_MARRIED BOOLEAN,
        ACCOMODATION_AVAILED BOOLEAN,
        IS_GUEST BOOLEAN
    )
    """
    create_officers_table_cursor = connection.cursor()
    create_officers_table_cursor.execute(create_officers_table_query)

    # Create FIXED_CHARGES table
    create_fixed_charges_table_query = """
    CREATE TABLE IF NOT EXISTS FIXED_CHARGES (
        SUB_NAME VARCHAR(50) PRIMARY KEY NOT NULL,
        RANK_1 FLOAT NOT NULL,
        RANK_2 FLOAT NOT NULL,
        RANK_3 FLOAT NOT NULL,
        RANK_4 FLOAT NOT NULL
    )
    """
    create_fixed_charges_table_cursor = connection.cursor()
    create_fixed_charges_table_cursor.execute(create_fixed_charges_table_query)


    sql = "INSERT IGNORE INTO FIXED_CHARGES (SUB_NAME, RANK_1, RANK_2, RANK_3, RANK_4) VALUES (%s, %s, %s, %s, %s)"
    val = ("Accomodation", "200", "200", "200", "200")
    mycursor = connection.cursor()
    mycursor.execute(sql, val)

    sql = "INSERT IGNORE INTO FIXED_CHARGES (SUB_NAME, RANK_1, RANK_2, RANK_3, RANK_4) VALUES (%s, %s, %s, %s, %s)"
    val = ("Spouse Memento Fund", "200", "200", "200", "200")
    mycursor.execute(sql, val)


    # Create TOTAL_CHARGES table
    create_total_charges_table_query = """
    CREATE TABLE IF NOT EXISTS TOTAL_CHARGES (
        UID VARCHAR(50) NOT NULL,
        DESCRIPTION VARCHAR(500),
        AMOUNT FLOAT NOT NULL,
        TYPE_OF_CHARGE VARCHAR(200),
        DATE VARCHAR(20) NOT NULL,
        REMARKS VARCHAR(200)
    )
    """
    create_total_charges_table_cursor = connection.cursor()
    create_total_charges_table_cursor.execute(create_total_charges_table_query)

    create_current_split_query = """
    CREATE TABLE IF NOT EXISTS CURRENT_SPLIT (
        NAME VARCHAR(100) PRIMARY KEY,
        AMOUNT FLOAT NOT NULL
    )
    """
    create_current_split_cursor = connection.cursor()
    create_current_split_cursor.execute(create_current_split_query)

    create_mess_ledger_query = """
    CREATE TABLE IF NOT EXISTS MESS_LEDGER (
        TYPE VARCHAR(50),
        DESCRIPTION VARCHAR(100),
        REMARKS VARCHAR(200),
        AMOUNT FLOAT NOT NULL,
        OFFICER VARCHAR(100) ,
        DATE VARCHAR(20) NOT NULL
    )
    """
    create_mess_ledger_cursor = connection.cursor()
    create_mess_ledger_cursor.execute(create_mess_ledger_query)

    
    print ("database initialised successfully")

    # Commit changes and close connection
    connection.commit()
    connection.close()
