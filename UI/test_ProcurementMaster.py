import time

from playwright.sync_api import Playwright, Page


#1.Aisle Master
def test_Aisle_Master(playwright:Playwright):
    browser =  playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page=context.new_page()
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.locator("img[src*='procurement']").click()
    page.get_by_text("Procurement Master").click()
    page.get_by_text("Aisle Master").click()
    page.get_by_role("button",name="create").click()
    page.locator("#aisleName").fill("Testingda")
    page.locator("#description").fill("Updated the Description")
    page.get_by_role("button",name="Create").click()
    time.sleep(5)

    #2.Rack Master
def test_Rack_Master(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.locator("img[src*='procurement']").click()
    page.get_by_text("Procurement Master").click()
    page.get_by_text("Rack Master").click()
    page.get_by_role("button",name ="Create").click()
    page.locator("#rackName").fill("Testing")
    page.locator("#aisleId").click()
    page.get_by_role("option",name ="Testingda").click()
    page.locator("#description").fill("Updated the Successfully")
    page.get_by_role("button",name="Create").click()
    time.sleep(5)

    #3.Shelf Master
def test_shelfMaster(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.locator("img[src*='procurement']").click()
    page.get_by_text("Procurement Master").click()
    page.get_by_text("Shelf Master").click()
    page.get_by_role("button",name="Create").click()
    page.locator("#shelfName").fill("Testing")
    page.locator("#rackId").click()
    page.get_by_role("option" ,name="IT Admin Section").click()
    page.locator("#shelfSizeId").click()
    page.get_by_role("option" ,name ="")



