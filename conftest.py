import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="function")
def driver(request):
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-extensions")
    options.add_argument("disable-plugins")
    # options.add_argument("headless")
    options.add_argument("disable-gpu")
    driver = webdriver.Chrome(service=service, options=options)
    driver.get("http://localhost:5173/")
    # driver.execute_script("document.body.style.zoom='50%'")
    request.cls.driver = driver
    yield driver
    driver.quit()