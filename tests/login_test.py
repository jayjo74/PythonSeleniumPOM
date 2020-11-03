'''
Navigate to the http://advantageonlineshopping.com/
Enter the userID and password
Verify that:
    Login userID
'''
import pytest
import time
from testdata import basedata as basedata
from pages.homePage import HomePage
import logging
from utilities import base_utils as bu

@pytest.mark.usefixtures("test_setup")
class TestLogin():

    log = bu.customLogger(logging.DEBUG)

    def test_login(self):
        try:
            self.log.info("Log In test started.")
            driver = self.driver
            home = HomePage(driver)

            home.verify_homepage()
            time.sleep(1)
            #sign in
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
            # home.verify_userID(basedata.UserID)
            home.verify_userID("Jay")
            self.log.info("2. Verified UserID.")
            time.sleep(1)

            #sign out
            home.click_userID()
            time.sleep(1)
            home.click_signout()
            self.log.info("3. Log out.")
            self.log.info("Log In test completed.")
        except AssertionError as error:
            print("Assertion error occurred.")
            self.log.exception(error)
            print(error)
            bu.save_screenshot(driver, "login_error")
            raise
        except Exception as exception:
            print("There was an exception")
            self.log.exception(exception)
            bu.save_screenshot(driver, "login_error")
            raise
        else:
            print("No exception occurred")

