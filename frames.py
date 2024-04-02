import tkinter as tk

def show_frame(frame_name):
    frames = {"Home": Home, "Statistics": Statistics, "Settings": Settings}
    frame = frames[frame_name]
    frame.tkraise()

    
    

def create_buttons():
    go_Home = tk.Button(text="Home", command=lambda: show_frame("Home"))
    go_Home.grid(row=0, column=1, sticky="nsew")

    go_Statistics = tk.Button(text="Statistics", command=lambda: show_frame("Statistics"))
    go_Statistics.grid(row=0, column=2, sticky="nsew")

    go_Settings = tk.Button(text="Settings", command=lambda: show_frame("Settings"))
    go_Settings.grid(row=0, column=3, sticky="nsew")  



class Home(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")
        
        create_buttons()

     
class Statistics(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")
        
        create_buttons()
   

class Settings(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.grid(row=0, column=0, sticky="nsew")
        
        create_buttons()