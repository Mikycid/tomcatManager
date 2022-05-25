from tkinter import ttk
from tabs.abstractTab import Tab
import subprocess

class TabServer(Tab):
    def __init__(self, master):
        super().__init__(master)
    
    def fill(self):
        try:
            tomcatStatus = subprocess.check_output(["systemctl", "is-active", self.serverVersion.name.lower()])
        except subprocess.CalledProcessError:
            tomcatStatus = 'inactive'
        status = ttk.Label(self)
        btn = ttk.Button(self)
        if(tomcatStatus == b"active\n"):
            status["text"] = f"{self.serverVersion.name} is running ..."
            btn["text"] = "Stop"
            btn["command"] = self.stopServer
        else:
            status["text"] = f"{self.serverVersion.name} is stopped"
            btn["text"] = "Start"
            btn["command"] = self.startServer

        status.pack()
        btn.pack()

    def startServer(self):
        subprocess.run(["systemctl", "start", self.serverVersion.name.lower()])
        self.reload()
    
    def stopServer(self):
        subprocess.run(["systemctl", "stop", self.serverVersion.name.lower()])
        self.reload()