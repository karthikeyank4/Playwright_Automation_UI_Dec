import pytest
from playwright.sync_api import Playwright

@pytest.fixture(scope= "module")
def config (playwright:Playwright):
    browser= playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page = context.new_page()
    page.goto("https://qa-awal.colanapps.in/")
    page.locator("#email").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    return page
