import sqlite3


p = input('Enter 3 for create\nEnter 2 for delete\nEnter 1 for check\n')
connection = sqlite3.connect('products.sl3', 5)
cur = connection.cursor()
#cur.execute('CREATE TABLE products (name TEXT, price TEXT, number TEXT)')
#connection.commit()

def pe():
      global m
      global nm
      global nmn
      global mn
      global cur
