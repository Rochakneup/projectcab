import sys
import mysql.connector


def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='taxi')
    except:
        print("Error: ", sys.exc_info())
    finally:
       return conn

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