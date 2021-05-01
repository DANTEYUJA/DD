# 对应lib套件下的webopen文件中 声明的 open_browser, mgr_login 方法
from lib.webopen import open_browser, mgr_login
from hytest import *
from hytest import STEP, INFO, CHECK_POINT
from time import sleep
from selenium import webdriver
# 导入Select类
from selenium.webdriver.support.ui import Select


# 初始化（英文叫 setup 方法）操作
# 与初始化正好相反的操作就是 清除（teardown方法 ）。
# 谁做的初始化操作对环境产生了 什么改变 ， 谁 就应该在 清除 操作里面做什么样的 还原 。

# 登录 单元测试
class DD0002:
    name = '消防 DD0002'

    # 初始化方法setup  登录模块
    # 对象wd调用lib/webui中open_browser，mgr_login()
    def setup(self):
        open_browser()
        wd = GSTORE['wd']
        # mgr_login中get网页被注释，因为这里需要使用局部变量wd的值
        mgr_login()
        wd.get('http://firecontrol.console.rayjeak.com/sign/login')

    # 清除方法teardown    清除浏览器对象wd中全局存储对象 GSTORE的代码
    # def teardown(self):
    #     INFO('清除初始化 执行下方用例')

    def teststeps(self):
        STEP(1, '添加警情')
        wd = GSTORE['wd']

        # 添加警情
        wd.find_element_by_class_name('add_list').click()
        sleep(1)

        # 录入警情
        sleep(1)
        wd.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div/div/div[2]/div/div[2]/div[1]/div[2]/input').send_keys('崇明丁丁测试')

        sleep(1)

        # 起火地点
        wd.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div/div/div[2]/div/div[2]/div[3]/div[2]/input').click()
        sleep(1)
        wd.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div/div/div[2]/div/div[2]/div[3]/div[2]/input').send_keys('崇明')
        sleep(1)

        # 放弃了，时间抓不到==
        # js = document.getElementById('请选择时间').removeAttribute("placeholder")
        # document.execute_script(js)
        # # 时间控件没有点击事件，直接send值
        # wd.find_element_by_xpath('//*[@id="root"]/section/section/main/div/div/div[2]\
        # /div/div[2]/div[2]/div[2]/span/div/input').send_keys('2021-04-13 11:24:46')

        # 所属乡镇选择
        # 创建Select对象 代表下拉选择框元素
        select = Select(
            wd.find_element_by_xpath(
                '/html/body/div[1]/section/section/main/div/div/div[2]/div/div[2]/div[4]/div[2]/span/span/span[1]/span').click())
        sleep(1)
        # 通过 Select 对象选中所属乡镇
        select.select_by_visible_text("新国村")

        wd.find_element_by_xpath(
            '/html/body/div[1]/section/section/main/div/div/div[2]/div/div[2]/div[4]/div[2]/span/span/span[1]/span').click()


