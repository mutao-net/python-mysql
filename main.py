import mysql.connector
# https://dev.mysql.com/doc/connector-python/en/connector-python-connectargs.html
config = {
            'user': 'user',
            'password': 'password',
            'host': 'localhost',
            'port': 4306,
            'database': 'database',
        }

try:
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()
    cursor.execute('select * from users')
    res = cursor.fetchall()
    for r in res:
        print(r)
except mysql.connector.Error as err:
  print(err)