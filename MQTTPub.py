import paho.mqtt.client as mqtt
import json

def publish(id,data,topic):
# This is the Publisher
  broker="34.93.40.246"
  port=1883
  #topic="CCS\test"
  payload={'id':str(id),'data':data}
  payload=json.dumps(payload)
  client = mqtt.Client()
  client.connect(broker,port,0)
  (rc,mid)=client.publish(topic,payload);
  client.disconnect();
