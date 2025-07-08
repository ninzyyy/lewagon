# pylint:disable=C0111,C0103

def detailed_orders(db):
    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''

    query = '''
    SELECT OrderID, ContactName, FirstName
    From Orders o
    JOIN Customers c ON o.CustomerID = c.CustomerID
    JOIN Employees e ON o.EmployeeID = e.EmployeeID
    ORDER BY OrderID
    '''
    db.execute(query)
    rows = db.fetchall()
    return rows

def spent_per_customer(db):
    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''

    query = '''
    SELECT c.ContactName, ROUND(SUM(od.Quantity * od.UnitPrice), 2) AS TotalPrice
    From Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Customers c ON o.CustomerID = c.CustomerID
    GROUP BY c.ContactName
    ORDER BY TotalPrice ASC
    '''
    db.execute(query)
    rows = db.fetchall()
    return rows

def best_employee(db):
    '''Implement the best_employee method to determine who's the best employee!
    By “best employee”, we mean the one who sells the most. We expect the
    function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of
    all purchase)). The order of the information is irrelevant'''

    query = '''
    SELECT e.FirstName, e.LastName, SUM(od.UnitPrice * od.Quantity) AS TotalSold
    From Orders o
    JOIN OrderDetails od ON o.OrderID = od.OrderID
    JOIN Employees e ON o.EmployeeID = e.EmployeeID
    GROUP BY e.LastName
    ORDER BY TotalSold DESC
    '''
    db.execute(query)
    results = db.fetchall()
    return results[0]

def orders_per_customer(db):
    '''Return a list of tuples where each tuple contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    query = '''
    SELECT c.ContactName, COUNT(o.OrderID) AS number_of_orders
    From Customers c
    LEFT JOIN Orders o ON c.CustomerID = o.CustomerID
    GROUP BY c.ContactName
    ORDER BY number_of_orders ASC
    '''
    db.execute(query)
    results = db.fetchall()
    return results

#import sqlite3
#conn = sqlite3.connect('data/ecommerce.sqlite')
#db = conn.cursor()
#print(spent_per_customer(db))
