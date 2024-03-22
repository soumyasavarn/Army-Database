import mysql.connector

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

