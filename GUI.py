import tkinter
from tkinter import font
import Alarm


class GUI(tkinter.Tk):

    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)

        self.title_font = font.Font(family='Helvetica', size=18, weight="bold", slant="italic")
        container = tkinter.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (HomePage, NewAlarm):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("HomePage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


class HomePage(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        label = tkinter.Label(self, text="Alarms", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)

        button1 = tkinter.Button(self, text="Create a new alarm", command=lambda: controller.show_frame("NewAlarm"))
        button1.pack()


class NewAlarm(tkinter.Frame):

    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        label = tkinter.Label(self, text="Create a New Alarm", font=controller.title_font)
        label.pack(side="top", fill="x", pady=10)
        button = tkinter.Button(self, text="Cancel", command=lambda: controller.show_frame("HomePage"))
        button.pack()
        
