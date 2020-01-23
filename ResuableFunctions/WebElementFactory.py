from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ResuableFunctions import globalVar


class WebElementFactory:
    def getElement(self,loc,locVal):
        if(loc=="xpath"):
            locator = (By.XPATH, locVal)
        elif (loc == "id"):
            locator = (By.ID, locVal)

        return WebDriverWait(globalVar.driver, 20).until(EC.element_to_be_clickable(locator))

    def getElements(self,loc,locVal):
        if (loc == "xpath"):
            lstEle = globalVar.driver.find_elements_by_xpath(locVal)
        elif (loc == "partialLinkText"):
            lstEle = globalVar.driver.find_elements_by_partial_link_text(locVal)
        return lstEle

    def clickElement(self,we,strWe):
        we.click()
        print("Clicking element '" + strWe + "'")

    def setText(self,we,strData):
        we.send_keys(strData)
        print("Setting Data:" + strData)

    def getCountOfItems(self,itm,strItemName):
        lstWe = WebElementFactory().getElements("partialLinkText",itm)
        print("Element Fetched.Count is " + len(lstWe))
        return len(lstWe)