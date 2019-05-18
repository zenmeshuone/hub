import requests
import re
import json

def request_dandan(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None

def parse_result(html):
    pattern = re.compile('<li>.*?<em class="">(\d+)</em>.*?<span class="title">(.*?)</span>.*?<p class="">.*?: (.*?\s).*?&nbsp;&nbsp;&nbsp;(.*?\s.*?)\s.*?</p>.*?<span class="inq">(.*?)</span>.*?</li>',re.S)
    items = re.findall(pattern, html)
    for item in items:
        yield {
            '排名': item[0],
            '片名': item[1],
            '导演': item[2]+item[3],
            '评价': item[4],
        }


def write_item_to_file(item):
    print('开始写入数据 ====> ' + str(item))
    with open('book2.txt', 'a', encoding='UTF-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')
        f.close()


def main(page):
    url = 'https://movie.douban.com/top250?start='+ str(page*25)+'&filter='
    html = request_dandan(url)
    items = parse_result(html) # 解析过滤我们想要的信息
    for item in items:
        write_item_to_file(item)


if __name__ == "__main__":
    for i in range(0, 10):
        main(i)
