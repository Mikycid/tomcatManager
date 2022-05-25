import subprocess
import os
import sys

class Compiler:

    def __init__(self, workingDir, deployPath, apiPath, console):
        self.workingDir = workingDir
        self.apiPath = apiPath
        self.deployPath = deployPath
        self.console = console

    def compile(self, file=False):
        path = "/".join(sys.argv[0].split("/")[:-1])
        path = os.path.join(path,'systemScripts/jee-compiler')
        file = file.split("/")[-1] if file else "all"
        output = subprocess.check_output([path, self.workingDir, self.apiPath, file])
        self.console.write(output.decode('utf-8'))

    def deploy(self):
        path = "/".join(sys.argv[0].split("/")[:-1])
        path = os.path.join(path,'systemScripts/jee-deploy')
        output = subprocess.check_output([path, self.deployPath, self.workingDir.split("/")[-1]])
        self.console.write(output.decode('utf-8'))

    def warfile(self):
        path = "/".join(sys.argv[0].split("/")[:-1])
        path = os.path.join(path,'systemScripts/jee-create-war-file')
        output = subprocess.check_output([path, self.workingDir])
        self.console.write(output.decode('utf-8'))

    def compileAndDeploy(self):
        self.compile()
        self.deploy()