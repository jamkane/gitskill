# -*- coding: utf-8 -*-
__author__ = 'zhoujim'

#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from apscheduler.schedulers.blocking import BlockingScheduler
import re
import json


#用户名、密码
I_user = '###'
I_pass= '###'
#打卡时间
c_minute="4"
c_hour="6,8"
c_week="mon-sun"

def work():
	right()      ##恩山论坛
	bbsmcx()     ##萌出血
	#wenku()      ##百度文库
	xingkong()   ##星空论坛
	znds()      ##智能电视论坛
	zhongdian()
	#smzdm()      ##什么值得买
	print("-------------------------------")
	print("")


def right():
	chrome_opt = Options()      # 创建参数设置对象.
	chrome_opt.add_argument('--headless')   # 无界面化.
	chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
	chrome_opt.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.
	browser = webdriver.Chrome(chrome_options=chrome_opt)
	#browser = webdriver.Chrome()
	try:
		with open('right.json', 'r', encoding='utf8') as f:
			listCookie = json.loads(f.read())
			#print(listCookie)
		browser.get("https://www.right.com.cn/forum/home.php?mod=spacecp&ac=credit&showcredit=1")
		browser.delete_all_cookies()
		time.sleep(2)
		for cookie in listCookie:
			#print("%s->%s" % (cookie['name'], cookie['value']))
			#print(cookie)
			if 'expiry' in cookie:
			 	del cookie['expiry']
			browser.add_cookie(cookie)
		# cookies = browser.get_cookies()
		# jsonCookies = json.dumps(cookies)
		# with open('right1.json','w') as f:
		#     f.write(jsonCookies)
		browser.refresh()
		browser.maximize_window()
		ttt = browser.find_element_by_xpath('//*[@onmouseover ="delayShow(this, showCreditmenu);"]')
		print('==恩山论坛===',ttt.text)
		time.sleep(5)
		browser.quit()
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 恩山论坛-签到成功!")
	except  Exception as e:
		print(e)
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 恩山论坛-签到失败!")
		browser.quit()

def znds():
	chrome_opt = Options()      # 创建参数设置对象.
	chrome_opt.add_argument('--headless')   # 无界面化.
	chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
	chrome_opt.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.
	browser = webdriver.Chrome(chrome_options=chrome_opt)
	#browser = webdriver.Chrome()
	try:
		with open('znds.json', 'r', encoding='utf8') as f:
			listCookie = json.loads(f.read())
			#print(listCookie)
		browser.get("https://www.znds.com/")
		browser.delete_all_cookies()
		time.sleep(2)
		for cookie in listCookie:
			#print("%s->%s" % (cookie['name'], cookie['value']))
			#print(cookie)
			if 'expiry' in cookie:
			 	del cookie['expiry']
			browser.add_cookie(cookie)
		browser.refresh()
		browser.maximize_window()
		time.sleep(1)
		ttt = browser.find_element_by_xpath('//*[@style ="cursor:pointer"]')
		#button = browser.find_element_by_class_name('pn')
		#button.click()
		ttt.click()
		time.sleep(1)
		#browser.execute_script('alert("签到成功啦")')
		time.sleep(5)
		browser.quit()
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 智能电视论坛-签到成功!")
	except  Exception as e:
		print(e)
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 智能电视论坛-签到失败!")
		browser.quit()
	# try:
	# 	browser.get("https://www.znds.com/member.php?mod=logging&action=login&referer=")
	# 	input_str = browser.find_element_by_name('username')
	# 	#print(input_str)
	# 	input_str.send_keys(I_user)
	# 	time.sleep(1)
	# 	#browser.find_element_by_name('password').click()
	# 	#input_str = browser.find_element_by_name('password')
	# 	#print(input_str)
	# 	input_str = browser.find_element_by_xpath('//input[@name="password" and @class="px p_fre"]')
	# 	print(input_str)
	# 	input_str.send_keys(I_pass)
	# 	#browser.close()
	# 	time.sleep(1)
	# 	#button = browser.find_element_by_class_name('pn')
	# 	#button.click()
	# 	time.sleep(1)
	# 	#browser.execute_script('alert("签到成功啦")')
	# 	#time.sleep(1)
	# 	browser.quit()
	# 	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 签到成功!")
	# except Exception as e:
	# 	print(e)
	# 	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 签到失败!")
	# 	browser.quit()

def bbsmcx():
	chrome_opt = Options()      # 创建参数设置对象.
	chrome_opt.add_argument('--headless')   # 无界面化.
	chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
	chrome_opt.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.
	#browser = webdriver.Chrome(chrome_options=chrome_opt)
	browser = webdriver.Chrome()
	try:
		browser.get("https://www.bbsmcx.com/member.php?mod=logging&action=login")
		#browser.get("https://www.bbsmcx.com/forum.php")
		#browser.find_element_by_xpath('/html/body/div[4]/div/div/div[4]/div/div/ul/li/a[1]').click()
		input_str = browser.find_element_by_name('username')
		input_str.send_keys(I_user)
		time.sleep(1)
		input_str = browser.find_element_by_name('password')
		input_str.send_keys(I_pass)
		time.sleep(1)
		button = browser.find_element_by_name('loginsubmit')
		button.click()
		time.sleep(1)
		#browser.execute_script('alert("签到成功啦")')
		browser.get("https://www.bbsmcx.com/plugin.php?id=dsu_paulsign:sign")
		browser.find_element_by_xpath('/html/body/div[5]/div[2]/div/div/ul/li[3]/a[1]').click()
		time.sleep(1)
		ttt = browser.find_element_by_xpath('//*[@src = "source/plugin/dsu_paulsign/img/emot/xq7.gif"]')
		ttt.click()
		ttt=browser.find_element_by_xpath('//*[@name="qdmode" and @value = "2"]')
		ttt.click()
		ttt = browser.find_element_by_xpath('//*[@src = "source/plugin/dsu_paulsign/img/qdtb.gif"]')
		ttt.click()
		time.sleep(1)
		#context = browser.page_source.lower()
		#print(context)
		#jifen = re.search(r'<b>(\d*)</b>', context).group()
		#print(jifen)
		browser.quit()
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": bbsmcx 签到成功!")
	except:
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": bbsmcx 签到失败!")
		browser.quit()

def wenku():
	chrome_opt = Options()      # 创建参数设置对象.
	chrome_opt.add_argument('--headless')   # 无界面化.
	chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
	chrome_opt.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.
	browser = webdriver.Chrome(chrome_options=chrome_opt)
	#browser = webdriver.Chrome()
	try:
		with open('wenku.json', 'r', encoding='utf8') as f:
			listCookie = json.loads(f.read())
		browser.get("https://wenku.baidu.com/task/browse/daily")
		time.sleep(2)
		for cookie in listCookie:
			#print("%s->%s" % (cookie['name'], cookie['value']))
			#print(cookie)
			browser.add_cookie(cookie)
		browser.refresh()
		browser.maximize_window()
		time.sleep(5)
		ttt = browser.find_element_by_xpath('//*[@class = "g-btn g-btn-pass js-signin-btn g-btn-no"]')
		ttt.click()
		time.sleep(2)
		browser.quit()
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 百度文库-签到成功!")
	except:
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 百度文库-签到失败!")
		browser.quit()


def smzdm():
	chrome_opt = Options()      # 创建参数设置对象.
	chrome_opt.add_argument('--headless')   # 无界面化.
	chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
	chrome_opt.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.
	browser = webdriver.Chrome(chrome_options=chrome_opt)
	#browser = webdriver.Chrome()
	try:
		str = ''
		with open('smzdm.json', 'r', encoding='utf8') as f:
			listCookie = json.loads(f.read())
		browser.get("https://www.smzdm.com/")
		time.sleep(2)
		for cookie in listCookie:
			#print(cookie)
			browser.add_cookie(cookie)
		browser.refresh()
		browser.maximize_window()
		time.sleep(3)
		ttt = browser.find_element_by_xpath('//*[@href = "javascript:void(0);" and @class = "J_punch"]')
		#print(ttt)
		ttt.click()
	# cookies = browser.get_cookies()
	# jsonCookies = json.dumps(cookies)
	# with open('smzdm.json','w') as f:
	# 	f.write(jsonCookies)
	# with open('smzdm.json', 'r', encoding='utf8') as f:
	# 	listCookie = json.loads(f.read())
	# for cookie in listCookie:
	# 	print(cookie)
		browser.quit()
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 什么值得买-签到成功!")
	except  Exception as  e:
		print("ERROR:",e)
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 什么值得买-签到失败!")
		browser.quit()

def xingkong():
	chrome_opt = Options()      # 创建参数设置对象.
	chrome_opt.add_argument('--headless')   # 无界面化.
	chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
	chrome_opt.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.
	browser = webdriver.Chrome(chrome_options=chrome_opt)
	#browser = webdriver.Chrome()
	try:
		str = ''
		with open('xinkong.json', 'r', encoding='utf8') as f:
			listCookie = json.loads(f.read())
			#print(listCookie)
		browser.get("https://bbs2.seikuu.com/home.php?mod=space&uid=374318")
		browser.delete_all_cookies()
		time.sleep(2)
		for cookie in listCookie:
			if 'expiry' in cookie:
				del cookie['expiry']
			#print(cookie)
			browser.add_cookie(cookie)
		browser.refresh()
		browser.maximize_window()
		ttt = browser.find_element_by_xpath('//*[@type = "text" and @name = "todaysay"]')
		ttt.send_keys("今天心情真不错!!")
		time.sleep(1)
		ttt = browser.find_element_by_xpath('//*[@src = "source/plugin/dsu_paulsign/img/emot/kx.gif"]')
		ttt.click()
		time.sleep(1)
		ttt = browser.find_element_by_xpath('//*[@type = "button" and @class = "pn pnc"]')
		ttt.click()
		time.sleep(5)
		# cookies = browser.get_cookies()
		# jsonCookies = json.dumps(cookies)
		# with open('xinkong.json','w') as f:
		#     f.write(jsonCookies)
		# for cookie in cookies:
		#     print("%s->%s" % (cookie['name'], cookie['value']))
		# print(cookies)
		browser.quit()
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 星空论坛-签到成功!")
	except  Exception as  e:
		print("ERROR:",e)
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 星空论坛-签到失败!")
		browser.quit()

def zhongdian():
	chrome_opt = Options()      # 创建参数设置对象.
	chrome_opt.add_argument('--headless')   # 无界面化.
	chrome_opt.add_argument('--disable-gpu')    # 配合上面的无界面化.
	chrome_opt.add_argument('--window-size=1366,768')   # 设置窗口大小, 窗口大小会有影响.
	browser = webdriver.Chrome(chrome_options=chrome_opt)
	#browser = webdriver.Chrome()
	try:
		str = ''
		with open('zhongdian.json', 'r', encoding='utf8') as f:
			listCookie = json.loads(f.read())
			#print(listCookie)
		browser.get("https://bbs.zdfx.net/k_misign-sign.html")
		time.sleep(5)
		browser.delete_all_cookies()
		time.sleep(2)
		for cookie in listCookie:
			if 'expiry' in cookie:
				del cookie['expiry']
			#print(cookie)
			browser.add_cookie(cookie)
		browser.refresh()
		browser.maximize_window()
		ttt = browser.find_element_by_xpath('//*[@id="JD_sign" and @class = "btn J_chkitot"]')
		ttt.click()
		time.sleep(15)
		browser.quit()
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 终点论坛-签到成功!")
	except  Exception as  e:
		print("ERROR:",e)
		print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": 终点论坛-签到失败!")
		browser.quit()

def job():
		print(datetime.now().strtime("%Y-%m-%d %H:%M:%S"))

if __name__ == '__main__':
	# wenku()
	# work()
	# right()
	# znds()
	# bbsmcx()
	# smzdm()
	# xingkong()
    # znds()
    # zhongdian()

	#添加任务
	scheduler = BlockingScheduler()
	scheduler.add_job(work, "cron", hour='6,8', minute=4)
	print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())+": Add Task Work!")
	try:
		scheduler.start()
	except (KeyboardInterrupt, SystemExit):
		scheduler.shutdown()
