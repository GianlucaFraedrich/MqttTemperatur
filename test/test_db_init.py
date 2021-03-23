#Füllt die Datenbank mit Testdaten (prüft nicht ob Reihen schon vorhanden sind)
import mysql.connector

testrooms = ("Room1","Room2","Room3")
testtopics = ("test/test1","test/test2","test/test3")

db = mysql.connector.connect(
    host="localhost",
    user="test",
    password="pw",
    database="mqtttemperatur"
)

cursor = db.cursor()

for x in testrooms:
    sql = "INSERT INTO Rooms (Name) VALUES (%s)"
    val = (x,)
    cursor.execute(sql, val)
    db.commit()

for x in range(len(testtopics)):
    sql = "INSERT INTO topics (topic, Rooms_ID) VALUES (%s,%s)"
    val = (testtopics[x], x+1)
    cursor.execute(sql, val)
    db.commit()

