from tkinter import *

root = Tk()
root.title("Simple Calculator")

def OnNumButtonClick(num : int):
    current = e.get()
    e.delete(0,END)
    e.insert(0, str(current) + str(num))
    
def OnClearButtonClick():
    e.delete(0, END)
    
def OnOperationButtonClick(operation : CHAR):
    global operator
    operator = operation
    global num1 
    num1 = int(e.get())
    e.delete(0, END)

def OnEqualButtonClick():
    global num2
    num2 = int(e.get())
    e.delete(0, END)
    if operator == '+':
        e.insert(0, str(num1 + num2))
    elif operator == '-':
        e.insert(0, str(num1 - num2))
    elif operator == '*':
        e.insert(0, str(num1 * num2))
    elif operator == "/":
        e.insert(0, str(num1 / num2))
    
e = Entry(root, width = 35,borderwidth= 5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

#define buttons
button_1 = Button(root, text="1", padx=40, pady=20, command=lambda:OnNumButtonClick(1))
button_2 = Button(root, text="2", padx=40, pady=20, command=lambda:OnNumButtonClick(2))
button_3 = Button(root, text="3", padx=40, pady=20, command=lambda:OnNumButtonClick(3))
button_4 = Button(root, text="4", padx=40, pady=20, command=lambda:OnNumButtonClick(4))
button_5 = Button(root, text="5", padx=40, pady=20, command=lambda:OnNumButtonClick(5))
button_6 = Button(root, text="6", padx=40, pady=20, command=lambda:OnNumButtonClick(6))
button_7 = Button(root, text="7", padx=40, pady=20, command=lambda:OnNumButtonClick(7))
button_8 = Button(root, text="8", padx=40, pady=20, command=lambda:OnNumButtonClick(8))
button_9 = Button(root, text="9", padx=40, pady=20, command=lambda:OnNumButtonClick(9))
button_0 = Button(root, text="0", padx=40, pady=20, command=lambda:OnNumButtonClick(0))

button_addn = Button(root, text="+", padx=39, pady=20, command=lambda:OnOperationButtonClick("+"))
button_subn = Button(root, text="-", padx=40, pady=20, command=lambda:OnOperationButtonClick("-"))
button_mult = Button(root, text="*", padx=40, pady=20, command=lambda:OnOperationButtonClick("*"))
button_div = Button(root, text="/", padx=41, pady=20, command=lambda:OnOperationButtonClick("/"))

button_equal = Button(root, text="=", padx=91, pady=20, command=OnEqualButtonClick)
button_clear = Button(root, text = "Clear", padx=79, pady=20, command=OnClearButtonClick)

#Put buttons on screen
button_1.grid(row="3", column="0")
button_2.grid(row="3", column="1")
button_3.grid(row="3", column="2")

button_4.grid(row="2", column="0")
button_5.grid(row="2", column="1")
button_6.grid(row="2", column="2")

button_7.grid(row="1", column="0")
button_8.grid(row="1", column="1")
button_9.grid(row="1", column="2")

button_0.grid(row="4", column="0")
button_clear.grid(row="4", column="1", columnspan=2)

button_addn.grid(row="5", column="0")
button_equal.grid(row="5", column="1", columnspan=2)

button_mult.grid(row="6", column="0")
button_div.grid(row="6", column="1")
button_subn.grid(row="6", column="2")

root.mainloop()