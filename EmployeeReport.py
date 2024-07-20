import mysql.connector
from mysql.connector import Error
from tkinter import messagebox
import tkinter as tk
from tkinter import ttk
def employeereport():
    report = tk.Tk()    
    report.geometry('1250x540+10+70')
    report.title("Employee's Report")
    report.resizable(0,0)
    report.configure(bg='pink')
    label = tk.Label(report, text="Employee's Report", font=("Arial",20), bg='pink')
    label.place(x=410, y=50)
    cols = ('Code', 'Name', 'Deptt', 'Designation', 'City','Basic Salary')
    listBox = ttk.Treeview(report, columns=cols, show='headings')
    for col in cols:
        listBox.heading(col, text=col)    
    listBox.place(x=26, y=100);
    mydb = mysql.connector.connect(host="localhost", user="root", passwd="", database="EmsDb")
    try:
        mycursor = mydb.cursor()
        sql = "select * from emp"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        for x in myresult:
            listBox.insert("", "end", values=(x[0], x[3], x[1], x[2], x[6], x[10]))
    except Error as error:
        messagebox.showinfo("Confirmation", error)
    report.mainloop()
