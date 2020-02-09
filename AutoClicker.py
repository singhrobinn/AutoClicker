from tkinter import *
from pyautogui import *


app =Tk()
app.title('AutoClicker')
app.geometry('450x500')


def validate(string_counter):
    tempcounter=0
    tempcounter = int(string_counter)
    if isinstance(tempcounter,int) or tempcounter==0:
       return True
    else:
       return False


def AutoClicker(counterprint,x,y):
    for i in range(counterprint):
        pyautogui.click(x,y)
        
def start():
    string_counter=counter.get()
    error=validate(string_counter)
    if error==False:
        errorLabel.pack()
    else:
        counterprint=setcounterInt(string_counter)
        x,y=FindSkip()
        AutoClicker(counterprint,x,y)

def setcounterInt(string_counter):
    return int(string_counter)

def FindSkip():
    x,y,width,height=pyautogui.locateOnScreen('skip.png')
    x=(x+(x+width)/2)
    y=(y+(x+height)/2)
    return x,y


counter=StringVar()
errorLabel=Label(app, text='Invalid Value',font=('bold',10),fg='red')
counterLabel=Label(app, text='Click Counter', font=('bold',14))
counterLabel.pack()
counterEntry=Entry(app,textvariable=counter)
counterEntry.pack()
counterprint=0
startButton = Button(app,text='Skip',width=15, command=start,pady=10)
startButton.pack()
counterLeftCounterLabel=Label(app,text=str(counterprint),font=('bold',25))
counterLeftCounterLabel.pack()
counterLeftLabel=Label(app, text='Clicks Left', font=('bold',14))
counterLeftLabel.pack()

#def get


app.mainloop()
