import unittest
from  test_01 import TestCase01

#实例化 suite为用例名称
suite = unittest.TestSuite()
#添加用例（以测试用例类里的每一种方法为为单位添加）
suite.addTest(TestCase01('testcase_01'))
#实例化
runner = unittest.TextTestRunner()
#执行
runner.run(suite)
