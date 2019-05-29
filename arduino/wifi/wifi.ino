#include <ESP8266WiFi.h>

SoftwareSerial mySerial(13, 12); 
String comdata;

void setup() {
  pinMode(11,OUTPUT);

  Serial.begin(115200);
  while (!Serial) {
      ; // wait for serial port to connect. Needed for native USB port only 
  }
  
  Serial.println("Hello World");
  mySerial.begin(115200);
  mySerial.println("AT+GMR");
}

void loop() {

    while (mySerial.available() > 0)  
    {
        comdata += char(mySerial.read());
        delay(2);
    }
    if (comdata.length() > 0)
    {
        comdata.trim();
        Serial.println(comdata);
        if (comdata.endsWith("A")){
          digitalWrite(11,HIGH);
          Serial.println("Buzz ON");
        }
        if (comdata.endsWith("a")){
          digitalWrite(11,LOW);
          Serial.println("Buzz OFF");
        }
        comdata = "";
    }
    if (Serial.available()) {
    mySerial.write(Serial.read());
    }
}
