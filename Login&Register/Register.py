import unittest
import warnings
from Tool import Auto
import time

class ExecuteCase(unittest.TestCase):
    def setUp(self):
        warnings.simplefilter('ignore', ResourceWarning)#处理unittest警告信息

    #测试手机号(test_1 -- test_8)
    def test_1(self):
        '''所有输入框为空'''
        expectResult = "手机号不能为空"
        register = Auto()
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    def test_2(self):
        '''输入12位手机号，密码为空，值为：184883658555'''
        expectResult = "手机号码格式不正确"
        register = Auto("184883658555")
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    def test_3(self):
        '''输入10位手机号，密码为空，值为：1848365858'''
        expectResult = "手机号码格式不正确"
        register = Auto("1848365858")
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    def test_4(self):
        '''输入1位手机号，密码为空，值为：1'''
        expectResult = "手机号码格式不正确"
        register = Auto("1")
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    def test_5(self):
        '''输入中文手机号，密码为空，值为：一八四八三六五八五八零'''
        expectResult = "手机号码格式不正确"
        register = Auto("一八四八三六五八五八零")
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    def test_6(self):
        '''输入特殊字符手机号，密码为空，值为：！！！？？ ++--@~'''
        expectResult = "手机号码格式不正确"
        register = Auto("！！！？？ ++--@~")
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    def test_7(self):
        '''输入正确手机号，密码为空，值为：18483658580'''
        expectResult = "密码不能为空"
        register = Auto("18483658580")
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    def test_8(self):
        '''手机号码输入js代码，值为：alert(test)'''
        expectResult = "手机号码格式不正确"
        register = Auto("alert(test)")
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    def test_9(self):
        '''输入已经注册过的账号，密码为空 值为：账号：18483658580'''
        expectResult = "该手机号已经注册过帐号"
        register = Auto()
        driver = register.driver
        driver.get("https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage")
        driver.find_element_by_name("Username").send_keys("18483658580")
        driver.find_element_by_css_selector("div.SnailInputDiv.NoBorder > a").click()
        time.sleep(0.5)
        actualResult = driver.find_element_by_class_name("ErrorMsg").text
        self.assertEqual(expectResult, actualResult)
        driver.quit()

    #测试密码(test_9 -- test_11) 网站注册页面密码未作校验
    def test_10(self):
        '''输入正确手机号，密码为中文，值为：天天向上'''
        expectResult = "密码格式不正确"
        register = Auto("18483658580", "天天向上")
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    def test_11(self):
        '''输入正确手机号，1位密码，值为：1'''
        expectResult = "密码格式不正确"
        register = Auto("18483658580", "1")
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    def test_12(self):
        '''输入正确手机号，密码输入js代码，值为：账号：18483658580 密码alert(test)'''
        expectResult = "验证码不能为空"
        register = Auto("18483658580", "alert(test)")
        actualResult = register.loginAuto()
        self.assertEqual(expectResult, actualResult)

    #测试验证码(test_12 -- test_14)
    def test_13(self):
        '''输入正确手机号，正确密码，值为：手机号：18483658580 密码：18483658580'''
        expectResult = "验证码不能为空"
        register = Auto("18483658580", "18483658580")
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    def test_14(self):
        '''输入正确手机号，正确密码，不点击发送验证码按钮，直接输入验证码，值为：手机号：18483658580 密码：18483658580 验证码：123'''
        expectResult = "请先获取验证码"
        register = Auto("18483658580", "18483658580", "123")
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    def test_15(self):
        '''输入正确手机号，正确密码，不点击发送验证码按钮，直接输入js验证码，值为：手机号：18483658580 密码：18483658580 验证码：alert(test)'''
        expectResult = "请先获取验证码"
        register = Auto("18483658580", "18483658580", "123")
        actualResult = register.registerAuto()
        self.assertEqual(expectResult, actualResult)

    #海外用户注册按钮点击测试
    def test_16(self):
        '''点击海外用户注册按钮，可以成功进入海外用户注册界面'''
        register = Auto()
        driver = register.driver
        expectResult = "阿富汗(+93)"
        driver.get("https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage")
        driver.find_elements_by_class_name("InputWarningA")[0].click()
        values = driver.find_elements_by_css_selector("option")
        self.assertEqual(expectResult, values[0].text)
        driver.quit()

    #已有账号，去登录按钮点击测试
    def test_17(self):
        '''点击已有账号，去登录按钮，可以成功进入登录界面'''
        register = Auto()
        driver = register.driver
        expectResult = "登录"
        driver.get("https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage")
        driver.find_elements_by_class_name("InputWarningA")[1].click()
        actualResult = driver.find_element_by_class_name("InputTitleText").text
        self.assertEqual(expectResult, actualResult)
        driver.quit()

    #友情链接点击
    def test_18(self):
        '''点击友情链接按钮，可以成功进入友情链接界面'''
        register = Auto()
        driver = register.driver
        expectResult = "http://vg.163.com/home"
        driver.get("https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage")
        driver.find_element_by_class_name("FooterLogo").click()
        driver.switch_to.window(driver.window_handles[1])
        actualaUrl = driver.current_url
        self.assertEqual(expectResult, actualaUrl)
        driver.quit()

    #SnailBigLogo点击测试
    def test_19(self):
        '''点击Logo图标可以成功进入主界面'''
        register = Auto()
        driver = register.driver
        expectResult = "https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCSnailHomePage"
        driver.get("https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage")
        driver.find_element_by_class_name("SnailBigLogo").click()
        actualaUrl = driver.current_url
        self.assertEqual(expectResult, actualaUrl)
        driver.quit()

    '''海外注册页面测试'''
    # 测试手机号(test_in_1 -- test_in_8) 海外注册页面,手机号未作格式校验
    def test_in_1(self):
        '''所有输入框为空'''
        expectResult = "手机号不能为空"
        register = Auto()
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    def test_in_2(self):
        '''输入12位手机号，密码为空，值为：184883658555'''
        expectResult = "手机号码格式不正确"
        register = Auto("184883658555")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    def test_in_3(self):
        '''输入10位手机号，密码为空，值为：1848365858'''
        expectResult = "手机号码格式不正确"
        register = Auto("1848365858")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    def test_in_4(self):
        '''输入1位手机号，密码为空，值为：1'''
        expectResult = "手机号码格式不正确"
        register = Auto("1")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    def test_in_5(self):
        '''输入中文手机号，密码为空，值为：一八四八三六五八五八零'''
        expectResult = "手机号码格式不正确"
        register = Auto("一八四八三六五八五八零")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    def test_in_6(self):
        '''输入特殊字符手机号，密码为空，值为：！！！？？ ++--@~'''
        expectResult = "手机号码格式不正确"
        register = Auto("！！！？？ ++--@~")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    def test_in_7(self):
        '''输入正确手机号，密码为空，值为：18483658580'''
        expectResult = "密码不能为空"
        register = Auto("18483658580")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    def test_in_8(self):
        '''手机号码输入js代码，值为：alert(test)'''
        expectResult = "手机号码格式不正确"
        register = Auto("alert(test)")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    # 测试密码(test_in_9 -- test_in_11) 海外注册页面,密码未作格式校验
    def test_in_9(self):
        '''输入正确手机号，密码为中文，值为：天天向上'''
        expectResult = "密码格式不正确"
        register = Auto("18483658580", "天天向上")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    def test_in_10(self):
        '''输入正确手机号，1位密码，值为：1'''
        expectResult = "密码格式不正确"
        register = Auto("18483658580", "1")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    def test_in_11(self):
        '''输入正确手机号，密码输入js代码，值为：账号：18483658580 密码alert(test)'''
        expectResult = "验证码不能为空"
        register = Auto("18483658580", "alert(test)")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    # 测试验证码(test_12 -- test_14)
    def test_in_12(self):
        '''输入正确手机号，正确密码，值为：手机号：18483658580 密码：18483658580'''
        expectResult = "验证码不能为空"
        register = Auto("18483658580", "18483658580")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    def test_in_13(self):
        '''输入正确手机号，正确密码，不点击发送验证码按钮，直接输入验证码，值为：手机号：18483658580 密码：18483658580 验证码：123'''
        expectResult = "请先获取验证码"
        register = Auto("18483658580", "18483658580", "123")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    def test_in_14(self):
        '''输入正确手机号，正确密码，不点击发送验证码按钮，直接输入js验证码，值为：手机号：18483658580 密码：18483658580 验证码：alert(test)'''
        expectResult = "请先获取验证码"
        register = Auto("18483658580", "18483658580", "123")
        actualResult = register.InRegisterAuto()
        self.assertEqual(expectResult, actualResult)

    #已有账号，去登录按钮点击测试
    def test_in_15(self):
        '''点击已有账号，去登录按钮，可以成功进入登录界面'''
        register = Auto()
        driver = register.driver
        expectResult = "登录"
        driver.get("https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCInternationalRegisterPage")
        driver.find_element_by_class_name("InputWarningA").click()
        actualResult = driver.find_element_by_class_name("InputTitleText").text
        self.assertEqual(expectResult, actualResult)
        driver.quit()

    #友情链接点击
    def test_in_16(self):
        '''点击友情链接按钮，可以成功进入友情链接界面'''
        register = Auto()
        driver = register.driver
        expectResult = "http://vg.163.com/home"
        driver.get("https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCInternationalRegisterPage")
        driver.find_element_by_class_name("FooterLogo").click()
        driver.switch_to.window(driver.window_handles[1])
        actualaUrl = driver.current_url
        self.assertEqual(expectResult, actualaUrl)
        driver.quit()

    #SnailBigLogo点击测试
    def test_in_17(self):
        '''点击Logo图标可以成功进入主界面'''
        register = Auto()
        driver = register.driver
        expectResult = "https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCSnailHomePage"
        driver.get("https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCInternationalRegisterPage")
        driver.find_element_by_class_name("SnailBigLogo").click()
        actualaUrl = driver.current_url
        self.assertEqual(expectResult, actualaUrl)
        driver.quit()

    #下拉菜单测试(test_in_18 -- test_in_19)
    def test_in_18(self):
        '''下拉菜单可以正确选择'''
        register = Auto()
        driver = register.driver
        expectResult = "1" #1为true,下拉菜单可以选择.
        driver.get("https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCInternationalRegisterPage")
        try:
            driver.find_elements_by_css_selector("option")[1].click()
            actualaUrl = "1"
            self.assertEqual(expectResult, actualaUrl)
        except:
            actualaUrl = "0" #下拉菜单选择失败
            self.assertEqual(expectResult, actualaUrl)
        finally:
            driver.quit()

    def test_in_19(self):
        '''下拉菜单可以正确选择'''
        register = Auto()
        driver = register.driver
        expectResult = "1" #1为true,下拉菜单可以选择.
        driver.get("https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCInternationalRegisterPage")
        try:
            driver.find_elements_by_css_selector("option")[233].click()
            actualaUrl = "1"
            self.assertEqual(expectResult, actualaUrl)
        except:
            actualaUrl = "0" #下拉菜单选择失败
            self.assertEqual(expectResult, actualaUrl)
        finally:
            driver.quit()

if __name__ == "__main__":
    unittest.main()