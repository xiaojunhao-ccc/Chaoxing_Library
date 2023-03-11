# 删除残留临时文件
def delete_rubbish():
    print('正在清除浏览器临时残留文件.....')
    import os
    import shutil
    folder = os.listdir(r'C:\Users\XIAOJU~1\AppData\Local\Temp')  # 存放有临时文件的路径
    for filename in folder:
        if 'scoped' in filename:  # 临时文件夹
            filepath = r'C:\Users\XIAOJU~1\AppData\Local\Temp\{0}'.format(filename)
            try:
                shutil.rmtree(filepath)  # shutil.rmtree()用于删除非空文件夹
                print(f'{filepath}已经删除.')
            except PermissionError:
                continue
    print('清除完毕!')


if __name__ == '__main__':
    delete_rubbish()
