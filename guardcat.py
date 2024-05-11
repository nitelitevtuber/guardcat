import customtkinter
from aiomcrcon import Client
from PIL import Image
import asyncio

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


#main window lmao
main = customtkinter.CTk()
main.title("guardcat")
main.geometry("520x720")

def settingsmenu():
        toplevel = customtkinter.CTkToplevel(main)
        toplevel.geometry("520x720")
        toplevel.grab_set()

        

# THE FUCKING CAT AAAAAAAAA
creature = customtkinter.CTkImage(dark_image=Image.open('creature.jpg'), size=(210,120))
thecreature = customtkinter.CTkLabel(main, text="", image=creature)
thecreature.grid(row=0, column=0, padx=30, pady=20)
silltext = customtkinter.CTkLabel(main, text="welcome to guardcat :3", font=('Segoe UI Bold', 20))
silltext.grid(row=0, column=1, padx=10  , pady=20)
startbutton = customtkinter.CTkButton(main, text="Start")
startbutton.grid(row=1, column=0, padx=50, pady=40)
stoptbutton = customtkinter.CTkButton(main, text="Stop")
stoptbutton.grid(row=1, column=1, padx=50, pady=40)
startbutton = customtkinter.CTkButton(main, text="Settings", command=settingsmenu)
startbutton.grid(row=3, column=1, padx=50, pady=40)











main.mainloop()