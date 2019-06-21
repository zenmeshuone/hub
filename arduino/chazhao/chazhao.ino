  
String str=" \r\nRecv 80 bytes\r\nSEND OK\r\n+IPD,4:2014CLOSED\r\n";
 
/*
   str 被查找的字符串
   b_str 对比的字符串头
   e_str 查找的结束符
   dest 获取到的字符串
   len 想要获取的长度
*/
char *parse_str(String *str, char * b_str, char *e_str, char *dest, int len) {
  char *pos, *p, *p2;
  int i;
  pos = strstr(str, b_str);
  if (pos == NULL) {
    return NULL;
  }
  pos = pos + strlen(b_str);
  p = pos;
  if (e_str == NULL) {
    p2 = NULL;
  } else {
    p2 = strstr(str, e_str);
  }
  if (p2 == NULL) {
    p2 = str + strlen(str);
  }
  i = 0;
  for (i = 0; p < p2 && (*p) && i < len; dest[i++] = *p, ++p)
    ;
  dest = 0;
  return dest;
}
 
void setup()
{
    Serial.begin(9600);
    //初始化保存获取到的数据的数组，并把内存置为0
    char res[6]; memset(res,0x00,sizeof(res));
 
    Serial.println("parse_str string...");
 
//    parse_str(str,"data=","&res",data,5);
//    Serial.println(data);
 
    parse_str(str,"+IPD,","CLOSED",res,7);
    Serial.println(res);
}
 
void loop()
{
}
