import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tutorial"
)
user = input("Enter User Id:")
attend = input("Enter Attendance:")
date = input("Enter Date:")
dcursor = conn.cursor()
sql="INSERT INTO attendance (user_id,attend,date) VALUES (%s,%s,%s)"
values=(user, attend, date)
dcursor.execute(sql,values)
conn.commit()
print(str(dcursor.rowcount) + "was inserted")