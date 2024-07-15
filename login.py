
import tkinter
from tkinter import *
from tkinter import messagebox
class login:
    def __init__(self,root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("1199x600+100+50")
        self.root.resizable(False,False)

        #background image
        self.bg = PhotoImage(file=r"c:\Users\ACER\Pictures\aanu.png")
        self.image = Label(self.root,image=self.bg).place(x=0,y=0,relheight=1,relwidth=1)
      
        #Frame 
        frame_login = Frame(self.root, bg="white")
        frame_login.place(x=330,y=150,width=500,height=400)

        #Label inside Frame
        login_here = Label(frame_login,text="LOGIN HERE",bg="white",font=("Impact",35,"bold"),fg="#6162FF").place(x=90,y=30)
        
        user = Label(frame_login,text="Username",bg="white",font=("Georgia",12,"bold"),fg="grey").place(x=90,y=110)
        self.entry1 = Entry(frame_login,font=("georgia",15),bg="#E7E6E6")
        self.entry1.place(x=90,y=135,height=33,width=279)

        password = Label(frame_login,text="Password",bg="white",font=("Georgia",12,"bold"),fg="grey").place(x=90,y=180)
        self.entry2 = Entry(frame_login,bg="#E7E6E6",font=("Georgia",15))
        self.entry2.place(x=90,y=205,height=33,width=279)

        #Button 
        forget = Button(frame_login,text="Forget Password?",cursor="hand2",bg="white",font=("Georgia",8,"bold"),fg="#6162FF",borderwidth=0).place(x=90,y=250)

        submit = Button(frame_login,text="Login",command=self.anurag,cursor="hand2",bg="#6162FF",activebackground="#6162FF",font=("Georgia",15,"bold"),fg="white",borderwidth=1).place(x=90,y=300,width=110)

        
    def anurag(self):
        if self.entry1.get() =="" or self.entry2.get()=="":
             messagebox.showerror("Error","All fields are Required",parent = self.root)
        elif self.entry1.get() != "anu123"or self.entry2.get()!="anurag":
            messagebox.showerror("Error","Invalid Username and Password",parent = self.root)
        else:
            messagebox.showinfo("Welcome",f"Welcome{self.entry1.get()}")



           
            





root = Tk()        
obj = login(root)
root.mainloop() 



