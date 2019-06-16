#include <stdlib.h>
#include <SoftwareSerial.h>
#include <dht11.h>            
dht11 DHT11;  
const int LEDpin = 13;                   //加灯
const int pin = 4;              // 将把 DHT11 的 data pin 連到 arduino Pin 4
uint8_t PinLightsensor = A0;    //光传感模块模拟数据接收引脚.注意：我是用的光传感器模块是随着光照增加输出减小的。
uint8_t PinLighthuoyan = A1;    //火焰传感器数据接收引脚
int pinRelay = 5;               //管脚D5连接到继电器模块的信号脚
int MaxLight = 550;             //光传感器模块完全遮蔽时的输出值（实际值比这个略小） 
int MinLight = 0;               //光传感模块在灯光下完全裸露时的输出值（实际值比这个值略大）
#define SSID "guoguo"     //wifi名
#define PASS "guoguo11"       //wifi密码
#define IP "140.143.202.52"     // 连接服务器
String GET = "GET /update?key=arduino"; //输入前面记下的API
SoftwareSerial monitor(10, 11); // 定义软串口RX, TX
String _comdata_wifi = "";      //接收函数

//初始化-----------------------------------------
void setup()
{
    Serial.begin(9600);
    pinMode(PinLightsensor, INPUT);
    pinMode(PinLighthuoyan, INPUT);
    pinMode(pinRelay, OUTPUT);   //设置pinRelay脚为输出状态
    pinMode(LEDpin, OUTPUT);   //设置LED脚为输出状态
    delay(5000);
    sendDebug("AT");             //指令测试
    delay(5000);
    if(Serial.find("OK"))        //接收指令正常则返回OK
    {
        connectWiFi();
    }
}

//主循环-----------------------------------------
void loop()
{   
    getWifiSerialData(); 
    if(_comdata_wifi != ""){
      Serial.print(_comdata_wifi);
      digitalWrite(LEDpin, HIGH);       //输出亮度，当光传感器得到的光照越多，那么LED就越亮
      delay(1000);
      digitalWrite(LEDpin,LOW );
      _comdata_wifi = String("");
    }  

    int curLight = analogRead(PinLightsensor);          //读取光传感器当前值
    int outVal = map(curLight, MinLight, MaxLight, 0, 255);   //把光传感器的值映射到0-255（PWM输出范围），需要注意的是Map函数不会强制结果在0-255范围内（当curLight超出map函数的第二三两参数的范围时出现超出0-255的情况）。
    outVal = 255 - constrain(outVal, 0, 255);             //强制映射后的值在0-255范围内
    int huoLight = analogRead(PinLighthuoyan);         //火焰模块
    DHT11.read(pin);  // 读取 DHT11 传感器
    float tempH = DHT11.humidity;
    float tempT = DHT11.temperature;

    char buffer[10];
    String HuoLight = dtostrf(huoLight, 4, 1, buffer);
    String OutVal = dtostrf(outVal, 4, 1, buffer);
    String temph = dtostrf(tempH, 4, 1, buffer);    
    String tempt = dtostrf(tempT, 4, 1, buffer);  
    updateTemp(temph,tempt,OutVal,HuoLight);
   
    delay(6000);
}


void updateTemp(String temph,String tempt,String outVal,String huoLight)          
{              
    String cmd = "AT+CIPSTART=\"TCP\",\"";
    cmd += IP;
    cmd += "\",8080";
    sendDebug(cmd);                         //发送指令，链接服务器
    delay(2000);
    cmd = GET + "&temperature=" + tempt + "&humidity=" + temph +"&brighten=" + outVal +"&ray=" + huoLight +"\r\n";        //记录值
    Serial.print("AT+CIPSEND=");
    Serial.println(cmd.length());
    if(Serial.find(">"))
    { 
        Serial.print(cmd);
    }
    else
    {
        sendDebug("AT+CIPCLOSE");
    }
}

void sendDebug(String cmd)
{
    Serial.println(cmd);
}

boolean connectWiFi()
{
    Serial.println("AT+CIPMUX=0");
    Serial.println("AT+CWMODE=1");
    delay(2000);
    String cmd="AT+CWJAP=\"";
    cmd+=SSID;
    cmd+="\",\"";
    cmd+=PASS;
    cmd+="\"";
    sendDebug(cmd);
    delay(7000);
}
void getWifiSerialData(){               //定义接收函数
  while(Serial.available()>0){
    _comdata_wifi += char(Serial.read());
    delay(3);
  }
}
