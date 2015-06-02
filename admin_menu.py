__author__ = 'deepanshu'

from tkinter import *
import root_method
import cal_and_dis


def admin_menu():
    admin = Tk()
    uid = 12
    password = 'garbage'

    def kill():
        admin.destroy()

    def login():
        global password
        global uid
        uid, password = entry_one.get(), entry_two.get()
        if cal_and_dis.check_if_valid(uid, password):
            kill()
            root_method.main()
        else:
            error = Tk()
            error.wm_title('Error')
            error.geometry('600x80')

            def kill2():
                error.destroy()

            error_label = Label(error, text="Id or Password not found Try Again")
            error_label.place(x=50, y=20)
            button_quit = Button(error, text="QUIT", command=kill2)
            button_quit.place(x=50, y=60, width=200, height=20)

    admin.geometry('400x300')
    admin.config(background='White')
    admin.wm_title("Admin Panel")

    label_uid = Label(admin, text='Enter uid')
    label_uid.place(x=50, y=30, width=120, height=30)
    entry_one = Entry(admin)
    entry_one.place(x=180, y=30, width=200, height=30)

    label_password = Label(admin, text='Enter password')
    label_password.place(x=50, y=100, width=120, height=30)
    entry_two = Entry(admin)
    entry_two.place(x=180, y=100, width=200, height=30)

    button_login = Button(admin, text='Login', command=login)
    button_login.place(x=100, y=150, width=200, height=30)

    admin.mainloop()