import tkinter as tk
import tkinter.messagebox
from tkinter.constants import SUNKEN

window=tk.Tk()
window.title("Calculator")

frame=tk.Frame(master=window,bg="#A39E92", padx=12)
frame.pack()

entry=tk.Entry(master=frame, relief=SUNKEN, borderwidth=3, width=30)
entry.grid(row=0, column=0, columnspan=3, ipady=2, pady=2)

def myClick(number):
    entry.insert(tk.END, number)

def equal():
    try:
        y=str(eval(entry.get())) #Eval->Kendisine verilen karakter dizisini değerlendirir ve bir sonuç verir.
        entry.delete(0,tk.END)
        entry.insert(0,y)

    except:
        tkinter.messagebox.showinfo("Error", "Syntax Error")

def clear():
    entry.delete(0,tk.END)

button1 = tk.Button(master=frame, text="1", padx=15,pady=5,width=3, command=lambda:myClick(1))
button1.grid(row=1,column=0,pady=2)
button2 = tk.Button(master=frame, text="2", padx=15,pady=5,width=3, command=lambda:myClick(2))
button2.grid(row=1,column=1,pady=2)
button3 = tk.Button(master=frame, text="3", padx=15,pady=5,width=3, command=lambda:myClick(3))
button3.grid(row=1,column=2,pady=2)
button4 = tk.Button(master=frame, text="4", padx=15,pady=5,width=3, command=lambda:myClick(4))
button4.grid(row=2,column=0,pady=2)
button5 = tk.Button(master=frame, text="5", padx=15,pady=5,width=3, command=lambda:myClick(5))
button5.grid(row=2,column=1,pady=2)
button6 = tk.Button(master=frame, text="6", padx=15,pady=5,width=3, command=lambda:myClick(6))
button6.grid(row=2,column=2,pady=2)
button7 = tk.Button(master=frame, text="7", padx=15,pady=5,width=3, command=lambda:myClick(7))
button7.grid(row=3,column=0,pady=2)
button8 = tk.Button(master=frame, text="8", padx=15,pady=5,width=3, command=lambda:myClick(8))
button8.grid(row=3,column=1,pady=2)
button9 = tk.Button(master=frame, text="9", padx=15,pady=5,width=3, command=lambda:myClick(9))
button9.grid(row=3,column=2,pady=2)
button0 = tk.Button(master=frame, text="0", padx=15,pady=5,width=3, command=lambda:myClick(0))
button0.grid(row=4,column=1,pady=2)

addButton=tk.Button(master=frame,text="+",padx=15,pady=5, width=3, command=lambda:myClick("+"))
addButton.grid(row=5,column=0,pady=2)

addSubstract=tk.Button(master=frame,text="-",padx=15,pady=5, width=3, command=lambda:myClick("-"))
addSubstract.grid(row=5,column=1,pady=2)

addMultiply=tk.Button(master=frame,text="*",padx=15,pady=5, width=3, command=lambda:myClick("*"))
addMultiply.grid(row=5,column=2,pady=2)

addDiv=tk.Button(master=frame,text="/",padx=15,pady=5, width=3, command=lambda:myClick("/"))
addDiv.grid(row=6,column=0,pady=2)

clearButton=tk.Button(master=frame,text="clear",padx=15,pady=5, width=3, command=clear)
clearButton.grid(row=6,column=1,pady=2)

buttonEqual=tk.Button(master=frame,text="=",padx=15,pady=5, width=3, command=equal)
buttonEqual.grid(row=6,column=2,pady=2)

window.mainloop()
