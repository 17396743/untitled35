from selenium import webdriver
import time


class Test_QQ():
    def test_one(self):
        global driver  # 防止浏览器运行完毕后自动关闭
        driver = webdriver.Chrome() # 调用浏览器驱动
        driver.set_window_size(1280, 720) # 设置显示大小
        driver.set_window_position(400, 150) # 设置显示位置
        print(driver.get_window_position()) # 输出显示位置
        url = "https://qzone.qq.com/"
        driver.get(url=url) # 设置访问地址
        time.sleep(3) # 休眠3秒

        login_frame = driver.find_element_by_id("login_frame") # 获取 frame 窗口id
        driver.switch_to.frame(login_frame)  # frame 窗口切换

        switcher_plogin = driver.find_element_by_id("switcher_plogin") # 获取 switcher_plogin 按钮 id
        switcher_plogin.click() # switcher_plogin 点击跳转

        time.sleep(3) # 休眠3秒

        # switcher_plogin = driver.find_element_by_xpath('//*[@id="switcher_plogin"]') # 获取 switcher_plogin 按钮 xpath
        # switcher_plogin.click() # switcher_plogin 点击跳转

        login = driver.find_element_by_id("u") # 获取账号输入框id
        login.send_keys("1481583730") # 输入账号
        password = driver.find_element_by_id("p")# 获取密码输入框id
        password.send_keys("@LHBM17396743") # 输入密码

        time.sleep(3) # 休眠3秒

        login_button = driver.find_element_by_id("login_button") # 获取登录id
        login_button.click() # 点击登录

        time.sleep(3) # 休眠3秒
        driver.refresh() # 刷新页面

        checkin_button = driver.find_element_by_id("checkin_button") # 获取 签到按钮 id
        checkin_button.click() # 点击签到按钮

        time.sleep(5) # 休眠3秒

        checkin_likeTipsFrame = driver.find_element_by_id("checkin_likeTipsFrame") # 获取frame窗口id
        driver.switch_to.frame(checkin_likeTipsFrame) # 切换 frame窗口

        item_dom = driver.find_element_by_xpath('//*[@id="j-container"]/div[2]/div/div/div/div/ul[1]/li[1]') # 获取列表型窗口的xpath参数
        item_dom.click() # 点击窗口

        time.sleep(3)# 休眠3秒

        btn_submit = driver.find_element_by_class_name("btn-submit") # 获取发布按钮id
        btn_submit.click() #点击发布按钮

        time.sleep(3)# 休眠3秒
        driver.refresh()#刷新页面

        print("QQ空间签到成功！")
        time.sleep(3)# 休眠3秒

        # driver.close()# 关闭 浏览器


if __name__ == '__main__':
    Test_QQ().test_one()
