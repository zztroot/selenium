from selenium import webdriver
import time

class Auto(object):
    def __init__(self, *args):
        login_url = 'https://snail.zhuozhuo.io/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCLoginPage'
        register_url = "https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCRegisterPage"
        InRegisterAuto_url = "https://getsuwo.com/?n=fastCat.fcFrontSnail.NewFront.NewFront.PCInternationalRegisterPage"
        driver = webdriver.Chrome()
        self.driver = driver
        self.login_url = login_url
        self.register_url = register_url
        self.InRegisterAuto_url = InRegisterAuto_url
        self.args = args

    #登录页面
    def loginAuto(self):
        self.driver.implicitly_wait(5)
        self.driver.get(self.login_url)
        self.driver.implicitly_wait(2)
        self.error('self.driver.find_element_by_name("Username").send_keys(self.args[0])')
        self.error('self.driver.find_element_by_name("Password").send_keys(self.args[1])')
        self.driver.find_element_by_css_selector("[type='submit']").click()
        try:
            time.sleep(0.5)
            result = self.driver.find_element_by_class_name("ErrorMsg").text
            return result
        except:
            return
        finally:
            self.driver.quit()

    #注册页面
    def registerAuto(self):
        self.driver.implicitly_wait(5)
        self.driver.get(self.register_url)
        self.driver.implicitly_wait(2)
        self.error('self.driver.find_element_by_name("Username").send_keys(self.args[0])')
        self.error('self.driver.find_element_by_name("Password").send_keys(self.args[1])')
        self.error('self.driver.find_element_by_name("code").send_keys(self.args[2])')
        self.driver.find_element_by_css_selector("[type='submit']").click()
        try:
            time.sleep(0.5)
            result = self.driver.find_element_by_class_name("ErrorMsg").text
            return  result
        except:
            return
        finally:
            self.driver.quit()

    #海外注册页面
    def InRegisterAuto(self):
        self.driver.implicitly_wait(5)
        self.driver.get(self.InRegisterAuto_url)
        self.driver.implicitly_wait(2)
        self.error('self.driver.find_element_by_name("Username").send_keys(self.args[0])')
        self.error('self.driver.find_element_by_name("Password").send_keys(self.args[1])')
        self.error('self.driver.find_element_by_name("code").send_keys(self.args[2])')
        self.driver.find_element_by_css_selector("[type='submit']").click()
        try:
            time.sleep(0.5)
            result = self.driver.find_element_by_class_name("ErrorMsg").text
            return  result
        except:
            return
        finally:
            self.driver.quit()

    #输入框为空时，异常处理
    def error(self, ifErr):
        try:
            exec(ifErr)
            return
        except IndexError:
            return


if __name__ == "__main__":
    '''测试代码'''
    auto = Auto("18483658580", "123456")
    a = auto.registerAuto()
    print(a)