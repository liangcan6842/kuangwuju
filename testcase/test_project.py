from librarys.project import Project
from librarys.login import Login
import pytest
from selenium import webdriver
driver = webdriver.Chrome()
# driver.set_window_size(1600,1000)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://mining.admin.sauou.com/#/home ')
login = Login(driver)
login.login('admin','123456')

class Test_project:
    """新增项目"""
    def test_001(self):
        test_001 = Project(driver)
        test_001.Add_project('测试项目812','测试甲方','2022-08-05','2022-08-31','重庆','26天','这是测试项目')


if __name__ == '__main__':
    pytest.main()


