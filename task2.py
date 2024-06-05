#!python3

"""
Create a window with 3 entry widgets and 1 button.
The first 2 entry widgets allow the user to enter in the 2 short sides of a right triangle.
When the button is clicked, calculate the length of the hypotenuse and display it in the 3rd entry widget.
Any labels you need for instruction are optional.
"""
import tkinter as tk 
win = tk.Tk()

eoutput = tk.StringVar()
eoutput.set("Output goes here")

def clickFunction(event):
    print(event)
    data1 = e2.get()
    data2 = e3.get()
    data1 = float(data1)
    data2 = float(data2)
    Totaldata = ((data1**2) + (data2**2))**0.5
    e1.delete(0,tk.END)
    e1.insert(0,Totaldata)
    b1.bind("<Button>",clickFunction)

win = tk.Tk()
e1 = tk.Entry(win,width=15)
b1 = tk.Button(win, text="Click to get hyp")
e2 = tk.Entry(win,width=15)
l1 = tk.Label(win, width=15, text="Number1")
e3 = tk.Entry(win,width=15)
l2 = tk.Label(win, width=15, text="Number2")


l1.pack()
e2.pack()
l2.pack()
e3.pack()
b1.pack()
e1.pack()



win.mainloop()