import requests
import re
import json

def request_dandan(url,headers):
    try:
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
    except requests.RequestException:
        return None


def parse_result(html):
    hjson = json.loads(html)
    # raw_train:
    # "|预订|550000Z16420|Z164|SHH|LSO|SHH|LSO|20:08|19:30|47:22|N|SIygZtG7LXRkGXyeINjk7T5kNo40ywRzkHSmSiTp6MyIlkHIGPlTcQfsc9U%3D|20190303|3|H2|01|14|0|0||||无|||无||无|无|||||10401030|1413|0|0|null"
    for raw_train in hjson:
        # 循环遍历每辆列车的信息
        data_list = raw_train.split('|')
        # 车次号码
        train_no = data_list[3]
        # 出发站

        # 出发时间
        start_time = data_list[8]
        # 到达时间
        arrive_time = data_list[9]
        # 总耗时
        time_used_up = data_list[10]
        # 一等座
        first_class_seat = data_list[31] or '--'
        # 二等座
        second_class_seat = data_list[30] or '--'
        # 软卧
        soft_sleep = data_list[23] or '--'
        # 硬卧
        hard_sleep = data_list[28] or '--'
        # 硬座
        hard_seat = data_list[29] or '--'
        # 无座
        no_seat = data_list[26] or '--'

        list = (
            '车次:{} 出发站:{} 目的地:{} 出发时间:{} 到达时间:{} 火车运行时间:{} 座位情况：\n 一等座：「{}」 二等座：「{}」 软卧：「{}」 硬卧：「{}」 硬座：「{}」 无座：「{}」'.format(
                train_no, from_station_name, to_station_name, start_time, arrive_time, time_used_up, first_class_seat,
                second_class_seat, soft_sleep, hard_sleep, hard_seat, no_seat))

        print('*' * 100)
        print(list)
        print('*' * 100)



def main():
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2019-04-18&leftTicketDTO.from_station=HFH&leftTicketDTO.to_station=GZQ&purpose_codes=ADULT'
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}
    html = request_dandan(url,headers)
    print(html)
    items = parse_result(html) # 解析过滤我们想要的信息
    print(items)



if __name__ == '__main__':
        for i in range(1):
            main()