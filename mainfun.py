from tkinter import *
from PIL import ImageTk, Image
import time
import pyautogui
from tkinter import messagebox


Aman =Tk()
Aman.geometry("850x850")


def clearTextInput():
    T.delete("1.0","end")
    inputtxt.delete("1.0","end")

def reset_values():
    second.set(5)

def o_and_t():
    clearTextInput()
    reset_values()


def Take_input(): 

    abcd = inputtxt.get("1.0", "end-1c")  
    abc = T.get("1.0", "end-1c") 
    pyautogui.click()
    #time.sleep(1)
    pyautogui.typewrite(abc,interval=abcd)

def submit():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(hour.get())*3600 + int(minute.get())*60 + int(second.get())
    except:
        print("Please input the right value")
    while temp >-1:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(temp,60) 
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue 
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to 
        # two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))
  
        # updating the GUI window after decrementing the
        # temp value every time
        Aman.update()
        time.sleep(1)
  
        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"
        #if (temp == 0):
            #messagebox.showinfo("thanks","Success")
         
        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1

def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func
 


hour=StringVar()
minute=StringVar()
second=StringVar()
  
# setting the default value as 0
hour.set("00")
minute.set("00")
second.set("05")
  

  
secondEntry= Entry(Aman, width=3, font=("Arial",18,""),textvariable=second)
secondEntry.place(x=115,y=400)
    


Aman.maxsize(850,850)
Aman.minsize(400,400)
Aman.title("AutoTyper")



f1= Frame(Aman, bg="grey", borderwidth=1)
f1.pack()

execute= Frame(Aman, borderwidth=1, bg="grey")
execute.pack(pady=10)


li = Label(text = "Interval in typing (must be in numeric)") 
inputtxt = Text(Aman, height = 1, 
                width = 10, 
                bg = "light yellow") 







b1=Button(execute,text="Exit" , command=Aman.destroy)
b1.pack(side=LEFT , padx=5)
#clear button
b2=Button(execute,text="Clear", command=o_and_t)
b2.pack(side=LEFT , padx=5)
#func button
b3 = Button(Aman, text = "Execute", command = sequence(submit, Take_input)) 
b3.pack(side=BOTTOM,anchor="s",pady=15) 

T = Text(Aman, height = 13, width = 62) 
l = Label(Aman, text = "enter your answer") 
l.config(font =("Courier", 14)) 

l.pack(pady=10) 
T.pack() 
li.pack() 
inputtxt.pack() 



Pyt=Label(text="made in python by Raj._.29")
Pyt.pack(side=TOP)

Aman.mainloop()

#copyright AMAN RAJ

