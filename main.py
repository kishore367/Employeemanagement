from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Database

db=Database("Employee.db")

root=Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="black")
root.state("zoomed")

name=StringVar()
age=StringVar()
doj=StringVar()
gender=StringVar()
email=StringVar()
contact=StringVar()

#Entry Frame
entries_frame=Frame(root,bg="grey")
entries_frame.pack(side=TOP,fill=X)
title=Label(entries_frame,text="Employee Management System",font=("Calibri",18,"bold"),bg="grey",fg="black")
title.grid(row=0,columnspan=2,padx=10,pady=20)

LBLname=Label(entries_frame,text="Name",font=("Calibri",12),bg="grey",fg="black")
LBLname.grid(row=1,column=0,padx=10,pady=10,sticky="w")
txtName=Entry(entries_frame,textvariable=name,font=("Calibri",12),width=30)
txtName.grid(row=1,column=1,padx=10,pady=10,sticky="w")

LBLage=Label(entries_frame,text="Age",font=("Calibri",12),bg="grey",fg="black")
LBLage.grid(row=1,column=2,padx=10,pady=10,sticky="w")
txtAge=Entry(entries_frame,textvariable=age,font=("Calibri",12),width=30)
txtAge.grid(row=1,column=3,padx=10,pady=10,sticky="w")

LBLDOJ=Label(entries_frame,text="D.O.J",font=("Calibri",12),bg="grey",fg="black")
LBLDOJ.grid(row=2,column=0,padx=10,pady=10,sticky="w")
txtDOJ=Entry(entries_frame,textvariable=doj,font=("Calibri",12),width=30)
txtDOJ.grid(row=2,column=1,padx=10,pady=10,sticky="w")

LBLmail=Label(entries_frame,text="Email",font=("Calibri",12),bg="grey",fg="black")
LBLmail.grid(row=2,column=2,padx=10,pady=10,sticky="w")
txtmail=Entry(entries_frame,textvariable=email,font=("Calibri",12),width=30)
txtmail.grid(row=2,column=3,padx=10,pady=10,sticky="w")

LBLgen=Label(entries_frame,text="Gender",font=("Calibri",12),bg="grey",fg="black")
LBLgen.grid(row=3,column=0,padx=10,pady=10,sticky="w")
comboGen=ttk.Combobox(entries_frame,font=("Calibri",12),width=30,textvariable=gender,state="readonly")
comboGen['values']=("Male","Female")
comboGen.grid(row=3,column=1,padx=10,sticky="w")

LBLcon=Label(entries_frame,text="Contact NO",font=("Calibri",12),bg="grey",fg="black")
LBLcon.grid(row=3,column=2,padx=10,pady=10,sticky="w")
txtcon=Entry(entries_frame,textvariable=contact,font=("Calibri",12),width=30)
txtcon.grid(row=3,column=3,padx=10,pady=10,sticky="w")

LBLadd=Label(entries_frame,text="Address",font=("Calibri",12),bg="grey",fg="black")
LBLadd.grid(row=4,column=0,padx=10,pady=10,sticky="w")
txtAdd=Text(entries_frame,width=85,height=5,font=("Calibri",12))
txtAdd.grid(row=5,column=0,columnspan=4,padx=10,sticky="w")

def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row =data["values"]
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    gender.set(row[5])
    email.set(row[4])
    contact.set(row[6])
    txtAdd.delete(1.0, END)
    txtAdd.insert(END,row[7])

def display_all():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert("",END,values=row)
def add_employee():
    if txtName.get()==""  or txtAge.get()=="" or comboGen.get()=="" or txtDOJ.get()=="" or txtcon.get()=="" or txtmail.get()=="" or txtAdd.get(1.0,END)=="":
        messagebox.showerror("Error in Input","Please Fill All the Datails!")
        return
    db.insert(txtName.get(),txtAge.get(),txtDOJ.get(),txtmail.get(),comboGen.get(),txtcon.get(),txtAdd.get(1.0,END))
    messagebox.showinfo("SUCCESS!","Record Inserted")
    clear_employee()
    display_all()

def edit_employee():
    if txtName.get() == "" or txtAge.get() == "" or comboGen.get() == "" or txtDOJ.get() == "" or txtcon.get() == "" or txtmail.get() == "" or txtAdd.get(
            1.0, END) == "":
        messagebox.showerror("Error in Input", "Please Fill All the Datails!")
        return
    db.update(row[0],txtName.get(), txtAge.get(), txtDOJ.get(), txtmail.get(), comboGen.get(), txtcon.get(),
              txtAdd.get(1.0, END))
    messagebox.showinfo("SUCCESS!", "Record Updated")
    clear_employee()
    display_all()

def del_employee():
    db.delete(row[0])
    clear_employee()
    display_all()

def clear_employee():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    txtAdd.delete(1.0,END)

btn_frame=Frame(entries_frame,bg="grey")
btn_frame.grid(row=6,column=0,columnspan=4,padx=10,pady=10,sticky="w")
btnAdd = Button(btn_frame, command=add_employee, text="Add Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                bg="#16a085", bd=0).grid(row=0, column=0)
btnEdit = Button(btn_frame, command=edit_employee, text="Update Details", width=15, font=("Calibri", 16, "bold"),
                 fg="white", bg="#2980b9",
                 bd=0).grid(row=0, column=1, padx=10)
btnDelete = Button(btn_frame, command=del_employee, text="Delete Details", width=15, font=("Calibri", 16, "bold"),
                   fg="white", bg="#c0392b",
                   bd=0).grid(row=0, column=2, padx=10)
btnClear = Button(btn_frame, command=clear_employee, text="Clear Details", width=15, font=("Calibri", 16, "bold"), fg="white",
                  bg="#f39c12",
                  bd=0).grid(row=0, column=3, padx=10)
#TableFrame
tree_frame=Frame(root,bg="white")
tree_frame.place(x=0,y=400,width=1600,height=520)
style=ttk.Style()
style.configure("mystyle.Treeview",font=("Callibri",12),rowheight=50)
style.configure("mystyle.Treeview.Heading",font=('Calibri',16))
tv=ttk.Treeview(tree_frame,columns=(1,2,3,4,5,6,7,8),style="mystyle.Treeview")
tv.heading("1",text="ID")
tv.column("1",width=1)
tv.heading("2",text="NAME")
tv.heading("3",text="AGE")
tv.column("3",width=2)
tv.heading("4",text="D.O.J")
tv.column("4",width=5)
tv.heading("5",text="Email")
tv.heading("6",text="GENDER")
tv.column("6",width=5)
tv.heading("7",text="Contact")
tv.column("7",width=10)
tv.heading("8",text="Address")
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.pack(fill=X)

display_all()
root.mainloop()