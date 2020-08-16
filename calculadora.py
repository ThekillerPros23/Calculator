from tkinter import * 
from tkinter import messagebox
import os
window=Tk()
window.title("Calculator")
window.geometry("400x400")  
window.maxsize(225,270)
window.minsize(225,270)
number1=IntVar()
number2=IntVar()
def change():
    x=number1.get()
def _init_():
    
    entrada_dato=Entry(window,textvariable=number1.get(),width=100)
    entrada_dato.grid(column=0,row=0)
    
    button_ac=Button(window,text="AC",width=2,height=2, bg="red",command=change)
    button_ac.place(x=0,y=21)
    
    button_1=Button(window,text="1",width=2,height=2,command=change)
    button_1.place(x=0,y=170)
    
    button_2=Button(window,text="2",width=2,height=2)
    button_2.place(x=50,y=170)
    
    button_3=Button(window,text="3",width=2,height=2)
    button_3.place(x=100,y=170)
    
    button_4=Button(window,text="4",width=2 ,height=2)
    button_4.place(x=0,y=120)
    
    button_5=Button(window,text="5",width=2,height=2)
    button_5.place(x=50,y=120)
    
    button_6=Button(window,text="6",width=2,height=2)
    button_6.place(x=100,y=120)
    
    button_7=Button(window,text="7",width=2,height=2)
    button_7.place(x=0,y=70)
    
    button_8=Button(window,text="8",width=2,height=2)
    button_8.place(x=50,y=70)
    
    button_9=Button(window,text="9",width=2,height=2)
    button_9.place(x=100,y=70)
    
    button_0=Button(window,text="0",width=2,height=2)
    button_0.place(x=0,y=220)
    
    button_point=Button(window,text=".",width=2,height=2)
    button_point.place(x=50,y=220)
    
    window.mainloop()

if __name__=="__main__":
    _init_()
