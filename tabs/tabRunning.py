from tkinter import ttk
from tabs.abstractTab import Tab
from proc.watch import Handler, Watcher

class TabRunning(Tab):
    def __init__(self, master, console):
        super().__init__(master)
        self.console = console
        self.handler = Handler(self.workingDir, self.deployPath, self.apiPath, console)
        self.watcher = Watcher(self.workingDir, self.handler)

        

    def fill(self):
        if(self.workingDir and self.apiPath):
            info = ttk.Label(self, text="Current running server : " + self.serverVersion.name + "\n Current project : " + self.workingDir.split("/")[-1])
            btnCompile = ttk.Button(self, text="Compile", command=self.handler.compile)
            btnDeploy = ttk.Button(self, text="Deploy", command=self.handler.deploy)
            btnBoth = ttk.Button(self, text="Compile & Deploy", command=self.handler.compileAndDeploy)
            if(self.watcher.observer.isAlive()):
                btnWatch = ttk.Button(self, text="Stop watching", command=self.stopWatcher)
            else:
                btnWatch = ttk.Button(self, text="Start watching", command=self.startWatcher)
            info.pack()
            btnCompile.pack()
            btnDeploy.pack()
            btnBoth.pack()
            btnWatch.pack()
        else:
            browseBtn = ttk.Label(self, text="\
                Directory path or server api jar path are not specifed. \n \
                Go to options tab and specify them.")
            browseBtn.pack()

    def reload(self):
        super().reload()
        self.handler = Handler(self.workingDir, self.deployPath, self.apiPath, self.console)
        self.watcher = Watcher(self.workingDir, self.handler)

    def startWatcher(self):
        self.watcher.run()
        self.reload()
    
    def stopWatcher(self):
        self.watcher.stop()
        self.reload()

    
    
    

    
            
