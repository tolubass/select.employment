import mysql.connector
conn = mysql.connector.connect(
    host = "localhost",
    username = "TRAIN",
    password = "train",
    database = "tutorial"
)
dcursor = conn.cursor()
sql = "DELETE FROM tabclass WHERE phone = '08087674598' ORDER BY id DESC LIMIT 1"
para = ('%080',)
dcursor.execute(sql)
conn.commit()
