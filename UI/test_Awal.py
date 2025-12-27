import time

from playwright.sync_api import Playwright, Page, expect


# 1.Login with Valid Credentials .

def test_login(playwright:Playwright):
    browser =  playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://qa-awal.colanapps.in/")
    page .get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button" , name ="Sign in").click()
    time.sleep(5)

    #2.Click on the Forgot passsword Button & click on the Sign-in Button

def test_forgotPass(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.locator(".cursor-pointer").click()
    page.get_by_text("Sign In").click()
    time.sleep(5)

    #3.Click on the Sales Masters
def test_SalesMasters(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Sales Masters").click()
    page.get_by_text("Customer Master").click()
    page.locator(".visible").click()
    page.get_by_placeholder("Enter Customer Name").fill("dummy")
    #page.get_by_role("option" ,name ="Government").click()
    #page.get_by_role("combobox").select_option("Government")
    dropdown_input = page.get_by_label("customer Group")
    dropdown_input.click()
    page.get_by_role("listbox").locator("li").nth(1).click()
    page.locator("#cprNumber").fill("12345")
    page.get_by_placeholder("Upload File").click()
    page.locator("input[type='file']").set_input_files(r"C:\Users\CIPL1666\Downloads\Testing files\Img.jpg ,strict=False")
    page.wait_for_selector("input[type='file']", state="attached")
    page .get_by_placeholder("Enter Flat No").fill("179")
    page.get_by_placeholder("Enter Area / Street").fill("Bahraini")
    page.get_by_placeholder("Enter City").fill("sarjah")
    page.get_by_placeholder("Enter State").fill("tamilnadu")
    page.get_by_placeholder("Country").click()
    page.get_by_text("Saudi Arabia").click()
    page.get_by_placeholder("Enter Pincode").fill("600057")
    page.get_by_label("Address Type").click()
    page.get_by_text("Billing").click()
    page.locator("input[id='billing.0.flatNo']").fill("200")
    page.locator("input[id ='billing.0.areaStreet']").fill("Dummy Street")
    page.locator("input[id='billing.0.city']").fill("chennai")
    page.locator("input[id='billing.0.state']").fill("Delhi")
    page.locator("input[id='billing.0.country']").click()
    page.get_by_text("Saudi Arabia").click()
    page.locator("input[id='billing.0.pincode']").fill("600058")
    page.locator("input[id='billing.0.isDefault']").click()
    page.locator("input[id='selectedCurrency']").click()
    page.get_by_text("BHD").click()
    page.get_by_text("Save & Next").click()
    time.sleep(5)

    #4. CustomerGroup Master

def test_Customer_Group_Master(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Sales Masters").click()
    page.get_by_text("Customer Group Master").click()
    page.get_by_text("Add New Row").click()
    page.locator("input[id='8-code']").fill("dummy")
    page.get_by_placeholder("Select Customer Name").click()
   # page.get_by_text("XYZ Industries").click()
    page.get_by_role("option", name="XYZ Industries").click()
    page.locator("input[id='8-shortDescription']").fill("dummy2")
    page.get_by_alt_text("Save").click()
    time.sleep(5)

    #5.Contact Master
def test_Contact_Master(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Sales Masters").click()
    page.get_by_text("Contact Master").click()
    page.get_by_role("button", name="Create").click()
    page.get_by_role("combobox" ,name =" Customer Name").click()
    page.get_by_role("option" , name=" Tech Solutions").first.click()
    page.locator("#contactPerson").fill("karthikeyan k ")
    page.get_by_role("combobox" ,name ="department").click()
    page.get_by_role("option",name ="Production").first.click()
    page.locator("#designation").fill("QA Lead")
    page.locator("#primaryMobile").fill("7092878754")
    page.locator("#secondaryMobile").fill("8073687599")
    page.locator("#primaryEmail").fill("karthikeyan@gmail.com")
    page.locator("#secondaryEmail").fill("dummybaba@gmail.com")
    page.get_by_role("combobox" ,name ="Active").click()
    page.get_by_role("option" ,name ="Active").first.click()
    page.get_by_role("button" ,name ="Cancel").click()
    time.sleep(5)
    # 6.City Master
def test_City_Master(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Sales Masters").click()
    page.get_by_text("City Master").click()
    page.get_by_text("Add New Row").click()
    page.locator("input[id='8-customer']").fill("12345")
    page.locator("input[id='8-customerName']").fill("Awal Plastic")
    page.locator("input[id='8-country']").fill("India")
    page.locator("input[id='8-city']").fill("sajaraj")
    page.locator("input[id='8-additionalcity1']").fill("dubai")
    page.locator("input[id='8-additionalcity2']").fill("dubai main road")
    page.get_by_alt_text("Save").click()
    time.sleep(5)

    #7.Mode of shipment

def test_Mode_OfShipment(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Sales Masters").click()
    page.get_by_text("Mode  Of Shipment").click()
    page.get_by_text("Add New Row").click()
    page.locator("input[id='4-customer']").fill("S1001")
    page.locator("input[id='4-customerName']").fill("Karthik")
    page.get_by_role("combobox" ,name ="Select").click()
    page.get_by_role("option",name ="Water").first.click()
    page.locator("input[id='4-description']").fill("added the Description")
    page.get_by_alt_text("Save").click()
    time.sleep(5)

    #8.PriceList Type
def test_priceList_Type(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Sales Masters").click()
    page.get_by_text("Price List Type").click()
    page.get_by_text("Add New Row").click()
    page.locator("#itemMaterialName").fill("Aluminum")
    page.locator("#description").fill("added the Description")
    page.get_by_role("combobox" ,name="uom").click()
    page.get_by_role("option" ,name ="Piece").first.click()
    page.locator("#purchasePrice").fill("2000")
    page.locator("#customerLocalPrice").fill("1999")
    page.locator("#customerOverseasPrice").fill("3000")
    page.get_by_role("button" ,name="Choose date").first.click()
    page.wait_for_selector("div[role='dialog']")
    page.get_by_role("button", name=re.compile("10")).click()
    page.get_by_role("button", name="Apply").click()
    time.sleep(5)

    #9.sales Target
def test_sales_Target(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Sales Masters").click()
    page.get_by_text("Sales Target").click()
    page.get_by_placeholder("Select").first.click()
    #page.get_by_text("Awal Plastics, Bahrain").click()
    page.get_by_role("option", name="Awal Plastics, Bahrain").click()
    page.get_by_role("combobox" ,name="Select").nth(1).click()
    page.get_by_role("option" ,name ="Sales Order").click()
    page.locator("#frequency").click()
    page.get_by_role("option" ,name="Monthly").click()
    page.get_by_placeholder("Amount").click()
    page.get_by_role("option" ,name= "Quantity").click()
    page.get_by_role("button" ,name ="Create").click()
    page.get_by_alt_text("Save").click()
    time.sleep(5)

    #10.Driver Profile.
def test_driver_Profile(page:Page): 
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Sales Masters").click()
    page.get_by_text("Driver Profile").click()
    page.get_by_role("button",name ="create").click()
    page.locator("#driverCode").fill("1234")
    page.locator("#driverName").fill("Karthikeyan k")
    page.locator("#drivingLicenseNumber").fill("1234566")
    page.locator("#visaNumber").fill("1324346")
    page.locator("#personalEmail").fill("dummybaba@gmail.com")
    page.locator("#officialEmail").fill("dummybaba2@gmail.com")
    page.get_by_placeholder("Enter Mobile Number").fill("78565788979")
    page.get_by_placeholder("Enter Alternate Mobile Number").fill("576765765")
    page.get_by_placeholder("Enter Hometown Mobile Number").fill("57867868768")
    page.locator("#country").click()
    page.get_by_role("option" ,name ="kuwait").click()
    page.locator("#cprNumber").fill("12345")
    page.locator("#status").click()
    page.get_by_role("option",name ="Active" ,exact=True).click()
    page.get_by_role("button",name="Upload").click()
    page.locator("input[type='file']").set_input_files(
        r"C:\Users\CIPL1666\Downloads\Testing files/file.pdf"
    )
    page.locator("#vehicleType").click()
    page.get_by_role("option" ,name ="Light Vehicle" ,exact=True).click()
    page.locator("#vehicleNumber").fill("2444")
    page.get_by_text("Save").click()
    page.get_by_alt_text("cancel").click()
    time.sleep(5)

    #11.Discount Master
def test_Discount_Master(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Sales Masters").click()
    page.get_by_text("Discount Master").click()
    page.get_by_text("Add New Row").click()
    page.locator("input[id='8-customername']").fill("Karthik")
    page.locator("input[id ='8-productname']").fill("Aluminium")
    page.locator("input[id='8-group']").fill("Group")
    page.locator("input[id='8-company']").fill("Awal")
    page.locator("input[id='8-cash']").fill("No")
    page.locator("input[id='8-creditdiscount']").fill("10%")
    page.locator("input[id='8-cashdiscount']").fill("10%")
    page.locator("#discountselection").click()
    page .get_by_role("option" ,name ="Overall cost" ,exact=True).click()
    page.locator("input[id='8-approvedby']").fill("Karthik")
    page.locator("input[id='8-remarks']").fill("remarks")
    page.get_by_alt_text("Save").click()
    time.sleep(5)

    #12.Terms & Condition .
def test_terms_Cond(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Sales Masters").click()
    page.get_by_text("Terms & Condition").click()
    page.get_by_role("button" ,name="Create").click()
    page.locator("#formName").click()
    page.get_by_role("option" ,name ="Common",exact=True).click()
    page.get_by_role("button", name="Choose date").nth(0).click()
    page.get_by_text("18", exact=True).click()
    page.get_by_role("button", name="Apply").click()
    page.get_by_role("button", name="Choose date").nth(1).click()
    page.locator("div.css-8uic9k", has_text="20").first.click()
    page.get_by_role("button", name="Apply").click()
    page.get_by_text("Add New Section").click()
    page.locator("#section").fill("Success ")
    page.get_by_alt_text("save").click()
    page.locator(".is-editor-empty").fill("Updated the content")
    page.locator("img[src*='tick']").click()
    page.get_by_role("button",name ="Save").click()
    page.get_by_role("button", name="Yes").click()
    page.locator("img[src*='cancel']").click()
    time.sleep(5)

    #13.Project Master Rules
def test_Project_Master(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Sales Masters").click()
    page.get_by_text("Project Master").click()
    page.get_by_role("button" ,name="Create").click()
    page.locator("#customerName").fill("Karthik")
    page.locator("#leadNumber").fill("123")
    page.locator("#enquiryNumber").fill("456")
    page.locator("#ppjo").click()
    page.get_by_role("option" ,name ="Open").first.click()
    page.locator("#quotation").click()
    page.get_by_role("option",name ="Open").click()
    page.locator("#salesOrder").click()
    page.get_by_role("option" ,name="Open").click()
    page.locator("#projectName").fill("Awal")
    page.locator("#projectDescription").fill("I updated the Description")
    page.get_by_role("button",name ="Save").click()
    page.get_by_role("button",name ="close").click()
    time.sleep(5)

    # Leads Creation Flow
def test_Leads(page:Page):
    page.goto("https://qa-awal.colanapps.in/")
    page.get_by_label("Email ID").fill("Karthik@colan.com")
    page.locator("#password").fill("1234")
    page.get_by_role("button", name="Sign in").click()
    page.get_by_text("Leads").click()
    page.get_by_text("Social Media").click()
    page.get_by_role("button",name="Lead").click()
    page.locator("#customerName").fill("Karthik")
    page.locator("#company").fill("Awal")
    page.locator("#city").fill("Chennai")
    page.locator("#value").fill("1234")
    page.locator("#owner").click()
    page.locator("#expectedDeliveryDate").fill("12/12/2025")
    page.locator("#leadSourceType").click()
    page.get_by_role("option" ,name="Instagram").first.click()
    page.locator("#phone").fill("7092878754")
    page.locator("#work1").fill("QA Engineer")
    page.locator("#email").fill("Karthikeyan@email.com")
    page.locator("#work2").fill("Amazon")
    page.get_by_placeholder("Upload File").click()
    page.locator("input[type='file']").set_input_files(r"C:\Users\CIPL1666\Downloads\Testing files\Test.pdf")
    page.locator("Notes Updated Successfully")
    page.get_by_role("button",name="Create Lead").click()
    time.sleep(5)



















