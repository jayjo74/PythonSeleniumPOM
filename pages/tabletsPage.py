from utilities import base_utils as bu
from selenium.webdriver.common.by import By

class TabletsPage:

    def __init__(self, driver):
        self.driver = driver
        self.tablet_first_list = (By.XPATH, "//div[2]/ul/li[1]")

    def click_first_tablet(self):
        bu.element_Click(self.driver, 10, self.tablet_first_list )

