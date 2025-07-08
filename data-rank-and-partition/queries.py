# pylint:disable=C0111,C0103

def order_rank_per_customer(db):
    query = '''
    SELECT o.OrderID, o.CustomerID, o.OrderDate,
    RANK() OVER (
	    PARTITION BY o.CustomerID
	    ORDER BY o.OrderDate
    ) AS OrderRank
    FROM Orders o
    '''
    db.execute(query)
    results = db.fetchall()
    return results



def order_cumulative_amount_per_customer(db):
    query = '''
    SELECT o.OrderID, o.CustomerID, o.OrderDate,
    SUM(SUM(od.UnitPrice * od.Quantity)) OVER (
	    PARTITION BY o.CustomerID
	    ORDER BY o.OrderDate
    ) AS OrderCumulativeAmount
    FROM Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    GROUP BY o.OrderID
    ORDER BY o.CustomerID
    '''
    db.execute(query)
    results = db.fetchall()
    return results


#import sqlite3
#conn = sqlite3.connect('data/ecommerce.sqlite')
#db = conn.cursor()
#print(spent_per_customer(db))
