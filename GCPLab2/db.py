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
								   pasword=db_password,
								   unix_socket=unix_socket,
								   db=db_name,
								   cursorclass=pymysql.cursor.DictCursor
								   )
	except pymysql.MySQLError as e:
		return e
	return conn

def get_customers():
	conn = open_connection()
	with conn.cursor() as cursor:
		cursor.execute('SELECT * FROM customer;')
		customers = cursor.fetchall()
		return customers

def create(customername, customerstreet, customercity)
	conn = open_connection()
	with conn.cursor() as cursor:
		cursor.execute('INSERT INTO customer (customer_name, customer_street, customer_city) VALUES (%s, %s, %s)',
					    (customername, customerstreet, customercity))
		conn.commit()
		conn.close()

