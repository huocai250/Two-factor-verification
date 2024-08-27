'''
  by    huocai
github https://www.github.com/huocai250
'''
import requests
import json

# 控制台
print("\033[31m")
print("  ____    ____    _____   _____")
print(" |___ \  / ___|  |  ___| |__  /")
print("   __) | \___ \  | |_      / / ")
print("  / __/   ___) | |  _|    / /_ ")
print(" |_____| |____/  |_|     /____|")
print("                               ")
print("    by      huocai       ")
print("  github    https://www.github.com/huocai250")
# 获取用户输入的身份证号码和姓名
name = input(" 请输入姓名：")
sfz = input(" 请输入身份证号码：")

url = "https://web.7k7k.com/api/fcmauth.php"

params = {
  'gid': "register",
  'uid': "346967518",
  'name': name,
  'idNum': sfz,
  'ck': "2",
  'version': "465926",
  '_': "6375254968375"
}

headers = {
  'User-Agent': "Mozilla/5.0 (Linux; Android 13; 23049RAD8C Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.6533.103 Mobile Safari/537.36",
  'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
  'Accept-Encoding': "gzip, deflate, br, zstd",
  'sec-ch-ua': "\"Not)A;Brand\";v=\"99\", \"Android WebView\";v=\"127\", \"Chromium\";v=\"127\"",
  'sec-ch-ua-mobile': "?1",
  'sec-ch-ua-platform': "\"Android\"",
  'Upgrade-Insecure-Requests': "1",
  'dnt': "1",
  'X-Requested-With': "mark.via",
  'Sec-Fetch-Site': "none",
  'Sec-Fetch-Mode': "navigate",
  'Sec-Fetch-User': "?1",
  'Sec-Fetch-Dest': "document",
  'Accept-Language': "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
  'Cookie': "SERVER_ID=f23e65e6418a4d03af6561d6cf390240; PHPSESSID=moj4v870tpjmcq25h5mmub20t4; loginfrom=0100; web_uniques=891188935; preparekk=Mjc4ODU3NDc2MQ%3D%3D; timekey=af368c8719fdf1c06f84c48716ae5844; username=k2788574761; identity=k2788574761; nickname=2788574800; userid=892853978; kk=2788574800; logintime=1724675254; avatar=http%3A%2F%2Fsface.7k7kimg.cn%2Fuicons%2Fphoto_default_s.png; securitycode=f3c28d2d823ed66afdd5717775aeb11c; k7_union=9999999; k7_username=k2788574761; k7_uid=892853978; k7_from=3841; k7_reg=1724675254; k7_ip=10.19.27.189; userprotect=eeda8be88efdeef8b26010266232be2d; userpermission=6a1558b9f756c09affad6f72ea3b0823; k7_lastlogin=2024-08-26+20%3A27%3A34; k7_lastlogin=1724675448"
}

response = requests.post(url, params=params, headers=headers)
json_text = response.json()
#print(json_text["info"])


# 输出响应内容
if json_text["info"] == "注册实名成功。":
    print(" 二要素通过")
    print(" " + "姓名" + " " + name)
    print(" " + "身份证" + " " + sfz)
else:
    print(" 二要素未通过")
