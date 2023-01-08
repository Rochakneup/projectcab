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

def bookings(pickupaddress,dropaddress,pickuptime,pickupdate):
    conn = None
    sql = """INSERT INTO allbooking (pickupaddress,dropaddress,pickuptime,pickupdate,Status) VALUES (%s, %s, %s,%s,"Pending")"""
    values = (pickupaddress,dropaddress,pickuptime,pickupdate)
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


def allTrip():
    conn = None
    sql = """SELECT * from allbooking"""
    records = None
    try:
        #connect
        conn = mysql.connector.connect(host='localhost', user='root', password='', database='taxi')
        cursor = conn.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()
        print(records)
        #close
        cursor.close()
        conn.close()
        print("Records retrieve sucessfully")
    except:
        print("Error: ", sys.exc_info())
    finally:
        del conn
        return records

def searchTrip(tno):
        conn = None
        sql = """SELECT * FROM  booking where tid = %s and status!= 'cancelled' """
        values = (tno,)
        trip = None
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306",
                                           database='taxibookingsystem')
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
        sql = """UPDATE booking SET status ='cancelled' WHERE tid=%s"""
        values = (tid,)
        result = False
        try:
            conn = mysql.connector.connect(host='localhost', user='root', password='', port="3306",
                                           database='taxibookingsystem')
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




