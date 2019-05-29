#include <dht11.h>

dht11 DHT11;
#define PIN_DHT11 2

uint8_t PinLed = 3;          //led正极
uint8_t PinLightsensor = A0;    //光传感模块模拟数据接收引脚
uint8_t PinLighthuoyan = A1;     //火焰传感器数据接收引脚
//注意：我是用的光传感器模块是随着光照增加输出减小的。
int MaxLight = 550;         //光传感器模块完全遮蔽时的输出值（实际值比这个略小）
int MinLight = 0;         //光传感模块在灯光下完全裸露时的输出值（实际值比这个值略大）
// the setup function runs once when you press reset or power the board
void setup() {
  Serial.begin(9600);
  pinMode(PinLed, OUTPUT);
  pinMode(PinLightsensor, INPUT);
  pinMode(PinLighthuoyan, INPUT);
}
 
// the loop function runs over and over again until power down or reset
void loop() {
  //光照模块
  int curLight = analogRead(PinLightsensor);          //读取光传感器当前值
  int outVal = map(curLight, MinLight, MaxLight, 0, 255);   //把光传感器的值映射到0-255（PWM输出范围），需要注意的是Map函数不会强制结果在0-255范围内（当curLight超出map函数的第二三两参数的范围时出现超出0-255的情况）。
  outVal = 255 - constrain(outVal, 0, 255);             //强制映射后的值在0-255范围内
  if (curLight <=  100)
  {
  analogWrite(PinLed,outVal );       //输出亮度，当光传感器得到的光照越多，那么LED就越亮
  delay(10);
  }
  else
  analogWrite(PinLed,0 );           //灯灭
  //火焰模块
  int huoLight = analogRead(PinLighthuoyan); 
  if(huoLight <= 45)
  {
    analogWrite(PinLed,200 );
    delay(10);
   }
  else
  analogWrite(PinLed,0 );

  //温湿模块
  DHT11.read(PIN_DHT11);               //获取数值
  int humidity = DHT11.humidity;
  int temperature = DHT11.temperature;
  if(temperature >= 40)
  {
     analogWrite(PinLed,200 );
     delay(10);
  }
  else
  analogWrite(PinLed,0 );
  
  Serial.print("光照亮度 : ");
  Serial.println(curLight);            //打印光照
  Serial.print("红外数值 : ");
  Serial.println(huoLight);            //打印火焰传感器数值
  Serial.print("湿度 (%): ");
  Serial.println(humidity);            //打印湿度
  Serial.print("温度 (oC): ");
  Serial.println(temperature);         //打印温度
  delay(1000);                         //延时

}
