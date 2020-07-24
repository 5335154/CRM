import unittest
from HTMLTestRunner import HTMLTestRunner
import time

discover = unittest.defaultTestLoader.discover(start_dir='test_case',
                                               pattern='test*.py',
                                               top_level_dir=None)
time_str = time.strftime("%Y%m%d%H%M",time.localtime())
report = 'report/report-'+time_str+'.html'
with open(report, "wb+") as f:
    runner = HTMLTestRunner(stream=f,
                            title='CRM自动化测试',
                            description='CRM自动化测试报告详情')
    runner.run(discover)