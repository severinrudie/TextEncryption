#Authors = Severin and Chris
import os
import tkinter as tk
import math as math
import random as ran

TITLE_FONT = ("Helvetica", 18, "bold")


class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)

        self.wm_title('Severin and Chris\'s Encryption Tool')

        #-----Menu Bar------
        menu_bar = MenuBar(self)
        self.config(menu=menu_bar)

        #-----Main Frame----
        main_frame = tk.Frame(self)
        main_frame.pack(side='top', fill='both', expand=True)
        main_frame.config(bg='red')
        main_frame.grid_columnconfigure(0, minsize=400, weight=1)
        main_frame.grid_rowconfigure(0, minsize=250, weight=1)


        #-----Frames List----
        self.frames = {}
        for name in (HomePage, KeyGenPage, EncryptionPage):
            frame = name(main_frame, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(HomePage)

    def show_frame(self, x):
        frame = self.frames[x]
        frame.tkraise()


class MenuBar(tk.Menu):
    def __init__(self, parent):
        tk.Menu.__init__(self, parent)

        file_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='File', menu=file_menu)
        help_menu = tk.Menu(self, tearoff=False)
        self.add_cascade(label='Help', menu=help_menu)

        file_menu.add_command(label='KeyGenerator', command=lambda x=KeyGenPage: parent.show_frame(x))
        file_menu.add_command(label='Encryption', command=lambda x=EncryptionPage: parent.show_frame(x))
        file_menu.add_separator()
        file_menu.add_command(label='Exit', command=self.quit)

        help_menu.add_command(label='View Readme', command=lambda x='notepad.exe ReadMe.txt': os.system(x))


class HomePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        for X in range(4):
            self.columnconfigure(X, minsize=100, weight=1)
        for X in range(5):
            self.rowconfigure(X, minsize=50, weight=1)

        label = tk.Label(self, text='Welcome to S&C\'s Encryption Tool!', font=TITLE_FONT)
        label.grid(row=0, column=0, columnspan=4, sticky='s')

        kgbtn = tk.Button(self, text='Key Generator', command=lambda x=KeyGenPage: controller.show_frame(x))
        kgbtn.grid(row=3, column=1, sticky='n')

        edbtn = tk.Button(self, text='File Encryption', command=lambda x=EncryptionPage: controller.show_frame(x))
        edbtn.grid(row=3, column=2, sticky='n')


class KeyGenPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        for X in range(4):
            self.columnconfigure(X, minsize=100, weight=1)
        for X in range(5):
            self.rowconfigure(X, minsize=50, weight=1)

        label = tk.Label(self, text='AES Key Generation', font=TITLE_FONT)
        label.grid(row=0, column=1, columnspan=2, sticky='s')

        keynamelabel = tk.Label(self, text='Enter this Key\'s Name')
        keynamelabel.grid(row=1, column=1, columnspan=2, sticky='s')
        keyname = tk.Entry(self, text='Enter this Key\'s Name')
        keyname.grid(row=2, column=1, columnspan=2, sticky='n')

        btn1 = tk.Button(self, text='Gen: 128 Bit Key')
        btn2 = tk.Button(self, text='Gen: 256 Bit Key')
        btn1.grid(row=3, column=1)
        btn2.grid(row=3, column=2)


class EncryptionPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        for X in range(4):
            self.columnconfigure(X, minsize=100, weight=1)
        for X in range(5):
            self.rowconfigure(X, minsize=50, weight=1)

        label = tk.Label(self, text='File Encryption/Decryption', font=TITLE_FONT)
        label.grid(row=0, column=1, columnspan=2, sticky='s')

        entrylabel = tk.Label(self, text='Select the .TXT File to Encrypt/Decrypt')
        entrylabel.grid(row=1, column=1, columnspan=2, sticky='s')

        fileentry = tk.Entry(self, width=40)
        fileentry.grid(row=2, column=1, columnspan=2, sticky='nsw', pady=13, padx=3)

        browsebtn = tk.Button(self, text='Browse...')
        browsebtn.grid(row=2, column=2, sticky='e')

        encryptbutton = tk.Button(self, text='Encrypt File')
        encryptbutton.grid(row=3, column=1)

        decryptbutton = tk.Button(self, text='Decrypt File')
        decryptbutton.grid(row=3, column=2)


app = MainWindow()
app.mainloop()