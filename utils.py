from enum import Enum

class ServerVersions(Enum):
    TOMCAT9 = 0
    TOMCAT10 = 1

class Tabs(Enum):
    CREATE = 0
    RUN = 1
    OPTIONS = 2
    SERVER = 3
    CONSOLE = 4
