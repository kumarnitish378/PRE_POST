import os
import sys
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
from random import randint, choice
import mypackadge.VARIABLES as var
import csv
from tkinter import filedialog, Text
from time import sleep

server_name = ""

class Abcd:
    def __init__(self):
        pass

    def get_data(self):
        for i in range(100):
            yield f"{i}\n"
            sleep(0.1)

class ComparePrePost:
    def __init__(self, pre, post, res, rt, root=""):
        self.root = root
        self.pre = pre
        self.post = post
        self.res = res
        self.rt = rt
        self.ig_cmd = [cmd.replace("\n", "") for cmd in open("settings/cmd_ignore.txt").readlines()]
        self.pre_files = [self.pre + "/" + i for i in  os.listdir(self.root + self.pre)]
        self.post_files = [self.post + "/" + i for i in  os.listdir(self.root + self.post)]
        self.ignore_files = []

    def setting_initial(self):
        if pre_files.__len__() != self.post_files.__len__():
            print("There is some file missing in folder.")
            print(f"{self.pre_files.__len__()} Files in pre test but,")
            print(f"{self.post_files.__len__()} Files in post test")
            self.pre_test = os.listdir(self.root + self.pre)
            self.post_test = os.listdir(self.root + self.post)
            for pfile in self.pre_test:
                if pfile not in self.post_test:
                    print(f"NOT FOUND in Post test: {pfile}")
                    self.ignore_files.append(self.pre + "/" + pfile)
                
                if pfile not in self.pre_test:
                    print(f"NOT FOUND in Pre test: {pfile}")
                    self.ignore_files.append(self.post + "/" + pfile)
            
            # Additional line of code.
            # if "y" not in input("Do you want to skip the file(y/n)?"):
            #     sys.exit(0)

        # remove Unmatched filename from files list
        for igf in self.ignore_files:
            if igf in self.pre_files:
                print("pre", self.pre_files.index(igf))
                self.pre_files.pop(self.pre_files.index(igf))

            if igf in self.post_files:
                print("post", self.post_files.index(igf))
                self.post_files.pop(self.post_files.index(igf))

        print(f"pre length: {self.pre_files.__len__()}")
        print(f"post length: {self.post_files.__len__()}")
        if self.post_files.__len__() == 0:
            print("Ther is no files fo compare")
            return "There is No File to compare"


    def compare_files(self):
        # Now Compareing The Files
        compare_result = [["Sn", "pre test", "post test", "result", "result_2", "error"]]
        index = 0
        success_falg = True
        for pre, post in zip(self.pre_files, self.post_files):
            with open(pre, "r") as pf:
                # pre_read = "".join(sorted(pf.read()))
                pre_read = pf.read()
            
            with open(post, "r") as rf:
                # post_read = "".join(sorted(rf.read()))
                post_read = rf.read()

            if pre_read == post_read:
                print("Succusses")
                yield "Succusses"
                compare_result.append([index, pre.split("/")[-1], post.split("/")[-1], "success", 1, 0])
            else:
                print(f"fails in {post}")
                print("Filed")
                yield f"fails in {post}"
                compare_result.append([index, pre.split("/")[-1], post.split("/")[-1], "filed", 0, 0])
                success_falg = False if post.split(".")[0] not in ig_cmd else True
            index += 1
            open(f"{RT}resut.txt", 'w').write("Success") if success_falg else open(f"{RT}resut.txt", 'w').write("Faild")
            print("Save Result in the result.txt file")


class SessionCompare(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        main_frame_bg = "#ffffff"  # "#010530"
        login_section_bg = "#3400f0"
        font_color = "#01011f"  # "#E1341E"
        self.server_name = ""
        self.server_ip = ""

        self.controller = controller
        self.configure(bg=main_frame_bg)
        # self.rowconfigure(0, weight=1)
        # self.columnconfigure(0, weight=1)
        font = tkFont.Font(family="Helvetica", size=16, weight="bold")
        out_font = tkFont.Font(family="Helvetica", size=12, weight="bold")
        s_font = tkFont.Font(family="Helvetica", size=26, weight="bold")
        font_for_list = tkFont.Font(family="Helvetica", size=16, weight="bold")
        self.conn_flag = False
        self.commad_list_for = []
        self.current_command = 0
        self.ypad = 20
        self.xpad = 30
        self.border = "#00D2FF"
        self.select_session = False

        self.btn_width = 150
        self.btn_height = 150

        # Session List ============= 
        self.sframe = Frame(self)
        self.sframe.pack(pady=20, padx=50, side=LEFT)

        self.lst = Label(self.sframe, text="Sessions", font=s_font)
        self.lst.grid(row=0, column=0, padx=50, pady=10)

        self.session_list = Listbox(self.sframe, bg="#ffffff",
                                   fg= "#000000", font=font_for_list, height=20, width=20)
        self.session_list.grid(row=1, column=0, padx=5, pady=20, rowspan=2, sticky=E+W+N+S)
        
         
        # Onselect Event
        self.session_list.bind('<<ListboxSelect>>', self.onselect)

        scr = Scrollbar(self.sframe)
        scr.grid(row=1, column=1, sticky=E+W+N+S)

        # Contecting to the listbox
        scr.config(command=self.session_list.yview)
        self.session_list.config(yscrollcommand=scr.set)
        # Fetching Server List from File

        self.sessions = os.listdir("logs")
        for line in self.sessions:
            self.session_list.insert(END, line.strip())

        self.next = Button(self, text="Home", width=10, border=0, bg="#00e3f2", height=5,
                        command=lambda : self.controller.show_frame(0))
        self.next.pack(pady=2, side=LEFT)

        self.refresh = Button(self, text="Refresh", width=10, border=0, bg="#00e3f2", height=5,
                        command=self.update_session)
        self.refresh.pack(pady=20, padx=10, side=LEFT)
        
        self.comp = Button(self, text="Compare", width=10, border=0, bg="#00e3f2", height=5,
                        command=lambda : self.insert_log())
        self.comp.pack(pady=20, padx=10, side=LEFT)
        
        # Sessin Details ============
        self.frame = tk.LabelFrame(self, text="Output Logs")
        self.frame.pack(pady=20, side=RIGHT)

        self.out_area = Text(self.frame, height=30, width=80)
        self.out_area.pack(side=LEFT)

        self.scrollbar = tk.Scrollbar(self.frame, command=self.out_area.yview)
        # self.scrollbar.grid(row=0, column=1, sticky="nsew")
        self.scrollbar.pack(side="left")

        self.out_area.config(yscrollcommand=self.scrollbar.set)

    
    def onselect(self, event):
        print("on select")
        w = event.widget
        print(f"Selection by mouse: {w.curselection()}")
        if len(w.curselection()) == 0:
            return 0
        index = int(w.curselection()[0])
        value = w.get(index)
        print('You selected item "%s"' % (value))
        var.SESSION = value
        self.server_name = value
        # data table
        # get all server ip
        self.server = os.listdir(f"logs\\{value}")
        print("Server List: ", self.server)


    def update_session(self):
        self.sessions = os.listdir("logs")
        self.session_list.delete(0, tk.END)
        for line in self.sessions:
            self.session_list.insert(END, line.strip())


    def insert_log(self):
        pass