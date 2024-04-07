from tkinter import *
from tkinter import ttk


root = Tk()
root.title("Personal Finances")
root.geometry("400x400")

BACKGROUND_COLOR = "white"
root.configure(bg=BACKGROUND_COLOR)

menu = Menu(root)
root.config(menu=menu)

def create_home():
    home_frame = Frame(root, bg=BACKGROUND_COLOR)
    home_frame.pack(fill="both", expand=1)
    for child in root.winfo_children():
        if child != home_frame:
            child.pack_forget()
    home_frame.grid_columnconfigure(0, weight=1)
    home_frame.grid_columnconfigure(1, weight=1)
    home_frame.grid_rowconfigure(0, weight=1)
    home_frame.grid_rowconfigure(1, weight=1)
    home_frame.grid_rowconfigure(2, weight=1)
    home_frame.grid_rowconfigure(3, weight=1)
    label_cards = Label(home_frame, text="Cards", bg=BACKGROUND_COLOR)
    label_cards.grid(row=0, column=0, sticky="nsew")
    label_cash = Label(home_frame, text="Cash", bg=BACKGROUND_COLOR)
    label_cash.grid(row=1, column=0, sticky="nsew")
    label_savings = Label(home_frame, text="Savings", bg=BACKGROUND_COLOR)
    label_savings.grid(row=2, column=0, sticky="nsew")
    label_total = Label(home_frame, text="Total", bg=BACKGROUND_COLOR)
    label_total.grid(row=3, column=0, sticky="nsew")
    label_amount_cards = Label(home_frame, text="Amount", bg=BACKGROUND_COLOR)
    label_amount_cards.grid(row=0, column=1, sticky="nsew")
    label_amount_cash = Label(home_frame, text="Amount", bg=BACKGROUND_COLOR)
    label_amount_cash.grid(row=1, column=1, sticky="nsew")
    label_amount_savings = Label(home_frame, text="Amount", bg=BACKGROUND_COLOR)
    label_amount_savings.grid(row=2, column=1, sticky="nsew")
    label_amount_total = Label(home_frame, text="Amount", bg=BACKGROUND_COLOR)
    label_amount_total.grid(row=3, column=1, sticky="nsew")

create_home()

def create_card():
    card_frame = Frame(root, bg=BACKGROUND_COLOR)
    card_frame.pack(fill="both", expand=1)
    for child in root.winfo_children():
        if child != card_frame:
            child.pack_forget()
    
    card_frame.grid_columnconfigure(0, weight=1)
    card_frame.grid_columnconfigure(1, weight=1)
    card_frame.grid_rowconfigure(0, weight=1)
    card_frame.grid_rowconfigure(1, weight=1)
    card_frame.grid_rowconfigure(2, weight=1)

    label_name = Label(card_frame, text="Card Account Name")
    label_name.grid(row=0, column=0, padx=5, sticky="e")
    entry_name = Entry(card_frame)
    entry_name.grid(row=0, column=1, sticky="w")
    entry_name.focus()
    label_amount = Label(card_frame, text="Amount")
    label_amount.grid(row=1, column=0, padx=5, sticky="e")
    entry_amount = Entry(card_frame)
    entry_amount.grid(row=1, column=1, sticky="w")
    button_create = Button(card_frame, text="Create")
    button_create.grid(row=2, column=0)
    button_cancel = Button(card_frame, text="Cancel", command=create_home)
    button_cancel.grid(row=2, column=1)

def create_cash():
    cash_frame = Frame(root, bg=BACKGROUND_COLOR)
    cash_frame.pack(fill="both", expand=1)
    for child in root.winfo_children():
        if child != cash_frame:
            child.pack_forget()

    cash_frame.grid_columnconfigure(0, weight=1)
    cash_frame.grid_columnconfigure(1, weight=1)
    cash_frame.grid_rowconfigure(0, weight=1)
    cash_frame.grid_rowconfigure(1, weight=1)
    cash_frame.grid_rowconfigure(2, weight=1)

    label_name = Label(cash_frame, text="Cash Account Name")
    label_name.grid(row=0, column=0, padx=5, sticky="e")
    entry_name = Entry(cash_frame)
    entry_name.grid(row=0, column=1, sticky="w")
    entry_name.focus()
    label_amount = Label(cash_frame, text="Amount")
    label_amount.grid(row=1, column=0, padx=5, sticky="e")
    entry_amount = Entry(cash_frame)
    entry_amount.grid(row=1, column=1, sticky="w")
    button_create = Button(cash_frame, text="Create")
    button_create.grid(row=2, column=0)
    button_cancel = Button(cash_frame, text="Cancel", command=create_home)
    button_cancel.grid(row=2, column=1)

def create_savings():
    savings_frame = Frame(root, bg=BACKGROUND_COLOR)
    savings_frame.pack(fill="both", expand=1)
    for child in root.winfo_children():
        if child != savings_frame:
            child.pack_forget()

    savings_frame.grid_columnconfigure(0, weight=1)
    savings_frame.grid_columnconfigure(1, weight=1)
    savings_frame.grid_rowconfigure(0, weight=1)
    savings_frame.grid_rowconfigure(1, weight=1)
    savings_frame.grid_rowconfigure(2, weight=1)

    label_name = Label(savings_frame, text="Savings Account Name")
    label_name.grid(row=0, column=0, padx=5, sticky="e")
    entry_name = Entry(savings_frame)
    entry_name.grid(row=0, column=1, sticky="w")
    entry_name.focus()
    label_amount = Label(savings_frame, text="Amount")
    label_amount.grid(row=1, column=0, padx=5, sticky="e")
    entry_amount = Entry(savings_frame)
    entry_amount.grid(row=1, column=1, sticky="w")
    button_create = Button(savings_frame, text="Create")
    button_create.grid(row=2, column=0)
    button_cancel = Button(savings_frame, text="Cancel", command=create_home)
    button_cancel.grid(row=2, column=1)

def create_income_outcome():
    income_outcome_frame = Frame(root, bg=BACKGROUND_COLOR)
    income_outcome_frame.pack(fill="both", expand=1)
    for child in root.winfo_children():
        if child != income_outcome_frame:
            child.pack_forget()

    income_outcome_frame.grid_columnconfigure(0, weight=1)
    income_outcome_frame.grid_rowconfigure(0, weight=1)
    income_outcome_frame.grid_rowconfigure(1, weight=50)
    income_outcome_frame.grid_rowconfigure(2, weight=1)
    income_outcome_frame.grid_rowconfigure(3, weight=1)
    income_outcome_frame.grid_rowconfigure(4, weight=1)
    income_outcome_frame.grid_rowconfigure(5, weight=1)
    
    label_income_outcome = Label(income_outcome_frame, text="Income/Outcome")
    label_income_outcome.grid(row=0, column=0, pady=2, sticky="n" )

    label_chart_income_outcome = Label(income_outcome_frame, text="Income/Outcome CHART")
    label_chart_income_outcome.grid(row=1, column=0) 

    global rad_income_outcome
    rad_income_outcome = IntVar()
    rad_income_outcome.set(1)

    radiobutton_income_outcome_weekly = Radiobutton(income_outcome_frame, text="Weekly", variable=rad_income_outcome, value=1)
    radiobutton_income_outcome_weekly.grid(row=2, column=0, pady=1, sticky="s")
    radiobutton_income_outcome_monthly = Radiobutton(income_outcome_frame, text="Monthly", variable=rad_income_outcome, value=2)
    radiobutton_income_outcome_monthly.grid(row=3, column=0, pady=1, sticky="s")
    radiobutton_income_outcome_yearly = Radiobutton(income_outcome_frame, text="Yearly", variable=rad_income_outcome, value=3)
    radiobutton_income_outcome_yearly.grid(row=4, column=0, pady=1, sticky="s")
  
    button_back_home = Button(income_outcome_frame, text="Back to Home", command=create_home)
    button_back_home.grid(row=5, column=0, pady=3)

def create_categories():
    categories_frame = Frame(root, bg=BACKGROUND_COLOR)
    categories_frame.pack(fill="both", expand=1)
    for child in root.winfo_children():
        if child != categories_frame:
            child.pack_forget()

    categories_frame.grid_columnconfigure(0, weight=1)
    categories_frame.grid_rowconfigure(0, weight=1)
    categories_frame.grid_rowconfigure(1, weight=50)
    categories_frame.grid_rowconfigure(2, weight=1)
    categories_frame.grid_rowconfigure(3, weight=1)
    categories_frame.grid_rowconfigure(4, weight=1)
    categories_frame.grid_rowconfigure(5, weight=1)

    label_categories = Label(categories_frame, text="Categories")
    label_categories.grid(row=0, column=0, pady=2, sticky="n")

    label_chart_categories = Label(categories_frame, text="Categories CHART")
    label_chart_categories.grid(row=1, column=0)

    global rad_categories
    rad_categories = IntVar()
    rad_categories.set(1)

    radiobutton_categories_weekly = Radiobutton(categories_frame, text="Weekly", variable=rad_categories, value=1)
    radiobutton_categories_weekly.grid(row=2, column=0, pady=1, sticky="s")
    radiobutton_categories_monthly = Radiobutton(categories_frame, text="Monthly", variable=rad_categories, value=2)
    radiobutton_categories_monthly.grid(row=3, column=0, pady=1, sticky="s")
    radiobutton_categories_yearly = Radiobutton(categories_frame, text="Yearly", variable=rad_categories, value=3)
    radiobutton_categories_yearly.grid(row=4, column=0, pady=1, sticky="s")

    button_back_home = Button(categories_frame, text="Back to Home", command=create_home)
    button_back_home.grid(row=5, column=0, pady=3)

def create_tendency():
    tendency_frame = Frame(root, bg=BACKGROUND_COLOR)
    tendency_frame.pack(fill="both", expand=1) 
    for child in root.winfo_children():
        if child != tendency_frame:
            child.pack_forget() 

    tendency_frame.grid_columnconfigure(0, weight=1)
    tendency_frame.grid_rowconfigure(0, weight=1)
    tendency_frame.grid_rowconfigure(1, weight=50)
    tendency_frame.grid_rowconfigure(2, weight=1)
    tendency_frame.grid_rowconfigure(3, weight=1)
    tendency_frame.grid_rowconfigure(4, weight=1)
    tendency_frame.grid_rowconfigure(5, weight=1)

    label_tendency = Label(tendency_frame, text="Tendency")
    label_tendency.grid(row=0, column=0, pady=2, sticky="n")
    
    label_tendency_chart = Label(tendency_frame, text="Tendency CHART")
    label_tendency_chart.grid(row=1, column=0)

    global rad_tendency
    rad_tendency = IntVar()
    rad_tendency.set(1)

    radiobutton_tendency_weekly = Radiobutton(tendency_frame, text="Weekly", variable=rad_tendency, value=1)
    radiobutton_tendency_weekly.grid(row=2, column=0, pady=1, sticky="s")
    radiobutton_tendency_monthly = Radiobutton(tendency_frame, text="Monthly", variable=rad_tendency, value=2)
    radiobutton_tendency_monthly.grid(row=3, column=0, pady=1, sticky="s")
    radiobutton_tendency_yearly = Radiobutton(tendency_frame, text="Yearly", variable=rad_tendency, value=3)
    radiobutton_tendency_yearly.grid(row=4, column=0, pady=1, sticky="s")

    button_back_home = Button(tendency_frame, text="Back to Home", command=create_home)
    button_back_home.grid(row=5, column=0, pady=3)

home_menu = Menu(menu)
menu.add_cascade(label="Home", menu=home_menu)
home_menu.add_command(label="New Card Account", command=create_card)
home_menu.add_separator()
home_menu.add_command(label="New Cash Account", command=create_cash)
home_menu.add_separator()
home_menu.add_command(label="New Savings Account", command=create_savings)
home_menu.add_separator()
home_menu.add_command(label="Exit", command=root.quit)

statistics_menu = Menu(menu)
menu.add_cascade(label="Statistics", menu=statistics_menu)
statistics_menu.add_command(label="Income/Outcome", command=create_income_outcome)
statistics_menu.add_separator()
statistics_menu.add_command(label="Categories", command=create_categories)
statistics_menu.add_separator()
statistics_menu.add_command(label="Tendency", command=create_tendency)

settings_menu = Menu(menu)
menu.add_cascade(label="Settings", menu=settings_menu)
settings_menu.add_command(label="Export data")






root.mainloop()
