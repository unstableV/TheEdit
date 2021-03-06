from tkinter import *
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter.filedialog import askopenfile
import tkinter

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)
 
def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()
 
def saveAs():
    f = asksaveasfile(defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oh No!", message="Unable to save file...")
 
root = Tk()

root.option_add("*background", "BLACK")
       
def openFile():
    global filename
    file = askopenfile(parent=root,title='Select a File')
    filename = file.name
    t = file.read()
    text.delete(0.0, END)
    text.insert(0.0, t)
    file.close()
 
 
 
root.title("TheEdit")
root.resizable(True,True) 
text = Text(root, width=400, height=400, fg = 'yellow' )

text.pack()
	
	
 
menubar = Menu(root, background='#374140', foreground='white',
activebackground='#374140', activeforeground='white')
filemenu = Menu(menubar,background='#374140', foreground='white',
activebackground='#374140', activeforeground='white')
filemenu.add_command(label="New", command=newFile)
filemenu.add_command(label="Open", command=openFile)
filemenu.add_command(label="Save", command=saveFile)
filemenu.add_command(label="Save As", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
	
root.config(menu=menubar)

root.mainloop()
