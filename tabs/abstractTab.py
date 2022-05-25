import abc
from tkinter import ttk
from tkinter import filedialog
from utils import ServerVersions


class Tab(ttk.Frame, metaclass=abc.ABCMeta):

    def __init__(self, master):
        self.master = master
        super().__init__(master)
        self.workingDir = master.getWorkingDir()
        self.serverVersion = master.getServerVersion()
        self.deployPath = master.getDeployPath()
        self.apiPath = master.getApiPath()

    def clear(self):
        for widget in self.winfo_children():
            widget.destroy()

    def reload(self):
        self.clear()
        self.workingDir = self.master.getWorkingDir()
        self.serverVersion = self.master.getServerVersion()
        self.deployPath = self.master.getDeployPath()
        self.apiPath = self.master.getApiPath()
        self.fill()

    def selectProject(self):
        path = filedialog.askdirectory()
        if(path != ()):
            self.master.setWorkingDir(path)
            self.workingDir = path
            self.clear()
            self.fill()

    def selectServerVersion(self, serverVersion):
        self.master.setServerVersion(ServerVersions[serverVersion])
        self.serverVersion = serverVersion

    @abc.abstractmethod
    def fill(self):
        pass


    