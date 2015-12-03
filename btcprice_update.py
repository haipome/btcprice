#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json
import sys
import datetime

def get_okcoin_btc_price():
    url = 'https://www.okcoin.cn/api/ticker.do'
    r = urllib2.urlopen(url, timeout=5)
    data = json.loads(r.read())
    return float(data['ticker']['last'])

def get_okcoin_ltc_price():
    url = 'https://www.okcoin.cn/api/ticker.do?symbol=ltc_cny'
    r = urllib2.urlopen(url, timeout=5)
    data = json.loads(r.read())
    return float(data['ticker']['last'])

def get_okcoin_btc_future_price_week():
    url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=this_week'
    r = urllib2.urlopen(url, timeout=5)
    data = json.loads(r.read())
    return float(data['ticker']['last'])

def get_okcoin_btc_future_price_quarter():
    url = 'https://www.okcoin.com/api/v1/future_ticker.do?symbol=btc_usd&contract_type=quarter'
    r = urllib2.urlopen(url, timeout=5)
    data = json.loads(r.read())
    return float(data['ticker']['last'])

def get_usdcny_rate():
    url = 'http://finance.yahoo.com/d/quotes.csv?e=.csv&f=sl1d1t1&s=USDCNY=X'
    r = urllib2.urlopen(url, timeout=5)
    data = r.read()
    return float(data.split(",")[1])

def main():
    try:
        okcoin_btc_price = get_okcoin_btc_price()
    except:
        print >> sys.stderr, 'get okcoin btc price fail'
        sys.exit(1)

    try:
        okcoin_ltc_price = get_okcoin_ltc_price()
    except:
        print >> sys.stderr, 'get okcoin ltc price fail'
        sys.exit(1)

    try:
        okcoin_btc_future_week = get_okcoin_btc_future_price_week()
    except:
        print >> sys.stderr, 'get okcoin btc future price this week fail'
        sys.exit(1)

    try:
        okcoin_btc_future_quarter = get_okcoin_btc_future_price_quarter()
    except:
        print >> sys.stderr, 'get okcoin btc future price quarter fail'
        sys.exit(1)

    try:
        usdcny_rate = get_usdcny_rate()
    except:
        print >> sys.stderr, 'get usdcny rate fail'
        sys.exit(1)

    time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
    msg = u'#BTC# 成交价: %.2f, #LTC# 成交价: %.2f, BTC期货当周: %.2f, 季度: %.2f, 数据来源: OkCoin, 更新时间: %s #比特币#' % \
          (okcoin_btc_price, okcoin_ltc_price, okcoin_btc_future_week * usdcny_rate, okcoin_btc_future_quarter * usdcny_rate, time_str)

    access_token = '2.00SCW_1E0piBGI7b5f5065480jyb9q'
    post_data = urllib.urlencode({'access_token' : access_token, 'status' : msg.encode('utf-8') })

    post_url = 'https://api.weibo.com/2/statuses/update.json'
    r = urllib2.urlopen(post_url, post_data, 5);
    print r.read()

if __name__ == '__main__':
    main()

