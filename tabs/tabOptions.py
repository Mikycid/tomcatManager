import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tabs.abstractTab import Tab
from utils import ServerVersions, Tabs

class TabOptions(Tab):
    def __init__(self, master):
        super().__init__(master)
        self.selectedVersion = tk.StringVar()

    def fill(self):
        mwd = self.master.getWorkingDir()
        if(not mwd):
            mwd = "No working dir specified"
        else:
            mwd = "Working directory : " + mwd
        workingDir = ttk.Label(self, text=mwd)
        changeWorkingDir = ttk.Button(self, text="Change", command=self.selectProject)
        options = [i.name for i in ServerVersions]
        serverVersionLabel = ttk.Label(self, text="Current server : ")
        serverVersion = ttk.OptionMenu(self, self.selectedVersion, self.master.getServerVersion().name, *options, command=self.selectServerVersion)
        serverDeployPath = ttk.Label(self, text=self.master.getDeployPath() or "No deploy path specified")
        
        configureServer = ttk.Button(self, text="Configure", command=self.selectDeployPath)
        serverApi = ttk.Label(self, text=self.master.getApiPath() or "No jar api specified")
        btnServerApi = ttk.Button(self, text="Configure", command=self.selectServerApi)
        saveBtn = ttk.Button(self, text="Save", command=self.master.save)


        workingDir.grid(row=0,column=0)
        changeWorkingDir.grid(row=0,column=1)
        serverVersionLabel.grid(row=1,column=0)
        serverVersion.grid(row=1,column=1)
        serverDeployPath.grid(row=2, column=0)
        configureServer.grid(row=2, column=1)
        serverApi.grid(row=3, column=0)
        btnServerApi.grid(row=3, column=1)
        saveBtn.grid(row=4, columnspan=2)

        self.grid_columnconfigure((0,1), weight=1)

    def selectProject(self):
        super().selectProject()
        self.master.reload(Tabs.RUN)

    def selectServerVersion(self, version):
        super().selectServerVersion(version)
        self.master.reload(Tabs.RUN)

    def selectDeployPath(self):
        path = filedialog.askdirectory()
        if path != ():
            self.deployPath = path
            self.master.setDeployPath(path)
            self.master.reload(Tabs.RUN)
            self.reload()

    def selectServerApi(self):
        path = filedialog.askopenfilename()
        if path != ():
            self.apiPath = path
            self.master.setApiPath(path)
            self.master.reload(Tabs.RUN)
            self.reload()