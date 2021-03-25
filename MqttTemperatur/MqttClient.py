#Mqtt Client speichert die Daten in einer json Datei
import paho.mqtt.client as mqtt
import json

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
    
    #Write the message to the json file
    global SubscriptionRoomList
    SubscriptionRoomList[msg.topic] = str(msg.payload,"utf-8")
    try:
        f = open("data\SubscriptionList.json","wt")
        f.write(json.dumps(SubscriptionRoomList))
        f.close() 
    except:
        print("error: Daten konnten nicht geschrieben werden")

#Create client instance
client = mqtt.Client("PythonClient") #Sollte noch durch eine eindeutige ID ausgetauscht werden
#client.on_log=on_log
client.on_connect=on_connect
client.on_message=on_message

#Connect to Broker
client.connect("192.168.0.87")

#Subscribe to topics
try:
    #Topics aus json file auslesen
    f = open("data\SubscriptionList.json","rt")
    SubscriptionRoomList=json.loads(f.read())
    f.close()
    #Subscribe and print topics
    for topic in SubscriptionRoomList:
        client.subscribe(topic)
        print("Subscribed to Topic: "+ topic)
except:
    print("error: Daten konnten nicht gelesen werden")

#Client loop
client.loop_forever()

#Mögliche Fehlerursachen
# - Der Client loop stört irgendwie -> Vielleicht in einem eigenem Prozess starten?


