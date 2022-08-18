from time import sleep
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://mining.admin.sauou.com/#/home ')


driver.find_element(By.XPATH, '/html/body/div/div/div/div[2]/div[2]/section/form/div[2]/div/div[1]/input').send_keys('admin')
driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/section/form/div[3]/div/div[1]/input').send_keys('123456')
driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/section/form/button/span').click() #点击登录
driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div/ul/div[2]/li/div/span[2]').click()  # 点击合同管理
driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div[1]/div/ul/div[2]/li/ul/div[1]/a/li').click()  # 点击项目管理
driver.find_element(By.XPATH,'/html/body/div/div/div[2]/section/div/div/div/form/div[6]/div/div/button[1]/span').click()  # 点击新增项目
# 输入项目信息
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[1]/div[1]/div/div/input').send_keys('测试809')  # 输入项目名称
sleep(1)
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[1]/div[2]/div/div/div/input').click()  # 选择项目类型
sleep(1)
driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[1]/div[1]/ul/li[2]/span').click()  # 选择项目大类
sleep(1)
driver.find_element(By.XPATH,'/html/body/div[4]/div[1]/div[2]/div[1]/ul/li/span').click()  # 选择项目专业类
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[2]/div[1]/div/div/div[1]').click()  # 选择实施单位
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[1]/div[1]/label/span/span').click()  # 选择实施单位（队领导）
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[2]/div[1]/div/div/div[2]/div/div[2]/button[2]/span').click()  # 确定
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[2]/div[2]/div/div/input').send_keys('测试甲方')  # 输入甲方单位
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[3]/div[1]/div/div/input').send_keys('2022-08-01')  # 输入项目开始时间
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[4]/div[1]/div/div/input').send_keys('2022-08-30')  # 输入项目结束时间
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[3]/div[2]/div/div/div[1]').click()  # 选择乙方单位
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[1]/label/span/span').click()  # 选择乙方单位（测试同步）
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[3]/div[2]/div/div/div[2]/div/div[2]/button[2]/span').click()  # 确定
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[4]/div[2]/div/div/input').send_keys('重庆')  # 填写项目地点
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[5]/div/div/input').send_keys('30天')  # 填写工作量
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[6]/div/div/textarea').send_keys('好好哈')  # 填写项目简介
driver.find_element(By.XPATH,'/html/body/div[3]/div/section/form/div[8]/div/div/div[2]').click()  # 选择项目经理
sleep(5)
driver.find_element(By.XPATH,'//div[@class="user-list"]/div[2]/div/div').click()  # 点击头像
driver.find_element(By.XPATH,'//div[@class="user-list"]/../../div[2]/button').click() #点击确定
