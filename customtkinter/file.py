import customtkinter as ctk
import json
import os

SETTINGS_FILE = "settings.json"

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        with open(SETTINGS_FILE, "r") as f:
            return json.load(f)
    return {"theme": "Dark"}

def save_settings(theme):
    with open(SETTINGS_FILE, "w") as f:
        json.dump({"theme": theme}, f)

def change_theme(choice):
    ctk.set_appearance_mode(choice)
    save_settings(choice)

settings = load_settings()

ctk.set_appearance_mode(settings["theme"])
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Professional Settings Manager")
app.geometry("600x400")

sidebar = ctk.CTkFrame(app, width=150)
sidebar.pack(side="left", fill="y", padx=10, pady=10)

label_theme = ctk.CTkLabel(sidebar, text="Motyw")
label_theme.pack(pady=10)

theme_menu = ctk.CTkOptionMenu(
    sidebar,
    values=["Light", "Dark"],
    command=change_theme
)
theme_menu.set(settings["theme"])
theme_menu.pack(pady=10)

main_frame = ctk.CTkFrame(app)
main_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

entry = ctk.CTkEntry(main_frame, placeholder_text="Wpisz tekst")
entry.pack(pady=10, padx=10)

checkbox = ctk.CTkCheckBox(main_frame, text="Akceptuję warunki")
checkbox.pack(pady=10)

button = ctk.CTkButton(main_frame, text="Zatwierdź")
button.pack(pady=10)

textbox = ctk.CTkTextbox(main_frame, height=150)
textbox.pack(pady=10, padx=10, fill="both", expand=True)

textbox.insert("0.0", "Przykładowe dane:\n- Element 1\n- Element 2\n- Element 3")

app.mainloop()