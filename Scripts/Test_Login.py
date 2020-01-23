from Pages.PgHome import PgHome
from Pages.PgSearch import PgSearch

import logging

from ResuableFunctions import globalVar

log = logging.getLogger(__name__)
class Test_Login:

    def test_Login1(self,setUp):
        pgHome = PgHome()
        pgSearch = PgSearch()

        strCamera = globalVar.configData.get("Brand")
        pgHome.clickDismissDialog()
        pgHome.setSearch("Camera")
        pgHome.clickSearchGo()
        pgSearch.WaitForSearchPageLoad()
        cnt = pgSearch.getCountOfItems(strCamera)
        print("Camera brand: " + strCamera + " Count of Cameras:" + str(cnt))

