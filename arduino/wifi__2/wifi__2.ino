#include <SoftwareSerial.h>
SoftwareSerial getData(0, 1);//esp8266-01的TX对应开发板的RX，esp8266-01的RX对应开发板的TX

void setup() {
  getData.begin(9600);
  
  getAT();
  Serial.begin(9600);
  
}

void loop() {
  if (getData.available() > 0){
      String str=getData.readString();
      Serial.println(str);
  }
}
void getAT(){
  getData.println("AT+CWMODE=1");//将8266设置为STA模式
  delay(4000);
    
  getData.println("AT+RST");//设置完之后重启
  delay(4000);
    
  getData.println("AT+CWJAP_DEF=\"Laboratory_1\",\"aa401aa402\"");//8266连接路由器发出的WiFi
  delay(4000);
    
  getData.println("AT+CIPMUX=0");//启动多连接
  delay(4000);
    
  getData.println("AT+CIPSTART=\"TCP\",\"140.143.202.52\",8080");//通过协议、IP和端口连接服务器
  delay(4000);
    
  getData.println("AT+CIPMODE=1");//设置透传
  delay(4000);
   
  getData.println("AT+CIPSEND=81");//启动发送
  delay(5000);
   
  getData.println("GET /receiveopen");//发送数据
  delay(5000);
    
 }
