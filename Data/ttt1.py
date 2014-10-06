# encoding:utf-8
from selenium import webdriver
import unittest
class Tt(unittest.TestCase):
    def test1(self):
        u"""打开百度"""
        br=webdriver.Firefox()
        br.get("http://www.baidu.com")
        br.find_element_by_link_text(u"新闻").click()
    def test2(self):
        u"""打开鲜易网"""
        br=webdriver.Firefox()
        br.get("http://www.xebest.com")
