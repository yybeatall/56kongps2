import pdprocess,loginsucc,logout
import unittest




# 执行登录
testcases = unittest.TestLoader().loadTestsFromTestCase(loginsucc.MyTestCase)

# 执行通过交接页实现提到货
testcases.addTest(pdprocess.MyTestCase("testFromTakeover"))
#testcases.addTest(pdprocess.MyTestCase("testFromPickup"))
#testcases.addTest(pdprocess.MyTestCase("testFromDelivery"))

#注销
testcases.addTest(logout.MyTestCase("testLogout"))

mysuite = unittest.TestSuite([testcases])


myrunner = unittest.TextTestRunner(verbosity=2)
myrunner.run(mysuite)
