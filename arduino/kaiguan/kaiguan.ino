#include <stdlib.h>
#include <SoftwareSerial.h>  
const int LEDpin = 13;                   //加灯
int pinRelay = 5;               //管脚D5连接到继电器模块的信号脚
#define SSID "guoguo"     //wifi名
#define PASS "guoguo11"       //wifi密码
#define IP "140.143.202.52"     // 连接服务器
String GET = "GET /receiveopen"; //输入前面记下的API
SoftwareSerial monitor(10, 11); // 定义软串口RX, TX
String _comdata_wifi = "";      //接收函数


//初始化-----------------------------------------
void setup()
{
    Serial.begin(9600);
    pinMode(pinRelay, OUTPUT);   //设置pinRelay脚为输出状态
    pinMode(LEDpin, OUTPUT);   //设置LED脚为输出状态
    digitalWrite(LEDpin, LOW);
    digitalWrite(pinRelay,HIGH );
    delay(2000);
    sendDebug("AT");             //指令测试
    delay(3000);
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
    if(Serial.find("+IPD,1:1CLOSED")){
      digitalWrite(LEDpin, HIGH);       //输出亮度，当光传感器得到的光照越多，那么LED就越亮
      delay(500);
      digitalWrite(LEDpin,LOW );
      digitalWrite(pinRelay, LOW);//输出LOW电平，继电器模块闭合
      delay(2000); //等待2000毫秒
      digitalWrite(pinRelay, HIGH);//输出HIGH电平，继电器模块断开
      delay(1000);//等待1000毫秒
    }
    _comdata_wifi = String("");
    }   
    updateTemp();
   
    delay(2000);
}


void updateTemp()          
{              
    String cmd = "AT+CIPSTART=\"TCP\",\"";
    cmd += IP;
    cmd += "\",8080";
    sendDebug(cmd);                         //发送指令，链接服务器
    delay(2000);
    cmd = GET+"\r\n";        //记录值
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
    delay(4000);
}
void getWifiSerialData(){               //定义接收函数
  while(Serial.available()>0){
    _comdata_wifi += char(Serial.read());
    delay(3);
  }
}
