import requests

def get_url(file):
    """取出文本中的url"""
    urls = []
    with open(file, mode='r') as f:
        for line in f.read().splitlines():
            urls.append(line)
    return urls

def check_url(urls):
    """检测url"""
    res_ls = []
    fail_ls = []
    for url in urls:
        try:
            r = requests.get(url, timeout=2)
            res_dict = {url: r.status_code}
            res_ls.append(res_dict)
        except:
            print(url + " 连接失败...\n")
            fail_ls.append(url)
    return res_ls, fail_ls


if __name__ == '__main__':
    urls = get_url("url_list.txt")
    res_ls, fail_ls = check_url(urls)

    print("连接成功的url：")
    for res in res_ls:
        for k, v in res.items():
            print('连接成功  状态码：' + str(v) + ' url地址：' + k)
            
    print("\n连接失败的url：")
    for i in fail_ls:
        print(i)

"""
=====url_list.txt example=====

https://www.163.com
https://www.baidu.com
https://www.qq.com
https://www.zhihu.com
https://texmqoef.com
https://gwkkka.com

"""
