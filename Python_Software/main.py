"""
Generic python software with tkinter
Window with fixed size and not resizable
Has a menu, with different frames.
A form to add something, saves all info temporally and shows this data in main screen.
Finally, has an exit option.
"""

from tkinter import *
from tkinter import ttk

# Define window
from tkinter import Label

window = Tk()
window.geometry('800x600')
window.minsize(600, 400)
window.title('Geberic Python Software')
window.resizable(0,0)

# Screens
def home():

    # Build home screen
    home_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=150,
        pady=20
    )
    home_label.grid(row=0,column=0)

    items_box.grid(row=1)

    # List items
    for i in items:
        if len(i) == 2:
            i.append('added')
            items_box.insert('', 0, text=i[0], values=(i[1]))


    # Delete other screens
    add_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    add_frame.grid_remove()


def add():

    add_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=150,
        pady=20
    )
    add_label.grid(row=0, column=0, columnspan=2)

    add_frame.grid(row=1)
    add_name_label.grid(row=1, column=0, padx=5, pady=5)
    add_name_entry.grid(row=1, column=1, padx=5, pady=5)

    add_details_label.grid(row=2, column=0, padx=5, pady=5)
    add_details_entry.grid(row=2, column=1, padx=5, pady=5)

    add_separator.grid(row=3)

    btn.grid(row=4, column=1, sticky=W)
    btn.config(padx=15, pady=5, bg='black', fg='white')

    # Delete other screens
    home_label.grid_remove()
    info_label.grid_remove()
    data_label.grid_remove()
    items_box.grid_remove()


def info():

    info_label.config(
        fg='white',
        bg='black',
        font=('Arial', 30),
        padx=150,
        pady=20
    )
    info_label.grid(row=0, column=0)

    data_label.grid(row=1, column=0)

    # Delete other screens
    add_label.grid_remove()
    home_label.grid_remove()
    add_frame.grid_remove()
    items_box.grid_remove()

def add_item():
    items.append([
        name_data.get(),
        details_data.get()
    ])

    name_data.set('')
    details_data.set('')

    home()



# variables
items = []
name_data = StringVar()
details_data = StringVar()

# Define screen variable (Home)
home_label: Label = Label(window, text='Index')

items_box = ttk.Treeview(height=12, columns=2)
items_box.grid(row=1, column=0, columnspan=2)
items_box.heading('#0', text='Name', anchor=W)
items_box.heading('#1', text='Details', anchor=W)


# Define screen variable (Add)
add_label: Label = Label(window, text='Add')

# Form fields
add_frame = Frame(window)

add_name_label = Label(add_frame, text='Name')
add_name_entry = Entry(add_frame, textvariable=name_data)

add_details_label = Label(add_frame, text='Details')
add_details_entry = Entry(add_frame, textvariable=details_data)

add_separator = Label(add_frame)

btn = Button(add_frame, text='Save', command=add_item)

# Define screen variables (Info & Data)
info_label: Label = Label(window, text='Info')
data_label: Label = Label(window, text='Created by Víctor León - 2022 ')

# Load index screen
home()

# Create menu
top_menu = Menu(window)

# Dropdown menu "add"
drop = Menu(top_menu, tearoff=0)
drop.add_cascade(label='Add Item', command=add)

# Menu options
top_menu.add_command(label='Index', command=home)
top_menu.add_cascade(label='Add', menu=drop)
top_menu.add_command(label='Info', command=info)
top_menu.add_command(label='Exit', command=window.quit)

# Load menu
window.config(menu=top_menu)


# Load window
window.mainloop()