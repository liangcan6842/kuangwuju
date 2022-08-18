
import pytest
'''
# 当有多个pu文件都需要调用这个登录功能的话，可以使用conftest的配置文件，
# 单独管理一些预置的操作场景，pytest里面默认读取conftest.py里面的配置
# 1、conftest.py配置脚本名称时固定的，不能改名称
# 2、conftest.py与运行的用例要在同一个package下，并且有__init__.py文件
# 3、不需要import导入conftest.py，pytest用例会自动查找
# '''
from librarys.login import Login
from selenium import webdriver
from setting import config

def get_browser():
    """获取浏览器"""
    browser = webdriver.Chrome(executable_path=config.driver_path)
    browser.implicitly_wait(10)
    browser.maximize_window()
    return browser

@pytest.fixture()
def browser():
    driver = get_browser()
    yield driver
    # driver.quit()

# browser()这个夹具是login_page()夹具的前置夹具
@pytest.fixture()
def login(browser):
    return Login(browser)
