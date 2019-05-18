from bs4 import BeautifulSoup   #beautifulsoup4
import requests #requests
import re
def fjiexiqi(a_text):
    return BeautifulSoup(a_text,"html.parser")
def fwendang(a_url):
    vrequest = requests.get(url = a_url)
    # newr = vrequest.text.replace('<br/>', '')
    s = '<br/>'
    # z = str.encode(s)
    x = '\n'
    # v = str.encode(x)
    # views = vrequest.content.replace(z, v)
    views = vrequest.text.replace(s,x)
    # print(views)
    return views


class I_text:
    def __init__(self):
        self.m_text = None
    def fchongxin(self):
        self.m_text = fjiexiqi(fwendang(self.fg_url()))
    def fzairu(self):
        if not self.m_text:
            self.fchongxin()
    def fg_url(self):
        raise NotImplementedError()
class I_xiaoshuo:
    def __init__(self):
        I_text.__init__(self)
    def fe_mulu(self):
        "返回(章节名, I章节 对象)"
        raise NotImplementedError()
class I_zhangjie:
    def __init__(self):
        I_text.__init__(self)
    def fg_zhenwen(self):
        "返回字符串"
        raise NotImplementedError()



class Cxiaoshuo(I_text, I_xiaoshuo):
    czhangjie = "chapters-list"
    def __init__(self, a_url):
        I_text.__init__(self)
        I_xiaoshuo.__init__(self)
        self.m_url = a_url
    def fg_url(self):
        return self.m_url
    def fe_mulu(self):
        self.fzairu()
        vmuluyuansu = self.m_text.find(name = "ul", id= Cxiaoshuo.czhangjie)
        # print(vmuluyuansu)
        valiebiao = vmuluyuansu.find_all(name = "li")
        #去除前面的最新章节和最后的重复章节
        valiebiao = valiebiao[72:]
        # print(valiebiao)
        for v in valiebiao:
            v_url = v.a.get("href")   #章节链接
            # print("https://www.boquge.com"+ v_url)
            v_text = v.a.string    #章节名
            if "xxxx" in v_text:    #去除最后的重复章节
                continue
            yield v_text,Czhangjie("https://www.boquge.com"+ v_url)
class Czhangjie(I_text, I_xiaoshuo):
    czhangjie = "txtContent"
    def __init__(self, a_url):
        I_text.__init__(self)
        I_xiaoshuo.__init__(self)
        self.m_url = a_url
    def fg_url(self):
        return self.m_url
    def fgzhengwen(self):
        self.fzairu()
        vzhengwen = self.m_text.find("div", id=Czhangjie.czhangjie)
        # vzhengwentext = vzhengwen.find("dd",id="contents)

        print(vzhengwen)
        return vzhengwen



c_url = "https://www.boquge.com/book/48588/"
c_url1 = b'\xa1\xc2\xde\xb7\xe7\xd6\xb8\xbb\xd3\xd7\xc5\xb4\xf3\xf7\xbc\xf7\xc3\xc2\xed\xb9\xca\xd2\xe2\xb1\xdc\xbf\xaa\xc1\xcb\xbd\xa9\xca\xac\xcd\xb7\xb2\xbb\xb2\xc8\xa3\xac\xd2\xbb\xd5\xf3\xc2\xed\xc8\xba\xb9\xfd\xba\xf3\xa3\xac\xb5\xd8\xc9\xcf\xd2\xb2\xbe\xcd\xca\xa3\xcf\xc2\xd2\xbb\xb8\xf6\xbd\xa9\xca\xac\xcd\xb7\xba\xcd\xd2\xbb\xb6\xd1\xb7\xd6\xb2\xbb\xc7\xe5\xca\xd6\xbd\xc5\xd0\xd8\xb1\xb3\xb5\xc4\xcb\xe9\xc6\xac\xc1\xcb\xa3\xa1\xb6\xd4\xd3\xda\xcd\xf6\xc1\xe9\xc9\xfa\xce\xef\xc0\xb4\xcb\xb5\xa3\xac\xd6\xbb\xd2\xaa\xcd\xb7\xb2\xbf\xb2\xbb\xca\xdc\xc9'
m = " "
def main():
    global m
    num = 1
    f2 = open('新建文本文档 (4).txt', 'w+', encoding='utf-8')
    # v_text =fjiexiqi(c_url1)
    v_text1 = Cxiaoshuo(c_url)
    # m = v_text1.fgzhengwen()
    # print(m)
    # print(v_text)

    for vmingc,czhangjie in v_text1.fe_mulu():
        c_url1 = czhangjie.fg_url()
        mera = Czhangjie(c_url1)
        # print(v_text1.fe_mulu())
        n = mera.fgzhengwen()
        # a = "\n\n\n"+"("+vmingc+")" + "\n" + n
        m = "\n\n\n" + "(" + vmingc + ")" + "\n" + n
        # try:
        #
        #     m = "\n\n\n"+"("+vmingc+")" + "\n" + n  # 你原来的执行函数。
        # except:
        #     print ('wrong')

        f2.write( m + "\n")
        num += 1
        print(num)
    f2.close()

if __name__ == "__main__":
    main()







