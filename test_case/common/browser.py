import time
import os
from selenium import webdriver
from utils.config import DRIVER_PATH,REPORT_PATH

CHROMEDRIVER_PATH = DRIVER_PATH + 'chromedriver.exe'
IEDRIVER_PATH = DRIVER_PATH + '\IEDriverServer.exe'
PHANTOMJDRIVER_PATH = DRIVER_PATH +'\phantomjs.exe'

TYPES = {'firefox':webdriver.Firefox,'chrome':webdriver.Chrome,'ie':webdriver.Ie,'phantomjs':webdriver.PhantomJS}
EXECUTABLE_PATH  = {'firefox':'wires','chrome':CHROMEDRIVER_PATH,'ie':IEDRIVER_PATH,'phantomjs':PHANTOMJDRIVER_PATH}


class UnSupportBrowserTypeError(Exception):
    pass


class Browser(object):
    def __init__(self,browser_type = 'firefox'):
        self._type = browser_type.lower()
        if self._type in TYPES:
            self.browser = TYPES[self._type]
        else:
            raise UnSupportBrowserTypeError('仅支持%s!' % ','.join(TYPES.keys()))
        self.driver = None

    def get(self,url,maximize_windows=True,implicitly_wait=30):
        self.driver = self.browser(executable_path=EXECUTABLE_PATH[self._type])
        self.driver.get(url)
        if maximize_windows:
            self.driver.maximize_window()
        self.driver.implicitly_wait(implicitly_wait)
        return self

    def save_screen_shot(self,name = 'screen_shot'):
        day = time.strftime('%Y%m%d',time.localtime(time.time()))

        screen_shot_path = REPORT_PATH + '\screenshot_%s' % day
        if not os.path.exists(screen_shot_path):
            os.makedirs(screen_shot_path)
        tm = time.strftime('%H%M%S',time.localtime(time.time()))
        screenshot = self.driver.save_screenshot(screen_shot_path + '\\%s_%s.png'(name,tm))
        return screenshot
    def close(self):
        self.driver.close()

    def quit(self):
        self.driver.quit()