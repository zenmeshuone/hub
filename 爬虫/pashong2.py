# 作者：周小馬
# 链接：https://www.zhihu.com/question/48900224/answer/266561350
# 来源：知乎
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
#
import requests
from bs4 import BeautifulSoup

def fjiexiqi(a_text):
    return BeautifulSoup(a_text,"html.parser")
def fwendang(a_url):
    vrequest = requests.get(url = a_url)
    s = '\r<br />\r\n'
    z = str.encode(s)
    x = '\n'
    v = str.encode(x)
    views = vrequest.content.replace(z,v)
    return views
c_url = "https://www.23us.so/files/article/html/24/24384/11719950.html"
n=b'\xad\x94\xef\xbc\x9f\xe2\x80\x9d\n&nbsp;&nbsp;&nbsp;&nbsp;\xe2\x80\x9c\xe4\xba\x8b\xe5\xae\x9e\xe4\xb8\x8a\xe5\xb9\xb6\xe4\xb8\x8d\xe6\x98\xaf\xef\xbc\x8c\xe6\x88\x91\xe5\x8f\xaf\xe8\x83\xbd\xe6\x98\xaf\xe6\x9c\x80\x9f\xe2\x80\x9d\xe9\x99\x88\xe6\x9b\x8c\xe9\x97\xae\xe9\x81\x93\xe3\x80\x82&nbsp;&nbsp;&nbsp;&nbsp;\xe2\x80\x9c\xe6\x88\x91\xe6\x80\x8e\xe4\xb9\x88\xe7\x9f\xa5\xe9\x81\x93\xe3\x80\x82\xe2\x80'
def main():
    b = fwendang(c_url)
    v_text = fjiexiqi(b)

    # for vzhangjiem,vzhangjie in v_text.fe_mulu():
    print(v_text)


if __name__ == "__main__":
    main()


