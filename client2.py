#!/usr/bin/python3
import paho.mqtt.client as mqtt
from pygame import mixer

host = "192.168.0.102"
topic = "control/sound"

mixer.init()
mixer.music.load("emoilenpho.mp3")

def on_connect(client, userdata, flags, rc):
	print('Connected, rc: ' + str(rc))


def on_message(client, userdata, msg):
	print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))
	topic1 = msg.topic	
	data = str(msg.payload)
	if(msg.topic == topic):
		if(data == "on"):
			print("bat nhac")
			mixer.music.play()
		elif(data == "off"):
			print("tat nhac")
			mixer.music.stop()
def on_publish(client, userdata, mid):
	print("mid: "+str(mid))

def on_subscribe(client, userdata, mid, granted_qos):
	pass
def on_log(client, userdata, level, buf):
	pass

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.on_publish = on_publish
client.connect(host)
client.subscribe(topic)

client.loop_forever()