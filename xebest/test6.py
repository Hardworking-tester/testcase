# encoding:utf-8
from selenium import webdriver
import time
br=webdriver.Firefox()
br.get("https://user.xebest.com:8443/reg.action")
br.find_element_by_id("userName").send_keys('wwg1544847112@163.com')
br.find_element_by_id("passWord").send_keys('wwg123456')
br.find_element_by_id('Again').send_keys('wwg123456')
br.find_element_by_id('mobile').send_keys('18635487699')
time.sleep(50)
br.find_element_by_id('regist-btn').click()