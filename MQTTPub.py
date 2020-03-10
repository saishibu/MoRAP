import paho.mqtt.client as mqtt
import json

# This is the Publisher
broker="34.93.40.246"
port=1883
topic="CCS\test"
payload={'message':"hello"}
payload=json.dumps(payload)
client = mqtt.Client()
client.connect(broker,port,0)
(rc,mid)=client.publish(topic,payload);
client.disconnect();
