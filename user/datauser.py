import sys
import mysql.connector

# function to connect to the mysql database
def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='taxi')
    except:
        print("Error: ", sys.exc_info())
    finally:
       return conn

# function to save user data to the database
def saveUSER(cname,cphone,cmail,cpassword):
    conn = None
    sql = """INSERT INTO usersdata (name,phone,email,password) VALUES (%s, %s, %s,%s)"""
    values = (cname, cphone, cmail, cpassword)
    try:
        # conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='level4b')
        conn = connect()
        cursor = conn.cursor()
        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()
        print("user added!")
    except:
        print("Error : ", sys.exc_info())
    finally:
        del values
        del sql
        del conn

# function to search for user in the database
def searchUSER(customerInfo):
    conn = None
    sql = """SELECT * FROM  usersdata where email = %s AND password = %s """
    values = (customerInfo.getCMAIL(), customerInfo.getCPASSWORD())
    trip = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='',port="3306", database='taxi')
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

# function to retrieve all user data from the database
def alluser():
    conn = None
    sql = """SELECT * from usersdata"""
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
