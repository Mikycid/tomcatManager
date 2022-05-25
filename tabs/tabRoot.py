import tkinter as tk
from tkinter import ttk
from tabs.tabConsole import TabConsole
from tabs.tabCreate import TabCreate
from tabs.tabRunning import TabRunning
from tabs.tabOptions import TabOptions
from tabs.tabServer import TabServer
from utils import ServerVersions, Tabs

class TabRoot(ttk.Notebook):
    def __init__(self, master):
        self.master = master
        super().__init__(master)
        self.tabCreate = TabCreate(self)
        self.tabOptions = TabOptions(self)
        self.tabServer = TabServer(self)
        self.tabConsole = TabConsole(self)

        self.tabRun = TabRunning(self, self.tabConsole)

        self.add(self.tabCreate, text="New project",padding="30")
        self.add(self.tabRun, text="Running",padding="30")
        self.add(self.tabOptions, text="Options",padding="30")
        self.add(self.tabServer, text="Server", padding="30")
        self.add(self.tabConsole, text="Console")
        self.pack(expand=1, fill="both")

        self.tabCreate.fill()
        self.tabRun.fill()
        self.tabOptions.fill()
        self.tabServer.fill()
        self.tabConsole.fill()
    
    def getWorkingDir(self):
        return self.master.getWorkingDir()

    def setWorkingDir(self, path):
        return self.master.setWorkingDir(path)
    
    def getServerVersion(self) -> ServerVersions:
        return self.master.getServerVersion()
    
    def setServerVersion(self, version:ServerVersions):
        self.master.setServerVersion(version)

    def setDeployPath(self, path):
        self.master.setDeployPath(path)

    def getDeployPath(self)->str:
        return self.master.getDeployPath()

    def setApiPath(self, path):
        self.master.setApiPath(path)
    
    def getApiPath(self) -> str:
        return self.master.getApiPath()

    def save(self):
        self.master.save()

    def reload(self, tab:Tabs):
        if tab == Tabs.CREATE:
            self.tabCreate.reload()
        elif tab == Tabs.RUN:
            self.tabRun.reload()
        elif tab == Tabs.OPTIONS:
            self.tabOptions.reload()