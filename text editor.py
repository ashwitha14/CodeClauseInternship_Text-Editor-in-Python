import tkinter as tk
from tkinter import *
t=tk.Tk()
#t.resizable(False,False)
t.title("Text Editor")
selectmode=tk.StringVar()
file_name=tk.StringVar()
content=tk.StringVar()
t.geometry("900x600")
save_btn=""
def savefile():
    global saved_label,savefile_btn,fname_label,input_label,text
    fn=file_name.get()
    new_ctn=text.get(1.0, "end-1c")
    print(new_ctn)
    file= open(fn,"w")
    file.write(new_ctn)
    file.close()
    savefile_btn.destroy()
    text.destroy()
    saved_label=tk.Label(t,text="Your file has been saved",width=30,font=("Arial", 25) )
    saved_label.grid(row=2,column=1)
    fname_label.destroy()
    input_label.destroy()
def open_file():
    global save_btn,text,savefile_btn,fname_label
    fn=file_name.get()
    print(fn)
    file=open(fn,'r')
    fr=file.read()
    #open_entry=tk.Entry(t,textvariable=content)
    #open_entry.grid(row=3,column=1)
    text=tk.Text(t,width=65,height=30)
    text.insert("1.0",fr)
    text.grid(row=1,column=1,padx=20,pady=20)
    save_btn.destroy()
    input_entry.destroy()
    fname_label=tk.Label(t,text=f"Selected File : {fn}")
    fname_label.grid(row=0,column=3)
    savefile_btn=tk.Button(t,text="Save",command=savefile)
    savefile_btn.grid(row=2,column=0)
def create_file():
    global input_entry,text,savefile_btn,fname_label,save_btn
    fn=input_entry.get()
    file=open(fn,'w')
    fname_label=tk.Label(t,text=f"Selected File : {fn}")
    fname_label.grid(row=0,column=3)
    file.close()
    text=tk.Text(t,width=65,height=30)
    text.grid(row=1,column=1,padx=20,pady=20)
    savefile_btn=tk.Button(t,text="Save",command=savefile)
    savefile_btn.grid(row=2,column=0)
    save_btn.destroy()
    input_entry.destroy()
def okay_fun():
    global ok_btn,lines_label
    lines_label.destroy()
    ok_btn.destroy()
def word_count():
    global file_name,c,k_btn,lines_label,ok_btn
    fn=file_name.get()
    c=0
    ftext=open(fn,'r')
    fcont=ftext.read()
    lines=fcont.split()
    c=len(lines)
    lines_label=tk.Label(t,text=f"Number of words: {c}")
    lines_label.grid(row=1,column=1)
    ok_btn=tk.Button(t,text="Ok",command=okay_fun)
    ok_btn.grid(row=1,column=2)
    
def newfile(a):
    global save_btn,input_entry,input_label
    input_mode=selectmode.get()
    if input_mode=="Save":
        file.close()
    if input_mode=="New file":
         input_label=tk.Label(t,text="Enter file name: ")
         input_label.grid(row=1,column=1)
         input_entry=tk.Entry(t,textvariable=file_name)
         input_entry.grid(row=1,column=2)
         save_btn=tk.Button(t,text="Create",command=create_file)
         save_btn.grid(row=1,column=3)
    else:
        input_label=tk.Label(t,text="Enter file name: ")
        input_label.grid(row=1,column=1)
        input_entry=tk.Entry(t,textvariable=file_name)
        input_entry.grid(row=1,column=2)
        save_btn=tk.Button(t,text="Open",command=open_file)
        save_btn.grid(row=1,column=3)
exit_button=tk.Button(t,text="EXIT",width=10,command=t.destroy)
options=["New file","Open","Save"]
drop=tk.OptionMenu(t,selectmode,*options,command=newfile)
print(selectmode.get())
selectmode.set("File")
wcount_btn=tk.Button(t,text="Word Count",command=word_count)
wcount_btn.grid(row=0,column=1)
drop.grid(row=0,column=0)
exit_button.grid(row=44,column=3)
t.mainloop()
