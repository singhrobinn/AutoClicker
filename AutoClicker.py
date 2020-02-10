from tkinter import *
import pyautogui as autopy


app =Tk()
app.title('AutoClicker')
app.geometry('450x300')


def validate(string_counter):
    tempcounter=0
    tempcounter = int(string_counter)
    if isinstance(tempcounter,int) or tempcounter==0:
       return True
    else:
       return False


def AutoClicker(counterprint,x,y):
    for i in range(counterprint):
        autopy.click(x,y)
        
def start():
    string_counter=counter.get()
    error=validate(string_counter)
    if error==False:
        errorLabel.pack()
    else:
        counterprint=setcounterInt(string_counter)
        buttonLocation=autopy.locateCenterOnScreen('reddit.png')
        if buttonLocation==None:
            errorLabel2.pack()
        else:
            AutoClicker(counterprint,buttonLocation[0],buttonLocation[1])

def setcounterInt(string_counter):
    return int(string_counter)

    


counter=StringVar()
errorLabel=Label(app, text='Invalid Value',font=('bold',10),fg='red')
errorLabel2=Label(app, text='Not Found',font=('bold',10),fg='red')
counterLabel=Label(app, text='Click Counter', font=('bold',14))
counterLabel.pack(pady=10)
counterEntry=Entry(app,textvariable=counter)
counterEntry.pack(pady=10)
counterprint=0
startButton = Button(app,text='Skip',width=15, command=start,pady=10)
startButton.pack()
counterLeftLabel=Label(app, text='Clicks Left', font=('bold',14))
counterLeftLabel.pack(side=BOTTOM,pady=20)
counterLeftCounterLabel=Label(app,text=str(counterprint),font=('bold',40))
counterLeftCounterLabel.pack(side=BOTTOM)


#def get


app.mainloop()
