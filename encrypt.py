"""用于学习通加密账号密码"""
import execjs


def encrypt(pw: str):
    key = 'u2oh6Vu^HWe4_AES'
    ctx = execjs.compile(open("cxpw.js", encoding="utf-8").read())
    js = f'encryptByAES("{pw}", "{key}")'
    pwd = ctx.eval(js)
    return pwd


if __name__ == '__main__':
    print(encrypt('1231313131'))
