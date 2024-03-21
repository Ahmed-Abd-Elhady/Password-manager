import customtkinter as ctk
version= '0.0.0'
about_content= "This Is Password Volet Programe From @Quntom Creators This Programe help\nMange your password auto login generate and more ! "

def about_window(window):
    frame = ctk.CTkFrame(window, width=1100, height=720, border_width=0)
    frame.place(x=220, y=0)
    connectLabel = ctk.CTkLabel(frame,text=f"About: Password Volet | @Quntom Creators ",font=("italic", 30, "bold"),
    )
    frame_about = ctk.CTkFrame(frame,width=800,height=500,corner_radius=12,border_width=1,border_color="#1E6BA5",
    )
    frame_about.place(x=80, y=140)
    connectLabel.place(x=190, y=40)
    version_label = ctk.CTkLabel(
        frame_about, text=f"App Version : {version} ", font=("italic", 20, "bold")
    )
    version_label.place(x=45, y=40)
    the_about = ctk.CTkLabel(frame_about,text=f"{about_content}",font=("italic", 20, "bold"),
    )
    the_about.place(x=30, y=90)
