import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Pages.PgHome import PgHome
from Pages.PgSearch import PgSearch
from ResuableFunctions.BrowserFactory import BrowserFactory
from pytest_html import extras

import logging

log = logging.getLogger(__name__)
class Test_Login:
    # def test_Login(self):
    #     driver = webdriver.Chrome(executable_path="C:\\LISSIA\\branches\\AIG\\E2E\\MTAF\\Drivers\\chromedriver.exe")
    #     driver.get("https://www.flipkart.com")
    #
    #     # ele = driver.find_element(By.NAME,"q")
    #     locator = (By.XPATH,"//button//span[text()='Login']//preceding::button[1]")
    #     ele = WebDriverWait(driver,20).until(EC.element_to_be_clickable(locator))
    #     ele.click()
    #     a=2

    def test_Login1(self,setUp):
        pgHome = PgHome()
        pgSearch = PgSearch()

        strCamera = "Canon"
        pgHome.clickDismissDialog()
        pgHome.setSearch("Camera")
        pgHome.clickSearchGo()
        pgSearch.WaitForSearchPageLoad()
        cnt = pgSearch.getCountOfItems(strCamera)
        print("Total Count of Cameras:" + str(cnt))

