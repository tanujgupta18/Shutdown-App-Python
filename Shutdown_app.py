from tkinter import *
import os

def restart():
    os.system("Shutdown /r /t 1")
def restart_time():
    os.system("Shutdown /r /t 20")
def logout():
    os.system("Shutdown -1")
def shutdown():
    os.system("Shutdown /s /t 1")

st = Tk()
st.title("Shutdown App")
st.geometry("500x500")
st.config(bg="Blue")

r_button = Button(st,text="Restart",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="",command=restart)
r_button.place(x=150,y=60,height=50,width=200)

rt_button = Button(st,text="Restart Time",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="",command=restart_time)
rt_button.place(x=150,y=160,height=50,width=200)

lg_button = Button(st,text="Log-Out",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="",command=logout)
lg_button.place(x=150,y=260,height=50,width=200)

st_button = Button(st,text="ShutDown",font=("Time New Roman",20,"bold"),relief=RAISED,cursor="",command=shutdown)
st_button.place(x=150,y=360,height=50,width=200)

st.mainloop()