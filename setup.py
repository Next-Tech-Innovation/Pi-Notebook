
import cx_Freeze
import sys
import os

base =None

if sys.platform == "win32":
    base = "Win32GUI"

os.environ["TCL_LIBRARY"] = r"C:\Users\yogesh\AppData\Local\Programs\Python\Python310\tcl\tcl8.6"
os.environ["TK_LIBRARY"] = r"C:\Users\yogesh\AppData\Local\Programs\Python\Python310\tcl\tk8.6"

executable = [cx_Freeze.Executable(r"C:\Users\yogesh\Documents\texteditor_project\pienotebook.py",base=base, icon=r"C:\Users\yogesh\Documents\texteditor_project\pi.ico")]

cx_Freeze.setup(
    name = "Pi-NoteBook Text Editor",
    options = {"build_exe": {"packages": ["tkinter","os","fpdf"], "include_files": [r"C:\Users\yogesh\Documents\texteditor_project\pi.ico",r"C:\Users\yogesh\Documents\texteditor_project\tcl86t.dll",r"C:\Users\yogesh\Documents\texteditor_project\tk86t.dll",r"C:\Users\yogesh\Documents\texteditor_project\image"]}},
    version = "0.1",
    description = "Text Editor",
    executables = executable
)