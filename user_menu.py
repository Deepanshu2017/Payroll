__author__ = 'deepanshu'

from tkinter import *
import cal_and_dis


def user_menu():
    user = Tk()
    uid = -2
    password = ''

    def my_destroy():
        user.destroy()

    def login():
        global password
        global uid
        uid, password = entry_one.get(), entry_two.get()
        if cal_and_dis.check_if_valid(uid, password):
            my_destroy()
            cal_and_dis.user_detail_method(uid, password)
        else:
            error = Tk()
            error.wm_title('Error')
            error.geometry('600x80')

            def kill():
                error.destroy()

            error_label = Label(error, text="Id or Password not found Try Again")
            error_label.place(x=50, y=20)
            button_quit = Button(error, text="QUIT", command=kill)
            button_quit.place(x=50, y=60, width=200, height=20)

    user.geometry('400x300')
    user.config(background='White')
    user.wm_title("User Panel")

    label_uid = Label(user, text='Enter uid')
    label_uid.place(x=30, y=30, width=120, height=30)
    entry_one = Entry(user)
    entry_one.place(x=180, y=30, width=200, height=30)

    label_password = Label(user, text='Enter password')
    label_password.place(x=30, y=100, width=120, height=30)
    entry_two = Entry(user)
    entry_two.place(x=180, y=100, width=200, height=30)

    button_login = Button(user, text='Login', command=login)
    button_login.place(x=100, y=150, width=200, height=30)

    user.mainloop()