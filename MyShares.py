#-*- coding: utf-8 -*-
# 
# __author__ : jianxing.wei
from time import sleep

from Ashare import *
import numpy as np

# 600546 山煤国际
# 000400 许继
# 601669 电建
# 600010 宝钢
# 600111 北方稀土
# 601179 中国西电
# 002714 牧原
shares = {}


def myshare():
    shares["SZ000400"] = "许继电器"
    shares["SZ000629"] = "攀钢"
    # shares["sh601669"] = "电建"
    shares["SZ002165"] = "红宝丽"
    shares["sh600111"] = "北方"
    # shares["sh600025"] = "华能水"
    shares["SZ000831"] = "五矿"
    # shares["sh601179"] = "西电"
    # shares["SZ000825"] = "太钢不锈"
    shares["SZ002714"] = "牧原"
    shares["sh000001"] = "ashares"

#
def myshare_test():

    shares["SZ002714"] = "牧原"
    # shares["sh000001"] = "ashares"

def get5m(c = 24):
    myshare()
    for k in shares.keys():
        print("" + shares[k])
        df = get_price(k, frequency='5m', count = c)
        sleep(3)
        print(df)

def get1m(c = 15):
    myshare()
    for k in shares.keys():
        print("" + shares[k])
        df = get_price(k, frequency='1m', count = c)
        sleep(3)
        print(df)
def get1day(c = 5):
    myshare()
    for k in shares.keys():
        print("" + shares[k])
        df = get_price(k, frequency='1d', count = c)
        sleep(3)
        print(df)

def get15m(c = 28):
    myshare()
    for k in shares.keys():
        print("" + shares[k])
        df = get_price(k, frequency='15m', count = c)
        sleep(3)
        print(df)
def get30m(c = 12):
    myshare()
    for k in shares.keys():
        print("" + shares[k])
        df = get_price(k, frequency='30m', count = c)
        sleep(3)
        print(df)

#最近某个时间段的数据信息
def get5m_Days(begin_m, end_m, days=1):
    myshare()
    for k in shares.keys():
        print("" + shares[k])
        # 9:30-11:30 : 13:00 - 15:00 4h*12
        size = days*48
        # 爬虫接口数据量大无返回
        df = get_price(k, frequency='5m', count = size)
        #panda 数据过滤
        print(df)
        df = df.between_time(begin_m,end_m)
        # df[df['day'].dt.hour.isin(np.arange(begin_m, end_m))]
        print("---------filter-------------")
        print(df)

    pass

def getVolumeDiff_5m(c = 5 ):
    myshare_test()
    volume_sell = 0
    volume_buy = 0
    for k in shares.keys():
        print("" + shares[k])
        df = get_price(k, frequency='5m', count=c)
        # print(df)
        sleep(3)
        for row in df.itertuples():
            print(getattr(row,'Index'), getattr(row,'open'), getattr(row,'close'),getattr(row,'volume'))
            diff_price = getattr(row,'close') - getattr(row,'open')

            if diff_price >= 0:
                volume_buy = getattr(row,'volume') + volume_buy
                print("up ",'%.3f'%(diff_price*100/getattr(row,'open')))
            else:
                volume_sell = getattr(row, 'volume') + volume_sell
                print("down ", '%.3f' % (diff_price*100 / getattr(row, 'open')))
        # print(df)
        print("sell/buy", '%.3f'%(volume_sell/volume_buy))
        diff = volume_buy - volume_sell
        print("volume buy diff sell", diff)

def getPrice_days(day = 3):
    df = get_price('sh000001', end_date='', frequency='5m', count=5)
    print(df)
if __name__ == '__main__':
    # getVolumeDiff_5m(24)
    get5m(12)
    # get1m(10)
    # get5m_Days('14:00','15:00',1)
    # getPrice_days()