from selenium import webdriver
import os
from selenium.webdriver.common.by import By
from utils.HTMLTestRunner import HTMLTestRunner
import unittest, time,re
from utils.config import Config,DRIVER_PATH,REPORT_PATH
from utils.mail import Email
from utils.file_reader import ExcelReader
from utils.log import logger


def time_format():
    current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return current_time


class TestLeisu(unittest.TestCase):

    URL = Config().get('URL')
    base_path = os.path.dirname(os.path.abspath(__file__)) + '\..'
    driver_path = os.path.abspath(base_path + '\drivers\chromedriver.exe')
    locator_result = (By.XPATH,'//*[@id="home"]/header')

    def setUp(self):
        self.driver= webdriver.Chrome(executable_path=DRIVER_PATH +'\chromedriver.exe')
        self.driver.implicitly_wait(10)
        self.driver.get(self.URL)
        self.verificationErrors = []
        self.accept_next_alert = True
        self.driver.maximize_window()

    def test1(self):
        '''
        测试登录/点击启动客户端
        '''
        driver = self.driver
        driver.find_element_by_css_selector('#login_page > div > ul > li.user > input').clear()
        driver.find_element_by_css_selector('#login_page > div > ul > li.user > input').send_keys('test')
        driver.find_element_by_css_selector('#login_page > div > ul > li.password > input').send_keys('123456')
        driver.find_element_by_css_selector('#login_page > div > ul > li.login_btn').click()
        time.sleep(10)
        driver.get_screenshot_as_file(u"E:\\Raysync2_project\\report\\登录是否成功.png")
        title = driver.title
        self.assertEqual(title,'镭速传输')
        try:
            self.driver.find_element_by_css_selector('body > app > div > div.content')
            print('弹出温馨提示')
            self.driver.find_element_by_css_selector('body > app > div > div.content > span > a:nth-child(4)').click() #启动客户端
            time.sleep(10)
            print('点击启动客户端')
        except Exception:
            print('已登录')
    def test2(self):
        '''
        测试是否登录成功
        '''
        driver = self.driver
        # driver.get(self.base_url + '/')
        driver.find_element_by_css_selector('#login_page > div > ul > li.user > input').clear()
        driver.find_element_by_css_selector('#login_page > div > ul > li.user > input').send_keys('test')
        driver.find_element_by_css_selector('#login_page > div > ul > li.password > input').send_keys('123456')
        driver.find_element_by_css_selector('#login_page > div > ul > li.login_btn').click()
        time.sleep(10)
        driver.get_screenshot_as_file(u"E:\\Raysync2_project\\report\\登录成功.png")
        try:
            self.driver.find_element_by_css_selector('#home > div.left_section > div.server_info > select-server > div > span')
            print('login success')
        except Exception:
            print('login failed')


    def tearDown(self):
        self.driver.quit()
        self.assertEqual([],self.verificationErrors)





if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestLeisu('test1'))
    suite.addTest(TestLeisu('test2'))


    reprot = REPORT_PATH + '\\report.html'
    with open(reprot,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='镭速2.0版本自动化测试',description='自动化测试报告')
        runner.run(suite)
    e = Email(title='Raysync 2.0 测试报告',
              message='这是今天的测试报告，请查收',
              receiver='772725218@qq.com',
              sender='wangxinlei@rayvision.com',
              password='Wxl.1314',
              server='smtp.exmail.qq.com',
              path =reprot,
              )
    e.send()

