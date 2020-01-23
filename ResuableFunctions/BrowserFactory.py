from selenium import webdriver
from ResuableFunctions import globalVar

class BrowserFactory:
    def __init__(self):
        if(globalVar.driver is None):
            globalVar.driver = webdriver.Chrome(globalVar.projectPath + globalVar.configData.get("chromePath"))
            globalVar.driver.get(globalVar.configData.get("appUrl"))

    def LaunchUrl(self,url):
        globalVar.driver.get(url)

    def getBrowserTitle(self):
        return globalVar.driver.title

    def closeBrowser(self):
        globalVar.driver.close()