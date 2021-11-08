#A股票行情数据获取演示   https://github.com/mpquant/Ashare
from  Ashare import *

# 600546 山煤国际
# 000400 许继
# 601669 电建
# 600010 宝钢
# 600111 北方稀土
# 601179 中国西电
# 002714 牧原
shares = {}
def myshare():
    shares["600546"] = "山煤国际"
    shares["000400"] = "许继"
    shares["601669"] = "电建"
    shares["600010"] = "宝钢"
    shares["600111"] = "北方稀土"
    shares["601179"] = "中国西电"
    shares["002714"] = "牧原"

    
# 证券代码兼容多种格式 通达信，同花顺，聚宽
# sh000001 (000001.XSHG)    sz399006 (399006.XSHE)   sh600519 ( 600519.XSHG ) 

df=get_price('sh000001',frequency='1m',count=20)      #默认获取今天往前5天的日线行情
print('上证指数日线行情\n',df)

# df=get_price('000001.XSHG',frequency='1d',count=5,end_date='2021-04-30')   #可以指定结束日期，获取历史行情
# print('上证指数历史行情\n',df)
#
# df=get_price('sh600546',frequency='15m',count=5)     #分钟线行情，只支持从当前时间往前推，可用'1m','5m','15m','30m','60m'
# print('shanmeiguoji_15\n',df)
#
# df=get_price('600546.XSHG',frequency='5m',count=6)  #分钟线行情，只支持从当前时间往前推，可用'1m','5m','15m','30m','60m'
# print('shanmeiguoji_5\n',df)

