"""
##### Task 1
Create entry widets to allow user to enter their:
* name
* student number
* grade

Create a button so that when they click on the button, it states all of the information in a 4th entry widget
"""
import tkinter as tk 

def run(e):
   
    print("This does not show up on your gui")
    print(f"The details of the event are {e}")
    data1 = e2.get()
    data2 = e3.get()
    data3 = e4.get()
    Totaldata = " Name :" + data1+ " Student number :" + data2 + " Grade :" + data3 
    e1.delete(0,tk.END)
    e1.insert(0,Totaldata)
   
    
   

win = tk.Tk()
e1 = tk.Entry(win,width=75)
b1 = tk.Button(win, text="Click to change the text")
e2 = tk.Entry(win,width=15)
l1 = tk.Label(win, width=15, text="Name")
e3 = tk.Entry(win,width=15)
l2 = tk.Label(win, width=15, text="student number")
e4 = tk.Entry(win,width=15)
l3 = tk.Label(win, width=15, text="grade")
b1.bind("<Button-1>",run)

l1.pack()
e2.pack()
l2.pack()
e3.pack()
l3.pack()
e4.pack()
b1.pack()
e1.pack()



win.mainloop()