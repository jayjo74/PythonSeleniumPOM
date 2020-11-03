'''
request.cls is the test class using the fixture,
so request.cls.driver = ... is essentially the same as MyTestClass.driver = ... if MyTestClass uses the fixture.

BTW: “request” is a pytest built-in fixture. with request.cls.driver = web_driver,
any class use this fixture will get an attribute driver automatically.
'''
import pytest
from testdata import basedata as basedata

'''
Create function to get browser name from arguments(command line)
'''

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    from webdriver_manager.chrome import ChromeDriverManager

    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.implicitly_wait(10)
    driver.get(basedata.URL)
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed.")