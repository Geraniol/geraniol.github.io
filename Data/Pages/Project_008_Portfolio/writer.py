#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

with open(sys.path[0]+"/temple.html", "rt")as f:
    content = f.read()

pointer = content.find('["python_database"]')

datas = [
    [
        "000.jpg",
        "今日份のChicken",
        "Describe: Null"
    ],
    [
        "001.jpg",
        "Chicken Union 2020",
        "仿制海报"
    ],
    [
        "002.jpg",
        "酒杯少女",
        "手办"
    ],
    [
        "003.jpg",
        "Futura",
        "仿制海报"
    ],
    [
        "004.jpg",
        "Geraniol",
        "原始头像"
    ],
    [
        "005.jpg",
        "伞",
        "Describe: Null"
    ],
    [
        "006.jpg",
        "Gimdong 娘",
        "原创 1 号画作"
    ],
    [
        "007.jpg",
        "鸡蛋花",
        "Describe: Null"
    ],
    [
        "008.jpg",
        "山、云与天空",
        "惬意的时光，高中教室外的风景"
    ],
    [
        "009.jpg",
        "镜子",
        "实验室里的意外发现让我得知了还有这种物品的存在"
    ],
    [
        "010.jpg",
        "窗外的风景（油画）",
        "家、城市与夕阳"
    ],
    [
        "011.jpg",
        "景观花",
        "见证了很多无意义的开销"
    ],
    [
        "012.jpg",
        "宿舍一角",
        "惬意的时光，大学宿舍外的风景"
    ],
    [
        "013.jpg",
        "奇幻的大学生活",
        "充满了不真实的感觉"
    ],
    [
        "014.jpg",
        "铝热熔融实验",
        "闪闪发光的高中回忆"
    ],
    [
        "015.jpg",
        "神秘的盒子",
        "她，惬意的夏日，以及漫不经心的高考"
    ]
]

for data in datas:
    data[0] = "./images/"+data[0]

with open(sys.path[0]+"/index.html", "wt")as f:
    f.write(content[:pointer]+str(datas)+content[pointer+19:])
