import time

from playwright.sync_api import Playwright


def test_grey(playwright:Playwright):
     browser = playwright.chromium.launch(headless=False)
     context= browser.new_context()
     page = context.new_page()
     page.goto("https://colaninfotech1.greythr.com/")
     page.locator("#username").fill("CIPL1666")
     page.locator("#password").fill("Victoryconform@9945")
     page.get_by_role("button",name=" Login ").click()
     time.sleep(5)



