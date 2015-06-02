__author__ = 'deepanshu'

from tkinter import *
import backend as bk


def user_detail_method(uid, password):
    user_detail1 = Tk()
    user_detail1.geometry('300x300')
    user_detail1.config(background='White')
    user_detail1.wm_title('User Details')
    my_uid = uid
    my_password = password

    def my_destroy():
        user_detail1.destroy()

    def get_details():
        global my_uid
        global my_password
        my_destroy()
        bk.get_values(uid, password)

    def calculate():
        global my_uid
        my_destroy()
        bk.calculate(uid)

    button_get_details = Button(user_detail1, text='Get Details', fg='Green', command=get_details)
    button_get_details.grid(row=1, column=1, padx=100, pady=30)

    button_calculate = Button(user_detail1, text='Calculate', fg='Green', command=calculate)
    button_calculate.grid(row=2, column=1, padx=100, pady=30)

    user_detail1.mainloop()


def check_if_valid(uid, password):
    return bk.check(uid, password)