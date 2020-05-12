#!/usr/bin/env python3

from influxdb import InfluxDBClient
import uuid
import paho.mqtt.client as mqtt
import random
import datetime
import numpy as np

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("livingroom/#")

def on_message(client, userdata, msg):
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    json_body = [
    {
        "measurement": "temperature",
        "tags": {
            "host": "aquarium",
        },
      #  "time": str(current_time),
        "fields": {
            "value": str(msg.payload)
        }
    }
    ]
    influx_client.write_points(json_body)
    print(msg.topic+" "+str(msg.payload))

influx_client = InfluxDBClient('localhost', 8086, database='collectd_db')
client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("192.168.43.86", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()
