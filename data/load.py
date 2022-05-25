from xml.etree.ElementTree import ParseError
import xml.etree.cElementTree as ET
from utils import ServerVersions

def load() -> "tuple[ServerVersions, str, str]":
    try:
        settings_tree = ET.parse("settings/settings.xml")
        root = settings_tree.getroot()
        lastServer = root.find("last-used-server").text or ""
        lastProject = root.find("project/path").text or ""

        serverTree = ET.parse("settings/servers.xml")
        root = serverTree.getroot()
        lastDeployPath = root.find(lastServer+"/deploy-path").text or ""
        lastApiPath = root.find(lastServer+"/api-path").text or ""

        return (ServerVersions[lastServer], lastDeployPath, lastApiPath, lastProject)
    except (FileNotFoundError, AttributeError, ParseError):
        return(ServerVersions.TOMCAT10, "", "", "")
