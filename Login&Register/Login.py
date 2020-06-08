import unittest
import warnings
from Tool import Auto

class ExecuteCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)  # 处理unittest警告信息

    # 测试账号(test_1 -- test_8)，登录页面账号未作格式校验
    def test_1(self):
        '''所有输入框为空'''
        expectResult = "帐号不能为空"
        login = Auto()
        actualResult = login.loginAuto()
        self.assertEqual(expectResult, actualResult)

    def test_2(self):
        '''输入12位手机号，密码为空，值为：184883658555'''
        expectResult = "手机号码格式不正确"
        login = Auto("184883658555")
        actualResult = login.loginAuto()
        self.assertEqual(expectResult, actualResult)

    def test_3(self):
        '''输入10位手机号，密码为空，值为：1848365858'''
        expectResult = "手机号码格式不正确"
        login = Auto("1848365858")
        actualResult = login.loginAuto()
        self.assertEqual(expectResult, actualResult)

    def test_4(self):
        '''输入1位手机号，密码为空，值为：1'''
        expectResult = "手机号码格式不正确"
        login = Auto("1")
        actualResult = login.loginAuto()
        self.assertEqual(expectResult, actualResult)

    def test_5(self):
        '''输入中文手机号，密码为空，值为：一八四八三六五八五八零'''
        expectResult = "手机号码格式不正确"
        login = Auto("一八四八三六五八五八零")
        actualResult = login.loginAuto()
        self.assertEqual(expectResult, actualResult)

    def test_6(self):
        '''输入特殊字符手机号，密码为空，值为：！！！？？ ++--@~'''
        expectResult = "手机号码格式不正确"
        login = Auto("！！！？？ ++--@~")
        actualResult = login.loginAuto()
        self.assertEqual(expectResult, actualResult)

    def test_7(self):
        '''输入正确手机号，密码为空，值为：18483658580'''
        expectResult = "密码不能为空"
        login = Auto("18483658580")
        actualResult = login.loginAuto()
        self.assertEqual(expectResult, actualResult)

    def test_8(self):
        '''账号输入js代码，输入正确密码，值为：账号：alert(test) 密码：1033141032'''
        expectResult = "账号不存在"
        login = Auto("alert(test)", "1033141032")
        actualResult = login.loginAuto()
        self.assertEqual(expectResult, actualResult)

    #测试密码(test_9 -- ) 登录页面密码未作格式校验
    def test_9(self):
        '''输入正确手机号，密码为中文，值为：天天向上'''
        expectResult = "密码格式不正确"
        login = Auto("18483658580", "天天向上")
        actualResult = login.loginAuto()
        self.assertEqual(expectResult, actualResult)

    def test_10(self):
        '''输入错误手机号，输入错误密码，值为：账号：184836585803 密码：123456'''
        expectResult = "账号不存在"
        login = Auto("184836585803", "123456")
        actualResult = login.loginAuto()
        self.assertEqual(expectResult, actualResult)

    def test_11(self):
        '''输入正确账号，密码输入js代码，值为：账号：18483658580 密码alert(test)'''
        expectResult = "密码错误"
        login = Auto("18483658580", "alert(test)")
        actualResult = login.loginAuto()
        self.assertEqual(expectResult, actualResult)

    def test_12(self):
        '''输入正确手机号，输入错误密码，值为：账号：18483658580 密码：123456'''
        expectResult = "密码错误"
        login = Auto("18483658580", "123456")
        actualResult = login.loginAuto()
        self.assertEqual(expectResult, actualResult)

    #正确账号，正确密码，登录成功
    '''def test_13(self):
        '''输入正确手机号，输入正确密码，值为：账号：18483658580 密码：正确密码'''
        expectResult = "1" #1为true,登录成功
        login = Auto("18483658580", "正确密码")
        actualResult = login.loginAuto()
        if actualResult == None:
            actualResult = "1"
            self.assertEqual(expectResult, actualResult)
        else:
            self.assertEqual(expectResult, actualResult)'''

    #找回密码按钮测试
    def test_14(self):
        '''点击找回密码按钮，成功进入密码找回页面'''
        login = Auto()
        driver = login.driver
        expectResult = "https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCForgetPasswordPage"
        driver.get("https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage")
        driver.find_element_by_class_name("GoResetPassword").click()
        actualResult = driver.current_url
        self.assertEqual(expectResult, actualResult)
        driver.quit()

    #注册按钮测试
    def test_15(self):
        login = Auto()
        driver = login.driver
        expectResult = "https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage"
        driver.get("https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage")
        driver.find_element_by_class_name("InputWarningA").click()
        actualResult = driver.current_url
        self.assertEqual(expectResult, actualResult)
        driver.quit()

    # 友情链接点击
    def test_16(self):
        '''点击友情链接按钮，可以成功进入友情链接界面'''
        register = Auto()
        driver = register.driver
        expectResult = "http://vg.163.com/home"
        driver.get("https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage")
        driver.find_element_by_class_name("FooterLogo").click()
        driver.switch_to.window(driver.window_handles[1])
        actualaUrl = driver.current_url
        self.assertEqual(expectResult, actualaUrl)
        driver.quit()

    #SnailBigLogo点击测试
    def test_18(self):
        '''点击Logo图标可以成功进入主界面'''
        register = Auto()
        driver = register.driver
        expectResult = "https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCSnailHomePage"
        driver.get("https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage")
        driver.find_element_by_class_name("SnailBigLogo").click()
        actualaUrl = driver.current_url
        self.assertEqual(expectResult, actualaUrl)
        driver.quit()

if __name__ == "__main__":
    unittest.main()