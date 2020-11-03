'''
Navigate to the http://advantageonlineshopping.com/
Enter the userID and password
Verify that:
    Login userID
'''
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome(executable_path="../drivers/chromedriver.exe")
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(10)
driver.maximize_window()

driver.get("http://advantageonlineshopping.com/")
time.sleep(5)

driver.find_element_by_id("menuUserLink").click()
time.sleep(3)
driver.find_element_by_name("username").send_keys("JayJo74")
driver.find_element_by_name("password").send_keys("Seattle123")

driver.find_element_by_id("sign_in_btnundefined").click()
time.sleep(4)

#Check userID name
element = driver.find_element_by_xpath("//a[@id='menuUserLink']/span").get_attribute('innerHTML')
assert element == "JayJo74"
time.sleep(3)

driver.find_element_by_xpath("//a[@id='menuUserLink']/span").click()
time.sleep(1)
driver.find_element_by_xpath("//div[@id='loginMiniTitle']/label[3]").click()
time.sleep(3)

driver.close()
driver.quit()
print("Test Completed.")

# driver.find_element(By.LINK_TEXT, "test")


