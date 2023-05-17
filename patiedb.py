import mysql.connector

database = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)
cursorObject=database.cursor()
cursorObject.execute("create database patients")
print(" Doctor database successfully created")