__author__ = 'deepanshu'

from tkinter import *
from user_menu import user_menu
from admin_menu import admin_menu


def kill():
    root.destroy()

root = Tk()
root.geometry('300x300')
root.config(background='White')
root.wm_title("Main Window")

label = Label(root, text="Welcome to the Payroll Management", fg='Green')
label.pack(padx=10, pady=10)

button_user = Button(root, text=' User ', fg='Green', command=user_menu)
button_user.pack(padx=20, pady=20)

button_admin = Button(root, text='Admin', fg='Green', command=admin_menu)
button_admin.pack(padx=20, pady=20)

button_exit = Button(root, text='Cancel', fg='Green', command=kill)
button_exit.pack(padx=20, pady=20)
root.mainloop()