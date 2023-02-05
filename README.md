# Pi-Notebook
Pi-NoteBook is a simple text editor make by using python tkinter Library.

# Preview

![Project 1 (2)](https://user-images.githubusercontent.com/83384315/216805993-f2ccf4fc-7420-4725-bd48-ee6055074707.jpg)

## Download Pi-Notebook from

[Visit](https://pi-notebook.netlify.app/)

# Docs

### Import Python libraries
```python
from tkinter import * 
from fpdf import FPDF
from PIL import Image , ImageTk
import tkinter as tk
from tkinter import BOTH, END, Canvas, Label, PhotoImage, ttk
from tkinter import font, colorchooser, filedialog, messagebox
import math
import random

import os
```
### Load tkinter
```python
main=tk.Tk()
main.wm_iconbitmap(r"pi.ico")
main.geometry('1000x400')
main.title('Pie Notebook text Editor')
```
 
 ### Main Menu
 ```python
 main_menu=tk.Menu()
file=tk.Menu(main_menu,tearoff=False)
```

### Tool bar
```python
tool_bar =ttk.Label(main)
tool_bar.pack(side=tk.TOP, fill=tk.X)
```

## Text Editor
```python
text_editor = tk.Text(main) # bg='black',fg='white'
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar = ttk.Scrollbar(main)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

add = PhotoImage(file=r"C:\Users\yogesh\Documents\texteditor_project\image\post-it.png")
text_editor.image_create(END,image=add)
```
### Font size and family functionlity
```python
current_font_family= 'Rage Italic'
current_font_size = 20
```
### Function to change the font
```python
def change_font(main):
    global current_font_family
    current_font_family = font_family.get()
    text_editor.configure(font=(current_font_family,current_font_size))

def change_size(main):
    global current_font_size
    current_font_size = size_var.get()
    text_editor.configure(font=(current_font_family,current_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)
font_size.bind("<<ComboboxSelected>>",change_size)
text_editor.configure(font=('Rage Italic',20))
```

### bold functionality 
```python
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)
```
### italic functionality 
```python
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))

italic_btn.configure(command=change_italic)
```
### underline functionality
```python
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['weight'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)
```
### change color functionality 
```python
def change_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

color_btn.configure(command=change_color)
```
### align left functionality
```python
def change_left():
    text_content = text_editor.get(1.0 ,'end')
    text_editor.tag_config('left' , justify=tk.LEFT)
    text_editor.delete(1.0 , tk.END)
    text_editor.insert(tk.INSERT , text_content , 'left')

left_btn.configure(command=change_left)
```
### align right functionality 
```python
def change_right():
    text_content = text_editor.get(1.0 ,'end')
    text_editor.tag_config('right' , justify=tk.RIGHT)
    text_editor.delete(1.0 , tk.END)
    text_editor.insert(tk.INSERT , text_content , 'right')

right_btn.configure(command=change_right)
```
### align center functionality
```python
def change_center():
    text_content = text_editor.get(1.0 ,'end')
    text_editor.tag_config('center' , justify=tk.CENTER)
    text_editor.delete(1.0 , tk.END)
    text_editor.insert(tk.INSERT , text_content , 'center')

center_btn.configure(command=change_center)
```
    
 ## STATUS BAR 
```python
status_bar =ttk.Label(main , text='Status Bar')
status_bar.pack(side=tk.BOTTOM)
```
### display count character anmd words
```python
text_change = False
def change(main):
    global text_change
    if text_editor.edit_modified():
        text_change = True
        words = len(text_editor.get(1.0 ,'end-1c').split())
        characters = len(text_editor.get(1.0 , 'end-1c').replace(' ',''))
        status_bar.config(text=f"characters : {characters} Words : {words}")
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",change)
```

