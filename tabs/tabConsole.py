from ctypes import alignment
import tkinter as tk
from tkinter import ttk
from lib.scrollableFrame import ScrollFrame
from tabs.abstractTab import Tab

class TabConsole(Tab):

    def __init__(self, master):
        super().__init__(master)
        self.frame = ScrollFrame(self)

    def fill(self):
        self.frame.pack(fill="both", expand=True)

    def write(self, text):
        text = tk.Label(self.frame.viewPort,  fg="white", bg="black", text="$ "+text, anchor='w', justify="left")
        text.pack(fill="both")