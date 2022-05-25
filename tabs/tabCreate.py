from tkinter import ttk
from tkinter import filedialog
import tkinter as tk
from tabs.abstractTab import Tab
import os
import subprocess
import sys

class TabCreate(Tab):
    def __init__(self, master):
        super().__init__(master)
        self.tk.call('tk', 'scaling', 2.0)
        self.input = ttk.Entry(self)
        self.path = ttk.Label(self, text="No directory specified")
        self.setAsCurrentProject = tk.BooleanVar()
        

    def fill(self):
        
        label = ttk.Label(self, text="Name : ")
        browse = ttk.Button(self, text="Choose", command=self.setDirectory)

        setAsCurrentProjectBtn = ttk.Checkbutton(self, text="Set as current project", variable=self.setAsCurrentProject)
        button = ttk.Button(self, text="Create", command=self.createProject)

        label.grid(row=0,column=0)
        self.input.grid(row=0,column=1)
        browse.grid(row=1, column=0)
        self.path.grid(row=1, column=1)
        setAsCurrentProjectBtn.grid(row=2, columnspan=2)
        button.grid(row=3, columnspan=2, rowspan=2)
        self.grid_columnconfigure((0,1), weight=1)

    def setDirectory(self):
        path = filedialog.askdirectory()
        self.path["text"] = path

    def createProject(self):
        if self.path["text"] == "" or self.input.get() == "":
            return
        path = os.path.join(self.path["text"],self.input.get())
        sPath = os.path.abspath(sys.argv[0])
        sPath = os.path.join("/".join(sPath.split('/')[:-1]), "systemScripts/jee-create-project")
        subprocess.run([sPath, path])
        if(self.setAsCurrentProject.get()):
            self.master.setWorkingDir(path)
