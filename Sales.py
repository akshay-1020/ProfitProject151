from tkinter import *

root = Tk()
root.geometry("800x400")
root.title("Sales")

lbl1 = Label(root)
lbl2 = Label(root)
lbl3 = Label(root)
lbl4 = Label(root)

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
profits = (45756, 53453, 4536, 4654, 875968, 45453, 45678, 45678909, 876787657, 56545, 76566, 34567876)

lbl1["text"] = str(months)
lbl2["text"] = str(profits)

lbl1.place(relx=0.5, rely = 0.3, anchor = CENTER)
lbl2.place(relx=0.5, rely = 0.4, anchor = CENTER)
lbl3.place(relx=0.5, rely = 0.6, anchor = CENTER)
lbl4.place(relx=0.5, rely = 0.8, anchor = CENTER)

def maximum():
    maxp = max(profits)
    maxindex = profits.index(maxp)
    maxmonth = months[maxindex]
    lbl3["text"] = "The maximum profit was " + str(maxp) + ", and it was recorded in the month of " + str(maxmonth)

def minimum():
    minp = min(profits)
    minindex = profits.index(minp)
    minmonth = months[minindex]
    lbl4["text"] = "The minimum profit was " + str(minp) + ", and it was recorded in the month of " + str(minmonth)

btn1 = Button(root, text="Show Maximum Profit", command=maximum)
btn2 = Button(root, text="Show Minimum Profit", command=minimum)

btn1.place(relx=0.5, rely=0.5, anchor=CENTER)
btn2.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()