from ResuableFunctions.WebElementFactory import WebElementFactory

class PgSearch:
    def WaitForSearchPageLoad(self):
        WebElementFactory().getElement("xpath","//span[text()='Next']")
        print("Waiting for Search Page")

    def ClickNext(self):
        we = WebElementFactory().getElement("xpath","//span[text()='Next']")
        WebElementFactory().clickElement(we, "Next")

    def getCountOfItems(self,itm):
        lstWe = WebElementFactory().getElements("partialLinkText",itm)
        return len(lstWe)
