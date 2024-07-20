import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
from tkinter import scrolledtext
from Tools.demo.sortvisu import WIDTH
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
def salaryinfo():
    def showsalarydetails():
        sv=cb.get()
        mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="EmsDb")
        mycursor = mydb.cursor()
        sql = "SELECT * FROM emp where Code=%s"
        val = (sv,)
        mycursor.execute(sql,val)
        myresult = mycursor.fetchall()
        cb['values']=""
        for x in myresult:
            t1.insert(0,x[1])
            t2.insert(0,x[2])
            t3.insert(0,x[3])
            t4.insert(0,x[4])
            t5.insert(0,x[10])
        sal=int(t5.get())
        ta=sal*5/100;
        da=sal*12/100;
        hra=sal*10/100;
        tds=sal*10/100;
        nsal=(sal+ta+da+hra)-tds
        t6.insert(0,str(ta))
        t7.insert(0,str(da))
        t8.insert(0,str(hra))
        t9.insert(0,str(tds))
        t10.insert(0,str(nsal))
    def updateemployee():
        v1=cb.get()
        v2=t1.get()
        v3=t2.get()
        v4=t3.get()
        v5=t4.get()
        v6=t5.get()
        v7=t6.get()
        v8=t7.get()
        v9=t8.get()
        v10=t9.get()
        v11=t10.get()
        if(v1=="Select"):
            messagebox.showinfo("Message", "Please select employee code")
            window.destroy();
        else:
            mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="EmsDb"
            )
            try:
                mycursor = mydb.cursor()
                sql = "update emp set Deptt=%s,Desi=%s,Name=%s,FName=%s,Address=%s,City=%s,BloodGroup=%s,Dob=%s,Qualification=%s,BSalary=%s where Code=%s"
                val = (v2, v3, v4, v5, v6, v7, v8, v9, v10,v11,v1)
                mycursor.execute(sql, val)
                mydb.commit()
                messagebox.showinfo("Confirmation", "Employee detail updated successfully")
                '''window.destroy()
                #updateemployeefun()
                cb.current(0)
                t1.delete(0, END)
                t2.delete(0, END)
                t3.delete(0, END)
                t4.delete(0, END)
                t5.delete(0, END)
                t6.delete(0, END)
                t7.delete(0, END)
                t8.delete(0, END)
                t9.delete(0, END)'''
            except Error as error:
                messagebox.showinfo("Confirmation", error)
                window.destroy()
    window=tkinter.Tk()
    window.geometry('620x690+325+30')
    window.title("Employee Salary Slip Form")
    window.resizable(0,0)
    frame = tk.Frame(window, bg='pink')
    frame.pack(fill='both', expand='yes')
    heading = tk.Label(frame, text="Employee's Payslip ", bg='pink', font=("Times New Roman", 18),fg='blue')
    heading.place(x=210, y=40)
    code = tk.Label(frame, text="Select Code", bg='pink')
    code.place(x=220, y=100)
    cb = ttk.Combobox(frame, values=("Select"))
    cb.place(x=310, y=100)
    cb.current(0)
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="EmsDb"
    )
    mycursor = mydb.cursor()
    sql = "SELECT * FROM emp"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    for x in myresult:
        if x not in cb['values']:
            cb['values'] += (x[0],)
    deptt = tk.Label(frame, text="Department" , bg='pink')
    deptt.place(x=120, y=150)
    t1 = tk.Entry(frame, text="", width=23)
    t1.place(x=220, y=150)
    desi = tk.Label(frame, text="Designation" , bg='pink')
    desi.place(x=120, y=200)
    t2 = tk.Entry(frame, text="", width=23)
    t2.place(x=220, y=200)
    name = tk.Label(frame, text="Name" , bg='pink')
    name.place(x=120, y=250)
    t3 = tk.Entry(frame, text="", width=23)
    t3.place(x=220, y=250)
    fname = tk.Label(frame, text="Father Name" , bg='pink')
    fname.place(x=120, y=300)
    t4 = tk.Entry(frame, text="", width=23)
    t4.place(x=220, y=300)
    salary = tk.Label(frame, text="Basic Salary" , bg='pink')
    salary.place(x=120, y=350)
    t5 = tk.Entry(frame, text="", width=23)
    t5.place(x=220, y=350)
    ta = tk.Label(frame, text="TA(5%)" , bg='pink')
    ta.place(x=120, y=400)
    t6 = tk.Entry(frame, text="", width=23)
    t6.place(x=220, y=400)
    da = tk.Label(frame, text="DA(12%)" , bg='pink')
    da.place(x=120, y=450)
    t7 = tk.Entry(frame, text="", width=23)
    t7.place(x=220, y=450)
    hra = tk.Label(frame, text="HRA(10%)" , bg='pink')
    hra.place(x=120, y=500)
    t8 = tk.Entry(frame, text="", width=23)
    t8.place(x=220, y=500)
    tds = tk.Label(frame, text="TDS(10%)" , bg='pink')
    tds.place(x=120, y=550)
    t9 = tk.Entry(frame, text="", width=23)
    t9.place(x=220, y=550)
    netsalary = tk.Label(frame, text="Net Salary" , bg='pink')
    netsalary.place(x=120, y=600)
    t10 = tk.Entry(frame, text="", width=23)
    t10.place(x=220, y=600)
    bt1 = Button(frame, text="Show Salary Detail", width=20, fg="blue", font=("Times New Roman", 7), command=showsalarydetails)
    bt1.place(x=470, y=100)
    window.mainloop()
