from Tkinter import *
import scripts


class Page(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)

    def show(self):
        self.lift()


class MainPage(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        self.curr_ip_address = None
        self.create_widgets()

    def create_widgets(self):
        # create page description label
        page_descrip = Label(self, text='Extract to Spreadsheet', font=('Consolas', 24))
        page_descrip.grid(row=1, column=0, pady=(30, 0))

        button_frame = Frame(self)
        button_frame.grid(row=2, column=0, sticky='W', pady=(10, 0))

        add_bits_btn = Button(button_frame, text='Add Bits to Spreadsheet', command=self.add_bits_window)
        set_ip_btn = Button(button_frame, text='Set IP Address', command=self.set_ip_window)

        self.ip_label = Label(button_frame, text='Current IP: ' + str(self.curr_ip_address))

        add_bits_btn.pack(side='left', padx=(0, 10))
        set_ip_btn.pack(side='left')
        self.ip_label.pack(side='left', padx=(10, 0))

    def add_bits_window(self):
        add_window = Toplevel(self.master)
        add_window.geometry('500x500')

    def set_ip_window(self):
        # create set ip address window and widgets
        self.ip_window = Toplevel(self.master)
        self.ip_window.geometry('300x100')

        ip_label = Label(self.ip_window, text='IP Address:')
        self.ip_entry = Entry(self.ip_window)
        ip_submit_btn = Button(self.ip_window, text='Submit', command=self.set_ip)

        ip_label.grid(row=0, column=0, padx=(20,0), pady=(30,0))
        self.ip_entry.grid(row=0, column=1, pady=(30,0))
        ip_submit_btn.grid(row=1, column=1, pady=(10, 0))

    def set_ip(self):
        ip_check = scripts.check_connection(self.ip_entry.get())
        if ip_check is True:
            self.curr_ip_address = self.ip_entry.get()
            self.ip_label['text'] = 'Current IP: ' + str(self.curr_ip_address)
            self.ip_window.destroy()
        else:
            self.create_warning_window(ip_check)

    def create_warning_window(self, warning):
        self.warn_window = Toplevel(self.master)
        self.warn_window.geometry('300x100')

        warn_label = Label(self.warn_window, text=warning)
        acknowledge_btn = Button(self.warn_window, text='Acknowledge', command=self.warn_window.destroy)

        warn_label.pack()
        acknowledge_btn.pack()


class FuturePage2(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text='Reserved')
        label.pack(side='top', fill='both', expand=True)


class FuturePage3(Page):
    def __init__(self, *args, **kwargs):
        Page.__init__(self, *args, **kwargs)
        label = Label(self, text='Reserved')
        label.pack(side='top', fill='both', expand=True)


class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, *args, **kwargs)
        self.create_topmenu()
        p1 = MainPage(self)
        p2 = FuturePage2(self)
        p3 = FuturePage3(self)

        buttonframe = Frame(self)
        container = Frame(self)
        buttonframe.pack(side='top', fill='x', expand=False)
        container.pack(side='top', fill='both', expand=True)

        p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        b1 = Button(buttonframe, text='Main', command=p1.show)
        b2 = Button(buttonframe, text='Reserved', command=p2.show)
        b3 = Button(buttonframe, text='Reserved', command=p3.show)

        b1.pack(side='left')
        b2.pack(side='left')
        b3.pack(side='left')

        p1.show()

    def close_window(self, window):
        window.destroy()

    def create_topmenu(self):
        # create main menu bar
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        # create file menu with commands
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label='Exit', command=self.quit)
        menubar.add_cascade(label='File', menu=filemenu)

        # create options menu with commands
        optionsmenu = Menu(menubar, tearoff=0)

        optionsmenu.add_command(label='Check PLC Connection', command=self.check_conn_window)

        menubar.add_cascade(label='Options', menu=optionsmenu)

    def check_conn_window(self):
        # create check connection window and widgets
        conn_window = Toplevel(self.master)
        conn_window.geometry('500x150')

        ip_label = Label(conn_window, text='IP Address:')
        ip_label.grid(row=0, column=0, pady=30)

        self.ip_entry = Entry(conn_window)
        self.ip_entry.grid(row=0, column=1, pady=0)

        check_conn_btn = Button(conn_window)
        check_conn_btn['text'] = 'Check Connection'
        check_conn_btn['command'] = self.run_ip_input
        check_conn_btn.grid(row=1, column=0, padx=30)

        self.ip_feedback = Label(conn_window)
        self.ip_feedback['text'] = ''
        self.ip_feedback.grid(row=1, column=1)

    def run_ip_input(self):
        ip_address = self.ip_entry.get()
        result = scripts.check_connection(ip_address)
        self.ip_feedback['text'] = result


if __name__ == '__main__':
    root = Tk()
    root.title('PLC Boy')
    main = MainWindow(root)
    main.pack(side='top', fill='both', expand=True)
    root.wm_geometry('900x600')
    root.mainloop()
