# import mysql.connector
# mydb = mysql.connector.connect(host="localhost",user="root",password="")
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE Game001")

# import mysql.connector
# mydb = mysql.connector.connect(
# host="localhost",
# user="root",
# password=""
# )
# print(mydb)

import mysql.connector
mydb = mysql.connector.connect(
host="localhost",
user="root",
password="",
database="game001")

mycursor = mydb.cursor()

# mycursor.execute(
#     """
#     CREATE TABLE sales (
#     id int AUTO_INCREMENT,
#     name VARCHAR(255),
#     count int,
#     PRIMARY KEY (id));
#     """
# )

sql = "INSERT INTO sales (id, name, count) VALUES (%s, %s, %s)"

val = [
('', 'Cooking-Gas', 40),
('', 'Shampoo', 10),
('', 'Milk', 20),
('', 'Books',14),
('', 'Chocos', 45),
('', 'Eggs', 12),
]

mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "record was inserted.")