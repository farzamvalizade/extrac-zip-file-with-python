from tkinter import *
import os
import zipfile
from tkinter.filedialog import askopenfilename,askdirectory

win=Tk()
win.minsize(200,200)
win.maxsize(200,200)
def extrac_file():
    save_dir=askdirectory()
    lbl_destination_adress['text']=save_dir
    if ent_folder_name.get()!="":
        file_name=ent_folder_name.get()
    else:
        file_name=os.path.basename(lbl_file_adress['text']).split(".")[0]
    with zipfile.ZipFile(lbl_file_adress['text'],mode='r') as result:
        result.extractall(os.path.join(save_dir,file_name))

extrac_btn=Button(win,text='Extract',command=extrac_file)
def open_file():
    filename=askopenfilename(title="Select zip file",filetypes=(("Zip File","*.zip"),("All file","*.*")))
    with zipfile.ZipFile(filename,mode="r") as archive:
       archive.printdir()
       lbl_file_adress['text']=filename
lbl_file_adress=Label(win)
lbl_destination_adress=Label(win)
lbl_file_adress.grid(row=1)
lbl_destination_adress.grid(row=2)

lbl_extract=Label(win,text="Enter Folder name")
lbl_extract.grid(row=3)
ent_folder_name=Entry(win)
ent_folder_name.grid(row=4)
extrac_btn.grid(row=5)
menu_bar=Menu(win)
file=Menu(menu_bar,tearoff=0)
menu_bar.add_cascade(label="File",menu=file)
file.add_command(label="Open",command=open_file)
win.config(menu=menu_bar)

win.mainloop()
