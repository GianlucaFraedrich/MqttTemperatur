import paho.mqtt.client as mqtt
import json


SubscriptionRoomList=""
    
#Define mqtt callbacks
#def on_log(client, userdata, level, buf):
    #Print logs
#   print("log: ",buf)


def on_connect(client, userdata, flags, rc):
    #Print connection result code
    print("Connected with result code "+str(rc))



#Create client instance
client = mqtt.Client("PythonClient")
#client.on_log=on_log
client.on_connect=on_connect


#Connect to Broker
client.connect("192.168.0.87")

#Subscribe to topics
try:
    #Topics aus json file auslesen
    f = open("MqttTemperatur\data\SubscriptionList","rt")
    SubscriptionRoomList=json.loads(f.read())
except:
    print("error")
finally:
    f.close()

for topic in SubscriptionRoomList:
    client.subscribe(topic)
    print("Subscribed to Topic: "+ topic)

#on message methode zum Client hinzufügen
def on_message(client, userdata, msg):
    #Print message
    print(msg.topic+" "+str(msg.payload,"utf-8"))
    
    #Write the message to the json file
    SubscriptionRoomList[msg.topic] = msg.payload
    try:
        f = open("MqttTemperatur\data\SubscriptionList","wt")
        f.write(json.dumps(SubscriptionRoomList))
    except:
        print("error")
    finally:
        f.close() 

client.on_message=on_message


#Client loop
client.loop_forever()

#Mögliche Fehlerursachen
# - Der Client loop stört irgendwie -> Vielleicht in einem eigenem Prozess starten?


