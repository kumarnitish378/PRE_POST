import os
import sys
import csv
import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import E, W, N, S
from turtle import left
from mypackadge.utils import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from datetime import datetime
from tkinter import *
from PIL import ImageTk, Image
from threading import Thread
from mypackadge.initiate import InitTest
from mypackadge.v2_details import ResultAnalysia, SessionList
from mypackadge.server_add import AddServer, PageThree, ViewServer, AddServerIp
from mypackadge.ignore_error import IngnoreTextEditor
from mypackadge.comand_editor import CommandTextEditor
from mypackadge.session_compare import SessionCompare



class MainWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        # print screen size
        w = self.winfo_screenwidth()
        h = self.winfo_screenheight()

        self.title("File Syatem Extender")
        self.geometry("{}x{}".format(w, h-40))
        self.resizable(True, True)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.fl = []
        all_pages = (SessionCompare,)
        for F in all_pages:
            frame = F(container, self)
            self.fl.append(frame)
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(0)


    def show_frame(self, cont):
        frame = self.fl[0]
        frame.tkraise()


if __name__ == "__main__":
    import sys
    app = MainWindow()
    app.mainloop()
    sys.exit()
