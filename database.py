import mysql.connector

# Default MySQL
host = 'localhost'
userName = 'root'
password = ''
dbName = 'db'
print("Connecting MySQL Server")
print(host + ", " + userName)

mydb = mysql.connector.connect(
    host = host,
    user = userName,
    passwd = password,
    database = dbName
)

print("Connected to " + host + ", " + userName)
mycursor = mydb.cursor()

def inputDB(name, age):
    insertSQL = ("INSERT INTO humans (NAME, AGE) VALUES (%s, %s)")
    dataSQL = (name, age)
    mycursor.execute(insertSQL, dataSQL)
    mydb.commit()