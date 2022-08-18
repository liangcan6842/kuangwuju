from time import sleep
from selenium.webdriver.common.by import By


class Project:
    def __init__(self,driver):
        self.driver = driver

    def Add_project(self,project_name,first_unit,first_time,end_time,project_place,project_workload,project_information):
        """新建项目"""
        self.driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div/ul/div[2]/li/div/span[2]').click()  # 点击合同管理
        self.driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li').click()  # 点击项目管理
        self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/section/div/div/div/form/div[6]/div/div/button[1]/span').click()  # 点击新增项目
        # 输入项目信息
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/section/form/div[1]/div[1]/div/div/input').send_keys(project_name)  # 输入项目名称
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[1]/div[2]/div/div/div/input').click()  # 选择项目类型
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[1]/div[1]/ul/li[2]/span').click()  # 选择项目大类
        self.driver.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/div[1]/ul/li/span').click()  # 选择项目专业类
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[2]/div[1]/div/div/div[1]').click()  # 选择实施单位
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/label/span/span').click()  # 选择实施单位（队领导）
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[2]/div[1]/div/div/div[2]/div/div[2]/button[2]/span').click()  # 确定
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/section/form/div[2]/div[2]/div/div/input').send_keys(first_unit)  # 输入甲方单位
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/section/form/div[3]/div[1]/div/div/input').send_keys(first_time)  # 输入项目开始时间
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/section/form/div[4]/div[1]/div/div/input').send_keys(end_time)  # 输入项目结束时间
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[3]/div[2]/div/div/div[1]').click()  # 选择乙方单位
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/label/span/span').click()  # 选择乙方单位（测试同步）
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[3]/div[2]/div/div/div[2]/div/div[2]/button[2]/span').click()  # 确定
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/section/form/div[4]/div[2]/div/div/input').send_keys(project_place)  # 填写项目地点
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/section/form/div[5]/div/div/input').send_keys(project_workload)  # 填写工作量
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/section/form/div[6]/div/div/textarea').send_keys(project_information)  # 填写项目简介

        element = self.driver.find_element(By.XPATH, '/html/body/div[3]/div/section/form/div[7]/div/div/div[2]/div/div') # 添加项目面貌
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        import pywinauto
        from pywinauto.keyboard import send_keys
        # 使用pywinauto来选择文件
        app = pywinauto.Desktop()
        # 选择文件上传的窗口
        dlg = app["打开"]
        # 选择文件地址输入框，点击激活
        dlg["Toolbar3"].click()
        # 键盘输入上传文件的路径
        send_keys("C:\\Users\\Administrator\\Desktop")
        # 键盘输入回车，打开该路径
        send_keys("{VK_RETURN}")
        # 选中文件名输入框，输入文件名
        dlg["文件名(&N):Edit"].type_keys("1.png")
        # 点击打开
        dlg["打开(&O)"].click()
        self.driver.find_element(By.XPATH, '/html/body/div[3]/div/section/form/div[8]/div/div/div[2]').click()  # 选择项目经理
        sleep(2)
        self.driver.find_element(By.XPATH, '//div[@class="user-list"]/div[2]/div/div').click()  # 点击头像
        self.driver.find_element(By.XPATH, '//div[@class="user-list"]/../../div[2]/button').click()  # 点击确定
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/div/button/span').click() #点击项目确定



