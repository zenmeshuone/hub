#include <stdlib.h>
#include <SoftwareSerial.h>
#include <dht11.h>            
dht11 DHT11;  
const int pin = 4;  // 将把 DHT11 的 data pin 連到 arduino Pin 4

#define SSID "Laboratory_1"      //wifi名
#define PASS "aa401aa402" //wifi密码
#define IP "184.106.153.149" // 连接thingspeak.com服务器
String GET = "GET /update?key=INGPOMNDO1WZEU67"; //输入前面记下的API
SoftwareSerial monitor(10, 11); // 定义软串口RX, TX

//初始化-----------------------------------------
void setup()
{
    monitor.begin(9600);
    Serial.begin(9600);
    delay(5000);
    sendDebug("AT");        //指令测试
    delay(5000);
    if(Serial.find("OK"))   //接收指令正常则返回OK
    {
        monitor.println("RECEIVED: OK");
        connectWiFi();
    }
}

//主循环-----------------------------------------
void loop()
{
    DHT11.read(pin);  // 读取 DHT11 传感器
    //Serial.print(DHT.humidity,1);    //串口打印湿度
    //Serial.print(",\t");  
    //Serial.println(DHT.temperature,1);   //打印温度
    float tempH = DHT11.humidity;
    float tempT = DHT11.temperature;
    char buffer[10];
    String temph = dtostrf(tempH, 4, 1, buffer);    
    String tempt = dtostrf(tempT, 4, 1, buffer);    
    updateTemp(temph,tempt);
    delay(5000);
}


void updateTemp(String temph,String tempt)          
{               
    String cmd = "AT+CIPSTART=\"TCP\",\"";
    cmd += IP;
    cmd += "\",80";
    sendDebug(cmd);                         //发送指令，链接服务器
    delay(2000);
    if(Serial.find("Error"))
    {
        monitor.print("RECEIVED: Error");
        return;
    }
    cmd = GET + "&field3=" + temph + "&field2=" + tempt +"\r\n";        //记录T和H的值
    Serial.print("AT+CIPSEND=");
    Serial.println(cmd.length());
    if(Serial.find(">"))
    {
        monitor.print(">");
        monitor.print(cmd);
        Serial.print(cmd);
    }
    else
    {
        sendDebug("AT+CIPCLOSE");
    }
    if(Serial.find("OK"))
    {
        monitor.println("RECEIVED: OK");
    }
    else
    {
        monitor.println("RECEIVED: Error");
    }
}

void sendDebug(String cmd)
{
    monitor.print("SEND: ");
    monitor.println(cmd);
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
    delay(5000);
    if(Serial.find("OK"))
    {
        monitor.println("RECEIVED: OK");
        return true;
    }else
    {
        monitor.println("RECEIVED: Error");
        return false;
    }
}
