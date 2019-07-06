char getstr;
void setup()
{
  Serial.begin(9600);
}
void loop()
{
  getstr=Serial.read();
  if(getstr=='h')
  {
    Serial.println("I am here!");
  }
  else if(getstr=='b'){
    Serial.println("See you!");
  }
}
