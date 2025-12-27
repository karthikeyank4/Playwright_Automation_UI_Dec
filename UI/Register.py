# Register and login the site
#https://rahulshettyacademy.com/client/#/auth/login
import time

from playwright.sync_api import Page


def test_Register(page:Page):
    # browser=  playwright.chromium.launch(headless=False)
    # context=browser.new_context()
    # page= context.new_page()
    page.goto("https://rahulshettyacademy.com/client/")
    #Register The user in the Site
    page.locator(".btn1").click()
    page.locator("#firstName").fill("karthikeyan")
    page.locator("#lastName").fill("K")
    page.locator("#userEmail").fill("dummybaba@gmail.com")
    page.locator("#userMobile").fill("7092878753")
    page.get_by_role("combobox").select_option("Engineer")
    page.locator("input[type='radio'][value='Male']").check()
    page.locator("#userPassword").fill("Dummybaba@4")
    page.locator("#confirmPassword").fill("Dummybaba@4")
    page.locator('input[type="checkbox"]').click()
    page.get_by_role("button", name="Register").click()
    time.sleep(5)
    #page.get_by_text('Already have an account? Login here').click()
    # login the site
def test_Login(page:Page):
    page.goto("https://rahulshettyacademy.com/client/")
    page.locator("#userEmail").fill("trendsnowofficial@gmail.com")
    page.locator("#userPassword").fill("Password@4")
    page.locator("#login").click()
    time.sleep(5)
    # page.get_by_role("button",name="Sign out").click()
    #time.sleep(5)
   # page.get_by_placeholder("search").fill("shoe")
    #page.get_by_role("textbox", name="search").fill("shoe")
    # Add to cart Functionality
    # page .get_by_role("button",name=" View").click()
  #  page.goto("https://rahulshettyacademy.com/client/")














