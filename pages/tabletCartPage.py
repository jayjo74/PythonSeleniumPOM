from utilities import base_utils as bu
from selenium.webdriver.common.by import By

class TabletCartPage:

    def __init__(self, driver):
        self.driver = driver
        self.add_cart = (By.XPATH, "//div[@id='productProperties']//button[@role='button']")
        self.shopping_cart = (By.ID, "shoppingCartLink")

    def click_add_cart(self):
        bu.element_Click(self.driver, 10, self.add_cart)

    def click_shopping_cart(self):
        bu.element_Click(self.driver, 10, self.shopping_cart)


