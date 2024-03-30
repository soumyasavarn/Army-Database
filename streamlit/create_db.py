import mysql.connector

def set_database():
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
    )
    print ("database connnected successfully")
    # Create database if not exists
    create_db_query = "CREATE DATABASE IF NOT EXISTS ARMY_CAMP"
    create_db_cursor = connection.cursor()
    create_db_cursor.execute(create_db_query)

    # Use ARMY_CAMP database
    use_db_query = "USE ARMY_CAMP"
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
        ACCOMADATION_AVAILED BOOLEAN,
        IS_GUEST BOOLEAN
    )
    """
    create_officers_table_cursor = connection.cursor()
    create_officers_table_cursor.execute(create_officers_table_query)

    # Create TOTAL_CHARGES table
    create_total_charges_table_query = """
    CREATE TABLE IF NOT EXISTS TOTAL_CHARGES (
        UID VARCHAR(50) NOT NULL,
        DESCRIPTION VARCHAR(500),
        AMOUNT INT NOT NULL,
        TYPE_OF_CHARGE VARCHAR(200),
        DATE VARCHAR(20),
        REMARKS VARCHAR(200)
    )
    """
    create_total_charges_table_cursor = connection.cursor()
    create_total_charges_table_cursor.execute(create_total_charges_table_query)

    create_current_split_query = """
    CREATE TABLE IF NOT EXISTS CURRENT_SPLIT (
        NAME VARCHAR(100),
        AMOUNT INT NOT NULL
    )
    """
    create_current_split_cursor = connection.cursor()
    create_current_split_cursor.execute(create_current_split_query)

    create_mess_ledger_query = """
    CREATE TABLE IF NOT EXISTS MESS_LEDGER (
        TYPE VARCHAR(50),
        DESCRIPTION VARCHAR(100),
        REMARKS VARCHAR(200),
        AMOUNT INT,
        OFFICER VARCHAR(100),
        DATE VARCHAR(20)
    )
    """
    create_mess_ledger_cursor = connection.cursor()
    create_mess_ledger_cursor.execute(create_mess_ledger_query)

    
    print ("database initialised successfully")

    # Commit changes and close connection
    connection.commit()
    connection.close()