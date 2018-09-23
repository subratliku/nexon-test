import pytest
from selenium.webdriver import Chrome,Firefox, Ie

def get_driver_instance():
    browser=pytest.config.option.type
    env=pytest.config.option.env
    if browser.lower()=='chrome':
        driver=Chrome('./browser-servers/chromedriver.exe')
    elif browser.lower()=='firefox':
        driver=Firefox('./browser-servers/geckodriver.exe')
    elif browser.lower()=='ie':
        driver=Ie('./browser-servers/IEDriverServer.exe')
    else:
        print('---------Invalid Browser option---------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    if  env.lower()=='test':
        driver.get('http://localhost')
    elif env.lower()=='prod':
        driver.get('http://www.facebook.com')
    else:
        print('--------Invalid Application URL----------')
    return driver



