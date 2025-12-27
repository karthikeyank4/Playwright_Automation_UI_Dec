# Login into the swab labs
import time

from playwright.sync_api import Playwright, expect


def test_login(playwright:Playwright):
    browser =  playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page= context.new_page()
    page.goto("https://www.saucedemo.com/")
    page.locator("#user-name").fill("standard_user")
    page.locator("#password").fill("secret_sauce")
    page.locator("#login-button").click()
    expect(page.get_by_text("Swag Labs")).to_be_visible()
    # page.locator(".product_sort_container").click()
    page.locator(".product_sort_container").select_option(label="Price (low to high)")
    #page.get_by_role("button",name="Add to cart").click()
    page.locator("#add-to-cart-sauce-labs-onesie").click()
    page.locator(".shopping_cart_link").click()
    page.locator("#checkout").click()
    page.locator("#first-name").fill("Karthikeyan ")
    page.locator("#last-name").fill("k")
    page.locator("#postal-code").fill("600057")
    page.locator("#continue").click()
    page.locator("#finish").click()
    page.locator("#back-to-products").click()
    page.locator("#react-burger-menu-btn").click()
    page.locator("#logout_sidebar_link").click()
    expect(page.get_by_text("Swag Labs")).to_be_visible()
    time.sleep(5)