from ResuableFunctions.WebElementFactory import WebElementFactory

class PgHome:
    def clickDismissDialog(self):
        we = WebElementFactory().getElement("xpath","//button//span[text()='Login']//preceding::button[1]")
        WebElementFactory().clickElement(we,"Dismiss Dialog")

    def setSearch(self,strData):
        we = WebElementFactory().getElement("xpath","//input[@name='q']")
        WebElementFactory().setText(we,strData)

    def clickSearchGo(self):
        we = WebElementFactory().getElement("xpath","//input[@name='q']//parent::div//following-sibling::button")
        WebElementFactory().clickElement(we,"Search Go")