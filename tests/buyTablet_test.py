'''
Test Step:
1. Navigate to the http://advantageonlineshopping.com/
2. Log In, Enter the userID and password
    Verify: Login userID
3. Select Tablets
4. Select first item
5. Click Add to Cart
6. Click Shopping Cart
7. Click Remove item
    Verify: "Your shopping cart is empty
8. Click 'Continue Shopping'
9. Log out
'''
import pytest
import time
from testdata import basedata as basedata
from pages.homePage import HomePage
from pages.tabletsPage import TabletsPage
from pages.tabletCartPage import TabletCartPage
from pages.shoppingCartPage import ShoppingCartPage
import logging
from utilities import base_utils as bu

@pytest.mark.usefixtures("test_setup")
class TestBuyTablet():
    log = bu.customLogger(logging.DEBUG)

    def test_buyTablet(self):
        try:
            self.log.info("Buy Tablet test started.")
            driver = self.driver
            home = HomePage(driver)

            home.verify_homepage()
            time.sleep(1)
            #2. Log In, Enter the userID and password
            home.open_login_window()
            time.sleep(1)
            home.enter_username(basedata.UserID)
            self.log.info("2. Log In, Enter the userID.")
            time.sleep(1)
            home.enter_password(basedata.Password)
            self.log.info("2. Log In, Enter password.")
            time.sleep(1)
            home.click_signin()
            self.log.info("2. Click Log In button.")
            time.sleep(1)
            home.verify_userID(basedata.UserID)
            self.log.info("2. Verified UserID.")
            time.sleep(1)

            #3. Select Tablets
            home.click_tablet()
            self.log.info("3. Select Tablets.")
            time.sleep(1)

            tablet = TabletsPage(driver)
            # 4. Select first item
            tablet.click_first_tablet()
            self.log.info("4. Select first item")
            time.sleep(1)

            tabletCart = TabletCartPage(driver)
            # 5. Click Add to Cart
            tabletCart.click_add_cart()
            self.log.info("5. Click Add to Cart.")
            time.sleep(1)
            # 6. Click Shopping Cart
            tabletCart.click_shopping_cart()
            self.log.info("6. Click Shopping Cart.")
            time.sleep(1)

            shopping = ShoppingCartPage(driver)
            # 7. Click Remove item
            shopping.click_remove()
            self.log.info("7. Click Remove item.")
            time.sleep(1)
            #Verity
            shopping.verify_empty_cart()

            # 8. Click 'Continue Shopping'
            shopping.click_continueshopping()
            self.log.info("8. Click 'Continue Shopping'.")
            time.sleep(1)
            # 9. Log out
            home.click_userID()
            time.sleep(1)
            home.click_signout()
            time.sleep(1)
            self.log.info("9. Log out.")

            self.log.info("Buy Tablet test completed.")
        except AssertionError as error:
            print("Assertion error occurred.")
            self.log.error("Assertion error occurred.")
            print(error)
            bu.save_screenshot(driver, "buyTablet_error")
            raise
        except:
            print("There was an exception")
            self.log.error("There was an exception")
            bu.save_screenshot(driver, "buyTablet_error")
            raise
        else:
            print("No exception occurred")