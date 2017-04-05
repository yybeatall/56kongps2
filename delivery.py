#usr/bin/python
#encoding:utf-8
#足迹版测试--到货
import unittest
from time import sleep

from appium import webdriver


class MyTestCase(unittest.TestCase):
    def setUp(self):
        #天天模拟器
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
        #desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    def testDelivery(self):
        try:
            sleep(3)
            # 小米7提示
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/close").click()
            if self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_delivery").is_displayed():
                #点击首页待提区域
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_delivery").click()
                sleep(2)
                #点击上传照片
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_picture").click()
                #点击回单
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_four").click()
                #点击确定
                self.driver.find_element_by_id("android:id/button3").click()
                #点击确认到货
                self.driver.find_element_by_xpath('//android.widget.Button[contains(@text, "确认到货")]').click()
                #点击取消
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_cancel").click()
                #再次点击确认到货
                self.driver.find_element_by_xpath('//android.widget.Button[contains(@text, "确认到货")]').click()
                #点击确定
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()


        except Exception as e:
            print("不存在到货任务")


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
