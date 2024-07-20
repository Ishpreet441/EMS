from AddEmployee import *
from UpdateEmployee import *
from EmployeeReport import *
from SearchEmployee import *
from EmployeePayslip import *
from tkinter import *
from tkinter import Menu
from tkinter import messagebox      
from distutils import command
def menuu():
    def show():
        messagebox.showinfo('About Me','Project Developed in Python with Mysql Database')
    def exitfun():
        title = 'Please Confirm'
        content = 'Really do you want to exit?'
        ans = messagebox.askquestion(title, content)
        if ans == 'yes':
            messagebox.showinfo('Status','Okay Bye Bye Visit Again......')
            quit()
        else:  
            messagebox.showinfo('Status','Press any key to continue')
    window = Tk()
    window.title("Employee Management System  EMS")
    w, h = window.winfo_screenwidth(), window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (w, h))
    window.configure(bg='cyan')
    menubar = Menu(window)
    window.config(menu=menubar)
    masaterdb = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Master Information", menu=masaterdb)
    masaterdb.add_command(label="Add Employee", command=addemployeefun)
    masaterdb.add_separator()
    masaterdb.add_command(label="Update Employee", command=updateemployeefun)
    transaction = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="View Information", menu=transaction)
    transaction.add_command(label="Search Employee", command=searchemployeefun)
    transaction.add_separator()
    transaction.add_command(label="Show All Employee", command=employeereport)
    '''transaction.add_separator()
    transaction.add_command(label="Stock in Hand", command=report)'''
    payslip = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Transaction", menu=payslip)
    payslip.add_command(label="Salary Calculation", command=salaryinfo)
    '''reports.add_separator()
    reports.add_command(label="Report", command=report)
    reports.add_separator()
    reports.add_command(label="Report", command=report)'''
    helpp = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=helpp)
    helpp.add_command(label="About Me", command=show)
    helpp.add_separator()
    helpp.add_command(label="Exit", command=exitfun)
    window.mainloop()
