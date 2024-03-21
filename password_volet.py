import customtkinter as ctk
from CTkListbox import *
import sqlite3
from tkinter import messagebox,filedialog
import os
import datetime
import shutil
import subprocess
from Password_volet_functions.delete_function import on_delete
from Password_volet_functions.accounts_view import show_account_info


subprocess.run(["python", "dataBase.py"])
first_name=None
last_name=None
date=None
mode=""





db = sqlite3.connect("app.db")
cr = db.cursor()
id_count_select = cr.execute("SELECT id FROM accounts")
id_count = len(id_count_select.fetchall())
db.close()


def add_cat_func(window,entry):
    if entry:
        try:
            print(entry.get())
            db=sqlite3.connect("app.db")
            cr=db.cursor()
            cr.execute("INSERT  INTO catgory (types) VALUES (?)",(entry.get(),))
            db.commit()
            messagebox.showinfo("Done","Catgory Added")
            window.destroy()
        finally:
            db.close()
    else:
        messagebox.showerror("ERror","You didn't insert catgory name")

def add_catgory():
    window = ctk.CTk()
    window.geometry('300x300')
    window.title("Add New Catgory")
    label = ctk.CTkLabel(window,text="Catgory Name : ",font=("",15))
    label.place(x=16,y=14)
    catgory_entry= ctk.CTkEntry(window,width=140,height=30,placeholder_text="GOOGLE",corner_radius=30)
    catgory_entry.place(x=140,y=14)
    button_save_catgory = ctk.CTkButton(window,command=lambda:add_cat_func(window,catgory_entry),text="Create",fg_color="green",corner_radius=12,width=140,height=30,font=("",20),cursor="hand2")
    button_save_catgory.place(x=90,y=60)
    catgorys_entry = ctk.CTkComboBox(window,width=180,height=30,corner_radius=12)
    catgorys_entry.place(x=55,y=110)
    try:
        db=sqlite3.connect("app.db")
        x= []
        cr=db.cursor()
        req_catgory =cr.execute("SELECT types FROM catgory")
        catogry = cr.fetchall()
        for data in catogry:
            x.append(data[0])  # Extract the value from the tuple
            catgorys_entry.configure(values=x)
            catgorys_entry.set(data[0])
        db.commit()
    finally:
        db.close()
    button_remove_catgory = ctk.CTkButton(window,command=lambda:remove_catgory(window,catgorys_entry),text="Remove",fg_color="red",corner_radius=12,width=140,height=30,font=("",20),cursor="hand2")
    button_remove_catgory.place(x=85,y=150)
    window.mainloop()



def make_switch_catogry(master,catgory):
    global y,x
    if x >= 850:
        y+=130
        print("PROCCES DOINE")
        x=0
    elif x < 850:
        x += 170
    google_switch  = ctk.CTkSwitch(master, text=catgory,font=("bold",20),progress_color="green")
    google_switch.place(x=x,y=y)
    print(x)
    




def click_other(x):
    button_show_account_det.invoke()

def show_accounts_function():
    try :
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        cr.execute("SELECT type FROM accounts ")
        accounts = cr.fetchall()
        cr.execute("SELECT username FROM accounts ")
        name=cr.fetchall()
        id_count_select_show = cr.execute("SELECT id FROM accounts")
        id_count_show = len(id_count_select_show.fetchall())
        if accounts :
                if mode == "light":
                    colorf = "black"
                else:
                    colorf="white"
                for i in range(id_count_show): show_accounts.insert(i,accounts[i][-1] + " Account Name :  " + name[i][-1])
                show_accounts.configure(font=("",30,"bold"),hover_color="green",highlight_color="green",text_color=colorf)
        show_accounts.update()
    except KeyError as e:
        print(f"There is a error {e}")
    finally:
        db.close()


def save_backup_codes(id):
    try:
        db = sqlite3.connect("app.db")
        cr=db.cursor()
        backup_data = cr.execute("SELECT backup_codes FROM accounts WHERE id = ?",(id.curselection(),))
        backup_data_print= backup_data.fetchall()[0][0]
        if backup_data:
            backup_codes = cr.fetchall()
            name =cr.execute("SELECT username FROM accounts WHERE id = ?",(id.curselection(),)).fetchall()[0][0]
            typex =cr.execute("SELECT type FROM accounts WHERE id = ?",(id.curselection(),)).fetchall()[0][0]
            file_path = filedialog.asksaveasfilename(defaultextension="*.txt",filetypes=[(".doc",".txt"),("All files", "*.*")],initialfile=f"{typex} Account backup_codes for  {name} Volet")
            if file_path:
                with open(file_path, 'w') as file:
                    file.write("---------------------------------------------\n")
                    file.write(f"Back Codes For Account Name  : {name}\n")
                    file.write(str({backup_data_print[0]}))
                    file.write("\n----------------------------------------------")

        else:
            messagebox.showerror("Error","This Account Dosen'y have backup codes")
    finally:
        db.close()


def open_externa_folder(id):
    path = f"C:/Users/{os.getlogin()}/AppData/Roaming/Password Volet/Extera Folder For Account Id {id.curselection()}"
    if os.path.exists(path):
        os.startfile(path)
    else:
        messagebox.showerror("Error","This account dosen't have Extera Files !")

def show_more_details(check):
    if check.curselection() is None:
        messagebox.showerror("Error","Choose Account First")
        return
    db = sqlite3.connect("app.db")
    cr=db.cursor()
    cr.execute("SELECT first FROM accounts WHERE id = ?",(check.curselection(),))
    window = ctk.CTk()
    window.geometry("300x200")
    first_label = ctk.CTkLabel(window,text="first Name :",font=("",20))
    first_label.place(x=12,y=12)
    first_entry = ctk.CTkEntry(window,font=("",20),width=160,height=30,corner_radius=12)
    first_entry.place(x=120,y=12)
    first_entry.delete(0,"end")
    first_entry.insert(0,cr.fetchall())
    first_entry.configure(state="readonly")
    #
    last_label = ctk.CTkLabel(window,text="Last Name :",font=("",20))
    last_label.place(x=12,y=60)
    last_entry = ctk.CTkEntry(window,font=("",20),width=160,height=30,corner_radius=12)
    cr.execute("SELECT last FROM accounts WHERE id = ?",(check.curselection(),))
    last_entry.place(x=125,y=60)
    last_entry.delete(0,"end")
    last_entry.insert(0,cr.fetchall())
    last_entry.configure(state="readonly")
    back_button= ctk.CTkButton(window,corner_radius=12,command=lambda:save_backup_codes(check),cursor="hand2",text="Save Backup Codes",hover_color="green",width=200,font=("",20))
    back_button.place(x=50,y=111)
    files_button= ctk.CTkButton(window,corner_radius=12,command=lambda:open_externa_folder(show_accounts),cursor="hand2",text="Open Extera Folder",hover_color="green",width=200,font=("",20))
    files_button.place(x=50,y=160)
    window.mainloop()
    db.close()

def on_save_volet(username,password,typex,backup,email,x):
    try:
        db = sqlite3.connect("app.db")
        cr = db.cursor()
        id_count_select = cr.execute("SELECT id FROM accounts")
        id_count = len(id_count_select.fetchall())
        if backup.get():
            backupx = backup.get()
        else:
            backupx =None
        if username.get() and password.get() and email.get() :
            print(id_count)
            cr.execute("INSERT INTO accounts (username, password, email,type,backup_codes,birth,first,last,id) VALUES (?, ?, ?,?,?,?,?,?,?)", (username.get(), password.get(), email.get(),typex.get(),backupx,date,first_name,last_name,id_count))
            db.commit()
            messagebox.showinfo("Succes","Account Addes Succes ✅")
        else:
            messagebox.showerror("Error ❌","You Must Insert Email,Password , Username at lest ⚠️")
    except KeyError as e:
        print(f"{e}")
    finally:
        x.destroy()
        show_accounts_function()
        db.close()
        return

def upload_extera_file(id,window):
    try:
        file_bath_acc = f"C:/Users/{os.getlogin()}/AppData/Roaming/Password Volet/Extera Folder For Account Id {id_count}"
        os.makedirs(file_bath_acc)
        file_paths = filedialog.askopenfilenames(title="Select Files", filetypes=[("All files", "*.*")])
        if file_paths:
            for file_path in file_paths:
                file_name = os.path.basename(file_path)
                destination_path = os.path.join(file_bath_acc, file_name)
                shutil.copyfile(file_path, destination_path)
            messagebox.showinfo("Scuess","Folder Copyed And Created Succ")
            window.destroy()
    except KeyError as e:
        print({e})

def the_extera_save(window):
        global last_name,first_name,date
        #
        if account_Last_name_entry.get():
            last_name = account_Last_name_entry.get()
        #
        if account_first_name_entry.get():
            first_name = account_first_name_entry.get()
        #
        if account_date_entry.get():
            date = account_date_entry.get()
        #
        window.destroy()

def extera_add_options(mode):
    global account_date_entry,account_first_name_entry,account_Last_name_entry
    window = ctk.CTk()
    window.title("Extera Options")
    window.geometry("400x350")
    account_date_label = ctk.CTkLabel(window,text="Account Birth day : ",font=("",17))
    account_date_label.place(x=15,y=22)
    account_date_entry = ctk.CTkEntry(window,width=220,height=35,corner_radius=12,placeholder_text="1999/12/2")
    account_date_entry.place(x=170,y=20)
    #
    account_first_name_label = ctk.CTkLabel(window,text="Account First Name : ",font=("",17))
    account_first_name_label.place(x=10,y=75)
    account_first_name_entry = ctk.CTkEntry(window,width=220,height=35,corner_radius=12,placeholder_text="Sara")
    account_first_name_entry.place(x=170,y=70)
    #
    account_Last_name_label = ctk.CTkLabel(window,text="Account Last Name : ",font=("",17))
    account_Last_name_label.place(x=10,y=130)
    account_Last_name_entry = ctk.CTkEntry(window,width=220,height=35,corner_radius=12,placeholder_text="Kitty")
    account_Last_name_entry.place(x=170,y=130)
    #
    Upload_Files_Needed_To_This_account = ctk.CTkLabel(window,text="Upload Extera Needed Files For The account",font=("",18))
    Upload_Files_Needed_To_This_account.place(x=13,y=180)
    buttton_add = ctk.CTkButton(window,text="Upload", width=200, height=30 , font=("bold",20),cursor="hand2",hover_color="green",corner_radius=12,command=lambda:upload_extera_file(show_accounts,window))
    buttton_add.place(x=100,y=220)
    button_save=ctk.CTkButton(window,text="Save",corner_radius=12,font=("sold",20),hover_color="green",command=lambda:the_extera_save(window),width=200,height=30,cursor="hand2")
    button_save.place(x=100,y=300)






    window.mainloop()



def add_account_window():
    window = ctk.CTk()
    window.geometry("400x350")
    window.title("Add Account Window")
    window.resizable(False,False)
    #ctk.set_appearance_mode(mode)
    add_accont_label = ctk.CTkLabel(window,text="Add account",font=("",20))
    add_accont_label.place(relx=0.5,rely=0.07,anchor="center")
    #
    email_label = ctk.CTkLabel(window,text="Email : ",font=("",17))
    email_label.place(x=30,y=50)
    email_label_entry = ctk.CTkEntry(window,width=220,height=35,corner_radius=12,placeholder_text="Enter Account Email")
    email_label_entry.place(x=160,y=50)
    #
    add_user_name_label = ctk.CTkLabel(window,text="User name : ",font=("",17))
    add_user_name_label.place(x=30,y=100)
    add_user_name_entry = ctk.CTkEntry(window,width=220,height=35,corner_radius=12,placeholder_text="Enter account username (optionail)")
    add_user_name_entry.place(x=160,y=98)
    add_password_label = ctk.CTkLabel(window,text="Password : ",font=("",17))
    add_password_label.place(x=30,y=150)
    add_password_entry = ctk.CTkEntry(window,width=220,height=35,corner_radius=12,placeholder_text="Enter account password")
    add_password_entry.place(x=160,y=148)
    add_type_label = ctk.CTkLabel(window,text="Type : ",font=("",17))
    add_type_label.place(x=30,y=200)
    add_type_entry = ctk.CTkComboBox(window,width=220,height=35,corner_radius=12)
    add_type_entry.place(x=160,y=198)
    try:
        db=sqlite3.connect("app.db")
        x= []
        cr=db.cursor()
        req_catgory =cr.execute("SELECT types FROM catgory")
        catogry = cr.fetchall()
        for data in catogry:
            x.append(data[0])  # Extract the value from the tuple
            add_type_entry.configure(values=x)
            add_type_entry.set(data[0])
            db.commit()
    finally:
        db.close()
    add_backup_code_label = ctk.CTkLabel(window,text="Backup Codes : ",font=("",17))
    add_backup_code_label.place(x=30,y=250)
    add_backup_code_entry = ctk.CTkEntry(window,width=220,height=35,corner_radius=12,placeholder_text="Enter Backup Codes If Exsist")
    add_backup_code_entry.place(x=160,y=250)
    button_extra_options = ctk.CTkButton(window,text="Extera Options", width=150 , height=25 , corner_radius=5, font=("bold",18),cursor="hand2",command=lambda:extera_add_options(mode))
    button_extra_options.place(x=220,y=300)
    button_add = ctk.CTkButton(window,text="Add Account",font=("bold",20),cursor="hand2",hover_color="gray",fg_color="green",command=lambda:on_save_volet(add_user_name_entry,add_password_entry,add_type_entry,add_backup_code_entry,email_label_entry,window))
    button_add.place(x=60,y=300)
    window.mainloop()
def remove_catgory(window,entry):
    try:
        db=sqlite3.connect("app.db")
        cr=db.cursor()
        print(f"HEEEEEEEEEEEEER {entry.get()}")
        cr.execute("DELETE FROM catgory WHERE types = ? ",(entry.get(),))
        db.commit()
        messagebox.showinfo("Done","Catgory DELETED")
        window.destroy()
    finally:
            db.close()

def password_volet(window,mode_main):
    global show_accounts,button_show_account_det,auto_login,mode
    mode = mode_main
    the_buttons_frame = ctk.CTkFrame(window, width=1100, height=720)
    the_buttons_frame.place(x=220, y=0)
    email_show_lable=ctk.CTkLabel(window,text="Email : ", font=("",22))
    email_show_lable.place(x=930,y=224)
    email_show_entry=ctk.CTkEntry(window,width=200,state="readonly",corner_radius=30,height=30,font=("",22))
    email_show_entry.place(x=1012,y=224)
    #
    user_name_show_lable=ctk.CTkLabel(window,text="UserName : ", font=("",22))
    user_name_show_lable.place(x=930,y=270)
    user_name_show_entry=ctk.CTkEntry(window,width=200,state="readonly",corner_radius=30,height=30,font=("",22))
    user_name_show_entry.place(x=1060,y=270)
    #
    Password_label=ctk.CTkLabel(window,text="Password : ", font=("",22))
    Password_label.place(x=930,y=312)
    Password_entry=ctk.CTkEntry(window,width=200,state="readonly",corner_radius=30,height=30,font=("",22))
    Password_entry.place(x=1060,y=312)
    #
    type_label=ctk.CTkLabel(window,text="Type : ", font=("",22))
    type_label.place(x=930,y=357)
    type_entry=ctk.CTkEntry(window,width=150,state="readonly",corner_radius=30,height=30,font=("",22))
    type_entry.place(x=1000,y=357)
    #
    birth_label=ctk.CTkLabel(window,text="Birth Day : ", font=("",22))
    birth_label.place(x=930,y=401)
    birth_entry=ctk.CTkEntry(window,width=150,state="readonly",corner_radius=30,height=30,font=("",22))
    birth_entry.place(x=1040,y=401)
    #
    show_accounts = CTkListbox(window,width=650,height=600,justify="center",command=click_other)
    show_accounts.place(x=240, y=80)
    show_accounts_function()
    #
    button_more=ctk.CTkButton(window,text="More Detials",command=lambda:show_more_details(show_accounts),cursor="hand2",corner_radius=12,font=("",20),width=200,height=30,hover_color="green")
    button_more.place(x=1000,y=445)
    #
    label_options = ctk.CTkLabel(the_buttons_frame, text="Volet Options", font=("sold", 30))
    label_options.place(x=880, y=40, anchor="center")
    button_add = ctk.CTkButton(
        the_buttons_frame,text="Add New Account",width=280,height=50,font=("bold", 25),corner_radius=12,cursor="hand2",hover_color="green",command=lambda:add_account_window()
    )
    button_add.place(x=740, y=80)
    button_remove=ctk.CTkButton(window,text="Delete Account",command=lambda:on_delete(show_accounts),cursor="hand2",corner_radius=12,font=("",25),width=280,height=50,fg_color="red")
    button_remove.place(x=960,y=140)
    button_show_account_det = ctk.CTkButton(window,fg_color="green",command=lambda:show_account_info(window,email_show_entry,user_name_show_entry,Password_entry,type_entry,birth_entry,show_accounts),text="",width=0,height=0,font=("",0),cursor="hand2")
    button_show_account_det.place(x=480,y=16)
    #
    button_add_catgory=ctk.CTkButton(window,text="Catgory options",cursor="hand2",corner_radius=12,font=("",25),width=280,height=50,command=add_catgory)
    button_add_catgory.place(x=960,y=520)
