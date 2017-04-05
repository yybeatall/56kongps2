# usr/bin/python
# encoding:utf-8
# 足迹版测试--注销
import unittest
from time import sleep

from appium import webdriver


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

    def testLogout(self):
        sleep(5)
        #小米7提示
        #self.driver.find_element_by_id("com.yihu001.kon.driver:id/close").click()
        #点击我的
        self.driver.find_elements_by_id("com.yihu001.kon.driver:id/bottom_navigation_container")[3].click()
        #self.driver.find_element_by_xpath('//com.yihu001.kon.driver:id/bottom_navigation_item_title[contains(@text, "我的")]').click()
        #self.driver.find_elements_by_class_name("android.widget.FrameLayout")[4].click()
        #点击设置按钮
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/profile_set").click()
        #滑动
        e1=self.driver.find_element_by_id("com.yihu001.kon.driver:id/update_password_layout")
        e2=self.driver.find_element_by_id("com.yihu001.kon.driver:id/image_cache_layout")
        self.driver.scroll(e1,e2)
        sleep(2)
        #点击退出
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/exit").click()
        #确定
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/ok").click()
        sleep(3)

    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()
