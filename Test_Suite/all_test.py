# encoding:utf-8

import unittest,HTMLTestRunner
import sys,time
testlistdir="F:\\pytest\\testcase\\Data"

def createsuite():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(
        testlistdir,pattern='success*.py',
        top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_suite)
    return testunit
alltestcases=createsuite()
now=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
filepath="F:\\testresult\\"+now+"result1.html"
fp=file(filepath,'wb')
runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行情况')
runner.run(alltestcases)
fp.close()
