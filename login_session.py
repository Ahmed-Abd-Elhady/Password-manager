import customtkinter as ctk
from PIL import Image
import sqlite3
from tkinter import messagebox
import subprocess
from pathes_fun_mange import resource_path



db = sqlite3.connect("app.db")
cr = db.cursor()
cr.execute("CREATE TABLE IF NOT EXISTS app_password(pass TEXT)")
db.close()

#Functions
def new_password(password,confrm,window):
    if password == confrm:
        try:
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            cr.execute("INSERT INTO app_password (pass) VALUES (?)",((password,)))
            db.commit()
            messagebox.showinfo("Succes","Password Added Succes")
            window.destroy()
        finally:
            db.close()
    else:
        messagebox.showerror("Password Don't mutch the confirm one")
        return




def login_acces(password_get,window):
    try:
        if password_get:
            db = sqlite3.connect("app.db")
            cr = db.cursor()
            cr.execute("SELECT pass FROM app_password")
            password = cr.fetchall()
            if password:
                if password_get == password[0][0]:
                    window.destroy()
                    subprocess.run(["python", "main.py"])
            else:
                messagebox.showinfo("New", " This is the first time u use the app u need to but password to open the app everytime u enter it")
                messagebox.showwarning("Warrning","If You Forget This Password u can't ACCES THE PASSWORDS DATA , PASSWORD CAN CHANGE IF U ALREDY KNOW IT")
                password_window_new = ctk.CTk()
                password_window_new.geometry("400x200")
                password_window_new.resizable(False,False)
                password_window_new.title("Make The App Password")
                password_new_label = ctk.CTkLabel(password_window_new,text="Enter App password : ", font=("bold",18))
                password_new_label.place(x=20,y=30) 
                password_new_entey = ctk.CTkEntry(password_window_new,corner_radius=30,font=("",15),width=200)
                password_new_entey.place(x=195,y=27)

                password_new_label_conf = ctk.CTkLabel(password_window_new,text="Confirm Password : ", font=("bold",18))
                password_new_label_conf.place(x=20,y=70) 

                password_new_entey_conf = ctk.CTkEntry(password_window_new,corner_radius=30,font=("",15),width=200)
                password_new_entey_conf.place(x=195,y=67)
                save_button = ctk.CTkButton(password_window_new,text="Change Password",command=lambda:new_password(password_new_entey.get(),password_new_entey_conf.get(),password_window_new),cursor="hand2",font=("",24),corner_radius=30,hover_color="green",width=300,height=40)
                save_button.place(x=80,y=150)
                password_window_new.mainloop()
        else:
            messagebox.showerror("Error","No Password Has Writed")
            return
    finally:
        db.close()
root = ctk.CTk()
root.geometry("1280x720")
root.resizable(False,False)
root.title("Login Session | @Quintom Creators")
root.iconbitmap(resource_path("./icon.png"))
quintom_img = ctk.CTkImage(dark_image=Image.open("./icon.png"),light_image=Image.open("./icon.png"),size=(250,250))
quintom_label = ctk.CTkLabel(root,text="",image=quintom_img)
quintom_label.place(x=512,y=21)
quintom_lensis = ctk.CTkLabel(root,text="@Quintom Creators",font=("bold",18))
quintom_lensis.place(x=1100,y=680)

Login_frame = ctk.CTkFrame(root,width=500,height=200,border_color='#1E6BA5',border_width=1, corner_radius=13)
Login_frame.place(x=384,y=340)

password_label = ctk.CTkLabel(Login_frame,text="Password : ", font=("bold",30))
password_label.place(x=25,y=60)

password_entry = ctk.CTkEntry(Login_frame,width=300,height=40,corner_radius=30  ,text_color="red",font=("bold",25))
password_entry.place(x=180,y=57)

login_button = ctk.CTkButton(Login_frame,command=lambda:login_acces(password_entry.get(),root),text="Login",font=("",27),width=300,corner_radius=30,cursor="hand2",height=45,hover_color="green")
login_button.place(x=120,y=135)




root.mainloop()