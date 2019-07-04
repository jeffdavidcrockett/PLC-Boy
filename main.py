from Tkinter import *
import scripts
from scripts import Xcl


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
        self.clear_warning = None
        self.spreadsheet_vals = []
        self.msg_selector = None
        self.xcl = Xcl()
        self.get_values_queue()

    def create_widgets(self):
        # create page description label
        page_descrip = Label(self, text='Extract to Spreadsheet', font=('Consolas', 24))
        page_descrip.grid(row=1, column=0, pady=(30, 0))

        button_frame = Frame(self)
        button_frame.grid(row=2, column=0, sticky='W', pady=(10, 0))

        values_frame = Frame(self)
        values_frame.grid(row=3, column=0, stick='W', padx=10, pady=(20, 0))

        add_values_frame = Frame(self)
        add_values_frame.grid(row=3, column=0, sticky=E+N)

        # add_tags_btn = Button(button_frame, text='Add Values to Queue', command=self.add_values_window)
        clear_queue_btn = Button(button_frame, text='Clear Queue', command=self.clear_warning_window)
        set_ip_btn = Button(button_frame, text='Set IP Address', command=self.set_ip_window)

        self.ip_label = Label(button_frame, text='Current IP: ' + str(self.curr_ip_address))

        # add_tags_btn.pack(side='left', padx=(5, 0))
        clear_queue_btn.pack(side='left', padx=5)
        set_ip_btn.pack(side='left')
        self.ip_label.pack(side='left', padx=(10, 0))

        values_label = Label(values_frame, text='Values in Queue', font='Helvetica 13 bold')
        values_label.pack(side='top')

        values_scroll = Scrollbar(values_frame)
        self.values_display = Text(values_frame, height=20, width=20)

        values_scroll.pack(side='right', fill=Y)
        self.values_display.pack()

        values_scroll.config(command=self.values_display.yview)
        self.values_display.config(yscrollcommand=values_scroll.set)

        add_tag_label = Label(add_values_frame, text='Add Tag to Queue', font='Helvetica 13 bold')
        add_tag_label.pack(side='top', pady=(21, 0))

        box_frame1 = Frame(add_values_frame)
        box_frame1.pack(side='top', fill='x', expand=False, padx=(5, 0), pady=(10, 0))

        box_frame2 = Frame(add_values_frame)
        box_frame2.pack(side='top', fill='x', expand=False, padx=(5, 0), pady=(20, 0))

        box_frame3 = Frame(add_values_frame)
        box_frame3.pack(side='top', fill='x', expand=False, padx=(5, 0), pady=(20, 0))

        # Frames and widgets for box frame 1
        data_type_frame = Frame(box_frame1)
        data_type_frame.pack(side='left', expand=False)

        file_num_frame = Frame(box_frame1)
        file_num_frame.pack(side='left', padx=(5, 0), expand=False)

        word_frame = Frame(box_frame1)
        word_frame.pack(side='left', padx=(5, 0), expand=False)

        bit_frame = Frame(box_frame1)
        bit_frame.pack(side='left', padx=(5, 0), expand=False)

        data_label = Label(data_type_frame, text='Data Type')
        data_label.pack(side='top')

        data_types = ['I', 'O', 'B', 'N', 'F']
        self.svar_data = StringVar()
        self.svar_data.set(data_types[0])
        self.data_menu = OptionMenu(data_type_frame, self.svar_data, *data_types)
        self.data_menu.pack()

        file_num_label = Label(file_num_frame, text='File #')
        file_num_label.pack(side='top')

        self.file_num = Entry(file_num_frame, width=5)
        self.file_num.pack(side='bottom')

        word_label = Label(word_frame, text='Word')
        word_label.pack(side='top')

        self.word_entry = Entry(word_frame, width=5)
        self.word_entry.pack()

        bit_label = Label(bit_frame, text='Bit')
        bit_label.pack(side='top')

        self.bit_entry = Entry(bit_frame, width=5)
        self.bit_entry.pack()

        # Frames and widgets for box frame 2
        through_frame = Frame(box_frame2)
        through_frame.pack(side='left', expand=False)

        word_frame2 = Frame(box_frame2)
        word_frame2.pack(side='left', padx=(15, 0), expand=False)

        bit_frame2 = Frame(box_frame2)
        bit_frame2.pack(side='left', padx=(5, 0), expand=False)

        self.through_var = IntVar()
        through_check = Checkbutton(through_frame, text='Through', variable=self.through_var)
        through_check.pack(side='left')

        word_label2 = Label(word_frame2, text='Word')
        word_label2.pack(side='top')

        self.word_entry2 = Entry(word_frame2, width=5)
        self.word_entry2.pack()

        bit_label2 = Label(bit_frame2, text='Bit')
        bit_label2.pack(side='top')

        self.bit_entry2 = Entry(bit_frame2, width=5)
        self.bit_entry2.pack()

        # Frames and widgets for box frame 3
        submit_frame = Frame(box_frame3)
        submit_frame.pack(side='top')

        add_btn = Button(submit_frame, text='Add Tag', command=self.get_values)
        add_btn.pack(side='left', padx=(0, 10))

        remove_btn = Button(submit_frame, text='Remove Tag', command=self.remove_tag)
        remove_btn.pack(side='left')

    def add_values_window(self):
        pass
        # add_window = Toplevel(self.master)
        # add_window.geometry('300x200')
        # add_window.title('Add Values')
        #
        # box_frame1 = Frame(add_window)
        # box_frame1.pack(side='top', fill='x', expand=False, padx=(5, 0), pady=(10, 0))
        #
        # box_frame2 = Frame(add_window)
        # box_frame2.pack(side='top', fill='x', expand=False, padx=(5, 0), pady=(20, 0))
        #
        # box_frame3 = Frame(add_window)
        # box_frame3.pack(side='top', fill='x', expand=False, padx=(5, 0), pady=(20, 0))
        #
        # # Frames and widgets for box frame 1
        # data_type_frame = Frame(box_frame1)
        # data_type_frame.pack(side='left', expand=False)
        #
        # file_num_frame = Frame(box_frame1)
        # file_num_frame.pack(side='left', padx=(5, 0), expand=False)
        #
        # word_frame = Frame(box_frame1)
        # word_frame.pack(side='left', padx=(5, 0), expand=False)
        #
        # bit_frame = Frame(box_frame1)
        # bit_frame.pack(side='left', padx=(5, 0), expand=False)
        #
        # data_label = Label(data_type_frame, text='Data Type')
        # data_label.pack(side='top')
        #
        # data_types = ['I', 'O', 'B', 'N', 'F']
        # self.svar_data = StringVar()
        # self.svar_data.set(data_types[0])
        # self.data_menu = OptionMenu(data_type_frame, self.svar_data, *data_types)
        # self.data_menu.pack()
        #
        # file_num_label = Label(file_num_frame, text='File #')
        # file_num_label.pack(side='top')
        #
        # self.file_num = Entry(file_num_frame, width=5)
        # self.file_num.pack(side='bottom')
        #
        # word_label = Label(word_frame, text='Word')
        # word_label.pack(side='top')
        #
        # self.word_entry = Entry(word_frame, width=5)
        # self.word_entry.pack()
        #
        # bit_label = Label(bit_frame, text='Bit')
        # bit_label.pack(side='top')
        #
        # self.bit_entry = Entry(bit_frame, width=5)
        # self.bit_entry.pack()
        #
        # # Frames and widgets for box frame 2
        # through_frame = Frame(box_frame2)
        # through_frame.pack(side='left', expand=False)
        #
        # word_frame2 = Frame(box_frame2)
        # word_frame2.pack(side='left', padx=(15, 0), expand=False)
        #
        # bit_frame2 = Frame(box_frame2)
        # bit_frame2.pack(side='left', padx=(5, 0), expand=False)
        #
        # self.through_var = IntVar()
        # through_check = Checkbutton(through_frame, text='Through', variable=self.through_var)
        # through_check.pack(side='left')
        #
        # word_label2 = Label(word_frame2, text='Word')
        # word_label2.pack(side='top')
        #
        # self.word_entry2 = Entry(word_frame2, width=5)
        # self.word_entry2.pack()
        #
        # bit_label2 = Label(bit_frame2, text='Bit')
        # bit_label2.pack(side='top')
        #
        # self.bit_entry2 = Entry(bit_frame2, width=5)
        # self.bit_entry2.pack()
        #
        # # Frames and widgets for box frame 3
        # submit_frame = Frame(box_frame3)
        # submit_frame.pack(side='top')
        #
        # submit_btn = Button(submit_frame, text='Submit', command=self.get_values)
        # submit_btn.pack(side='left')

    def set_ip_window(self):
        # create set ip address window and widgets
        self.ip_window = Toplevel(self.master)
        self.ip_window.geometry('300x100')
        self.ip_window.title('Set IP Address')

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
            self.ip_warning_window(ip_check)

    def ip_warning_window(self, warning):
        self.warn_window = Toplevel(self.master)
        self.warn_window.geometry('350x100')
        self.warn_window.title('Attention!')

        warn_label = Label(self.warn_window, text=warning)
        acknowledge_btn = Button(self.warn_window, text='Acknowledge',
                                 command=self.warn_window.destroy)

        warn_label.pack(pady=(10, 0))
        acknowledge_btn.pack(pady=(10, 0))

    def get_values_queue(self):
        self.values_display.config(state='normal')
        self.values_display.delete('1.0', END)
        if not self.xcl.tags_is_empty():
            self.values_display.insert(END, 'None' + '\n')
        else:
            for val in self.xcl.tag_queue.values():
                if len(val) != 0:
                    for i in range(len(val)):
                        self.values_display.insert(END, val[i] + '\n')
        self.values_display.config(state=DISABLED)

    def get_values(self):
        data_val = self.svar_data.get()
        file_val = self.file_num.get()
        word_val = self.word_entry.get()
        bit_val = self.bit_entry.get()
        val_list = []
        check_val = ''

        if len(file_val) > 0:
            val_list.append('1')
            if len(word_val) > 0:
                val_list.append('1')
                if len(bit_val) > 0:
                    val_list.append('1')
                else:
                    val_list.append('0')
                check_val = int(check_val.join(val_list))

                if data_val == 'N' or data_val == 'F':
                    self.NnF_add(check_val, data_val, file_val, word_val)
                if data_val == 'B':
                    self.b_add(check_val, data_val, file_val, word_val, bit_val)
            else:
                self.values_warning_window('Must have a Word value!')
        else:
            self.values_warning_window('Must have a File value!')

    def NnF_add(self, check_val, d_val, f_val, w_val):
        if check_val == 110:
            full_tag = d_val + f_val + ':' + w_val
            if self.xcl.duplicate_tags_check(full_tag):
                self.values_warning_window('Tag is already in queue!')
            else:
                self.xcl.queue_tag(full_tag)
            self.get_values_queue()
        elif check_val == 111:
            self.values_warning_window('No bit in Integer or Float type!')

    def b_add(self, check_val, d_val, f_val, w_val, b_val):
        if check_val == 111:
            full_tag = d_val + f_val + ':' + w_val + '/' + b_val
            self.xcl.queue_tag(full_tag)
            self.get_values_queue()
        elif check_val == 110:
            self.values_warning_window('Need a bit with Binary type!')

    def remove_tag(self):
        data_val = self.svar_data.get()
        file_val = self.file_num.get()
        word_val = self.word_entry.get()
        bit_val = self.bit_entry.get()

        if data_val == 'N' or data_val == 'F':
            self.xcl.remove_tag(data_val + file_val + ':' + word_val)
        elif data_val == 'B':
            self.xcl.remove_tag(data_val + file_val + ':' + word_val + '/' + bit_val)
        self.get_values_queue()

    def values_warning_window(self, warning):
        value_warning = Toplevel(self.master)
        value_warning.geometry('350x100')
        value_warning.title('Attention!')

        warn_label = Label(value_warning, text=warning)
        acknowledge_btn = Button(value_warning, text='Acknowledge',
                                 command=value_warning.destroy)

        warn_label.pack(pady=(10, 0))
        acknowledge_btn.pack(pady=(10, 0))

    def clear_warning_window(self):
        self.clear_warning = Toplevel(self.master)
        self.clear_warning.geometry('350x100')
        self.clear_warning.title('Attention!')

        warn_label = Label(self.clear_warning, text='Are you sure you want to clear the queue?')
        ok_btn = Button(self.clear_warning, text='Ok',
                        command=self.clear_queue_nclose)
        cancel_btn = Button(self.clear_warning, text='Cancel',
                            command=self.clear_warning.destroy)

        warn_label.pack(pady=(10, 0))
        ok_btn.pack(pady=(10, 0))
        cancel_btn.pack(pady=(5, 10))

    def clear_queue_nclose(self):
        self.xcl.clear_queue()
        self.get_values_queue()
        self.clear_warning.destroy()


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

        b1.pack(side='left', padx=(5, 0), pady=(5, 0))
        b2.pack(side='left', pady=(5, 0))
        b3.pack(side='left', pady=(5, 0))

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
        if result is True:
            self.ip_feedback['text'] = 'Connection Successful'
        else:
            self.ip_feedback['text'] = result


if __name__ == '__main__':
    root = Tk()
    root.title('PLC Boy')
    # root.iconbitmap(r'C:\Users\David\PycharmProjects\PLC Boy\face.png')
    main = MainWindow(root)
    main.pack(side='top', fill='both', expand=True)
    root.wm_geometry('900x600')
    root.mainloop()
