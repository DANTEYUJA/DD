# 对应lib套件下的webui文件中 声明的 open_browser, mgr_login 方法
from lib.webui import open_browser, mgr_login
from hytest import *
from hytest import STEP, INFO, CHECK_POINT
from time import sleep
from selenium import webdriver
# 导入Select类
from selenium.webdriver.support.ui import Select

class DD0004:
    name = '异常登录 DD0004'

    # 先初始化打开浏览器
    def setup(self):
        INFO('打开浏览器')
        open_browser()

    def teststeps(self):
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
                wd.find_element_by_class_name(
                    '/html/body/div[1]/section/section/main/div/div/div[2]/div/div[2]/div[4]/div[2]/span/span/span[1]/span').click())
            sleep(1)
            # 通过 Select 对象选中所属乡镇
            select.select_by_visible_text("新国村")

            wd.find_element_by_xpath(
                '/html/body/div[1]/section/section/main/div/div/div[2]/div/div[2]/div[4]/div[2]/span/span/span[1]/span').click()

            # 清除方法teardown    清除浏览器对象wd中全局存储对象 GSTORE的代码

