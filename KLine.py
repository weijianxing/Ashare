#-*- coding: utf-8 -*-
# 
# __author__ : jianxing.wei

import  mplfinance
from matplotlib.dates import date2num
from mplfinance.original_flavor import candlestick_ohlc

# import tushare as ts
# import pandas as pd
# import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib import ticker
# from matplotlib.pylab import date2num
# import numpy as np
import matplotlib.pyplot as plt
# from matplotlib.pylab import date2num
# import mpl_finance
# from mpl_finance import candlestick_ohlc
import  datetime

from Ashare import get_price


# def format_date(x,pos):
#     if x<0 or x>len(date_tickers)-1:
#         return ''
#     return date_tickers[int(x)]

# 600546 山煤国际
# 000400 许继
# 601669 电建
# 600010 宝钢
# 600111 北方稀土
# 601179 中国西电
# 002714 牧原

df=get_price('600546.XSHG',frequency='5m',count=30)      #默认获取今天往前120天的日线行情

print('山煤日线行情\n',df.tail(5))


# data_list = []
# for dates,row in df.iterrows():
#     date_time = datetime.datetime.strptime(str(dates), '%Y-%m-%d %H:%M:%S')
#     # print(date_time)
#     t = date2num(date_time)
#     open, close, high, low = row[:4]
#     data = (t, open, high, low, close)
#     data_list.append(data)
#
# # 创建一个figure
# fig, ax = plt.subplots()
# fig.subplots_adjust(bottom=0.2)
#
#
# # 设置x轴为日期
# ax.xaxis_date()
# plt.xticks(rotation=45)
# plt.yticks()
# plt.title('a share')
# plt.xlabel("时间")
# plt.ylabel("股价（元）")
#
# candlestick_ohlc(
#     ax=ax,
#     quotes=data_list,
#     width=0.2,
#     colorup='#ff1717',
#     colordown='#53c16',
#     alpha=1)
#
# plt.grid(True)
# plt.show()