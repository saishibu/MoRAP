#!/usr/bin/python3
import sys
import os
#botUpdate
import time
import paho.mqtt.client as paho
import datetime

global mqttclient;
global broker;
global port;
broker = "0.0.0.0";
port = 1883;
# This is the Subscriber
mypid = os.getpid()
print("Process started at: " +str(mypid))
client_uniq = "pubclient_"+str(mypid)
mqttclient = paho.Client(client_uniq, False) #nocleanstart
mqttclient.connect(broker, port, 60)
mqttclient.subscribe("CCS/#")

def test(client, userdata, message):
	payload=message.payload.decode()
	print(payload)

mqttclient.message_callback_add("CCS/test", test)


mqttclient.loop_forever()



