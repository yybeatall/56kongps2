# usr/bin/python
# encoding:utf-8
# 足迹版测试--执行交接提到货流程
import unittest
from time import sleep
from appium import webdriver
from method import setPrama

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = setPrama.setParam(self)

    '''①从首页交接按钮进入'''
    def testFromTakeover(self):
        try:
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/iv_handover").click()
            sleep(3)
            #点击确认提货
            self.driver.find_element_by_xpath('//android.widget.Button[contains(@text, "确认提货")]').click()
            # 点击确定
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()
            sleep(3)
            #点击确认到货
            self.driver.find_element_by_xpath('//android.widget.Button[contains(@text, "确认到货")]').click()
            # 点击确定
            self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()
            sleep(2)
            #返回
            self.driver.find_elements_by_class_name("android.widget.ImageButton").click()

        except Exception as e:
            print("不存在任务")
            print(e)

    '''②从首页提货按钮进入'''
    def testFromPickup(self):
        try:
            sleep(3)
            # 小米7提示
            #self.driver.find_element_by_id("com.yihu001.kon.driver:id/close").click()
            if self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_pickup").is_displayed():
                #点击首页待提区域
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_pickup").click()
                sleep(2)
                #点击确认提货
                self.driver.find_element_by_xpath('//android.widget.Button[contains(@text, "确认提货")]').click()
                #点击确定
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()
                sleep(2)
                # 返回
                self.driver.find_elements_by_class_name("android.widget.ImageButton").click()

        except Exception as e:
            print("不存在提货任务")
            print(e)

    '''③从首页到货按钮进入'''
    def testFromDelivery(self):
        try:
            if self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_delivery").is_displayed():
                #点击首页待提区域
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/rl_delivery").click()
                sleep(2)
                #点击确认到货
                self.driver.find_element_by_xpath('//android.widget.Button[contains(@text, "确认到货")]').click()
                #点击确定
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()
                sleep(2)
                # 返回
                self.driver.find_elements_by_class_name("android.widget.ImageButton").click()

        except Exception as e:
            print("不存在到货任务")
            print(e)

    ''''④从消息页进入'''
    def testFromMess(self):
        # 点击消息
        self.driver.find_elements_by_id("com.yihu001.kon.driver:id/bottom_navigation_container")[2].click()
        self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "业务消息")]')
        try:
            if self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "调度任务")]').is_displayed():
                #点击调度任务
                self.driver.find_element_by_xpath('//android.widget.TextView[contains(@text, "调度任务")]').click()
                sleep(2)
                #点击确认提货
                self.driver.find_element_by_xpath('//android.widget.Button[contains(@text, "确认提货")]').click()
                #点击确定
                self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_ok").click()
                sleep(2)
                #点击确认到货
                self.driver.find_element_by_xpath('//android.widget.Button[contains(@text, "确认到货")]').click()
                # 返回
                self.driver.find_elements_by_class_name("android.widget.ImageButton").click()

        except Exception as e:
            print("不存在到货任务")
            print(e)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
