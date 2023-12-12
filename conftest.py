"""
conftest.py
"""
from selenium import webdriver
import pytest
from datetime import datetime
import os
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from constants.login_data import LOGIN_PAGE_URL, STANDARD_USER, STANDARD_PASSWORD


@pytest.fixture(scope="class")
def browser(request):
    browser = webdriver.Chrome()
    request.cls.browser = browser
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def login_as_standard_user(browser, request):
    browser.get(LOGIN_PAGE_URL)
    page = LoginPage(browser)
    credentials = (STANDARD_USER, STANDARD_PASSWORD)
    page.login(*credentials)
    post_login_page = ProductsPage(browser)
    request.cls.post_login_page = post_login_page
    return post_login_page


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    report_dir = 'reports'
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    config.option.htmlpath = f'{report_dir}/{datetime.now().strftime("%d-%m-%Y %H-%M-%S")}.html'

