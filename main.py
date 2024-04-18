from tkinter import *
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

# okno
window = customtkinter.CTk()
window.title ("Úkoláček")
window.geometry("600x510")
window.resizable(True, True)

# definice - fonty a barvy
main_font = ("Calibri", 12)
main_color = "#dd7f00"
button_color = "#ffbe66"

#Funkce
def add_item():
    list_box.insert(END,input.get())
    input.delete(0,END)

def delete_item():
    list_box.delete(ANCHOR)

def delete_all():
    list_box.delete(0,END)

def save_tasks():
    with open("ukoly.txt", "w") as file:
        my_tasks = list_box.get(0, END)
        for one_task in my_tasks:
            if one_task.endswith("\n"):
                file.write(f"{one_task}")
            else:
                file.write(f"{one_task}\n")

def open_tasks():
    try:
        with open ("ukoly.txt", "r") as file:
            for one_line in file:
                list_box.insert(END,one_line)
    except:
        print ("chyba v otevírání souboru s úkoly")

# framy
input_frame = customtkinter.CTkFrame(window)
text_frame = customtkinter.CTkFrame(window)
button_frame = customtkinter.CTkFrame(window)
input_frame.pack()
text_frame.pack()
button_frame.pack()

# vložení
input = customtkinter.CTkEntry(input_frame, width=410)
input.grid(row=0, column=0, padx=5, pady=5)
add = customtkinter.CTkButton(input_frame, text="Přidat", command=add_item)
add.grid(row=0, column=1, padx=5, pady=5, ipadx=12)

# Scroll
text_scrollbar = Scrollbar(text_frame)
text_scrollbar.grid(row=0, column=1, sticky=NS)


# Textové pole
list_box = Listbox(text_frame, width=87, height=21, borderwidth=3, font=main_font, yscrollcommand=text_scrollbar.set)
list_box.grid(row=0, column=0)

#Propojení scrollbaru s listboxem
text_scrollbar.config(command=list_box.yview)

# pole tlačitek
remove_button=customtkinter.CTkButton(button_frame, text="Smazat položku", command=delete_item)
clear_button=customtkinter.CTkButton(button_frame, text="Smazat VŠE", command=delete_all)
save_button=customtkinter.CTkButton(button_frame, text="Uložit",  command=save_tasks)
quit_button=customtkinter.CTkButton(button_frame, text="Ukončit", command=window.destroy)

remove_button.grid(row = 0, column = 0, padx=5, pady=10)
clear_button.grid(row = 0, column = 1, padx=5, pady=10)
save_button.grid(row = 0, column = 2, padx=5, pady=10)
quit_button.grid(row = 0, column = 3, padx=5, pady=10)

#Načtení seznamu úkolů
open_tasks()

# hlavní cyklus
window.mainloop()