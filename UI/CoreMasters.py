import random
import string
import time


from playwright.sync_api import Playwright, Page, expect


def random_text(prefix="Auto", length=4):
    return prefix + ''.join(random.choices(string.ascii_uppercase, k=length))

#Country Master
def test_countryMaster(config):
    page=config
    country_name = random_text()
    short_name =random_text("SHR_")
    page.get_by_role("heading", name="Master").click()
    page.get_by_text("Home").click()
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("Country Master").click()
    page.get_by_text("Add New Country").click()
    page.locator("#countryName").fill(country_name)
    page.locator("#countryShortName").fill(short_name)
    page.locator("#currencyId").click()
    page.get_by_role("option" ,name ="EUR" ).first.click()
    page.locator("#phoneCode").fill("91")
    page.locator("#vat").click()
    page.locator("#status").click()
    page.get_by_role("option" ,name ="Active" ,exact=True).click()
    page.locator("#remarks").fill("Updated successfully")
    page.get_by_role( "button", name="Create Country").click()
    #expect(page.get_by_text("City created successfully")).to_be_visible()
    page.locator("img[src*='edit.svg']").first.click()
    page.locator("#countryShortName").fill("INR")
    page.get_by_role("button",name="Save Country",exact=True).click()
    time.sleep(5)

    #2.Bank Master
def test_Bank_Master(config):
    page=config
    bank_name=random_text("Ban_")
    branch_Name = random_text("BR_")
    swift_code =random_text("shift_")
    Ibn =random_text("ib_")
    page.get_by_role("heading", name="Master").click()
    page.get_by_text("Home").click()
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("Bank Master").click()
    page.get_by_text("Add New Bank").click()
    page.locator("#bankName").fill(bank_name)
    page.locator("#branchName").fill(branch_Name)
    page.locator("#country").click()
    page.get_by_role("option" ,name ="United State of America",exact=True).click()
    page.locator("#state").click()
    page.get_by_role("option" ,name ="USA State" ,exact=True).click()
    page.locator("#city").click()
    page.get_by_role("option" ,name="pernambut" ,exact=True).click()
    page.locator("#swiftCode").fill(swift_code)
    page.locator("#ibanPrefix").fill(Ibn)
    page.locator("#bankAddress").fill("Ennore Branch ")
    page.locator("#contactPerson").fill("Karthikeyan k")
    page.locator("#contactNumber").fill("70928787543")
    page.locator("#emailId").fill("karthikeyan@colan.com")
    page.locator("#status").click()
    page.get_by_role("option" ,name ="Active" ,exact=True).click()
    page.locator("input[type='checkbox']").first.click()
    page.locator("input[type='checkbox']").nth(1).click()
    page.locator("#remarks").fill("Update the remarks Section")
    page.get_by_role("button",name ="Create Bank").click()
    time.sleep(5)

    #3.City Master
def test_city_Master(config):
    page=config
    city_name =random_text()
    page.get_by_role("heading", name="Master").click()
    page.get_by_text("Home").click()
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("City Master").click()
    page.get_by_text("Add New City").click()
    page.locator("#countryId").click()
    page.get_by_role("option" ,name="United State of America",exact=True).click()
    page.locator("#stateId").click()
    page.get_by_role("option" ,name ="USA State",exact=True).click()
    page.locator("#cityName").fill(city_name)
    page.locator("#postalCode").fill("600057")
    page.locator("#status").click()
    page.get_by_role("option" ,name ="Active",exact=True).click()
    page.get_by_role("button" ,name="Create City").click()
    page.locator("img[src*='edit.svg']").first.click()
    page.locator("#cityName").fill("Thousandlights")
    page.get_by_role("button",name="Save City").click()
    time.sleep(5)

    #4. State Master
def test_state_Master(config):
    page=config
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("State Master").click()
    page.get_by_role("button",name ="Add New State").click()
    page.locator("#stateName").fill("Tamilnadu")
    page.locator("#countryId").click()
    page.get_by_role("option",name="America",exact=True).click()
    page.locator("#regionTypeId").click()
    page.get_by_role("option",name="Southern Governorate",exact=True).click()
    page.locator("#status").click()
    page.get_by_role("option",name="Active" ,exact=True).click()
    page.locator("#remarks").fill("Updated the remarks Section")
    page.get_by_role("button",name ="Create State").click()
    time.sleep(5)

    #5.Mode of Shipment
def test_mode_Of_Shipment(config):
    page =config
    page.get_by_role("button", name="Sign in").click()
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("Mode Of Shipment").click()
    page.get_by_role("button",name="Create").click()
    page.locator("#mode").fill("Air")
    page.locator("#description").fill("Air Shipment Mode Updated Successfully")
    time.sleep(5)

    #6.Project Master
def test_Project_Master(config):
    page=config
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("Project Master").click()
    page.get_by_role("button",name="Create").click()
    page.locator("#projectName").fill("#3D Print")
    page.locator("#customerId").click()
    page.get_by_role("option",name ="Awal Plastics W.L.L. - Updated").click()
    page.locator("#leadId").click()
    page.get_by_role("option",name ="LN100").click()
    page.locator("#enquiryId").click()
    page.get_by_role("option",name="EQ020").click()
    page.locator("#ppjoId").click()
    page.get_by_role("option",name="PJ082").click()
    page.locator("#quotationId").click()
    page.get_by_role("option",name ="QT-2025-001").click()
    page.locator("#salesOrderId").click()
    page.get_by_role("option",name="SO-2025-001").click()
    page.locator("#estimationId").click()
    page.get_by_role("option",name="EST-75675").click()
    page.locator("#projectTypeId").click()
    page.get_by_role("option",name ="Awal Project").click()
    page.get_by_role("button", name="Choose date").nth(0).click()
    page.locator(".css-8uic9k", has_text="9").first.click()
    page.get_by_role("button", name="Apply").click()
    page.get_by_role("button", name="Choose date").nth(1).click()
    page.locator(".css-8uic9k", has_text="10").first.click()
    page.get_by_role("button", name="Apply").click()
    page.locator("#statusId").click()
    page.get_by_role("option",name="InProgress").click()
    page.locator("#priorityId").click()
    page.get_by_role("option",name="High").click()
    page.locator("#projectManagerId").click()
    page.get_by_role("option",name="Aisha").click()
    page.locator("#location").fill("Chennai")
    page.locator("#remarks").fill("Update the Description")
    page.get_by_role("button" ,name ="Create Project Master").click()
    time.sleep(5)

    #7.Department
def test_Department(config):
    page=config
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("Department Master").click()
    page.get_by_text("Add New Department").click()
    page.locator("#departmentName").fill("Department")
    page.locator("#reportingTo").click()
    page.get_by_role("option",name="Aisha").click()
    page.locator("#email").fill("Karthikeyan@gmail.com")
    page.locator("#approvalHierarchyId").click()
    page.get_by_role("option",name="Aisha NSS").click()
    page.locator("#status").click()
    page.get_by_role("option",name="Active",exact=True).click()
    page.locator("#description").fill("Updated the Description")
    page.get_by_role("button",name="Create Department").click()
    time.sleep(5)

    #8.Employee Master
def test_Employee_Master(config):
    page=config
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("Employee Master").click()
    page.get_by_role("button" ,name ="Add Employee").click()
    page.locator("#empName").fill("Neelamegam")
    page.get_by_role("button",name="Choose date").nth(0).click()
    page.locator(".css-8uic9k",has_text="12").first.click()
    page.get_by_role("button",name ="apply").click()
    page.locator("#genderId").click()
    page.get_by_role("option",name="Male").first.click()
    page.locator("#countryOfBirthId").click()
    page.get_by_role("option",name="India").click()
    page.locator("#stateOfBirthId").click()
    page.get_by_role("option",name ="Tamil Nadu").click()
    page.locator("#cityOfBirthId").click()
    page.get_by_role("option",name ="Chennai").click()
    time.sleep(5)

    #9.Designation
def test_Designation(page:Page):
    page=config
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("Designation / Role Master").click()
    page.get_by_role("button",name="Add New Designation").click()
    page.locator("#designationName").fill("Senior Software Test Engineer")
    page.locator("#department").click()
    page.get_by_role("option",name="Sales").click()
    page.locator("#jobCategory").click()
    page.get_by_role("option",name="Skilled").click()
    page.locator("#gradeLevel").click()
    page.get_by_role("option",name="G4 - Senior").click()
    page.locator("#bahrainMolJobClassification").click()
    page.get_by_role("option" ,name ="Managers & Professionals").click()
    page.locator("#reportingTo").click()
    page.get_by_role("option",name ="General Manager").click()
    page.locator("#linkedErpRoleRbac").click()
    page.get_by_role("option" ,name="System Administrator")
    page.locator("#status").click()
    page.get_by_role("option",name ="Active",exact=True).click()
    page.locator("#description").fill("Updated the Description")
    page.locator("#notes").fill("Updated the Notes Successfully")
    page.get_by_role( "button",name="Create Designation").click()
    time.sleep(10)

    # 10.UOM
def test_UOM(page:Page):
    page=config
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("UOM Master (Unit of Measurement Master)").click()
    page.get_by_role("button",name="Create").click()
    page.locator("#unitName").fill("Neelamegam")
    page.locator("#unitCode").fill("123")
    page.locator("#status").click()
    page.get_by_role("option" ,name ="Active",exact=True).click()
    page.get_by_text("Submit").click()
    time.sleep(5)

     #11.User master
def test_UserMaster(config):
    page=config
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("User Master").click()
    page.get_by_role("button",name ="Add New User").click()
    page.locator("#fullName").fill("Karthikeyan k")
    page.locator("#usernameEmail").fill("karthikeyan@colan.com")
    page.locator("#contactNumber").fill("7092878759")
    page.locator("#employeeId").click()
    page.get_by_role("option",name="Test User").click()
    page.locator("#departmentid").click()
    page.get_by_role("option",name="Department" ,exact=True).click()
    page.locator("#designationId").click()
    page.get_by_role("option",name="QA testing").click()
    page.locator("#accessRoleId").click()
    page.get_by_role("option",name="Employee - Limited Access").click()
    page.locator("#accessScopeId").click()
    page.get_by_role("option",name ="Specific Department").click()
    page.locator("#branchId").click()
    page.get_by_role("option",name="Head Office - Storage").click()
    page.locator("#isActive").click()
    page.get_by_role("option" ,name ="Active",exact=True).click()
    page.locator("#notesRemarks").fill("Updated the Notes Successfully")
    page.locator("#passwordHash").fill("1234")
    page.locator("#confirmPasswordHash").fill("1234")
    page.locator("#allowedLoginIpRange").fill("192.168.1.101/24")
    page.locator("#sessionTimeout").fill("30")
    page.get_by_role("button",name="Create User").click()
    time.sleep(10)

    #12.Document Type Master
def test_Document_type_Master(config):
    page=config
    page.get_by_alt_text("Master").click()
    page.get_by_text("Home").click()
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("Document Type Master").click()
    page.get_by_text("Add New Document Type").click()
    page.locator("#documentName").fill("NoteBook")
    page.locator("#documentCategoryId").click()
    page.get_by_role("option",name="Sales").click()
    page.locator("#linkedModuleId").click()
    page.get_by_role("option",name="HRMS").click()
    page.locator("#description").fill("Updated the Description Successfully")
    page.locator("#prefixFormat").fill("MR")
    page.locator("#suffixFormat").fill("MS")
    page.locator("#numberPadding").fill("123")
    page.locator("#separatorSymbol").fill("dhh")
    page.locator("#startingNumber").fill("12345")
    page.locator("#resetFrequencyId").click()
    page.get_by_role("option",name="Month",exact=True).click()
    page.locator("#vatApplicable").click()
    page.locator("#nbrCompliantFormat").click()
    page.locator("#defaultPaperSizeId").click()
    page.get_by_role("option",name="A0").click()
    page.locator("#templateVersion").fill("12345")
    page.locator("#requiresApprovalBeforeIssue").click()
    page.locator("#digitalSignatureRequired").click()
    page.locator("#remarks").fill("The Remarks Updated Successfully")
    page.locator("#status").click()
    page.get_by_role("option", name="Active",exact=True).click()
    page.get_by_role("button",name ="Create").click()
    page.locator("img[src*='edit-svg']").click()
    time.sleep(5)

    #13. Employee Grade master
def test_Employee_Grade_Master(config):
    page=config
    page.locator("img[src*='user-setting']").click()
    page.get_by_text("Employee Grade Master").click()
    page .locator("#gradeName").fill("Senior Executive")
    page.get_by_role("button",name ="Create").click()
    page.get_by_placeholder("Enter Grade Name").fill("Test Engineer")
    page.locator("#hierarchyLevel").fill("2")
    page.locator("#status").click()
    page.get_by_role("option",name="Active",exact=True).click()
    page.locator("#description").fill("Updated the Description Successfully")
    page.get_by_role("button",name="Save").click()
    time.sleep(5)

    #14.Material Sub Master
    #14a.Material Sub Master -Material Type
def test_MaterialType(config):
    page=config
    page.get_by_alt_text("Master").click()
    page.get_by_text("Home").click()
    page.locator("img[src*='user-setting-white']").click()
    page.get_by_text("Material Sub Master").click()
    page.get_by_role("button",name="Create").click()
    page.locator("#materialName").fill("Aluminium")
    page.locator("#description").fill("Update the Description Successfully")
    page.get_by_role("button",name="Create").click()
    time.sleep(5)

def test_Materialcolor(config):
    page = config
    page.get_by_alt_text("Master").click()
    page.get_by_text("Home").click()
    page.get_by_text("Material Sub Master").click()
    page.get_by_text("Material Color").click()
    page.get_by_role("button",name="Create").click()
    page.locator("#colorName").fill('789347')
    page.locator("#description").fill("update the Description Successfully")
    page.get_by_role("button",name="Create").click()
    time.sleep(5)

def test_MaterialFinish(config):
    page = config
    page.get_by_alt_text("Master").click()
    page.get_by_text("Home").click()
    page.get_by_text("Material Sub Master").click()
    page.get_by_text("Material Finish").click()
    page.get_by_text("Create").click()
    page.locator("#materialFinish").fill("Aluminium")
    page.locator("#description").fill("Update the  Description Successfully")
    page.get_by_role("button",name="Create").click()
    time.sleep(5)


    #Material Sub Master -Material Size
def test_MaterialSize(config):
    page = config
    page.get_by_alt_text("Master").click()
    page.get_by_text("Home").click()
    page.get_by_text("Material Sub Master").click()
    page.get_by_text("Material Size").click()
    page.get_by_text("create").click()
    page.locator("#materialSize").fill("900")
    page.locator("#description").fill("update the description Successfully")
    page.get_by_role("button",name="Create").click()
    time.sleep(5)

     #Material Sub Master - Material Category
def test_MaterialNature(config):
    page = config
    page.get_by_alt_text("Master").click()
    page.get_by_text("Home").click()
    page.get_by_text("Material Sub Master").click()
    page.get_by_text("Material Nature").click()
    page.get_by_text("create").click()
    page.locator("#materialName").fill("Material")
    page.locator("#description").fill("update the description Successfully")
    page.get_by_role("button",name="Create").click()























