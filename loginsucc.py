# usr/bin/python
# encoding:utf-8
# 足迹版测试--登录
import unittest
from time import sleep

from appium import webdriver
from ddt import ddt, data, unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        # 天天模拟器
        # desired_caps['platformVersion'] = '4.4.4'
        # desired_caps['deviceName'] = '127.0.0.1:6555'
        #小米真机
        desired_caps['platformVersion'] = '5.1.1'
        desired_caps['deviceName'] = 'd727fe13'
        desired_caps['appPackage'] = 'com.yihu001.kon.driver'
        desired_caps['appActivity'] = '.activity.MainActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        # desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @data(("13900001127", "123456"))
    @unpack
    def testLoginsucc(self, username, password):
        global exist
        #小米7提示
        #self.driver.find_element_by_id("com.yihu001.kon.driver:id/close").click()
        sleep(2)
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_user_name").send_keys(username)
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_pwd").send_keys(password)
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_sign").click()

        sleep(3)

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
