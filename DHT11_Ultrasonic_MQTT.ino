#include <WiFi.h>
#include <PubSubClient.h>
#include "DHT.h"
#include "ArduinoJson.h"
const int trigPin = 2; //D2(Use the suffix of D2)
const int echoPin = 5; //D5(Use the suffix of D5)

long duration;
int distance;

#define DHTPIN 4     // Digital pin connected to the DHT sensor
// Feather HUZZAH ESP8266 note: use pins 3, 4, 5, 12, 13 or 14 --
// Pin 15 can work but DHT must be disconnected during program upload.
#define DHTTYPE DHT11   // DHT 11

char* ssid = "Smartgridlab";
char* password =  "amma@123";
const char* mqttServer = "192.168.1.32";
const int mqttPort = 1883;
char payload[10];

DHT dht(DHTPIN, DHTTYPE);
WiFiClient espClient;
PubSubClient client(espClient);

void(* resetFunc) (void) = 0;//declare reset function at address 0

void setup() {
  
  pinMode(trigPin, OUTPUT); // Sets the trigPin as an Output
  pinMode(echoPin, INPUT); // Sets the echoPin as an Input
  
  Serial.begin(115200);
  WiFi.begin(ssid, password);
  Serial.println("Connecting to WiFi");
  dht.begin();
  
  while (WiFi.status() != WL_CONNECTED) {
    digitalWrite(4, HIGH);
    delay(500);
    Serial.print(".not connected.");
    digitalWrite(4, LOW);

  }

  Serial.println("\nConnected to the WiFi network");

  client.setServer(mqttServer, mqttPort);

  while (!client.connected()) {
    Serial.println("Connecting to MQTT...");

    if (client.connect("ESP32Client" )) {

      Serial.println("connected");
//      signals = WiFi.RSSI();
      Serial.println(WiFi.RSSI());

    } else {

      Serial.print("failed with state ");
      Serial.print(client.state());
      digitalWrite(4, HIGH);
      delay(2000);
      digitalWrite(4, LOW);
      Serial.println("Reset");
      delay(1000);
      resetFunc();

    }
  }
}
void loop() {
  // Wait a few seconds between measurements.
  delay(2000);
  
  // Reading temperature or humidity takes about 250 milliseconds!
  // Sensor readings may also be up to 2 seconds 'old' (its a very slow sensor)
  float h = dht.readHumidity();
  // Read temperature as Celsius (the default)
  float t = dht.readTemperature();
  // Read temperature as Fahrenheit (isFahrenheit = true)
  float f = dht.readTemperature(true);

  // Check if any reads failed and exit early (to try again).
  if (isnan(h) || isnan(t) || isnan(f)) {
    Serial.println(F("Failed to read from DHT sensor!"));
    return;
  }

  // Compute heat index in Fahrenheit (the default)
  float hif = dht.computeHeatIndex(f, h);
  // Compute heat index in Celsius (isFahreheit = false)
  float hic = dht.computeHeatIndex(t, h, false);

  Serial.print(F("Humidity: "));
  Serial.print(h);
  Serial.print(F("%  Temperature: "));
  Serial.print(t);
  Serial.print(F("°C "));
  Serial.print(f);
  Serial.print(F("°F  Heat index: "));
  Serial.print(hic);
  Serial.print(F("°C "));
  Serial.print(hif);
  Serial.println(F("°F"));

    // Clears the trigPin
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);

  // Sets the trigPin on HIGH state for 10 micro seconds
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  // Reads the echoPin, returns the sound wave travel time in microseconds
  duration = pulseIn(echoPin, HIGH);

  // Calculating the distance
  distance = duration * 0.034 / 2;
  // Prints the distance on the Serial Monitor
  Serial.print("Distance: ");
  Serial.println(distance);
  delay(500);
  
  Serial.println(WiFi.status());
  if (client.connected()) {
    StaticJsonBuffer<200> JSONBuffer;
    JsonObject& root = JSONBuffer.createObject();
    root["Temperature"] = t;
    root["Humidity"] = h;
    root["Heat_index"] = f;
    root["Distance"] = distance;
    
    char JSONmessageBuffer[100];
    root.printTo(JSONmessageBuffer, sizeof(JSONmessageBuffer));
    JsonArray& data = root.createNestedArray("data");
    Serial.println(JSONmessageBuffer);
    client.publish("MoRAP/test", JSONmessageBuffer);
//    client.publish("MoRAP/dht", "DHT Called");
    client.loop();
    delay(2000);
  }
  else {
    Serial.println("WiFi Not Connected");
    Serial.println("Reset");
    delay(1000);
    resetFunc();
  }
}
