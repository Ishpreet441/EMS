import mysql.connector
from tkinter import messagebox
from tkinter.test.support import destroy_default_root
from Menubar import menuu
import tkinter
from tkinter import *
import tkinter as tk
def clicked():
    un=t1.get()
    pwd=t2.get()
    if(un==""):
        messagebox.showinfo("Message", "Please enter username")
    elif(pwd==""):
        messagebox.showinfo("Message", "Please enter password")
    else:
        mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="EmsDb"
        )
        mycursor = mydb.cursor()
        sql = "select * from Login where Username = %s and Password = %s"
        val = (un, pwd)
        mycursor.execute(sql, val)
        myresult = mycursor.fetchall()
        if(mycursor.rowcount>0):
            messagebox.showinfo("Confirmation", "Username/Password accepted....")
            window.destroy()
            menuu()
        else:
            messagebox.showinfo("Confirmation", "Invalid Username/Password....")
window=tkinter.Tk()
window.geometry('650x320+325+200')
window.title("Login Form")
window.resizable(0,0)
frame = tk.Frame(window, bg='cyan')
frame.pack(fill='both', expand='yes')
heading = tk.Label(frame, text="Login Form", bg='cyan', font=("Times New Roman", 18),fg='blue')
heading.place(x=270, y=40)
un = tk.Label(frame, text="Username", bg='cyan')
un.place(x=180, y=100)
t1 = tk.Entry(frame, text="", width=30)
t1.place(x=270, y=100)
pwd = tk.Label(frame, text="Password", bg='cyan')
pwd.place(x=180, y=150)
t2 = tk.Entry(frame, text="", show="*", width=30)
t2.place(x=270, y=150)
bt1 = Button(text="Login", width=10, fg="blue", font=("Times New Roman", 10), command=clicked)
bt1.place(x=275, y=200)
window.mainloop()
