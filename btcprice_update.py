#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib
import urllib2
import json
import sys
import datetime

def get_okcoin_btc_price():
	url = 'https://www.okcoin.com/api/ticker.do'
	r = urllib2.urlopen(url)
	data = json.loads(r.read())
	return float(data['ticker']['last'])

def get_okcoin_ltc_price():
	url = 'https://www.okcoin.com/api/ticker.do?symbol=ltc_cny'
	r = urllib2.urlopen(url)
	data = json.loads(r.read())
	return float(data['ticker']['last'])

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

	time_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')
	msg = u'BTC 最近成交价: %.2f, LTC 最新成交价: %.2f, 数据来源: OkCoin, 更新时间: %s' % \
	      (okcoin_btc_price, okcoin_ltc_price, time_str)

	access_token = 'your_access_token'
	post_data = urllib.urlencode({'access_token' : access_token, 'status' : msg.encode('utf-8') })

	post_url = 'https://api.weibo.com/2/statuses/update.json'
	r = urllib2.urlopen(post_url, post_data);
	print r.read()

if __name__ == '__main__':
	main()

