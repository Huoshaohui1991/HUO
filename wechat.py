#!/usr/bin/python
# -*- coding: utf-8 -*-
import itchat
import re
import jieba
import matplotlib.pyplot as plt
import PIL.Image as Image
import numpy as np
import os
from wordcloud import WordCloud, ImageColorGenerator

TList = []


def get_signature():
    friends = itchat.get_friends(update=True)[0:]
    for friend in friends:
        signature = friend["Signature"].strip()
        signature = re.sub("<span.*>", "", signature)
        signature = re.sub(" ", "", signature)
        signature = re.sub("emoji ", "", signature)
        TList.append(signature)


def cloud_pic():
    raw_signature_string = ''.join(TList)
    text = jieba.cut(raw_signature_string, cut_all=True)
    wl_space_split = ' '.join(text)

    d = os.path.dirname(os.path.abspath(__file__))

    alice_coloring = np.array(Image.open(os.path.join(d, "dm.jpg")))  # 原图

    my_wordcloud = WordCloud(background_color="black",  # 背景色
                             max_words=2500,  # 字数上限
                             stopwords=STOPWORDS.add("said"),
                             mask=alice_coloring,  # 形状
                             max_font_size=75,  # 字体大小
                             random_state=150,  # 随机数量
                             font_path='C:/Windows/Fonts/simhei.ttf').generate(wl_space_split)  # 中文字体
    image_color = ImageColorGenerator(alice_coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_color))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()


def main():
    itchat.login()
    get_signature()
    cloud_pic()
    itchat.logout()


if __name__ == '__main__':
    main()
