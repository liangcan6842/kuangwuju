from librarys.project import Project
from librarys.login import Login
from librarys.contract import Contract
import pytest
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://mining.admin.sauou.com/#/home ')
login = Login(driver)
login.login('admin','123456')

class Test_process:
    """新增项目"""
    def test_001(self):
        """新建项目"""
        test_001 = Project(driver)
        test_001.Add_project('测试项目813','测试甲方','2022-08-13','2022-08-31','重庆','18天','这是测试项目813')

    def test_002(self):
        """新建合同"""
        test_002 = Contract(driver)
        test_002.Add_contract('承包合同813','','测试项目813','1000','主合同','2000000','2022-08-13','2022-08-31','2022-08-13','重庆','2022','实体技术负责人','项目管理人','通过')

    def test_003(self):
        """新建"""
