from time import sleep
from selenium.webdriver.common.by import By

class Contract:
    def __init__(self,driver):
        self.driver = driver

    def Add_contract(self,contract_name,contract_number,project_name,promiss_magin,contract_type,contract_amount,
                     contract_fristTIme,contract_endTIme,contract_sign,sign_place,contract_year,audit_node,audit_people,reason):
        self.driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div/ul/div[2]/li/div/span[2]').click()  # 点击菜单合同管理
        self.driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div/ul/div[2]/li/ul/div[2]/a/li').click()  # 点击合同管理
        self.driver.find_element(By.XPATH,'/html/body/div/div/div[2]/section/div/div/section[3]/div/div/form/div[6]/div/div/button[1]/span').click()  # 点击新增承包合同
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[1]/div[1]/div/div[1]/input').send_keys(contract_name)  # 输入合同名称
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[1]/div[2]/div/div/input').send_keys(contract_number)  # 输入合同编号
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[2]/div[1]/div/div/div/input').send_keys(project_name)  # 选择项目名称
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[2]/div[2]/div/div[1]/input').send_keys(promiss_magin)  # 输入履约保证金
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[3]/div[1]/div/div/div[1]/input').send_keys(contract_type)  # 选择合同类型
        # self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[4]/div[1]/div/div/div/input').send_keys(revise_amount)  # 选择是否修改金额（补充合同可选）
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[5]/div[1]/div/div[1]/input').send_keys(contract_amount)  #输入合同金额
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[6]/div[1]/div/div/input').send_keys(contract_fristTIme)  #选择合同开始日期
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[6]/div[2]/div/div/input').send_keys(contract_endTIme)  #选择合同结束日期
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[7]/div[1]/div/div[1]/input').send_keys(contract_sign)  #选择合同签订日期
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[7]/div[2]/div/div/input').send_keys(sign_place)  #输入合同签订地点
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[8]/div[1]/div/div/input').send_keys(contract_year)  #选择合同年度
        self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/div').click()  #点击空白
        sleep(2)
        # self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[8]/div[2]/div/div/span').click()  # 点击是否自营（默认为是，点击为否）
        """添加附件"""
        element=self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[9]/div/div/div[1]/div/div[1]/div/div')  # 点击上传
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
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/div/button/span').click()  # 点击下一步
        self.driver.find_element(By.XPATH,'/html/body/div[10]/div/section/form/div[1]/div/div/div/input').send_keys(audit_node)  #选择审核节点
        self.driver.find_element(By.XPATH,'/html/body/div[10]/div/section/form/div[2]/div/div/div/input').send_keys(audit_people)  #选择审核人
        self.driver.find_element(By.XPATH,'/html/body/div[10]/div/section/form/div[3]/div/div/textarea').send_keys(reason)  #输入原因
        self.driver.find_element(By.XPATH,'/html/body/div[10]/div/section/div/button/span').click()  #点击确定进入审批流程

class Subcontract:
    def __init__(self,driver):
        self.driver = driver

    def Add_subcontract(self,contract_name,contract_number,project_name,promiss_magin,contract_type,contract_amount,second_unit,
                     contract_fristTIme,contract_endTIme,contract_sign,sign_place,contract_year,audit_node,audit_people,reason):
        self.driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div/ul/div[2]/li/div/span[2]').click()  # 点击菜单合同管理
        self.driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div/ul/div[2]/li/ul/div[2]/a/li').click()  # 点击合同管理
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/section/div/div/section[2]/div/div/div[2]/div[1]').click()  # 点击分包合同
        self.driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/section/div/div/section[3]/div/div/form/div[6]/div/div/button[1]/span').click()  # 点击新增分包合同
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[2]/div[1]/div/div/div[1]/input').send_keys(contract_name)  # 输入合同名称
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[1]/div[2]/div/div/input').send_keys(contract_number)  # 输入合同编号
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[2]/div[1]/div/div/div/input').send_keys(project_name)  # 选择项目名称
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[2]/div[2]/div/div[1]/input').send_keys(promiss_magin)  # 输入履约保证金
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[3]/div[1]/div/div[1]/div/input').send_keys(contract_type)  # 选择合同类型
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[3]/div[2]/div/div/div[1]').click()  # 选择甲方单位
        element = self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[1]/label/span/span') # 选择项目管理
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        element.click()
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div[2]/div[2]/div[2]/div[1]/label/span/span').click()  # 选择测试
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[4]/div[1]/div/div[1]/input').send_keys(contract_amount)  #输入合同金额
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[4]/div[2]/div/div[1]/div/input').send_keys(second_unit)  # 选择乙方单位
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[5]/div[1]/div/div[1]/input').send_keys(contract_fristTIme)  #选择合同开始日期
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[5]/div[2]/div/div[1]/input').send_keys(contract_endTIme)  #选择合同结束日期
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[6]/div[1]/div/div[1]/input').send_keys(contract_sign)  #选择合同签订日期
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[6]/div[2]/div/div/input').send_keys(sign_place)  #输入合同签订地点
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/form/div[7]/div/div/div/input').send_keys(contract_year)  #选择合同年度
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/div').click()  #点击空白
        sleep(2)
        """添加附件"""
        element=self.driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[9]/div/div/div[1]/div/div[1]/div/div')  # 点击上传
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
        self.driver.find_element(By.XPATH,'/html/body/div[4]/div/section/div/button/span').click()  # 点击下一步
        self.driver.find_element(By.XPATH,'/html/body/div[12]/div/section/form/div[1]/div/div/div[1]/input').send_keys(audit_node)  #选择审核节点
        self.driver.find_element(By.XPATH,'/html/body/div[12]/div/section/form/div[2]/div/div/div[1]/input').send_keys(audit_people)  #选择审核人
        self.driver.find_element(By.XPATH,'/html/body/div[12]/div/section/form/div[3]/div/div/textarea').send_keys(reason)  #输入原因
        self.driver.find_element(By.XPATH,'/html/body/div[12]/div/section/div/button/span').click()  #点击确定进入审批流程


















































