//MQ135

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(9600);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(A0);
  // print out the value you read:
  if(sensorValue>600){
    Serial.println("Poor Quality Air inside building");
  }
  else{
    Serial.println("Air Quality OK");
  }
  Serial.println("Present Air Quality");
  Serial.println(sensorValue/2);
  delay(5);        // delay in between reads for stability
}
