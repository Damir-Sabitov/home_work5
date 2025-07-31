from selene import browser
import pytest


@pytest.fixture(autouse=True)
def open_browser():
    browser.open('https://demoqa.com/automation-practice-form')


    yield

    browser.quit()

