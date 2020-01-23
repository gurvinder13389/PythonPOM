import os
import pytest
import yaml

from ResuableFunctions import globalVar
from ResuableFunctions.BrowserFactory import BrowserFactory

@pytest.fixture(scope="session")
def setUp():
    globalVar.projectPath = os.path.dirname(__file__)
    globalVar.configData = yaml.safe_load(open(globalVar.projectPath + "/Resources/config.yaml"))
    browser = BrowserFactory()
    yield setUp
    BrowserFactory().closeBrowser()



