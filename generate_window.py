import customtkinter as ctk
from tkinter import messagebox
import pyperclip
from faker import Factory
fake = Factory.create()  
def generate(button,length,special,numbers,upper,password):
    button.configure(text="Copy",fg_color="#1E6BA5")
    password.configure(state="normal")
    try:
        int(length.get())
    except ValueError:
        length.delete(0,"end")
        messagebox.showerror("ERROR","Enter Length , numbers only")
        return
    
    s = True
    num = True
    u = True
    if special.get() == 0:
        s = False
    if numbers.get() == 0:
        num = False
    if upper.get() == 0:
        u = False
    password.delete(0,"end")
    password.insert(0,fake.password(length=int(length.get()), special_chars=s, digits=num, upper_case=u))
    password.configure(state="readonly")

def copy(entry,button):
    if entry.get() == "":
        messagebox.showerror("Error","No Password Generated to copy")
        return
    pyperclip.copy(entry.get())
    button.configure(text="Copied!",fg_color="green")



def generate_password(window):
    backup_frame = ctk.CTkFrame(window, width=1100, height=720,corner_radius=12)
    backup_frame.place(x=220, y=0)
    labe_gen = ctk.CTkLabel(window,text="Generate Password :",font=("",30))
    labe_gen.place(x=250,y=200)
    entry_gen = ctk.CTkEntry(window,state="readonly",width=300,height=30,corner_radius=30,font=("",23))
    entry_gen.place(x=550,y=204)
    options_label = ctk.CTkLabel(window,text="Options",font=("",35))
    options_label.place(x=1010,y=30)
    length_label=ctk.CTkLabel(window,text="Length : " , font=("",24))
    length_label.place(x=920,y=180)
    length_entry=ctk.CTkEntry(window,width=120,corner_radius=30,height=30,font=("",22))
    length_entry.place(x=1030,y=180)
#
    special_label=ctk.CTkLabel(window,text="Special chars : " , font=("",24))
    special_label.place(x=920,y=240)
    special_entry=ctk.CTkSwitch(window,text="State",width=120,corner_radius=30,height=30,font=("",22))
    special_entry.place(x=1100,y=240)
#
    digit_label=ctk.CTkLabel(window,text="Numbers : " , font=("",24))
    digit_label.place(x=920,y=280)
    digit_entry=ctk.CTkSwitch(window,text="State",width=120,corner_radius=30,height=30,font=("",22))
    digit_entry.place(x=1100,y=280)
#
    upper_label=ctk.CTkLabel(window,text="Upper Chrs: " , font=("",24))
    upper_label.place(x=920,y=320)
    upper_entry=ctk.CTkSwitch(window,text="State",width=120,corner_radius=30,height=30,font=("",22))
    upper_entry.place(x=1100,y=320)
#
    button_geb=ctk.CTkButton(window,command=lambda:copy(entry_gen,button_geb),text="Copy pass",cursor="hand2",font=("",30),width=300,height=30,corner_radius=12)
    button_geb.place(x=230,y=280)
    gen=ctk.CTkButton(window,command=lambda:generate(button_geb,length_entry,special_entry,digit_entry,upper_entry,entry_gen),text="Generate pass",cursor="hand2",font=("",30),hover_color="green",width=300,height=30,corner_radius=12)
    gen.place(x=540,y=280)