#include <IRremote.h>

int RECV_PIN = 11;
int LED_PIN = 13;

IRrecv irrecv(RECV_PIN);

decode_results results;

void setup()
{
  Serial.begin(9600);
  irrecv.enableIRIn(); // Start the receiver
  pinMode(LED_PIN, OUTPUT);
  digitalWrite(LED_PIN, HIGH);
}
void loop() {
  if (irrecv.decode(&results)) {
    Serial.println(results.value，);
    if (results.value == 3816986177) //开灯的值
    {
      digitalWrite(LED_PIN, LOW);
    } else if (results.value == 4294967295) //关灯的值
    {
      digitalWrite(LED_PIN, HIGH);
    }
    irrecv.resume(); // Receive the next value
  }
  delay(100);
}
