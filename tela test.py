from tkinter import *
root = Tk()

e = Entry(root, width=35, borderwidth=5)
e.grid(row= 0, column=0, columnspan=3,padx=10, pady=10)

def buttonClick(number):
    #e.delete(0,END)
    e.insert(0, number)
    return



button1 = Button(text= "1", padx= 40, pady=20,borderwidth=5, command=lambda: buttonClick(1))
button2 = Button(text= "2", padx= 40, pady=20,borderwidth=5, command= lambda:buttonClick(2))
button3 = Button(text= "3", padx= 40, pady=20,borderwidth=5, command= lambda: buttonClick(3))
button4 = Button(text= "4", padx= 40, pady=20,borderwidth=5, command= lambda: buttonClick(4))
button5 = Button(text= "5", padx= 40, pady=20,borderwidth=5, command= lambda: buttonClick(5))
button6 = Button(text= "6", padx= 40, pady=20,borderwidth=5, command= lambda: buttonClick(6))
button7 = Button(text= "7", padx= 40, pady=20,borderwidth=5, command=  lambda: buttonClick(7))
button8 = Button(text= "8", padx= 40, pady=20,borderwidth=5, command= lambda: buttonClick(8))
button9 = Button(text= "9", padx= 40, pady=20,borderwidth=5, command= lambda: buttonClick(9))
button0 = Button(text= "0", padx= 40, pady=20,borderwidth=5, command=  lambda: buttonClick(0))
buttonadd = Button(text = "+", padx=40, pady= 20, borderwidth=5, command= buttonClick)
buttonEqual = Button(text = "=", padx=89, pady= 20, borderwidth=5, command= buttonClick)
buttonClear = Button(text = "Clear", padx=79, pady= 20, borderwidth=5, command= buttonClick)

button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonadd.grid(row=5, column=0)
buttonClear.grid(row= 5, column=1, columnspan=2)

buttonEqual.grid(row=4, column=1,columnspan=2)
root.mainloop()