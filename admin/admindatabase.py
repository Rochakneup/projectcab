import sys
import mysql.connector

"""my sql for admin to connect database and Gui"""
def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='taxi')
    except:
        print("Error: ", sys.exc_info())
    finally:
       return conn

# mysql to search admin with the help of email and password
def searchAdmin(customerInfo):
    conn = None
    sql = """SELECT * FROM  admins where email = %s AND password = %s """
    values = (customerInfo.getAMAIL(), customerInfo.getAPASSWORD())
    trip = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306", database='taxi')
        cursor = conn.cursor()
        cursor.execute(sql, values)
        trip = cursor.fetchone()
        cursor.close()
        conn.close()
        print("User searched")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del values
        del sql
        del conn
        return trip