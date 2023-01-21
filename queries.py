# pylint:disable=C0111,C0103

def query_orders(db):
    # return a list of orders displaying each column
    query = '''
    SELECT * FROM Orders o
    ORDER BY OrderID ASC
    '''
    db.execute(query)
    rows = db.fetchall()
    return rows


def get_orders_range(db, date_from, date_to):
    # return a list of orders displaying all columns with OrderDate between
    # date_from and date_to (excluding date_from and including date_to)
    query = '''
    SELECT o.* FROM Orders o
    WHERE (OrderDate > ? AND OrderDate <= ?)
    ORDER BY OrderDate ASC
    '''
    db.execute(query, (date_from, date_to))
    rows = db.fetchall()
    return rows


def get_waiting_time(db):
    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    query = '''
    SELECT o.*, JULIANDAY(ShippedDate) - JULIANDAY(OrderDate) AS TimeDelta
    FROM Orders o
    ORDER BY TimeDelta ASC
    '''
    db.execute(query)
    rows = db.fetchall()
    return rows

#import sqlite3
#conn = sqlite3.connect('data/ecommerce.sqlite')
#db = conn.cursor()
#print(get_waiting_time(db))
