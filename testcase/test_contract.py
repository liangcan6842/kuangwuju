from librarys.login import Login
from librarys.contract import Contract,Subcontract
import pytest
from selenium import webdriver
driver = webdriver.Chrome()
# driver.set_window_size(1600,1200)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://mining.admin.sauou.com/#/home ')
login = Login(driver)
login.login('admin','123456')

class Test_contract:
    """新增合同"""
    def test_001(self):
        test_001 = Contract(driver)
        test_001.Add_contract('承包合同812','','测试项目812','1000','主合同','2000000','2022-08-12','2022-08-30','2022-08-12','重庆','2022','实体技术负责人','项目管理人','通过')

    def test_002(self):
        test_001 = Subcontract(driver)
        test_001.Add_subcontract('分包包合同812','','测试项目812','1000','分包类','200000','','','')
