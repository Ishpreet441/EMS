import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from tkinter import scrolledtext
from Tools.demo.sortvisu import WIDTH
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
def searchemployeefun():
    def searchdetails():
        sv=t1.get()
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="EmsDb")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM emp where Code=%s"
        val = (sv,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        for x in myresult:
            t2.insert(0,x[1])
            t3.insert(0,x[2])
            t4.insert(0,x[3])
            t5.insert(0,x[4])
            t6.insert(0,x[5])
            t7.insert(0,x[6])
            t8.insert(0,x[7])
            t9.insert(0,x[8])
            t10.insert(0,x[9])
            t11.insert(0,x[10])
    window=tkinter.Tk()
    window.geometry('620x690+325+30')
    window.title("Employee Record Searching Form")
    window.resizable(0,0)
    frame = tk.Frame(window, bg='pink')
    frame.pack(fill='both', expand='yes')
    heading = tk.Label(frame, text="Employee Record Search", bg='pink', font=("Times New Roman", 18),fg='blue')
    heading.place(x=210, y=40)
    code = tk.Label(frame, text="Enter Employee Code", bg='pink')
    code.place(x=220, y=100)
    t1 = tk.Entry(frame, text="", width=23)
    t1.place(x=360, y=100)
    deptt = tk.Label(frame, text="Department" , bg='pink')
    deptt.place(x=120, y=150)
    t2 = tk.Entry(frame, text="", width=23)
    t2.place(x=220, y=150)
    desi = tk.Label(frame, text="Designation" , bg='pink')
    desi.place(x=120, y=200)
    t3 = tk.Entry(frame, text="", width=23)
    t3.place(x=220, y=200)
    name = tk.Label(frame, text="Name" , bg='pink')
    name.place(x=120, y=250)
    t4 = tk.Entry(frame, text="", width=23)
    t4.place(x=220, y=250)
    fname = tk.Label(frame, text="Father Name" , bg='pink')
    fname.place(x=120, y=300)
    t5 = tk.Entry(frame, text="", width=23)
    t5.place(x=220, y=300)
    address = tk.Label(frame, text="Address" , bg='pink')
    address.place(x=120, y=350)
    t6 = tk.Entry(frame, text="", width=23)
    t6.place(x=220, y=350)
    city = tk.Label(frame, text="City" , bg='pink')
    city.place(x=120, y=400)
    t7 = tk.Entry(frame, text="", width=23)
    t7.place(x=220, y=400)
    bgroup = tk.Label(frame, text="Blood Group" , bg='pink')
    bgroup.place(x=120, y=450)
    t8 = tk.Entry(frame, text="", width=23)
    t8.place(x=220, y=450)
    dob = tk.Label(frame, text="Date of Birth" , bg='pink')
    dob.place(x=120, y=500)
    t9 = tk.Entry(frame, text="", width=23)
    t9.place(x=220, y=500)
    quali = tk.Label(frame, text="Qualification" , bg='pink')
    quali.place(x=120, y=550)
    t10 = tk.Entry(frame, text="", width=23)
    t10.place(x=220, y=550)
    salary = tk.Label(frame, text="Basic Salary" , bg='pink')
    salary.place(x=120, y=600)
    t11 = tk.Entry(frame, text="", width=23)
    t11.place(x=220, y=600)
    bt1 = Button(frame, text="Search", width=10, fg="blue", font=("Times New Roman", 7), command=searchdetails)
    bt1.place(x=520, y=100)
    window.mainloop()
