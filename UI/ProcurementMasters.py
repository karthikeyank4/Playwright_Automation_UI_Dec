
#1.Aisle Master
def test_AisleMaster(config):
    page =config
    page.locator("img[alt='Procurement']").click()
    page.get_by_text("Home").click()
    page.locator("img[src*='procurement-active.svg']").click()




