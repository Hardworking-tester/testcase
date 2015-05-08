# encoding:utf-8
from selenium import webdriver
import unittest
class Pt(unittest.TestCase):


    def test1(self):
        br=webdriver.Firefox()
        br.find_element_by_link_text(u"请登录").click()
        br.find_element_by_id("userName").clear()
        br.find_element_by_id("userName").send_keys("wwg74581@163.com")
        br.find_element_by_id("password").clear()
        br.find_element_by_id("password").send_keys('wwg123456')
        br.find_element_by_id("imgLogin").click()
        print br.switch_to_alert().text

        br.switch_to_alert().accept()