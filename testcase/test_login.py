import pytest
from data.login_data import login_fail
class Test_login:
    def test_1(self,login_page):
        """测试登录功能"""
        #隔离测试数据，需要时添加，修改时可以单独在模块中修改
        username = login_file['username']
        password = login_file['password']
        expected = login_file['expected']
        # 2、浏览器管理应该可以重复使用，单独封装
        # 3、需要把驱动进行隔离管理，1.可以存储多个浏览器驱动，2.可以灵活配置，想用哪个用哪个
        # 4、base url 域名，ip
        # 访问url
        # url = config.host + 'User/login.html'
        # browser.get(url)
        login_page.load()
        # 5、登录操作可以重复使用：该项目通用
        # 6、登录操作的特殊性：可以记住状态，token，session，cookie
        # po模式：页面操作和测试用例隔离
        # 输入用户名
        # login_page = LoginPage(browser)
        login_page.login(username, password)
        # 获取文本
        actual = login_page.get_error_tips()
        # 断言
        assert actual == expected

