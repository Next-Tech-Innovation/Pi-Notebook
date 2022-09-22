# making by yogesh 😊

from tkinter import * 
from fpdf import FPDF
from PIL import Image , ImageTk
import tkinter as tk
from tkinter import BOTH, END, Canvas, Label, PhotoImage, ttk
from tkinter import font, colorchooser, filedialog, messagebox
import math
import random

import os
main=tk.Tk()
main.wm_iconbitmap(r"C:\Users\yogesh\Documents\texteditor_project\pi.ico")
# if "nt" == os.name:
#     main.wm_iconbitmap(bitmap="pi.ico")
# logo = PhotoImage(file=r'C:\Users\yogesh\Documents\texteditor_project\image\notebook-paper-1806473.jpg')

# main.tk.call('wm','iconphoto',main._w, logo)
# else:
#     main.wm_iconbitmap(bitmap="@pi.xbm")
main.geometry('1000x400')
main.title('                                                                                                                                                 Pie Notebook text Editor')

#====================================== MAIN MENU==============================================

main_menu=tk.Menu()

file=tk.Menu(main_menu,tearoff=False)



#==================================== TOOL BARS=============================================

#In tool bar we use font, bold,itali, underline etc
tool_bar =ttk.Label(main)
tool_bar.pack(side=tk.TOP, fill=tk.X)

### =========================== text hover tooltips ========================================
# class Tooltip(object):

#     def __init__(self,wigdet):
#         self.wigdet = wigdet
#         self.tipwindow = None
#         self.id = None
#         self.x = self.y = 0

#     def showtip(self ,text):
#         self.text = text
#         if self.tipwindow or not self.text:
#             return
#         x,y,cy = self.wigdet.bbox("insert")
#         x = x+self.wigdet.winfo_rootx()
#         y = y + cy +self.wigdet.winfo_rooty()
#         self.tipwindow = tw = Toplevel(self.wigdet)
#         tw.wm_overrideredirect(1)
#         tw.wm_geometry("+%d+%d" %(x,y))
#         label = Label(tw,text=self.text ,justify=left,background="#ffffe0" ,relief=SOLID , borderwidth=1)
#         label.pack(ipadx=1)

#     def hidetip(self):
#         tw = self.tipwindow
#         self.tipwindow = None
#         if tw:
#             tw.destroy()

# def createtooltip(wigdet ,text):
#     tooltip  = Tooltip(wigdet)
#     def enter(event):
#         tooltip.showtip(text)
#     def leave(event):
#         tooltip.hidetip()
#     wigdet.bind('<Enter>',enter)
#     wigdet.bind('<Leave>', leave)



#bold,italic,underine buttons
bold_img = tk.PhotoImage(file=r"C:\Users\yogesh\Documents\texteditor_project\image\bold-button2.png")
bold_btn = ttk.Button(tool_bar ,image=bold_img)
# createtooltip(bold_btn, text='Bold')
italic_img = tk.PhotoImage(file=r"C:\Users\yogesh\Documents\texteditor_project\image\italic2.png")
italic_btn = ttk.Button(tool_bar , image=italic_img)

underline_img = tk.PhotoImage(file=r"C:\Users\yogesh\Documents\texteditor_project\image\underline2.png")
underline_btn = ttk.Button(tool_bar, image=underline_img)

bold_btn.grid(row=0,column=0,padx=5)
italic_btn.grid(row=0,column=1,padx=5)
underline_btn.grid(row=0,column=2,padx=5)

#Align Button
left_img = tk.PhotoImage(file=r"C:\Users\yogesh\Documents\texteditor_project\image\align-left.png")
left_btn=ttk.Button(tool_bar, image=left_img)

center_img = tk.PhotoImage(file = r"C:\Users\yogesh\Documents\texteditor_project\image\center.png")
center_btn=ttk.Button(tool_bar, image=center_img)

right_img = tk.PhotoImage(file = r"C:\Users\yogesh\Documents\texteditor_project\image\align-right.png")
right_btn=ttk.Button(tool_bar, image=right_img)

left_btn.grid(row=0,column=3,padx=5)
center_btn.grid(row=0,column=4,padx=5)
right_btn.grid(row=0,column=5,padx=5)



font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='randomly')
font_box['values']=font_tuple
font_box.current(font_tuple.index('Rage Italic'))
font_box.grid(row=0,column=6,padx=5)


#Size Box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,80,2))  #(8,10,12,14,.....)
font_size.current(6)
font_size.grid(row=0,column=7,padx=5)

# color picker button
color_img = tk.PhotoImage(file=r"C:\Users\yogesh\Documents\texteditor_project\image\color.png")
color_btn = ttk.Button(tool_bar, image=color_img)
color_btn.grid(row=0, column=8, padx=5)

#=========================== Notebbok tab widget =====================================
# my_note = ttk.Notebook(main)
# my_note.pack(expand=1, fill=BOTH)

# #==== create tab =====
# def new_tab():
#     tab =ttk.Frame(my_note)
#     my_note.add(tab,text_edi)

#===================================== TEXT EDITOR ========================================

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

#==== Selected text =============
# sel = text_editor.get(tk.SEL_FIRST, tk.SEL_LAST)
# text_editor.insert(tk.END,sel)
# range = text_editor.tag_ranges(tk.SEL)
# if range:
#     print("slelcted text is %r" %text_editor.get(*range))
# content = text_editor.selection_get()

#======== Add image ======
# def insert_image():
#     yourimage = filedialog.askopenfilename(title="select your image ", filetypes=[("Image file","*.png"),("Image file","*.jpg")])
#     insert = ImageTk.PhotoImage(file=yourimage)
#     text_editor.image_create(1.0,image=insert)


def add_imag():
    # image = Image.open("image\header.png")
    # img = image.resize((e.width, e.height),Image.ANTIALIAS)
    img2= tk.PhotoImage(file=r"C:\Users\yogesh\Documents\texteditor_project\image\header.png",)
    text_editor.image_create(tk.END, image = img2)

text_editor.pack(pady=2)



# Font size and family functionlity
current_font_family= 'Rage Italic'
current_font_size = 20

# Function to change the font
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

###############  button function #########################
# print(tk.font.Font(font=text_editor['font']).actual())
# {'family': 'Rage Italic', 'size': 20, 'weight': 'normal', 'slant': 'roman', 'underline': 0, 'overstrike': 0}

# ===== bold functionality ======
def change_bold():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight'] == 'normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight'] == 'bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

bold_btn.configure(command=change_bold)

# ====== italic functionality ==========
def change_italic():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant'] == 'roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))
    if text_property.actual()['slant'] == 'italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))

italic_btn.configure(command=change_italic)

#====== underline functionality =========
def change_underline():
    text_property = tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['weight'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

underline_btn.configure(command=change_underline)

# ====== chanee color functionality ===========
def change_color():
    color_var = tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

color_btn.configure(command=change_color)

# ===== align left functionality ========
def change_left():
    text_content = text_editor.get(1.0 ,'end')
    text_editor.tag_config('left' , justify=tk.LEFT)
    text_editor.delete(1.0 , tk.END)
    text_editor.insert(tk.INSERT , text_content , 'left')

left_btn.configure(command=change_left)

# ====== align right functionality =======
def change_right():
    text_content = text_editor.get(1.0 ,'end')
    text_editor.tag_config('right' , justify=tk.RIGHT)
    text_editor.delete(1.0 , tk.END)
    text_editor.insert(tk.INSERT , text_content , 'right')

right_btn.configure(command=change_right)

# ===== align center functionality ======
def change_center():
    text_content = text_editor.get(1.0 ,'end')
    text_editor.tag_config('center' , justify=tk.CENTER)
    text_editor.delete(1.0 , tk.END)
    text_editor.insert(tk.INSERT , text_content , 'center')

center_btn.configure(command=change_center)

    
 #=================================== STATUS BAR ===========================================

status_bar =ttk.Label(main , text='Status Bar')
status_bar.pack(side=tk.BOTTOM)

# ===== display count character anmd words ========
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




#=================================== FUNCTION MENU =====================================

# ===== new file functionality ======
file_path = ''
def new_file(event=None):
    global file_path
    file_path = ''
    text_editor.delete(1.0 , tk.END)

# ===== open file functionality ======
def open_file(event=None):
    global file_path
    if file_path:
        with open(file_path,'r') as fr:
            text_editor.insert(1.0 , fr.read())
    file_path = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select file' , filetypes=(('Text File', '*.txt'),('All Files','*.*')))
    try:
        with open(file_path,'r') as fr:
            text_editor.delete(1.0 , tk.END)
            text_editor.insert(1.0 , fr.read())

            # v1 = pdf.ShowPdf()
            # v2= v1.pdf_view()
            # text_editor.insert(1.0, v2)
            # if file_path:
            #     pdf_file = pdf.PdfFileReader(file_path)
            #     page =pdf_file.getPage(0)
            #     page_stuff = page.extractText() 
            #     text_editor.insert(1.0, page_stuff)
    except FileNotFoundError:
        return
    except:
        return
    main.title(os.path.basename(file_path))

# ====== save file functionality ======= 
def save_file(event=None):
    global file_path
    try:
        if file_path:
            content = str(text_editor.get(1.0 ,tk.END))
            with open(file_path,'w', encoding='utf8') as fw:
                fw.write(content)
        else:
            file_path = filedialog.asksaveasfile(mode= 'w' , defaultextension='.txt' ,filetypes=(('Text File', '*.txt'),('All Files','*.*')))
            content2 = text_editor.get(1.0, tk.END)
            file_path.write(content2)
            file_path.close()
    except:
        return
    
# ===== save as file functionality ========
def saveas_file(event=None):
    global file_path
    try:
        content = text_editor.get(1.0, tk.END)
        file_path = filedialog.asksaveasfile(mode= 'w' , defaultextension='.txt' ,filetypes=(('Text File', '*.txt'),('All Files','*.*')))
        file_path.write(content)
        file_path.close()
    except:
        return 

# ======= exit functionality ========
def exit_file(event=None):
    global file_path , text_change
    try:
        if text_change:
            if file_path:
                main.destroy()
            else:
                message = messagebox.askyesnocancel('Pie-Notebook', 'Do you want to save the file ?')
                if message is True:
                    if file_path:
                        content = text_editor.get(1.0 , tk.END)
                        with open(file_path ,'w', encoding='utf-8') as fw:
                            fw.write(content)
                            main.destroy()
                    else:
                        content2 = str(text_editor.get(1.0 , tk.END))
                        file_path = filedialog.asksaveasfile(mode= 'w' , defaultextension='.txt' ,filetypes=(('Text File', '*.txt'),('All Files','*.*')))
                        file_path.write(content2)
                        file_path.close()
                        main.destroy()

                elif message is False:
                    main.destroy()
        else:
            main.destroy()
    except:
        return
    

main.protocol("WM_DELETE_WINDOW", exit_file)
# ======== print file ====== 
def print_file(event=None):
    global file_path
    pdf  = FPDF()
    pdf.add_page()
    pdf.set_font("Arial",size=18)
    if file_path:
        f =open(file_path,'r')
        for x in f:
            pdf.cell(200,10,txt=x, ln=1,align='L')
        pdf.output(file_path +'.pdf')
        messagebox.askokcancel("Pi-NoteBook", "PDF file saved.")
    else:
        message = messagebox.askokcancel("Pi-Notebook","You must save file to convert into pdf.")
        if message:
            save_file()
    
    # mess = messagebox.OK("Pi-NoteBook", "Your text file is converted into pdf.")
    # if mess:
    #     return

#===== Recent file ========
# def recent_file(event=None):
#     global file_path

  

# Add dropdown

file.add_command(label='New File',compound=tk.LEFT,accelerator='ctrl+N',command=new_file)
file.add_separator()
# file.add_command(label='New File',compound=tk.LEFT,accelerator='ctrl+N',command=new_file)
# file.add_separator()
file.add_command(label='Open File',compound=tk.LEFT,accelerator='ctrl+O',command=open_file)
file.add_separator()
file.add_command(label='Save File',compound=tk.LEFT,accelerator='ctrl+S',command=save_file)
file.add_separator()
file.add_command(label='Save As',compound=tk.LEFT,accelerator='ctrl+Alt+S',command=saveas_file)
file.add_separator()
# file.add_command(label='Recent',compound=tk.LEFT,accelerator='ctrl+Alt+R',command=recent_file)
# # sep = ttk.Separator(file,orient='horizontal')
# # sep.place(relx=0, rely=0.47, relheight=1, relwidth=1)
# file.add_separator()
file.add_command(label='Convert into PDF',compound=tk.LEFT,accelerator='ctrl+P',command=print_file)
file.add_separator()
file.add_command(label='Exit',compound=tk.LEFT,accelerator='ctrl+Q', command=exit_file)



edit=tk.Menu(main_menu,tearoff=False)


# ==== find functionality ============
def find_only(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos =f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos =end_pos
                text_editor.tag_config('match', foreground='red', background='')

    global file_path
    #open find window.....
    find_window = tk.Toplevel()
    find_window.geometry('450x250+500+200')
    find_window.title("Find")
    find_window.resizable(0,0)

    #  frame create....
    find_frame = ttk.LabelFrame(find_window,text='Find/Replace')
    find_frame.pack(pady=20)

    ### label create...
    find_label = ttk.Label(find_frame, text='Find : ')

    ##  Entry/input box for find / replace.....
    find_input = ttk.Entry(find_frame , width=30)

    ##  Button create...
    find_button = ttk.Button(find_frame, text='Find',command=find)
    

    find_label.grid(row=0,column=0, padx=4, pady=4)
    find_input.grid(row=0,column=1,padx=4,pady=4)
    find_button.grid(row=2,column=0,padx=8,pady=8)
    find_window.mainloop()

#====== find and replace functionality ==========
def find_func(event=None):

    def find():
        word = find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches = 0
        if word:
            start_pos = '1.0'
            while True:
                start_pos = text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos =f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos =end_pos
                text_editor.tag_config('match', foreground='green', background='gray')

    def replace():
        word = find_input.get()
        replace_text = replace_input.get()
        content = text_editor.get(1.0,tk.END)
        new_content = content.replace(word, replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)

    global file_path
    #open find window.....
    find_window = tk.Toplevel()
    find_window.geometry('450x250+500+200')
    find_window.title("Find")
    find_window.resizable(0,0)

    #  frame create....
    find_frame = ttk.LabelFrame(find_window,text='Find/Replace')
    find_frame.pack(pady=20)

    ### label create...
    find_label = ttk.Label(find_frame, text='Find : ')
    replace_label = ttk.Label(find_frame,text='Repalce :')

    ##  Entry/input box for find / replace.....
    find_input = ttk.Entry(find_frame , width=30)
    replace_input = ttk.Entry(find_frame, width=30)

    ##  Button create...
    find_button = ttk.Button(find_frame, text='Find',command=find)
    replace_button = ttk.Button(find_frame , text='Replace',command= replace)
    

    find_label.grid(row=0,column=0, padx=4, pady=4)
    replace_label.grid(row=1,column=0,padx=4,pady=4)
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)
    find_button.grid(row=2,column=0,padx=8,pady=8)
    replace_button.grid(row=2,column=1,padx=8,pady=8)

    find_window.mainloop()


# Add Dropdown 
edit.add_command(label='Undo',compound=tk.LEFT,accelerator='ctrl+Z',command=lambda : text_editor.event_generate("<Control z>"))
edit.add_separator()
edit.add_command(label='Redo',compound=tk.LEFT,accelerator='ctrl+Y',command=lambda : text_editor.event_generate("<Control y>"))
edit.add_separator()
edit.add_command(label='Copy',compound=tk.LEFT,accelerator='ctrl+C',command=lambda : text_editor.event_generate("<Control c>"))
edit.add_separator()
edit.add_command(label='Cut',compound=tk.LEFT,accelerator='ctrl+X',command=lambda : text_editor.event_generate("<Control x>"))
edit.add_separator()
edit.add_command(label='Paste',compound=tk.LEFT,accelerator='ctrl+V',command=lambda : text_editor.event_generate("<Control v>"))
edit.add_separator()
edit.add_command(label='Find',compound=tk.LEFT,accelerator='ctrl+F',command=find_only)
# edit.add_separator()
# edit.add_command(label='Insert image',compound=tk.LEFT,accelerator='ctrl+I',command=insert_image)
edit.add_separator()
edit.add_command(label='Replace',compound=tk.LEFT,accelerator='ctrl+H',command=find_func)
edit.add_separator()
edit.add_command(label='Clear All',compound=tk.LEFT,accelerator='ctrl+Alt+X',command=lambda : text_editor.delete(1.0,tk.END))


view=tk.Menu(main_menu,tearoff=False)

# ==== view check functionalityb ====
show_status = tk.BooleanVar()
show_status.set(True)
show_tool = tk.BooleanVar()
show_tool.set(True)
fullscreen = tk.BooleanVar()
fullscreen.set(False)
dark = tk.BooleanVar()
dark.set(True)

def hide_tool():
    global show_tool
    if show_tool:
        tool_bar.pack_forget()
        show_tool = False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP ,fill=tk.X)
        text_editor.pack(fill=tk.BOTH ,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_tool=True

def hide_status():
    global show_status
    if show_status:
        status_bar.pack_forget()
        show_status=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_status=True

def no_fullscreen():
    global fullscreen
    if fullscreen:
        main.attributes('-fullscreen',True)
        fullscreen = False
    else:
        main.wm_geometry('1000x400')
        fullscreen = True

def dark_theme():
    global dark
    if dark:
        text_editor.configure(bg='black',fg='white',insertbackground='white')
        tool_bar.configure(background='black')

        dark = False
    else:
        text_editor.config(bg='white',fg='black',insertbackground='black')
        tool_bar.configure(background='white')
        dark = True
# Dropdown
view.add_checkbutton(label='Light Themes', onvalue=True, offvalue=False, variable=dark, compound=tk.LEFT, command=dark_theme)
view.add_checkbutton(label='Full Screen',onvalue=True, offvalue=False, variable=fullscreen, compound=tk.LEFT,command=no_fullscreen, accelerator='F11')
view.add_separator()
view.add_checkbutton(label='Tool Bar',onvalue =True ,offvalue=False,variable=show_tool, compound=tk.LEFT,accelerator='Ctr+Alt+F11',command=hide_tool)
view.add_separator()
view.add_checkbutton(label='Status Bar',onvalue=True , offvalue=False, variable=show_status, compound=tk.LEFT,accelerator='Ctr+shift+F11',command=hide_status)

#=========================== Draw menu ===================================

# draw = tk.Menu(main_menu,tearoff=False)

# # ======= Pencil Functionality ========

# class Paint(object):

#     DEFAULT_PEN_SIZE = 5.0
#     DEFAULT_COLOR = 'black'

#     def __init__(self):
#         self.root = text_editor
#         # def pen(self):
#         self.pen_button = Button(self.root, text='pen', command=self.use_pen)
#         self.pen_button.grid(row=0, column=0)

#         self.brush_button = Button(self.root, text='brush', command=self.use_brush)
#         self.brush_button.grid(row=0, column=1)

#         self.color_button = Button(self.root, text='color', command=self.choose_color)
#         self.color_button.grid(row=0, column=2)

#         self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
#         self.eraser_button.grid(row=0, column=3)

#         self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
#         self.choose_size_button.grid(row=0, column=4)

#         self.c = Canvas(self.root, bg='#000000', width=600, height=600)
#         self.c.grid(row=1, columnspan=5)
#         label = tk.Label(self.c,borderwidth=0,bg='#000000')
#         self.root.overrideredirect(True)
#         self.root.wm_attributes('-transparentcolor','#000000')
#         self.root.wm_attributes('-topmost', True)
#         self.c.create_window(0, 0, anchor=tk.NW, window=label)
#         self.setup()
#         self.root.mainloop()

#     def setup(self):
#         self.old_x = None
#         self.old_y = None
#         self.line_width = self.choose_size_button.get()
#         self.color = self.DEFAULT_COLOR
#         self.eraser_on = False
#         self.active_button = self.pen_button
#         self.c.bind('<B1-Motion>', self.paint)
#         self.c.bind('<ButtonRelease-1>', self.reset)

#     def use_pen(self):
#         self.activate_button(self.pen_button)

#     def use_brush(self):
#         self.activate_button(self.brush_button)

#     def choose_color(self):
#         self.eraser_on = False
#         self.color = colorchooser.askcolor(color=self.color)[1]

#     def use_eraser(self):
#         self.activate_button(self.eraser_button, eraser_mode=True)

#     def activate_button(self, some_button, eraser_mode=False):
#         self.active_button.config(relief=RAISED)
#         some_button.config(relief=SUNKEN)
#         self.active_button = some_button
#         self.eraser_on = eraser_mode

#     def paint(self, event):
#         self.line_width = self.choose_size_button.get()
#         paint_color = 'white' if self.eraser_on else self.color
#         if self.old_x and self.old_y:
#             self.c.create_line(self.old_x, self.old_y, event.x, event.y,
#                                width=self.line_width, fill=paint_color,
#                                capstyle=ROUND, smooth=TRUE, splinesteps=36)
#         self.old_x = event.x
#         self.old_y = event.y

#     def reset(self, event):
#         self.old_x, self.old_y = None, None


# if __name__ == '__main__':
#     Paint()

#======= pen functionality ============
# def pen():
#     # def draw(event):
#     pass
        

# #======== shapes Functionality ========
# def shapes():
#     pass
#Dropdown
# draw.add_command(label='Pencil',compound=tk.RIGHT,accelerator='ctrl+shift+P',command=Paint)
# draw.add_separator()
# draw.add_command(label='Pen',compound=tk.LEFT,accelerator='ctrl+shift+L',command=pen)
# draw.add_separator()
# draw.add_command(label='Shapes',compound=tk.LEFT,accelerator='ctrl+shift+G',command=shapes)

help=tk.Menu(main_menu,tearoff=False)


#====== about functionlaity ===========
# def about():
#     logo_img =tk.PhotoImage(file="image\mylogo.ico")
#     about_window = tk.Toplevel(main)
#     about_window.geometry('450x250+500+200')
#     about_window.title("About Pi-Notebook")
#     about_window.resizable(0,0)
#     Label(about_window,text="Name : pi-NoteBook TextEditor\n version : 0.0.1 \n @2022 NEXT TECHOLOGY Foundation pvt.")
#     about_window.mainloop()
def open_popup():
    messagebox.showinfo('Pie-Notebook', "Name : Pi-NoteBook TextEditor\n version : 0.0.1 \n @2022 \n NEXT TECH. INNOVATION ")
#    top= Toplevel(main)
#    top.geometry("450x250")
#    top.title("About Pi-Notebook")
#    label(text="Name : pi-NoteBook TextEditor\n version : 0.0.1 \n @2022 NEXT TECHOLOGY Foundation pvt.", font=('Arial')).place(x=0,y=0)


#Dropdown
# help.add_command(label='Get Started',compound=tk.LEFT)
# help.add_separator()
# help.add_command(label='Documentation',compound=tk.LEFT)
# help.add_separator()
help.add_command(label='Send Feedback',compound=tk.LEFT)
help.add_separator()
help.add_command(label='About Pi-Notebook',compound=tk.LEFT,command=open_popup)



#cascade in main
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
# main_menu.add_cascade(label='Draw', menu=draw)
main_menu.add_cascade(label='Help', menu=help)




main.config(menu=main_menu)
main.bind("<Control-n>",new_file)
main.bind("<Control-o>",open_file)
main.bind("<Control-s>",save_file)
main.bind("<Control-Alt-s>",saveas_file)
main.bind("<Control-q>",exit_file)
main.bind("<Control-f>",find_only)
main.bind("<Control-h>",find_func)

# ------it transparent background ------
# main.wm_attributes("-transparentcolor",'white')
main.mainloop()