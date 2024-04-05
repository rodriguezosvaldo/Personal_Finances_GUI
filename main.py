from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Personal Finances")
root.geometry("500x500")

tabs = ttk.Notebook(root)
tabs.pack(pady=2)

frame_home = Frame(tabs, width=500, height=500, bg="gray")
frame_home.pack(fill="both", expand=1)
frame_statistics = Frame(tabs, width=500, height=500, bg="blue")
frame_statistics.pack(fill="both", expand=1)
frame_settings = Frame(tabs, width=500, height=500, bg="green")
frame_settings.pack(fill="both", expand=1)

frame_chart_income_outcome = Frame(frame_statistics, width=500, height=100, bg="red")
frame_chart_income_outcome.pack(fill="both", expand=1)
frame_chart_categories = Frame(frame_statistics, width=500, height=100, bg="yellow")
frame_chart_categories.pack(fill="both", expand=1)
frame_tendency_categories = Frame(frame_statistics, width=500, height=100, bg="purple")
frame_tendency_categories.pack(fill="both", expand=1)

tabs.add(frame_home, text="Home")
tabs.add(frame_statistics, text="Statistics")
tabs.add(frame_settings, text="Settings")

button_cards = Button(frame_home, text="+")
button_cards.grid(row=0, column=0, padx=10, pady=50)
button_cash = Button(frame_home, text="+")
button_cash.grid(row=1, column=0, padx=10, pady=50)
button_savings = Button(frame_home, text="+")
button_savings.grid(row=2, column=0, padx=10, pady=50)
button_income_outcome_yearly = Button(frame_chart_income_outcome, text="Yearly")
button_income_outcome_yearly.grid(row=0, column=0, padx=10, pady=10)
button_income_outcome_monthly = Button(frame_chart_income_outcome, text="Monthly")
button_income_outcome_monthly.grid(row=0, column=1, padx=10, pady=10)
button_income_outcome_weekly = Button(frame_chart_income_outcome, text="Weekly")
button_income_outcome_weekly.grid(row=0, column=2, padx=10, pady=10)

label_amount_cards = Label(frame_home, text="Cards               Amount")
label_amount_cards.grid(row=0, column=1)
label_amount_cash = Label(frame_home, text="Cash               Amount")
label_amount_cash.grid(row=1, column=1)
label_amount_savings = Label(frame_home, text="Savings               Amount")
label_amount_savings.grid(row=2, column=1)
label_chart_income_outcome = Label(frame_chart_income_outcome, text="Income/Outcome")
label_chart_income_outcome.grid(row=1, column=0, padx=10, pady=10, ) 
label_chart_categories = Label(frame_chart_categories, text="Categories")
label_chart_categories.pack()
label_tendency_categories = Label(frame_tendency_categories, text="Tendency")
label_tendency_categories.pack()



root.mainloop()
