__author__ = 'deepanshu'

import backend as bk
from tkinter import *


def add_user():
    add_value = Tk()
    add_value.geometry('400x400')
    add_value.wm_title('New user details')

    def kill_main():
        add_value.destroy()

    def get_val():
        uid = entry_one.get()
        name = entry_two.get()
        age = entry_three.get()
        salary = entry_four.get()
        password = entry_five.get()
        workdays = entry_six.get()
        print(uid, name, age, salary, password, workdays)
        if len(str(uid)) and len(str(name)) and len(str(age)) and len(str(salary)) and len(str(password)) and len(str(workdays)) and bk.check_if_uid(uid):
                kill_main()
                bk.add_into_table(uid, name, age, salary, password, workdays)

        else:
            tb = Tk()

            def kill():
                tb.destroy()

            try_again = Button(tb, text='No field could be exists and/or ID already exists', command=kill)
            try_again.pack()

    label_uid = Label(add_value, text='Enter uid')
    label_uid.place(x=30, y=30, width=120, height=30)
    entry_one = Entry(add_value)
    entry_one.place(x=180, y=30, width=200, height=30)

    label_uid = Label(add_value, text='Name')
    label_uid.place(x=30, y=90, width=120, height=30)
    entry_two = Entry(add_value)
    entry_two.place(x=180, y=90, width=200, height=30)

    label_uid = Label(add_value, text='Age')
    label_uid.place(x=30, y=150, width=120, height=30)
    entry_three = Entry(add_value)
    entry_three.place(x=180, y=150, width=200, height=30)

    label_uid = Label(add_value, text='Salary')
    label_uid.place(x=30, y=210, width=120, height=30)
    entry_four = Entry(add_value)
    entry_four.place(x=180, y=210, width=200, height=30)

    label_uid = Label(add_value, text='Password')
    label_uid.place(x=30, y=250, width=120, height=30)
    entry_five = Entry(add_value)
    entry_five.place(x=180, y=250, width=200, height=30)

    label_uid = Label(add_value, text='Workdays')
    label_uid.place(x=30, y=310, width=120, height=30)
    entry_six = Entry(add_value)
    entry_six.place(x=180, y=310, width=200, height=30)

    button_add = Button(add_value, text='Add', command=get_val)
    button_add.place(x=50, y=370, width=200, height=30)


def display_details():
    dp = Tk()
    dp.wm_title('Display Details')
    dp.geometry('400x400')
    uid = 0
    password = 'pwd'

    def get_all():
        global uid
        global password
        uid, password = entry_one.get(), entry_two.get()
        if bk.check(uid, password):
            bk.get_values(uid, password)
        else:
            tb = Tk()
            tb.geometry('300x100')
            tb.wm_title('Error')

            def kill():
                tb.destroy()

            l = Label(tb, text='Id or Password is wrong')
            l.place(x=30, y=20, width=200, height=20)
            button_quit = Button(tb, text='Quit', command=kill)
            button_quit.place(x=30, y=60, width=200, height=20)

    label_uid = Label(dp, text='UID')
    label_uid.place(x=30, y=30, width=80, height=30)
    entry_one = Entry(dp)
    entry_one.place(x=180, y=30, width=200, height=30)
    label_password = Label(dp, text='Password')
    label_password.place(x=30, y=100, width=80, height=30)
    entry_two = Entry(dp)
    entry_two.place(x=180, y=100, width=200, height=30)
    button_submit = Button(dp, text='Submit', command=get_all)
    button_submit.place(x=50, y=160, width=100, height=30)


def remove():
    dp = Tk()
    dp.wm_title('Remove Details')
    dp.geometry('400x400')
    uid = 0
    password = 'pwd'

    def kill2():
        dp.destroy()

    def delete():
        global uid
        global password
        uid, password = entry_one.get(), entry_two.get()
        if bk.check(uid, password):
            bk.delete(uid, password)
            kill2()
        else:
            tb = Tk()
            tb.geometry('300x100')
            tb.wm_title('Error')

            def kill():
                tb.destroy()

            l = Label(tb, text='Id or Password is wrong')
            l.place(x=30, y=20, width=200, height=20)
            button_quit = Button(tb, text='Quit', command=kill)
            button_quit.place(x=30, y=60, width=200, height=20)

    label_uid = Label(dp, text='UID')
    label_uid.place(x=30, y=30, width=80, height=30)
    entry_one = Entry(dp)
    entry_one.place(x=180, y=30, width=200, height=30)
    label_password = Label(dp, text='Password')
    label_password.place(x=30, y=100, width=80, height=30)
    entry_two = Entry(dp)
    entry_two.place(x=180, y=100, width=200, height=30)
    button_submit = Button(dp, text='Submit', command=delete)
    button_submit.place(x=50, y=160, width=100, height=30)


def update():
    add_value = Tk()
    add_value.geometry('400x400')
    add_value.wm_title('Update details')

    def kill_main():
        add_value.destroy()

    def get_val():
        uid = entry_one.get()
        name = entry_two.get()
        age = entry_three.get()
        salary = entry_four.get()
        password = entry_five.get()
        workdays = entry_six.get()
        print(uid, name, age, salary, password, workdays)
        if len(str(uid)) and len(str(name)) and len(str(age)) and len(str(salary)) and len(str(password)) and len(str(workdays)) and bk.check(uid, password):
                kill_main()
                bk.update(uid, name, age, salary, password, workdays)

        else:
            tb = Tk()

            def kill():
                tb.destroy()

            try_again = Button(tb, text='No field could be exists and/or ID already exists', command=kill)
            try_again.pack()

    label_uid = Label(add_value, text='Enter uid')
    label_uid.place(x=30, y=30, width=120, height=30)
    entry_one = Entry(add_value)
    entry_one.place(x=180, y=30, width=200, height=30)

    label_uid = Label(add_value, text='Name')
    label_uid.place(x=30, y=90, width=120, height=30)
    entry_two = Entry(add_value)
    entry_two.place(x=180, y=90, width=200, height=30)

    label_uid = Label(add_value, text='Age')
    label_uid.place(x=30, y=150, width=120, height=30)
    entry_three = Entry(add_value)
    entry_three.place(x=180, y=150, width=200, height=30)

    label_uid = Label(add_value, text='Salary')
    label_uid.place(x=30, y=210, width=120, height=30)
    entry_four = Entry(add_value)
    entry_four.place(x=180, y=210, width=200, height=30)

    label_uid = Label(add_value, text='Password')
    label_uid.place(x=30, y=250, width=120, height=30)
    entry_five = Entry(add_value)
    entry_five.place(x=180, y=250, width=200, height=30)

    label_uid = Label(add_value, text='Workdays')
    label_uid.place(x=30, y=310, width=120, height=30)
    entry_six = Entry(add_value)
    entry_six.place(x=180, y=310, width=200, height=30)

    button_add = Button(add_value, text='Add', command=get_val)
    button_add.place(x=50, y=370, width=200, height=30)


def work():
    dp = Tk()
    dp.wm_title('Update Workdays')
    dp.geometry('400x400')
    uid = 0
    password = 'pwd'
    workdays = 0

    def kill2():
        dp.destroy()

    def up_work():
        global uid
        global password
        global workdays
        uid, password, workdays = entry_one.get(), entry_two.get(), entry_three.get()
        if bk.check(uid, password):
            bk.update_work(uid, workdays)
            kill2()
        else:
            tb = Tk()
            tb.geometry('300x100')
            tb.wm_title('Error')

            def kill():
                tb.destroy()

            l = Label(tb, text='Id or Password is wrong')
            l.place(x=30, y=20, width=200, height=20)
            button_quit = Button(tb, text='Quit', command=kill)
            button_quit.place(x=30, y=60, width=200, height=20)

    label_uid = Label(dp, text='UID')
    label_uid.place(x=30, y=30, width=80, height=30)
    entry_one = Entry(dp)
    entry_one.place(x=180, y=30, width=200, height=30)
    label_password = Label(dp, text='Password')
    label_password.place(x=30, y=100, width=80, height=30)
    entry_two = Entry(dp)
    entry_two.place(x=180, y=100, width=200, height=30)
    label_work = Label(dp, text='Workdays')
    label_work.place(x=30, y=170, width=80, height=30)
    entry_three = Entry(dp)
    entry_three.place(x=180, y=170, width=200, height=30)
    button_submit = Button(dp, text='Submit', command=up_work)
    button_submit.place(x=50, y=240, width=100, height=30)