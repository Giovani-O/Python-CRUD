import mysql.connector

connection = mysql.connector.connect(host='localhost', user='root', password='', database='user_py', charset='utf8')
cursor = connection.cursor(dictionary=True)