__author__ = 'deepanshu'

import sqlite3
from tkinter import *
import os.path

conn = sqlite3.connect('encrypt.db')


def create_table():
    conn.execute(''' CREATE TABLE IF NOT EXISTS COMPANY
        (ID INT PRIMARY KEY  NOT NULL,
        NAME     TEXT       NOT NULL,
        AGE	     INT	NOT NULL,
        SALARY   REAL NOT NULL,
        PASSWORD TEXT NOT NULL,
        WORKDAYS INT NOT NULL);''')


def add_some_value():
    conn.execute("INSERT INTO COMPANY (ID, NAME, AGE, SALARY, PASSWORD, WORKDAYS) VALUES (0, 'root', 0, 0.00, 'pwd', 30)")
    conn.commit()

"""
def print_values():
    cursor = conn.execute("SELECT id, name, age, salary, password  from COMPANY")
    for row in cursor:
        print("ID: ", row[0])
        print("NAME: ", row[1])
        print("AGE: ", row[2])
        print("SALARY: ", row[3])
        print("PASSWORD: ", row[4])
"""


def update(uid, name, age, salary, password, workdays):

    conn.execute("UPDATE COMPANY set name = ?, age = ?, SALARY = ?, password = ?, workdays = ? where ID = ?", (name, age, salary, password, workdays, uid))
    conn.commit()


def delete(uid, password):
    conn.execute("DELETE from COMPANY where ID = ? AND password = ?;", (uid, password))
    conn.commit()


def get_values(uid, password):
    cursor = conn.execute("SELECT *  from COMPANY WHERE id = ? AND PASSWORD = ?", (uid, password))
    for row in cursor:
        test = Tk()
        test.wm_title('Details')
        test.geometry('300x300')
        label_id = Label(test, text='Id: ' + str(row[0]))
        label_id.place(x=50, y=30, width=200, height=30)
        label_name = Label(test, text='Name: ' + str(row[1]))
        label_name.place(x=50, y=60, width=200, height=30)
        label_age = Label(test, text='Age: ' + str(row[2]))
        label_age.place(x=50, y=90, width=200, height=30)
        label_salary = Label(test, text='Salary: ' + str(row[3]))
        label_salary.place(x=50, y=120, width=200, height=30)
        label_password = Label(test, text='Password: ' + str(row[4]))
        label_password.place(x=50, y=150, width=200, height=30)
        label_workdays = Label(test, text='Work Days: ' + str(row[5]))
        label_workdays.place(x=50, y=180, width=200, height=30)

        def kill():
            test.destroy()

        button_quit = Button(test, text="Quit", command=kill)
        button_quit.place(x=50, y=210, width=200, height=30)


def calculate(uid):
    cursor = conn.execute("SELECT * from COMPANY WHERE id = ?", (uid,))
    sal = ''
    for row in cursor:
        sal = row[3]
        workdays = row[5]
    test = Tk()

    def kill():
        test.destroy()

    test.geometry('300x300')
    test.wm_title('Salary Calculation')

    sal = int(sal)
    workdays = int(workdays)

    per_day_sal = sal / 30
    total_salary = workdays * per_day_sal

    #Space for tds and stuff

    salary_label = Label(test, text='Salary: ' + str(sal))
    salary_label.place(x=50, y=30)
    workdays_label = Label(test, text='Workdays: ' + str(workdays))
    workdays_label.place(x=50, y=60)
    total_salary_label = Label(test, text='Total Salary: ' + str(total_salary))
    total_salary_label.place(x=50, y=90)

    button_quit = Button(test, text='Quit', command=kill)
    button_quit.place(x=50, y=120, width=200, height=30)


def check(uid, password):
    cursor = conn.execute("SELECT * from COMPANY where id = ?", (uid,))
    data = cursor.fetchall()
    if len(data):
        tup = data[0]
        if password == tup[4]:
            return True
    return False


def check_if_uid(uid):
    cursor = conn.execute("SELECT * from COMPANY where id = ?", (uid,))
    data = cursor.fetchall()
    if len(data):
        return False
    return True


def add_into_table(iid, name, age, salary, password, workdays):
    conn.execute('''INSERT INTO COMPANY (ID, NAME, AGE, SALARY, PASSWORD, WORKDAYS) VALUES
                 (?, ?, ?, ?, ?, ?)''', (iid, name, age, salary, password, workdays))
    conn.commit()


def update_work(uid, workdays):
    conn.execute('UPDATE COMPANY set WORKDAYS = ? where id = ?', (workdays, uid))
    conn.commit()

if __name__ == '__main__':
    create_table()
    add_some_value()