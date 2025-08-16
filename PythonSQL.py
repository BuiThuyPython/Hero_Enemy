import mysql.connector

# Create the database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS GameData")

# Connect to the new database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="GameData"
)
mycursor = mydb.cursor()

# Create the table
mycursor.execute("""
    CREATE TABLE IF NOT EXISTS CoSoDuLieu (
        id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(255) NOT NULL,
        Mobile VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        PRIMARY KEY (id)
    )
""")

# Insert sample data
sql = "INSERT INTO CoSoDuLieu (name, Mobile, email) VALUES (%s, %s, %s)"
val = [
    ('ram', '984309119', 'cothuy@gmail.com'),
    ('shyam', '983124567', 'mailcuatui@gmail.com'),
    ('Manish Sharma', '935213654', 'khongbiet@gmail.com'),
    ('Sharad Gupta', '976345123', 'aido@gmail.com'),
    ('Vinod Kumar', '973235645', 'dungdodi@gmail.com'),
]

mycursor.executemany(sql, val)
mydb.commit()

print(mycursor.rowcount, "record was inserted.")

