#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests


# -------------------------------- 参数 --------------------------------

# phpsessid: 从已登陆浏览器的 Cookie 中复制 PHPSESSID
phpsessid = "Null"

# -------------------------------- 参数 --------------------------------


if phpsessid == "Null":
    print("\033c请从已登陆浏览器的 Cookie 中复制 PHPSESSID 至程序头部变量处")
    exit()

false = true = null = None

userAgent = "Mozilla/5.0 (Macintosh; Mac OS 2020; rv:105.0) Gecko/20100101 Firefox/105.0"
cookie = "PHPSESSID="+phpsessid
home = int(phpsessid.split("_")[0])

pixivHeaders = {
    "User-Agent": userAgent,
    "Cookie": cookie
}

pximgHeaders = {
    "User-Agent": userAgent,
    "referer": "https://www.pixiv.net/"
}


def report(code=0):
    input("按下回车以继续")


def getFollowingId(home):

    userId = []

    i = 0
    while True:
        url = "https://www.pixiv.net/ajax/user/"+str(home)+"/following?offset=" + \
            str(100*i) + "&limit=100&rest=show"

        try:
            page = requests.get(url, headers=pixivHeaders, timeout=5)
            if page.status_code == 200:
                page = page.text
            else:
                print("关注页面返回状态错误：第 "+str(i)+" 页返回了 " +
                      str(page.status_code)+" 状态码")
                report(2)

            users = eval(page)["body"]["users"]
            if not users:
                break
            for user in users:
                userId.append(int(user["userId"]))
        except:
            print("获取关注页面错误：第 "+str(i)+" 页")
            report(1)

        i += 1

    return userId


def getAuthorPicId(uid):

    picId = []

    url = "https://www.pixiv.net/ajax/user/"+str(uid)+"/profile/all"

    try:
        page = requests.get(url, headers=pixivHeaders, timeout=5)
        if page.status_code == 200:
            page = page.text
        else:
            print("用户作品页面返回状态错误：用户 ID "+str(uid))
            report(2)

        pics = eval(page)["body"]["illusts"]
        if not pics:
            print("找不到此用户的作品：用户 ID "+str(uid))
            report(3)
        for pic in pics:
            picId.append(int(pic))
    except:
        print("获取用户作品页面错误：用户 ID "+str(uid))
        report(1)

    return picId


def getAllPicUrl(pid):

    picUrl = []

    url = "https://www.pixiv.net/ajax/illust/"+str(pid)+"/pages"

    try:
        page = requests.get(url, headers=pixivHeaders, timeout=5)
        if page.status_code == 200:
            page = page.text
        else:
            print("作品详情页返回状态错误：作品 ID "+str(pid))
            report(2)

        urls = eval(page)["body"]
        for url in urls:
            picUrl.append(url["urls"]["original"].replace("\\", ""))
    except:
        print("获取作品详情页错误：作品 ID "+str(pid))
        report(1)

    return picUrl


# -------------------------------- 示例 --------------------------------

print("\033c", end="")

# getFollowingId( integer-Home ) -> list-UIDs: list of integers
# 输入用户 ID 获取所有关注者 UID
print(getFollowingId(home))

# getAuthorPicId( integer-UID ) -> list-PIDs: list of integers
# 输入作者 UID 获取作者所有作品 PID
print(getAuthorPicId(212801))

# getAllPicUrl( integer-PID ) -> list-URLs: list of strings
# 输入作品 PID 获取作品所有图片 URL
print(getAllPicUrl(78551403))

# -------------------------------- 示例 --------------------------------
