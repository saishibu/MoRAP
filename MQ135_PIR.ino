//MQ135

void setup() {
  // initialize serial communication at 9600 bits per second:
  Serial.begin(115200);
  pinMode(33, INPUT);
}

// the loop routine runs over and over again forever:
void loop() {
  // read the input on analog pin 0:
  int sensorValue = analogRead(32);
  int PIRValue=digitalRead(33);
  // print out the value you read:
  if(sensorValue>600){
    Serial.println("Poor Quality Air inside building");
  }
  else{
    Serial.println("Air Quality OK");
  }

  if(PIRValue==0){
    Serial.println("No movement detected");
    
  }
  else{
    Serial.println("Movement present");
  }
  Serial.println("Present Air Quality Index");
  Serial.println(sensorValue/8);
  delay(300);        // delay in between reads for stability
}
