import sys
import mysql.connector
from booking.Connect import *
import Global

# Connect to the database
def connect():
    conn = None
    try:
        conn = mysql.connector.connect(host='localhost', port='3306', user='root', password='', database='taxi')
    except:
        print("Error: ", sys.exc_info())
    finally:
       return conn

# Insert a new booking into the database
def bookings(pickupaddress,dropaddress,pickuptime,pickupdate,cid):
    conn = None
    sql = """INSERT INTO allbooking (pickupaddress,dropaddress,pickuptime,pickupdate,Status,cid) VALUES (%s, %s, %s,%s,"Pending",%s)"""
    values = (pickupaddress,dropaddress,pickuptime,pickupdate,cid)
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

# Retrieve all trips for a specific customer from the database
def allTrip(cid):
    conn = None
    sql = """SELECT * from allbooking WHERE cid = %s"""
    records = None
    values = (cid,)
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='taxi')
        cursor = conn.cursor()
        cursor.execute(sql,values)
        records = cursor.fetchall()
        print(records)
        cursor.close()
        conn.close()
        print("Records retrieve sucessfully")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del conn
        return records

# Retrieve all trips from the database
def all():
    conn = None
    sql = """SELECT * from allbooking"""
    records = None
    try:
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='taxi')
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        print(records)
        cursor.close()
        conn.close()
        print("Records retrieve sucessfully")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del conn
        return records

# Search for a specific trip in the database
def searchTrip(tno):
        conn = None
        sql = """SELECT * FROM  booking where tid = %s and status!= 'cancelled' """
        values = (tno,)
        trip = None
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306",
                                           database='taxi')
            cursor = conn.cursor()
            cursor.execute(sql, values)
            trip = cursor.fetchall()
            cursor.close()
            conn.close()
            print("Trip Searched")
        except:
            print("Error: ", sys.exc_info())
        finally:
            del values
            del sql
            del conn
            return trip

def updateTrip(pickup,time, dropoff, date,tid):
        conn = None
        sql = "UPDATE allbooking SET pickupaddress = %s, dropaddress = %s,pickuptime = %s, pickupdate = %s WHERE tid =%s"
        values = (pickup, dropoff,time, date,tid)
        result = False
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306",
                                           database='taxi')
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()  # Change
            cursor.close()
            result = True
            print("Customer Updated")
        except:
            print("Error: ", sys.exc_info())
        finally:
            del values
            del sql
            del conn
            return result

def cancelTrip(tripInfo):
        sql = """SELECT * FROM  booking where status!='cancelled'"""
        trips = None
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306",
                                           database='taxibookingsystem')
            cursor = conn.cursor()
            cursor.execute(sql)
            trips = cursor.fetchall()
            print(trips)
            cursor.close()
            conn.close()
            # print("All Drivers Displayed")
        except:
            print("Error: ", sys.exc_info())
        finally:
            del sql
            return trips

def deleteTrip(tid):
        conn = None
        sql = """Delete from  allbooking  WHERE tid=%s"""
        values = (tid,)
        result = False
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306",
                                           database='taxi')
            cursor = conn.cursor()
            cursor.execute(sql, values)
            conn.commit()
            cursor.close()
            conn.close()
            result = True
        except:
            print("Error: ", sys.exc_info())
        finally:
            del values
            del sql
            del conn
            return result




