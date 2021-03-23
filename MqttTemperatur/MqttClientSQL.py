#Mqtt Client speichert die Daten in einer SQL Datenbank
import paho.mqtt.client as mqtt
import mysql.connector
import datetime

SubscriptionRoomList={}

#Define mqtt callbacks
#def on_log(client, userdata, level, buf):
    #Print logs
#   print("log: ",buf)

def on_connect(client, userdata, flags, rc):
    #Print connection result code
    print("Connected with result code "+str(rc))

def on_message(client, userdata, msg):
    #Print message
    print(msg.topic+" "+str(msg.payload,"utf-8"))
    #Get Room_ID from topic
    cursor=db.cursor()
    sql = "SELECT Rooms_ID FROM topics WHERE topic = %s"
    val = (msg.topic,)
    cursor.execute(sql, val)
    result = cursor.fetchall()
    room_id = result[0][0]
    #Insert Temperature into Temperature table with datetime
    sql = "INSERT INTO temperature (Temperature, time, Rooms_ID) VALUES (%s, %s, %s)"
    val = (str(msg.payload,"utf-8"), datetime.datetime.now(), room_id)
    cursor.execute(sql, val)
    db.commit()


#Establish SQL Connection
db = mysql.connector.connect(
    host="localhost",
    user="test",
    password="pw",
    database="mqtttemperatur"
)

#Create client instance
client = mqtt.Client("PythonClient") #Sollte noch durch eine eindeutige ID ausgetauscht werden
#client.on_log=on_log
client.on_connect=on_connect
client.on_message=on_message

#Connect to Broker
client.connect("192.168.0.87")

#Subscribe to topics
cursor = db.cursor()
cursor.execute("SELECT topic FROM topics")
topics = cursor.fetchall()
for topic in topics:
    client.subscribe(topic[0])
    print("Subscribed to ", topic[0])

#Client loop
client.loop_forever()


