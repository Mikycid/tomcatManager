from proc.compile import Compiler
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class Watcher:
    def __init__(self, directory, handler):
        self.observer = Observer()
        self.handler = handler
        self.directory = directory

    def run(self):
        print(self.observer.isAlive())
        print("running !")
        self.observer.schedule(
            self.handler, self.directory, recursive=True
        )
        self.observer.start()

    def stop(self):
        self.observer.stop()

class Handler(FileSystemEventHandler):
    def __init__(self, workingDir, deployPath, apiPath, console):
        super().__init__()
        self.compiler = Compiler(workingDir, deployPath, apiPath, console)

    def on_any_event(self,event):
        if event.is_directory or event.event_type == 'created' or event.src_path.endswith(".class"):
            return None
        elif event.event_type == 'modified':
            file:str = event.src_path
            if file.endswith(".java"):
                self.compiler.compile(file)
            else:
                self.compiler.warfile()
            self.deploy()
            print(event.src_path+" Modified !")

    def compile(self):
        self.compiler.compile()
    
    def deploy(self):
        self.compiler.deploy()
    
    def warfile(self):
        self.compiler.warfile()

    def compileAndDeploy(self):
        self.compiler.compileAndDeploy()

    