import logging
from utilities import base_utils as bu
from selenium.webdriver.common.by import By

class HomePage:

    log = bu.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver
        '''
        will not use 'find_element_by_id' type for use function
        '''
        # self.login_user_id = "menuUserLink"
        self.loginimage = (By.ID, "menuUserLink")
        self.input_user = (By.NAME, "username")   #userID box
        self.input_password = (By.NAME, "password")
        self.button_signin = (By.ID, "sign_in_btnundefined")
        self.userID_span = (By.XPATH, "//a[@id='menuUserLink']/span") #after log in, can see userID
        self.signout_lable = (By.XPATH, "//div[@id='loginMiniTitle']/label[3]")
        self.tablet_label = (By.ID, "tabletsLink")

    def verify_homepage(self):
        bu.is_enabled(self.driver, 10, self.loginimage)

    def open_login_window(self):
        bu.element_Click(self.driver, 10, self.loginimage)

    def enter_username(self, username):
        bu.clear_text(self.driver, 10, self.input_user)
        bu.enter_text(self.driver, 10, self.input_user, username)
        # self.driver.find_element_by_name(self.input_user_name).clear()
        # self.driver.find_element_by_name(self.input_user_name).send_keys(username)

    def enter_password(self, password):
        bu.clear_text(self.driver, 10, self.input_password)
        bu.enter_text(self.driver, 10, self.input_password,password)

    def click_signin(self):
        bu.element_Click(self.driver, 10, self.button_signin)

    def verify_userID(self, username):
        bu.assert_element_text(self.driver, 10, self.userID_span, username)

    def click_userID(self):
        bu.element_Click(self.driver, 10, self.userID_span)

    def click_signout(self):
        bu.element_Click(self.driver, 10, self.signout_lable)

    def click_tablet(self):
        bu.element_Click(self.driver, 10 , self.tablet_label)


