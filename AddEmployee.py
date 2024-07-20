from mysql.connector import Error
from tkinter import messagebox
from tkinter import scrolledtext
from Tools.demo.sortvisu import WIDTH
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import mysql.connector
def addemployeefun():
    def saveemployee():
        v1=cb.get()
        v2=t1.get()
        v3=t2.get()
        v4=t3.get()
        v5=t4.get()
        v6=t5.get()
        v7=cb1.get()
        v8=cb2.get()+"-"+cb3.get()+"-"+cb4.get();
        v9=cb5.get()
        v10=t6.get()
        if(v1=="Select"):
            messagebox.showinfo("Message", "Please select department")
            window.destroy();
            addemployeefun()
        elif(v2==""):
            messagebox.showinfo("Message", "Please enter designation")
            window.destroy();
            addemployeefun()
        elif(v3==""):
            messagebox.showinfo("Message", "Please enter employee name")
            window.destroy();
            addemployeefun()
        elif(v4==""):
            messagebox.showinfo("Message", "Please enter father name")
            window.destroy();
            addemployeefun()
        elif(v5==""):
            messagebox.showinfo("Message", "Please enter address")
            window.destroy();
            addemployeefun()
        elif(v6==""):
            messagebox.showinfo("Message", "Please enter city")
            window.destroy();
            addemployeefun()
        elif(cb1.get()=="Select"):
            messagebox.showinfo("Message", "Please select blood group")
            window.destroy();
            addemployeefun()
        elif(cb2.get()=="Day"):
            messagebox.showinfo("Message", "Please select day")
            window.destroy();
            addemployeefun()
        elif(cb3.get()=="Month"):
            messagebox.showinfo("Message", "Please select month")
            window.destroy();
            addemployeefun()
        elif(cb4.get=="Year"):
            messagebox.showinfo("Message", "Please select year")
            window.destroy();
            addemployeefun()
        elif(cb5.get()=="Select"):
            messagebox.showinfo("Message", "Please select qualification")
            window.destroy();
            addemployeefun()
        elif(v7==""):
            messagebox.showinfo("Message", "Please enter basic salary")
            window.destroy();
            addemployeefun()
        else:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="EmsDb"
            )
            try:
                mycursor = mydb.cursor()
                sql = "INSERT INTO emp(Deptt,Desi,Name,FName,Address, City, BloodGroup,Dob, Qualification,BSalary) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = (v1, v2, v3, v4, v5, v6, v7, v8, v9, v10)
                mycursor.execute(sql, val)
                mydb.commit()
                messagebox.showinfo("Confirmation", "Employee Record submitted successfully")
                window.destroy()
                addemployeefun()
                cb.current(0)
                cb1.current(0)
                t1.delete(0, END)
                t2.delete(0, END)
                t3.delete(0, END)
                t4.delete(0, END)
                t5.delete(0, END)
                t6.delete(0, END)
                cb2.current(0)
                cb3.current(0)
                cb4.current(0)
                cb5.current(0)
            except Error as error:
                messagebox.showinfo("Confirmation", error)
                window.destroy()
                addemployeefun()
    window=tkinter.Tk()
    window.geometry('620x640+325+70')
    window.title("Employee Addition Form")
    window.resizable(0,0)
    frame = tk.Frame(window, bg='pink')
    frame.pack(fill='both', expand='yes')
    heading = tk.Label(frame, text="Employee Record", bg='pink', font=("Times New Roman", 18),fg='blue')
    heading.place(x=210, y=40)
    deptt = tk.Label(frame, text="Deptt." , bg='pink')
    deptt.place(x=120, y=100)
    cb = ttk.Combobox(frame, values=("Select","Purchase","Sale","Marketing","Production","IT"))
    cb.place(x=220, y=100)
    cb.current(0)
    desi = tk.Label(frame, text="Designation" , bg='pink')
    desi.place(x=370, y=100)
    t1 = tk.Entry(frame, text="", width=23)
    t1.place(x=440, y=100)
    name = tk.Label(frame, text="Name" , bg='pink')
    name.place(x=120, y=150)
    t2 = tk.Entry(frame, text="", width=23)
    t2.place(x=220, y=150)
    fname = tk.Label(frame, text="Father Name" , bg='pink')
    fname.place(x=120, y=200)
    t3 = tk.Entry(frame, text="", width=23)
    t3.place(x=220, y=200)
    address = tk.Label(frame, text="Address" , bg='pink')
    address.place(x=120, y=250)
    t4 = tk.Entry(frame, text="", width=23)
    t4.place(x=220, y=250)
    city = tk.Label(frame, text="City" , bg='pink')
    city.place(x=120, y=300)
    t5 = tk.Entry(frame, text="", width=23)
    t5.place(x=220, y=300)
    bgroup = tk.Label(frame, text="Blood Group" , bg='pink')
    bgroup.place(x=120, y=350)
    cb1 = ttk.Combobox(frame, values=("Select","A+","A-","B+","B-","O+","O-","AB+","AB-"))
    cb1.place(x=220, y=350)
    cb1.current(0)
    dob = tk.Label(frame, text="Date of Birth" , bg='pink')
    dob.place(x=120, y=400)
    cb2 = ttk.Combobox(frame, values=("Day"), width=6)
    cb2.place(x=220, y=400)
    cb2.current(0)
    for i in range(1, 32):
        cb2['values'] += (i,)
    cb3 = ttk.Combobox(frame, values=("Month", "January","February","March","April","May","June","July","August","September","October","November","December"), width=10)
    cb3.place(x=292, y=400)
    cb3.current(0)
    cb4 = ttk.Combobox(frame, values=("Year"), width=6)
    cb4.place(x=392, y=400)
    cb4.current(0)
    for i in range(1960, 2021):
        cb4['values'] += (i,)
    quali = tk.Label(frame, text="Qualification" , bg='pink')
    quali.place(x=120, y=450)
    cb5 = ttk.Combobox(frame, values=("Select","8th","10th","12th","Graduate","Post Graduate"))
    cb5.place(x=220, y=450)
    cb5.current(0)
    salary = tk.Label(frame, text="Basic Salary" , bg='pink')
    salary.place(x=120, y=500)
    t6 = tk.Entry(frame, text="", width=23)
    t6.place(x=220, y=500)
    bt1 = Button(frame, text="Save", width=10, fg="blue", font=("Times New Roman", 10), command=saveemployee)
    bt1.place(x=222, y=550)
    window.mainloop()
