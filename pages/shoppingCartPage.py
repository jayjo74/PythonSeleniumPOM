from utilities import base_utils as bu
from selenium.webdriver.common.by import By

class ShoppingCartPage:

    def __init__(self, driver):
        self.driver = driver
        self.remove_text = (By.LINK_TEXT, "REMOVE")
        self.contiuneshopping_text = (By.LINK_TEXT, "CONTINUE SHOPPING")
        self.cartEmpty_label = (By.XPATH, "//div[@id='shoppingCart']//label[.='Your shopping cart is empty']")

    def click_remove(self):
        bu.element_Click(self.driver, 10, self.remove_text)

    def click_continueshopping(self):
        bu.element_Click(self.driver, 10, self.contiuneshopping_text)

    def verify_empty_cart(self):
        bu.is_visible(self.driver, 10, self.cartEmpty_label)

