from tkinter.constants import GROOVE, RAISED, RIDGE
import cv2
import pyzbar.pyzbar as pyzbar
import time
from datetime import date, datetime
import tkinter as tk 
from tkinter import Frame, ttk, messagebox
from tkinter import *

window = tk.Tk()
window.title('Smart Attendance System')
window.geometry('900x600') 
                          
                          
sem= tk.StringVar()      
branch= tk.StringVar()
sec= tk.StringVar() 
period= tk.StringVar()

title = tk.Label(window,text="Smart Attendance System",bd=10,relief=tk.GROOVE,font=("times new roman",40),bg="lavender",fg="black")
title.pack(side=tk.TOP,fill=tk.X)

Manage_Frame=Frame(window,bg="lavender")
Manage_Frame.place(x=0,y=80,width=480,height=530)

ttk.Label(window, text = "Semester",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=150)
combo_search=ttk.Combobox(window,textvariable=sem,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('1','2','3','4','5','6','7','8') 
combo_search.place(x=250,y=150)

ttk.Label(window, text = "Branch",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=200)
combo_search=ttk.Combobox(window,textvariable=branch,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=("Mechanical Engineering","Information Technology Engineering","Computer Engineering", 'Civil Engineering')
combo_search.place(x=250,y=200)


ttk.Label(window, text = "Period",background="lavender", foreground ="black",font = ("Times New Roman", 15)).place(x=100,y=300)
combo_search=ttk.Combobox(window,textvariable=period,width=10,font=("times new roman",13),state='readonly')
combo_search['values']=('LAB','Lecture')
combo_search.place(x=250,y=300)

def checkk():
    if(sem.get() and branch.get() and period.get() ):
        window.destroy()
    else:
        messagebox.showwarning("Warning", "All fields required!!")

exit_button = tk.Button(window,width=13, text="Submit",font=("Times New Roman", 15),command=checkk,bd=2,relief=RIDGE)
exit_button.place(x=300,y=380)



Manag_Frame=Frame(window,bg="lavender")
Manag_Frame.place(x=480,y=80,width=450,height=530)

canvas = Canvas(Manag_Frame, width = 300, height = 300,background="lavender")      
canvas.pack()      
img = PhotoImage(file="E:\Python Project\Smart Attendence System\QR_Attendance\KSV.png")      
canvas.create_image(50,50, anchor=NW, image=img) 

window.mainloop()

cap = cv2.VideoCapture(0)
names=[]
today=date.today()
d= today.strftime("%b-%d-%Y")

fob=open(d+'.xlsx','w+')
fob.write("Reg No."+'\t')
fob.write("Class & Sec"+'\t')
fob.write("sem"+'\t')
fob.write("Period"+'\t')
fob.write("In Time"+'\n')

def enterData(z):   
    if z in names:
        pass
    else:
        it=datetime.now()
        names.append(z)
        z=''.join(str(z))
        intime = it.strftime("%H:%M:%S")
        fob.write(z+'\t'+branch.get()+'-'+sec.get()+'\t'+sem.get()+'\t'+period.get()+'\t'+intime+'\n')
    return names 
    
print('Reading...')

def checkData(data):
    data=str(data)    
    if data in names:
        print('Already Present')
    else:
        print('\n'+str(len(names)+1)+'\n'+'present...')
        enterData(data)

while True:
    _, frame = cap.read()         
    decodedObjects = pyzbar.decode(frame)
    for obj in decodedObjects:
        checkData(obj.data)
        time.sleep(1)
       
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1)&0xFF == ord('g'):
        cv2.destroyAllWindows()
        break
    
fob.close()
