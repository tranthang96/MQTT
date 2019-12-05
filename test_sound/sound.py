# MQTT Client demo
# Continuously monitor two different MQTT topics for data,
# check if the received data matches two predefined 'commands'
from pygame import mixer
import time 
import paho.mqtt.client as mqtt
 
mixer.init()
#mixer.music.load("emoilenpho.mp3")
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
 
    # Subscribing in on_connect() - if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("control/sound")
    #client.subscribe("CoreElectronics/topic")

def playmp3(nameFile):
    try:
        mixer.music.load(nameFile)
        mixer.music.play()
        #phan gui play sound cho cac tu client
        
        #lent = len(nameFile)
        #filemp3 = nameFile[lent-7 : lent-4]
        #for sock in allConnection:
            #allConnection[sock].send(b'\x10\x0a' +filemp3.encode() )#sent stop

    except Exception as e :
        print("error in playmp3" + str(e), nameFile)
 
# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))
    msg.payload = msg.payload.decode("utf-8")
    if msg.topic == "control/sound":
        msg.payload = msg.payload.decode("utf-8")
        tenfile = msg.payload+".mp3"
        if msg.payload == "off":
            print("bat nhac")
            mixer.music.stop()
        else :
            playmp3(tenfile)

# Create an MQTT client and attach our routines to it.
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
 
client.connect("192.168.0.102", 1883, 60)
 
# Process network traffic and dispatch callbacks. This will also handle
# reconnecting. Check the documentation at
# https://github.com/eclipse/paho.mqtt.python
# for information on how to use other loop*() functions
client.loop_forever()




