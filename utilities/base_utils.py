import logging
import inspect
import time
from datetime import datetime
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def customLogger(logLevel=logging.DEBUG):
    #Get the name of the class/method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    fileHandler = logging.FileHandler(filename="./logs/logfile.log", mode='a')
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)
    logger.setLevel(logging.DEBUG)
    return logger

def get_Text(driver, sec, by_locator):
    element = WebDriverWait(driver, sec).until(EC.visibility_of_element_located(by_locator))
    text = element.text
    if len(text) == 0:
        text = element.get_attribute("innerText")
    if len(text) != 0:
        text = text.strip()
    return text

def element_Click(driver, sec, by_locator):
    WebDriverWait(driver, sec).until(EC.visibility_of_element_located(by_locator)).click()

# this function asserts comparison of a web element's text with passed in text.
def assert_element_text(driver, sec, by_locator, element_text):
    text = get_Text(driver, 10, by_locator)
    assert text == element_text, "Asserting Error occurred - {} != {}".format(text, element_text)

# this function performs text entry of the passed in text, in a web element whose locator is passed to it.
def enter_text(driver, sec, by_locator, text):
    return WebDriverWait(driver, sec).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

def clear_text(driver, sec, by_locator):
    WebDriverWait(driver, sec).until(EC.visibility_of_element_located(by_locator)).clear()

# this function checks if the web element whose locator has been passed to it, is enabled or not and returns
# web element if it is enabled.
def is_enabled(driver, sec,  by_locator):
    return WebDriverWait(driver, sec).until(EC.visibility_of_element_located(by_locator))

# this function checks if the web element whose locator has been passed to it, is visible or not and returns
# true or false depending upon its visibility.
def is_visible(driver, sec, by_locator):
    element = WebDriverWait(driver, sec).until(EC.visibility_of_element_located(by_locator))
    return bool(element)

# this function moves the mouse pointer over a web element whose locator has been passed to it.
def hover_to(driver, sec, by_locator):
    element = WebDriverWait(driver, sec).until(EC.visibility_of_element_located(by_locator))
    ActionChains(driver).move_to_element(element).perform()

def get_attribute_value(driver, by_locator, attribute):
    element = driver.find_element(by_locator).get_attribute(attribute)
    return element

def save_screenshot(driver, errorStep):
    '''Take the screenshot with the current date and time'''
    folder = "D:\\AutomationPracticeCom\\screenshots\\"
    now = datetime.now()
    time_string = now.strftime("%Y-%m-%d-%H-%M")
    file_name = folder + errorStep +"_" + time_string +".png"
    driver.save_screenshot(file_name)




