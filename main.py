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
      if p =='3':
            m = input('Enter name')
            nm = int(input('Enter price'))
            nmn = int(input('Enter number'))
            print('OK it is create')
            cur.execute(f'INSERT INTO products (name, price, number) VALUES ("{m}" , "{nm}" , "{nmn}")')
            connection.commit()
      if p =='2':
            mn = input('Enter row id')
            cur.execute(f'DELETE FROM products WHERE rowid = {m}')
            connection.commit()
      if p == '1':
            print(res)

cur.execute('SELECT rowid, name, price, number FROM products')
connection.commit()
res = cur.fetchall()
pe()

connection.close()