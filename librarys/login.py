from selenium.webdriver.common.by import By
class Login:
    # url = 'https://mining.admin.sauou.com/'

    def __init__(self,driver):
        self.driver = driver

    # def load(self):
    #     """加载页面"""
    #     return self.driver.get(self.url)

    def login(self,username,password):
        """登录"""
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/section/form/div[2]/div/div[1]/input').send_keys(username)
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/section/form/div[3]/div/div[1]/input').send_keys(password)
        self.driver.find_element(By.XPATH,'/html/body/div/div/div/div[2]/div[2]/section/form/button/span').click()
        #获取断言信息







