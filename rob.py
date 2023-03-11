"""抢座位"""
from requestium import Session
from encrypt import encrypt

GLOBAL_HEADERS = {
    'User-Agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
}
INDEX_URL = 'https://passport2.chaoxing.com/login?fid=&newversion=true&refer=http%3A%2F%2Fi.chaoxing.com'
LOGIN_URL = "https://passport2.chaoxing.com/fanyalogin"
ROB_URL = 'http://office.chaoxing.com/front/apps/seatengine/select?id=roomid&day=date&backLevel=level&seatId=_seat'


def login(session, headers, uname, pw):
    global LOGIN_URL
    url = LOGIN_URL
    pw = encrypt(pw)
    uname = encrypt(uname)
    print('pw: ', pw)
    print('uname: ', uname)
    data = {
        "fid": "-1",
        "uname": f"{uname}",
        "password": f"{pw}",
        "refer": "http%3A%2F%2Fi.chaoxing.com",
        "t": "true",
        "forbidotherlogin": "0",
        "validate": "",
        "doubleFactorLogin": "0",
        "independentId": "0",
    }
    session.post(url, data=data, headers=headers)


# 获取roomid
def get_roomid(floor: int):
    """ 864(2楼) 865(3楼) 866(4楼)"""
    if floor == 2:
        return '864'
    elif floor == 3:
        return '865'
    elif floor == 4:
        return '866'


def rob(task: dict):
    session = task['session']
    headers = task['headers']
    uname = task['uname']
    pw = task['pw']
    level, seat, date, time_start, time_end = task['love_seats'][0]
    login(session, headers, uname, pw)
    session.transfer_session_cookies_to_driver()
    rob_url = ROB_URL
    rob_url = rob_url.replace('date', date)
    rob_url = rob_url.replace('level', str(level))
    rob_url = rob_url.replace('_seat', str(seat))
    rob_url = rob_url.replace('roomid', str(get_roomid(level)))
    print(rob_url)
    session.driver.get(rob_url)
    """...在这里补充selenium拖动滑块的代码..."""


if __name__ == '__main__':

    prefs = {  # 2代表禁止加载，1代表允许加载
        'profile.default_content_setting_values': {
            # 'images': 2,  # 禁止加载图片
            'permissions.default.stylesheet': 2,  # 禁止加载CSS
        }
    }

    """在这里定义你的任务"""
    task = {
        'uname': '18574485514',
        'pw': 'thy123456',
        'session': Session(webdriver_path='chromedriver.exe',
                           browser='chrome',
                           default_timeout=15,
                           webdriver_options={'prefs': prefs}),
        'love_seats': [(2, '115', '2023-03-11', '22:00', '22:30')],
        'headers': GLOBAL_HEADERS,
    }
    rob(task)
