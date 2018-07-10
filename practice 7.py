#!/usr/bin/python
# -*- coding: utf-8 -*-
import itchat
import re
import jieba


def echart_pie(friends):
    total = len(friends) - 1
    male = female = other = 0

    for friend in friends[1:]:
        sex = friend["Sex"]
        if sex == 1:
            male += 1
        elif sex == 2:
            female += 1
        else:
            other += 1
    from echarts import Echart, Legend, Pie
    chart = Echart('%s的微信好友性别比例' % (friends[0]['Name']), 'from WeChat')
    chart.use(Pie('WeChat',
                  [{'value': male, 'name': '男性 %.2f%%' % (float(male) / total * 100)},
                   {'value': female, 'name': '女性 %.2f%%' % (float(female) / total * 100)},
                   {'value': other, 'name': '其他 %.2f%%' % (float(other) / total * 100)}],
                  radius=["50%", "70%"]))
    chart.use(Legend(["male", "female", "other"]))
    del chart.json["xAxis"]
    del chart.json["yAxis"]
    chart.plot()


def word_cloud(friends):
    import matplotlib.pyplot as plt
    from wordcloud import WordCloud, ImageColorGenerator
    import PIL.Image as Image
    import os
    import numpy as np
    d = os.path.dirname(os.path.abspath(__file__))
    alice_coloring = np.array(Image.open(os.path.join(d, "wechat.jpg")))
    signature_list = []
    for friend in friends:
        signature = friend["Signature"].strip()
        signature = re.sub("<span.*>", "", signature)
        signature_list.append(signature)
    raw_signature_string = ''.join(signature_list)
    text = jieba.cut(raw_signature_string, cut_all=True)
    target_signatur_string = ' '.join(text)

    my_wordcloud = WordCloud(background_color="black", max_words=4000, mask=alice_coloring,
                             max_font_size=50, random_state=75,
                             font_path=r"C:\Windows\Fonts\simhei.ttf").generate(target_signatur_string)
    image_colors = ImageColorGenerator(alice_coloring)
    plt.imshow(my_wordcloud.recolor(color_func=image_colors))
    plt.imshow(my_wordcloud)
    plt.axis("off")
    plt.show()
    # 保存图片 并发送到手机
    my_wordcloud.to_file(os.path.join(d, "wechat_cloud.png"))
    itchat.send_image("wechat_cloud.png", 'filehelper')


itchat.auto_login(hotReload=True)
itchat.dump_login_status()

friends = itchat.get_friends(update=True)[:]

# echart_pie(friends)

word_cloud(friends)