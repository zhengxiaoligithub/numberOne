# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#Item是保存数据的容器
class BilibiliItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    sex = scrapy.Field()
    level = scrapy.Field()
    birthday = scrapy.Field()
    follower = scrapy.Field()
    following = scrapy.Field()
    animation = scrapy.Field()#动画
    Life = scrapy.Field()
    Music = scrapy.Field()
    Game = scrapy.Field()
    Dance = scrapy.Field()
    Documentary = scrapy.Field()#纪录片
    Ghost = scrapy.Field()#鬼畜
    science = scrapy.Field()
    Opera = scrapy.Field()
    entertainment = scrapy.Field()#娱乐
    Movies = scrapy.Field()
    National = scrapy.Field()
    Digital = scrapy.Field()
    fashion = scrapy.Field()

    pass
