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
        label = Label(self, text='This is page 1')
        label.pack(side='top', fill='both', expand=True)


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

        b1 = Button(buttonframe, text='Main', command=p1.lift)
        b2 = Button(buttonframe, text='Reserved', command=p2.show)
        b3 = Button(buttonframe, text='Reserved', command=p3.show)

        b1.pack(side='left')
        b2.pack(side='left')
        b3.pack(side='left')

        p1.show()

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
        # create check connection window
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


# OLD ORIGINAL ****************************************************************************************

from Tkinter import *
import scripts


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.master.title('Doughey')
        self.pack()
        self.create_topmenu()
        self.create_widgets()

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

    def create_widgets(self):
        # create main screen widgets
        self.QUIT = Button(self)
        self.QUIT['text'] = 'QUIT'
        self.QUIT['fg'] = 'red'
        self.QUIT['command'] = self.quit

        self.QUIT.grid(row=0, column=0)

        self.hi_there = Button(self)
        self.hi_there['text'] = 'Hello'

        self.hi_there.grid(row=1, column=0)

    def check_conn_window(self):
        # create check connection window
        self.conn_window = Toplevel(self.master)
        self.conn_window.geometry('500x200')

        self.ip_label = Label(self.conn_window, text='IP Address:')
        self.ip_label.grid(row=0, column=0, pady=30)

        self.ip_entry = Entry(self.conn_window)
        self.ip_entry.grid(row=0, column=1, pady=0)

        self.check_conn_btn = Button(self.conn_window)
        self.check_conn_btn['text'] = 'Check Connection'
        self.check_conn_btn['command'] = self.run_ip_input
        self.check_conn_btn.grid(row=1, column=0, padx=30)

        self.ip_feedback = Label(self.conn_window)
        self.ip_feedback['text'] = ''
        self.ip_feedback.grid(row=1, column=1)

    def run_ip_input(self):
        ip_address = self.ip_entry.get()
        result = scripts.check_connection(ip_address)
        self.ip_feedback['text'] = result





root = Tk()
root.geometry('900x600')
app = Application(master=root)
app.mainloop()
root.destroy()