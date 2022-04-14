# db.py model

import os
import pymysql
from flask import jsonify

db_user = os.environ.get('CLOUD_SQL_USERNAME')
db_password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
db_connection_name = os.environ.get('CLOUD_SQL_CONNECTION_NAME')

def open_connection():
    unix_socket = '/cloudsql/{}'.format(db_connection_name)
    try:
        if os.environ.get('GAE_ENV') == 'standard':
            conn = pymysql.connect(user=db_user,
                                   password=db_password,
                                   unix_socket=unix_socket,
                                   db=db_name,
                                   cursorclass=pymysql.cursors.DictCursor
                                   )
    except pymysql.MySQLError as e:
        return e
    return conn

def get_loaners():
    conn = open_connection()
    with conn.cursor() as cursor:
        cursor.execute('''select c.customer_name, c.customer_city
                        from customer as c, borrower as b, loan as l
                        where c.customer_name = b.customer_name and b.loan_number = l.loan_number
                        and l.branch_name = 'Perryridge';''')
        loaners = cursor.fetchall()
        return loaners