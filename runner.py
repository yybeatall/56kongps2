import loginsucc
import pickup,delivery,logout
import unittest

# mysuite = unittest.TestSuite()
# mysuite.addTest(loginsucc.MyTestCase("testLogIn"))
# mysuite.addTest(loginsucc.MyTestCase("testLoginsucc"))
# mysuite.addTest(pickup.MyTestCase("testPickup"))


# 执行登录
logincases = unittest.TestLoader().loadTestsFromTestCase(loginsucc.MyTestCase)
# 执行提货
pickupcases = unittest.TestLoader().loadTestsFromTestCase(pickup.MyTestCase)
# 执行到货
deliverycases = unittest.TestLoader().loadTestsFromTestCase(delivery.MyTestCase)
#注销
logutcases = unittest.TestLoader().loadTestsFromTestCase(logout.MyTestCase)

mysuite = unittest.TestSuite([logincases, pickupcases, deliverycases,logutcases])

# mysuite.addTest(unittestdemo.MyTestCase("testLogIn"))
# mysuite.addTest(pickup.MyTestCase("testPickup"))




myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)
