import sys
import mysql.connector

# function to establish a connection to the 'taxi' database
def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='taxi')
    except:
        print("Error: ", sys.exc_info())
    finally:
       return conn

# function to insert data into the 'drivers' table in the 'taxi' database
def saveDRIVER(dname,dphone,dmail,dpassword,dliscense):
    conn = None
    sql = """INSERT INTO drivers (name,phone,mail,password,licenseno) VALUES (%s, %s, %s,%s,%s)"""
    values = (dname, dphone, dmail, dpassword,dliscense)
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

    except:
        print("Error : ", sys.exc_info())
    finally:
        del values
        del sql
        del conn

# function to retrieve all data from the 'drivers' table in the 'taxi' database
def alldriver():
    conn = None
    sql = """SELECT * from drivers"""
    records = None
    try:
    # connect
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='taxi')
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        print(records)
    # close
        cursor.close()
        conn.close()
        print("Records retrieve sucessfully")
    except:
            print("Error: ", sys.exc_info())
    finally:
        del conn
        return records

# function to search for a specific driver in the 'drivers' table in the 'taxi' database based on email and password
def searchDriver(customerInfo):
    conn = None
    sql = """SELECT * FROM  drivers where mail = %s AND password = %s """
    values = (customerInfo.getDMAIL(), customerInfo.getDPASSWORD())
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
