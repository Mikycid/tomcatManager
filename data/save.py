import xml.etree.cElementTree as ET
from utils import ServerVersions

def save(serverVersion:ServerVersions, deployPath:str, apiPath:str, projectPath:str):
    settings = ET.Element("settings")

    project = ET.SubElement(settings, "project")
    title = ET.SubElement(project, "title")
    title.text = projectPath.split("/")[-1]
    path = ET.SubElement(project, "path")
    path.text = projectPath

    lastServer = ET.SubElement(settings, "last-used-server")
    lastServer.text = serverVersion.name

    ET.ElementTree(settings).write("settings/settings.xml")
    try:
        servers = ET.parse("settings/servers.xml")
        servers_root = servers.getroot()
        for server in servers_root.iter():
            if server.tag == serverVersion.name:
                server.find('deploy-path').text = deployPath
                server.find('api-path').text = apiPath
                servers.write("settings/servers.xml")
                return
        server = ET.SubElement(servers_root, serverVersion.name)
        server.text = deployPath

        servers.write("settings/servers.xml")
    except ET.ParseError:
        servers = ET.Element("servers")
        server = ET.SubElement(servers, serverVersion.name)
        sDeployPath = ET.SubElement(server, 'deploy-path')
        sDeployPath.text = deployPath
        sApiPath = ET.SubElement(server, 'api-path')
        sApiPath.text = apiPath
        ET.ElementTree(servers).write("settings/servers.xml")

    


