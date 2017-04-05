#usr/bin/python
#encoding:utf-8
#足迹版登录测试
import unittest
from time import sleep

from appium import webdriver
from ddt import ddt, data, unpack

@ddt
class MyTestCase(unittest.TestCase):
    def setUp(self):
        #天天模拟器
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.4.4'
        desired_caps['deviceName'] = '127.0.0.1:6555'
        desired_caps['appPackage'] = 'com.yihu001.kon.driver'
        desired_caps['appActivity'] = '.activity.LoginActivity'
        desired_caps["unicodeKeyboard"] = "True"
        desired_caps["resetKeyboard"] = "True"
        #desired_caps["automationName"] = "Selendroid"
        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

    @data(("13900000217","123456","用户13900000217不存在！",False,True),
          ("13900001127","12345","密码错误！",False,True),
          ("1390000112","123456","用户1390000112不存在！",False,True),
          ("13900001127","123456","登录成功",True,False)
          )

    @unpack
    def testLogIn(self, username, password, toastmessage, expectedresult, toastresult):
        global exist, toastexist
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_user_name").send_keys(username)
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/et_pwd").send_keys(password)
        self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_sign").click()

        sleep(3)
        # try:
        #     if self.driver.find_element_by_link_text(toastmessage).is_displayed():
        #         toastexist = True
        # except Exception as e:
        #     toastexist = False
        try:
            if self.driver.find_element_by_id("com.yihu001.kon.driver:id/btn_sign").is_displayed():
                exist = False
                print(self.driver.find_element_by_link_text(toastmessage).text)
                try:
                    if self.driver.find_element_by_link_text(toastmessage).is_displayed():
                        toastexist = True
                except Exception as e:
                    toastexist = False
        except Exception as e:
            exist = True

        self.assertEqual(exist,expectedresult)
        self.assertEqual(toastexist, toastresult)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
