import tkinter as tk
from tkinter import messagebox
from ttkthemes import ThemedTk
from tabs.tabRoot import TabRoot
from utils import ServerVersions
from data.save import save
from data.load import load
import os

class App(ThemedTk):
    def __init__(self):
        super().__init__(theme="radiance")
        if(os.geteuid() != 0):
            message = messagebox.Message(self, message="This program must be run with root privileges.")
            message.show()
            self.destroy()
            return

        data = load()
        self._workingDir:str = data[3]
        self._serverVersion:ServerVersions = data[0]
        self._saveOptionsOnQuit:bool = True
        self._deployPath:str = data[1]
        self._apiPath:str = data[2]

        self.configure()
        
    def setWorkingDir(self, workingDir:str):
        self._workingDir = workingDir

    def getWorkingDir(self)->str:
        return self._workingDir

    def setServerVersion(self, version:ServerVersions):
        self._serverVersion = version
    
    def getServerVersion(self)->ServerVersions:
        return self._serverVersion

    def setDeployPath(self, path):
        self._deployPath = path

    def getDeployPath(self)->str:
        return self._deployPath

    def setApiPath(self, path):
        self._apiPath = path

    def getApiPath(self)->str:
        return self._apiPath

    def configure(self):
        self.title('Tomcat Manager')

        screenWidth = self.winfo_screenwidth()
        windowWidth = int(screenWidth / 2)
        centerX = int(screenWidth/2 - windowWidth/2)

        self.iconphoto(False, tk.PhotoImage(file='imgs/tomcat_logo.png'))

        tabControl = TabRoot(self)
        tabControl.pack(expand=1, fill="both")
    
    def save(self):
        save(self._serverVersion, self._deployPath, self._apiPath, self._workingDir)
        message = messagebox.Message(self,message="Successfully saved settings")
        message.show()


    def __exit__(self):
        super().__exit__()
        if(self._saveOptionsOnQuit):
            self.save()
            



        

