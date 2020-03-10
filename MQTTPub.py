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
  client.connect(broker,port,60)
  (rc,mid)=client.publish(topic,payload);
  client.disconnect();

humidity, temperature = Adafruit_DHT.read_retry(sensor, gpio)
if humidity is not None and temperature is not None:
  StaticJsonBuffer<200> JSONBuffer;
  JsonObject& root = JSONBuffer.createObject();
  root["Temperature"] = t;
  root["Humidity"] = h;
  char JSONmessageBuffer[100];
  root.printTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
  JsonArray& data = root.createNestedArray("data");
  print(JSONmessageBuffer);
  publish(DHT, JSONmessageBuffer, CCS\test)
else:
  print('Failed to get reading. Try again!')
