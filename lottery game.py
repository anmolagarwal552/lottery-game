from tkinter import *
import time
import random
root=Tk()
root.geometry("415x300")
root.title("LUCKY LOTTERY")
root.config(bg='white')
variable=StringVar()
variable.set('000')
variable1=StringVar()
variable1.set('000')
variable2=StringVar()
variable2.set('000')
lottext=StringVar()
lottext.set('LUCKY LOTTERY GAME !!')

def reset():
    variable.set('000')
    variable1.set('000')
    variable2.set('000')

def lot():
    lottext.set(' LUCKY LOTTERY GAME !!.')
    root.update()
    lottext.set('  LUCKY LOTTERY GAME !!..')
    root.update()
    lottext.set('   LUCKY LOTTERY GAME !!...')
    root.update()
def update_label():
    ii=0
    while ii!=5:
        global i
        ii+=1
        for i in range(100,1000,3):
            variable.set(str(i))
            variable1.set(str(i))
            variable2.set(str(i))
            lot()
            #time.sleep(0.03)
            root.update()
    endit()
def endit():
    variable.set(random.randrange(100,1000))
    variable1.set(random.randrange(100,1000))
    variable2.set(random.randrange(100,1000))
your_label=Label(root,textvariable=lottext,font="comicsansms 19 bold",relief='raised',bg='black',fg='white',pady=5).pack(fill='both',pady=3)
f = Frame(root,bg='white')
f.pack(anchor='nw')
#----------------------------------------------------------------------------------------------------------
your_label1=Label(f,textvariable=variable,relief="raised",bg="black",fg='white',padx=40,font=30,pady=10).grid(column=1,padx=4,pady=10)
your_label2=Label(f,textvariable=variable1,relief="raised",bg="black",fg='white',padx=40,font=30,pady=10).grid(row=0,column=2)
your_label3=Label(f,textvariable=variable2,relief="raised",bg="black",fg='white',padx=40,font=30,pady=10).grid(row=0,column=3,padx=4)
#----------------------------------------------------------------------------------------------------------
start_button=Button(f,text="START",relief='raised',font="comicsansms 15 bold",bg='brown',command=update_label,padx=40).grid(column=2)
reset_button=Button(f,text="RESET",relief='raised',font="comicsansms 15 bold",bg='brown',command=reset,padx=40).grid(column=2,pady=3)

your_label3=Label(f,text="BY ANMOL AGARWAL",fg='black',bg='white').grid(row=6,column=3)
#stop_button=Button(f,text="stop",command =).grid()
root.mainloop()
