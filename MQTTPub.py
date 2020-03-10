import paho.mqtt.client as mqtt
import Adafruit_DHT

import json
gpio=17
  
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

humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
if humidity is not None and temperature is not None:
  print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
  dht_data = 
  publish(DHT, dht_data, 'CCS\test')
else:
  print('Failed to get reading. Try again!')
