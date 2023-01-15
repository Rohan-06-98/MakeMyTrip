import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--ignore-certificate-error')
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        service_obj = Service(r"C:/Users/arnan/Downloads/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "Firefox":
        print("firefox driver")
        service_obj = Service()
        driver = webdriver.Firefox(service=service_obj)
    else:
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
    driver.implicitly_wait(10)
    driver.get("https://www.makemytrip.com/")
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
