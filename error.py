from email import message
import tkinter as tk
from tkinter import messagebox

class Error(messagebox.Message):
    def __init__(self, e):
        root = tk.Tk()
        message = "Something went wrong when openning this application.\nExited with error : \n"+str(e)
        super().__init__(root, message=message)
        self.show()