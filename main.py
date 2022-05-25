from app import App
from error import Error
import os
"""
if __name__ == "__main__":
    try:
        os.chdir('/usr/share/tomcatManager')
        app = App()
        app.mainloop()
    except Exception as e:
        app = Error(e)
"""

if __name__ == "__main__":
        app = App()
        app.mainloop()