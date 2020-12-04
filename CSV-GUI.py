import sys
import csv

from tkinter import *
       
screen = Tk()
screen.geometry('400x350')
screen.title('ROS')
heading = Label(text = 'Rakhra OS', bg = 'grey', fg = 'black', width = '500', height = '3')
heading.pack()

def save_info():
    item1_info = item_1.get()
    sale1_info = sale_1.get()
    sales1_info = sales_1.get()
    profit1_info = sales1_info - sale1_info
    with open('file.csv', 'w', newline = '') as f:
        fieldnames = ['Item Name', 'My Cost', 'Sale Cost', 'Profit']
        write = csv.DictWriter(f, fieldnames = fieldnames)
        write.writeheader()
        write.writerow({'Item Name' : item1_info, 'My Cost' : sale1_info, 'Sale Cost' : sales1_info, 'Profit' : profit1_info})
        screen.destroy()

item1_text = Label(text = 'Item 1: ')
sale1_text = Label(text = 'How much did you pay for item 1: ')
sales1_text = Label(text = 'How much did you sell item 1 for: ')
item1_text.place(x=5,y=55)
sale1_text.place(x=5,y=95)
sales1_text.place(x=5,y=135)

item_1 = StringVar()
sale_1 = IntVar()
sales_1 = IntVar()


item1_entry = Entry(textvariable = item_1)
sale1_entry = Entry(textvariable = sale_1)
sales1_entry = Entry(textvariable = sales_1)
item1_entry.place(x=5,y=75)
sale1_entry.place(x=5,y=115)
sales1_entry.place(x=5,y=155)

finish = Button(screen, text = 'Continue', width = '54', height = '5', command = save_info)
finish.place(x=5,y=250)

screen.mainloop()

