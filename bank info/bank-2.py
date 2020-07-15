from tkinter import *
from tkinter import Tk,StringVar,ttk
from tkinter import messagebox
import tkinter.messagebox as tkMessageBox
import tkinter as tk
import sqlite3 as mycon

root=Tk()
root.geometry("520x520+0+0")
root.title("BANK")
root.configure(background='white')

#-----------variables--------------

var1=StringVar()
var1.set('')
acc_no=IntVar()
c_name=StringVar()
c_no=IntVar()
c_add=StringVar()
acc_type=StringVar()
bal=StringVar()


Tops=Frame(root,width=560,height=10,bd=14,relief='raise')
Tops.pack(side=TOP)
Bottom=Frame(root,width=260,height=10,bd=14,relief='raise')
Bottom.pack(side=BOTTOM)

Tops.configure(background="light blue")
Bottom.configure(background="light blue")


#------------------------insert-----------
def UpdateData():
    if acc_no.get() == "":
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        tree2.delete(*tree2.get_children())
        conn = sqlite3.connect("bank.db")
        cursor = conn.cursor()
        cursor.execute("UPDATE `cust_det` SET `acc_no` = ?, `c_name` = ?, `c_no` =?, `c_add` = ? WHERE `mem_id` = ?", (str(acc_no.get()), str(c_name.get()), str(c_no.get()), str(c_add.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `cust_det` ORDER BY `c_name` ASC")
        fetch2 = cursor.fetchall()
        for data2 in fetch2:
            tree2.insert('', 'end', values=(data2))
        cursor.close()
        conn.close()
        acc_no.set("")
        c_name.set("")
        c_no.set("")
        c_add.set("")

def AddNew():
    global NewWindow
    acc_no.set("")
    c_name.set("")
    c_no.set("")
    c_add.set("")
    NewWindow = Toplevel()
    NewWindow.title("Cust_Entry")
    width = 400
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
    #===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Cust_Entry", font=('arial', 16), bg="#66ff66",  width = 300)
    lbl_title.pack(fill=X)
    lbl_name = Label(ContactForm, text="Acc_no", font=('arial', 14), bd=5)
    lbl_name.grid(row=0, sticky=W)
    lbl_age = Label(ContactForm, text="C_Name", font=('arial', 14), bd=5)
    lbl_age.grid(row=1, sticky=W)
    lbl_tickets = Label(ContactForm, text="C_No", font=('arial', 14), bd=5)
    lbl_tickets.grid(row=2, sticky=W)
    lbl_ticket_id = Label(ContactForm, text="C_Add", font=('arial', 14), bd=5)
    lbl_ticket_id.grid(row=3, sticky=W)
    #===================ENTRY===============================
    name = Entry(ContactForm, textvariable=acc_no, font=('arial', 14))
    name.grid(row=0, column=1)
    age = Entry(ContactForm, textvariable=c_name, font=('arial', 14))
    age.grid(row=1, column=1)
    tickets = Entry(ContactForm, textvariable=c_no, font=('arial', 14))
    tickets.grid(row=2, column=1)
    ticket_id = Entry(ContactForm, textvariable=c_add,  font=('arial', 14))
    ticket_id.grid(row=3, column=1)
    #==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="Save", width=50, command=SubmitData1)
    btn_addcon.grid(row=6, columnspan=2, pady=10)
    
def SubmitData1():
    if  acc_no.get() == "" or c_name.get() == "" or c_no.get() == "" or c_add.get() == "" :
        result = tkMessageBox.showwarning('', 'Please Complete The Required Field', icon="warning")
    else:
        for i in tree2.get_children():
                tree2.delete(i)
        conn = mycon.connect("bank.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO `cust_det` (acc_no, c_name, c_no, c_add) VALUES(?, ?, ?, ?)", (str(acc_no.get()), str(c_name.get()), str(c_no.get()), str(c_add.get())))
        conn.commit()
        cursor.execute("SELECT * FROM `cust_det` ORDER BY `c_name` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree2.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        acc_no.set("")
        c_name.set("")
        c_no.set("")
        c_add.set("")


#------------------------------------------
def Find():
    global NewWindow
    acc_no.set("")
    NewWindow = Toplevel()
    NewWindow.title("Find_Cust")
    width =600
    height = 600
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) - 455) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    NewWindow.resizable(0, 0)
    NewWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'UpdateWindow' in globals():
        UpdateWindow.destroy()
    #===================FRAMES==============================
    FormTitle = Frame(NewWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(NewWindow)
    ContactForm.pack(side=TOP, pady=10)
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Find_Cust", font=('arial', 16), bg="#66ff66",  width = 300)
    lbl_title.pack(fill=X)
    lbl_name = Label(ContactForm, text="Acc_no", font=('arial', 14), bd=5)
    lbl_name.grid(row=0, sticky=W)
#     lbl_age = Label(ContactForm, text="C_Name", font=('arial', 14), bd=5)
#     lbl_age.grid(row=1, sticky=W)
    #===================ENTRY===============================
    name = Entry(ContactForm, textvariable=acc_no, font=('arial', 14))
    name.grid(row=0, column=1)
#     age = Entry(ContactForm, textvariable=c_name, font=('arial', 14))
#     age.grid(row=1, column=1)
    
    
    def SubmitData2():
        for i in tree.get_children():
            tree.delete(i)
        conn = mycon.connect("bank.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cust_det c NATURAL JOIN bank_det d  WHERE acc_no= "+(str(acc_no.get())))
        conn.commit()
        fetch = cursor.fetchall()
        for data in fetch:
             tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()
        acc_no.set("")
        c_name.set("")
        c_no.set("")
        c_add.set("")
        acc_type.set("")
        bal.set("")
        
    
    #==================BUTTONS==============================
    btn_addcon = Button(ContactForm, text="Find", width=50, command=SubmitData2)
    btn_addcon.grid(row=6, columnspan=2, pady=10)

    
    Top = Frame(NewWindow, width=600, bd=1, relief=SOLID)
    Top.pack(side=TOP)
    TableMargin = Frame(NewWindow, width=600)
    TableMargin.pack(side=TOP)
    lbl_title = Label(Top, text="Bank_Det", font=('arial', 16), width=10)
    lbl_title.pack(fill=X)
    scrollbarx = Scrollbar(TableMargin, orient=HORIZONTAL)
    scrollbary = Scrollbar(TableMargin, orient=VERTICAL)
    tree = ttk.Treeview(TableMargin, columns=("Acc_no","C_Name", "C_No","C_Add","Acc_Type", "Bal"), height=10, selectmode="extended", yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree1.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    tree.heading('Acc_no', text="Acc_no", anchor=W)
    tree.heading('C_Name', text="C_Name", anchor=W)
    tree.heading('C_No', text="C_No", anchor=W)
    tree.heading('C_Add', text="C_Add", anchor=W)
    tree.heading('Acc_Type', text="Acc_Type", anchor=W)
    tree.heading('Bal', text="Bal", anchor=W)
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=80)
    tree.column('#2', stretch=NO, minwidth=0, width=80)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=80)
    tree.column('#5', stretch=NO, minwidth=0, width=80)
    tree.pack()
    tree.bind('<Double-Button-1>', OnSelected)

#     def treeDel():        
#             for i in tree.get_children():
#                 tree.delete(i)
#     b = Button(NewWindow, text="Clear",command=treeDel)
#     b.pack()
#-----------------------------------------

def Exit():
    exit()
#-----------------------------------------

def OnSelected(event):
    global mem_id, UpdateWindow
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    acc_no.set("")
    c_name.set("")
    c_no.set("")
    c_add.set("")
    acc_no.set(selecteditem[1])
    c_name.set(selecteditem[2])
    c_no.set(selecteditem[3])
    c_add.set(selecteditem[4])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact List")
    width = 300
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()
    #===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Updating Contacts", font=('arial', 16), bg="orange",  width = 200)
    lbl_title.pack(fill=X)
    lbl_name = Label(ContactForm, text="Acc_no", font=('arial', 14), bd=5)
    lbl_name.grid(row=0, sticky=W)
    lbl_age = Label(ContactForm, text="C_Name", font=('arial', 14), bd=5)
    lbl_age.grid(row=1, sticky=W)
    lbl_tickets = Label(ContactForm, text="C_No", font=('arial', 14), bd=5)
    lbl_tickets.grid(row=2, sticky=W)
    lbl_ticket_id = Label(ContactForm, text="C_Add", font=('arial', 14), bd=5)
    lbl_ticket_id.grid(row=3, sticky=W)
    #===================ENTRY===============================
    name = Entry(ContactForm, textvariable=acc_no, font=('arial', 14))
    name.grid(row=0, column=1)
    age = Entry(ContactForm, textvariable=c_name, font=('arial', 14))
    age.grid(row=1, column=1)
    tickets = Entry(ContactForm, textvariable=c_no, font=('arial', 14))
    tickets.grid(row=2, column=1)
    ticket_id = Entry(ContactForm, textvariable=c_add,  font=('arial', 14))
    ticket_id.grid(row=3, column=1)

#--------------------------------------------------------

menubar = Menu(root)
# create a pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Insert", command=AddNew)
filemenu.add_command(label="Find_Cust", command=Find)
menubar.add_cascade(label="Cust_Det", menu=filemenu)

#----------------------
menubar.add_command(label="Exit", command=Exit)
# display the menu
root.config(menu=menubar)

#-----------------------------------------------------table---------------------------------
def Database2():
    conn = mycon.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `cust_det`")
    fetch2 = cursor.fetchall()
    for data2 in fetch2:
        tree2.insert('', 'end', values=(data2))
    cursor.close()
    conn.close()
def Database1():
    conn = mycon.connect("bank.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM `bank_det`")
    fetch1 = cursor.fetchall()
    for data1 in fetch1:
        tree1.insert('', 'end', values=(data1))
    cursor.close()
    conn.close()

def OnSelected2(event):
    global mem_id2, UpdateWindow
    curItem = tree2.focus()
    contents =(tree2.item(curItem))
    selecteditem = contents['values']
    mem_id2 = selecteditem[0]
    acc_no.set("")
    c_name.set("")
    c_no.set("")
    c_add.set("")
    acc_no.set(selecteditem[1])
    c_name.set(selecteditem[2])
    c_no.set(selecteditem[3])
    c_add.set(selecteditem[4])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact List")
    width = 300
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 450) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()
    #===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Updating Contacts", font=('arial', 16), bg="orange",  width = 200)
    lbl_title.pack(fill=X)
    lbl_name = Label(ContactForm, text="Acc_no", font=('arial', 14), bd=5)
    lbl_name.grid(row=0, sticky=W)
    lbl_age = Label(ContactForm, text="C_Name", font=('arial', 14), bd=5)
    lbl_age.grid(row=1, sticky=W)
    lbl_tickets = Label(ContactForm, text="C_No", font=('arial', 14), bd=5)
    lbl_tickets.grid(row=2, sticky=W)
    lbl_ticket_id = Label(ContactForm, text="C_Add", font=('arial', 14), bd=5)
    lbl_ticket_id.grid(row=3, sticky=W)
    #===================ENTRY===============================
    name = Entry(ContactForm, textvariable=acc_no, font=('arial', 14))
    name.grid(row=0, column=1)
    age = Entry(ContactForm, textvariable=c_name, font=('arial', 14))
    age.grid(row=1, column=1)
    tickets = Entry(ContactForm, textvariable=c_no, font=('arial', 14))
    tickets.grid(row=2, column=1)
    ticket_id = Entry(ContactForm, textvariable=c_add,  font=('arial', 14))
    ticket_id.grid(row=3, column=1)

def OnSelected1(event):
    global mem_id1, UpdateWindow
    curItem = tree1.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id2 = selecteditem[0]
    acc_no.set("")
    acc_type.set("")
    bal.set("")
    acc_no.set(selecteditem[1])
    acc_type.set(selecteditem[2])
    bal.set(selecteditem[3])
    UpdateWindow = Toplevel()
    UpdateWindow.title("Contact List")
    width = 600
    height = 300
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    x = ((screen_width/2) + 650) - (width/2)
    y = ((screen_height/2) + 20) - (height/2)
    UpdateWindow.resizable(0, 0)
    UpdateWindow.geometry("%dx%d+%d+%d" % (width, height, x, y))
    if 'NewWindow' in globals():
        NewWindow.destroy()
    #===================FRAMES==============================
    FormTitle = Frame(UpdateWindow)
    FormTitle.pack(side=TOP)
    ContactForm = Frame(UpdateWindow)
    ContactForm.pack(side=TOP, pady=10)
    #===================LABELS==============================
    lbl_title = Label(FormTitle, text="Updating Contacts", font=('arial', 16), bg="orange",  width = 400)
    lbl_title.pack(fill=X)
    lbl_name = Label(ContactForm, text="Acc_no", font=('arial', 14), bd=5)
    lbl_name.grid(row=0, sticky=W)
    lbl_age = Label(ContactForm, text="Acc_Type", font=('arial', 14), bd=5)
    lbl_age.grid(row=1, sticky=W)
    lbl_tickets = Label(ContactForm, text="Bal", font=('arial', 14), bd=5)
    lbl_tickets.grid(row=2, sticky=W)
    #===================ENTRY===============================
    name = Entry(ContactForm, textvariable=acc_no, font=('arial', 14))
    name.grid(row=0, column=1)
    age = Entry(ContactForm, textvariable=acc_no_type, font=('arial', 14))
    age.grid(row=1, column=1)
    tickets = Entry(ContactForm, textvariable=bal, font=('arial', 14))
    tickets.grid(row=2, column=1)


#----------------------Database Frame_1-------
Top1 = Frame(Tops, width=600, bd=1, relief=SOLID)
Top1.pack(side=TOP)
TableMargin1 = Frame(Tops, width=600)
TableMargin1.pack(side=RIGHT)
lbl_title1 = Label(Top1, text="Bank_Det", font=('arial', 16), width=10)
lbl_title1.pack(fill=X)
scrollbarx1 = Scrollbar(TableMargin1, orient=HORIZONTAL)
scrollbary1 = Scrollbar(TableMargin1, orient=VERTICAL)
tree1 = ttk.Treeview(TableMargin1, columns=("Acc_no", "Acc_Type", "Bal"), height=10, selectmode="extended", yscrollcommand=scrollbary1.set, xscrollcommand=scrollbarx1.set)
scrollbary1.config(command=tree1.yview)
scrollbary1.pack(side=RIGHT, fill=Y)
scrollbarx1.config(command=tree1.xview)
scrollbarx1.pack(side=BOTTOM, fill=X)
tree1.heading('Acc_no', text="Acc_no", anchor=W)
tree1.heading('Acc_Type', text="Acc_Type", anchor=W)
tree1.heading('Bal', text="Bal", anchor=W)
tree1.column('#0', stretch=NO, minwidth=0, width=0)
tree1.column('#1', stretch=NO, minwidth=0, width=80)
tree1.column('#2', stretch=NO, minwidth=0, width=80)
tree1.column('#3', stretch=NO, minwidth=0, width=120)
tree1.pack()
tree1.bind('<Double-Button-1>', OnSelected1)

#----------------------Database Frame_2-------
Top2 = Frame(Bottom, width=450, bd=1, relief=SOLID)
Top2.pack(side=TOP)
TableMargin2 = Frame(Bottom, width=400)
TableMargin2.pack(side=LEFT)
lbl_title2 = Label(Top2, text="Cust_Det", font=('arial', 16), width=15)
lbl_title2.pack(fill=X)
scrollbarx2 = Scrollbar(TableMargin2, orient=HORIZONTAL)
scrollbary2 = Scrollbar(TableMargin2, orient=VERTICAL)
tree2 = ttk.Treeview(TableMargin2, columns=("Acc_no", "C_Name", "C_No", "C_Add"), height=80, selectmode="extended", yscrollcommand=scrollbary2.set, xscrollcommand=scrollbarx2.set)
scrollbary2.config(command=tree2.yview)
scrollbary2.pack(side=RIGHT, fill=Y)
scrollbarx2.config(command=tree2.xview)
scrollbarx2.pack(side=BOTTOM, fill=X)
tree2.heading('Acc_no', text="Acc_no", anchor=W)
tree2.heading('C_Name', text="C_Name", anchor=W)
tree2.heading('C_No', text="C_No", anchor=W)
tree2.heading('C_Add', text="C_Add", anchor=W)
tree2.column('#0', stretch=NO, minwidth=0, width=0)
tree2.column('#1', stretch=NO, minwidth=0, width=80)
tree2.column('#2', stretch=NO, minwidth=0, width=80)
tree2.column('#3', stretch=NO, minwidth=0, width=120)
tree2.column('#4', stretch=NO, minwidth=0, width=90)
tree2.pack()
tree2.bind('<Double-Button-1>', OnSelected2)

Database1()
Database2()
root.mainloop()
