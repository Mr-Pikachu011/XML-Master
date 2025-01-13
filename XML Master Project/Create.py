import shutil
import os
from tkinter import *
import customtkinter
import subprocess
import platform
from tkinter import messagebox


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

root = customtkinter.CTk()
root.title("Create App")
root.geometry("300x200")


directory = "C:/XML Master"
os.makedirs(directory, exist_ok=True)

label = customtkinter.CTkLabel(
    root, text="XML Coding", font=("Cambria",20) )
label.place(x=10,y=10)

label = customtkinter.CTkLabel(
    root, text="File Name : ", font=("Cambria",15) )
label.place(x=10,y=60)

entry = customtkinter.CTkEntry(root,width=205)
entry.place(x=85,y=60)

# button function

def button_event():
    h1 = entry.get()
    # print(h1)
    label1 = customtkinter.CTkLabel(
    root, text= h1 +" App is Created Succsessfully", font=("Cambria",12) )
    label1.place(x=10,y=170)
    
    
    # read file of source code 
        
    with open('source_directory/code.txt', 'r') as file:
        content = file.read()
    extracted_text = content[:700]

    name = entry.get()
    
    # copy folder

    source_folder = 'source_directory'
    destination_folder = "C:/XML Master/"+name+"/App/source"

    if not os.path.exists(destination_folder):
        shutil.copytree(source_folder, destination_folder)
        messagebox.showinfo("Info", h1 +" App is Created Succsessfully")
    else:
        print(f"Destination folder '{destination_folder}' already exists.")
        messagebox.showwarning("Warning", h1 +" App is Already Created")
                

    # make python file
    
    directory = "C:/XML Master/"+name+"/App"
    os.makedirs(directory, exist_ok=True)

    file = open(directory+"/"+name+".py", "w")
    file.write(extracted_text)
    file.close()
    
    root.destroy()
    
    # open folder location

    folder_path = "C:\\XML Master\\"+name
    

    if platform.system() == "Windows":
        subprocess.run(["explorer", folder_path])
    elif platform.system() == "Darwin":  # macOS
        subprocess.run(["open", folder_path])
    else:  # Linux or others
        subprocess.run(["xdg-open", folder_path])
        
        
# button

button = customtkinter.CTkButton(
    root, text="Create App", command=button_event,width=280)
button.place(x=10,y=110)


label1 = customtkinter.CTkLabel(
    root, text= "Started .", font=("Cambria",12) )
label1.place(x=10,y=170)

root.mainloop()

