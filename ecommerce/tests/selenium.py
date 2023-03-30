import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope="module")
def chrome_driver_instance(request):
    # provides a selenium webdriver instance
    options = Options()
    options.add_argument("--headless")
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.close()