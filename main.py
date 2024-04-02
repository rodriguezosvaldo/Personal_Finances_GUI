import tkinter as tk
from frames import *

class Manager(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Personal Finances")
        self.geometry("800x600")

        



        home_frame = Home(self, self)
        home_frame.grid(row=0, column=0, sticky="nsew")

        statistics_frame = Statistics(self, self)
        statistics_frame.grid(row=0, column=0, sticky="nsew")

        settings_frame = Settings(self, self)
        settings_frame.grid(row=0, column=0, sticky="nsew")
        
    
        



        
        

    
    
    
        

if __name__ == "__main__":
    app = Manager()
    app.mainloop()









