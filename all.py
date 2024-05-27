from HTMLTestRunner_PY3 import HTMLTestRunner
import unittest


if __name__ == '__main__':
    #执行需要的测试用例，生成测试报告
    #使用unittest默认的加载器去 发现testcase下面的所有测试用例
    suit = unittest.defaultTestLoader.discover("./testcase","*.py")
    #生成html报告文件
    report_file = open("./report/reports.html","wb")
    #生成一个html运行器对象（必须下载个htmlrunner.py放到pythonlib没目录下面
    runner = HTMLTestRunner(stream=report_file, title="自动化测试报告", description="报告详情")
    runner.run(suit)
