__author__ = 'deepanshu'

from tkinter import *
import all_the_method


def main():
    main_panel = Tk()
    main_panel.config(background='White')
    main_panel.wm_title('Admin account')
    main_panel.geometry('300x350')

    button_add = Button(main_panel, text='     Add user     ', fg='Green', command=all_the_method.add_user)
    button_add.place(x=75, y=50, width=150, height=30)

    button_remove = Button(main_panel, text='     Remove user  ', fg='Green', command=all_the_method.remove)
    button_remove.place(x=75, y=100, width=150, height=30)

    button_update_record = Button(main_panel, text='     Update Record', fg='Green', command=all_the_method.update)
    button_update_record.place(x=75, y=150, width=150, height=30)

    button_working_days = Button(main_panel, text='Working Days Entry', fg='Green', command=all_the_method.work)
    button_working_days.place(x=75, y=200, width=150, height=30)

    button_display = Button(main_panel, text='  Display Details', fg='Green', command=all_the_method.display_details)
    button_display.place(x=75, y=250, width=150, height=30)

    main_panel.mainloop()

