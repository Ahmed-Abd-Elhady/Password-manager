import customtkinter as ctk
from PIL import Image
from run_admin import run_as_admin
from pathes_fun_mange import resource_path
from about_window import about_window
from generate_window import generate_password
from password_volet import password_volet
from settings_window import setting



#shutil.rmtree(f"C:/Users/user/AppData/Roaming/Password Volet/Extera Folder For Account Id 0")
# vars
file_path = '/your/desired/path/example.txt'
mode = ""
def Change_mode(switch):
    global mode
    if switch.get():
        ctk.set_appearance_mode("light")
        mode = "light"
    else:
        ctk.set_appearance_mode("dark")
        mode = "dark"


#
x = 0
y = 120

def backup(window):
    backup_frame = ctk.CTkFrame(window, width=1100, height=720,corner_radius=12)
    backup_frame.place(x=220, y=0)
    label_backup = ctk.CTkLabel(backup_frame,text="Choose Volt Accounts Backup",font=("bold",40))
    label_backup.place(x=280,y=30)
    #for every_catgory in catogry:
        #make_switch_catogry(backup_frame,every_catgory)
        



root = ctk.CTk()
root.title("Password Volet | @Quntom Creators")
root.geometry("1280x720")
run_as_admin(root)

root.resizable(False, False)
root.iconbitmap(resource_path("./icon.png"))
ctk.set_appearance_mode(mode)
# Switch button appernce
dark_mode_button = ctk.CTkSwitch(root, text="Dark mode")
dark_mode_button.place(x=20, y=680)
#



frame_options = ctk.CTkFrame(
    root, width=220, height=720, corner_radius=10, border_width=1, border_color="#1E6BA5"
)
frame_options.place(x=0, y=0)

quintom_lensis = ctk.CTkLabel(root,text="@Quntom Creators",font=("bold",18))
quintom_lensis.place(x=1100,y=680)
quintom_img = ctk.CTkImage(dark_image=Image.open("./icon.png"),light_image=Image.open("./icon.png"),size=(250,250))
quintom_label = ctk.CTkLabel(root,text="",image=quintom_img,bg_color='#242424')
quintom_label.place(x=600,y=130)
app_name = ctk.CTkLabel(root, text="Password Volet | Made By @Quntom Creators",font=("bold",40))
app_name.place(x=340,y=450)


password_volet_button = ctk.CTkButton(frame_options,text="Password Volet",corner_radius=30,width=200,height=50,font=("bold", 20),cursor="hand2",hover_color="green",command=lambda:password_volet(root,mode),
)
password_volet_button.place(x=11, y=30)

password_generator = ctk.CTkButton(frame_options,text="Generate Pass",corner_radius=30,width=200,height=50,font=("bold", 20),cursor="hand2",hover_color="green",command=lambda:generate_password(root),
)
password_generator.place(x=11, y=100)

about = ctk.CTkButton(frame_options,text="About App",corner_radius=30,width=200,height=50,font=("bold", 20),cursor="hand2",hover_color="green",command=lambda:about_window(root)
)
about.place(x=11, y=170)


settings = ctk.CTkButton(frame_options,text="Settings",corner_radius=30,width=200,height=50,font=("bold", 20),cursor="hand2",hover_color="green",command=lambda:setting(root)
)
settings.place(x=11, y=260)

switch = ctk.CTkSwitch(frame_options, text="Themes", command=lambda:Change_mode(switch))
switch.place(x=14,y=680)





root.mainloop()
