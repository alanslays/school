import tkinter as tk
from tkinter import ttk

def save_settings():
    pbar.start(10)
    root.after(3000, finish_save)

def finish_save():
    pbar.stop()
    print("Ustawienia zapisane!")

root = tk.Tk()
root.title("Ustawienia Systemu")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both", padx=10, pady=10)

tab_appearance = ttk.Frame(notebook, padding=10)
tab_privacy = ttk.Frame(notebook, padding=10)

notebook.add(tab_appearance, text="Wygląd")
notebook.add(tab_privacy, text="Prywatność")

ttk.Label(tab_appearance, text="Motyw:").grid(row=0, column=0, sticky="w", padx=5, pady=5)

theme_combo = ttk.Combobox(
    tab_appearance,
    values=["Jasny", "Ciemny", "Systemowy"],
    state="readonly"
)
theme_combo.current(2)
theme_combo.grid(row=0, column=1, padx=5, pady=5)

contrast_var = tk.BooleanVar()
ttk.Checkbutton(
    tab_appearance,
    text="Włącz Wysoki Kontrast",
    variable=contrast_var
).grid(row=1, column=0, columnspan=2, sticky="w", padx=5, pady=5)

privacy_var = tk.StringVar(value="Anonimowe")

ttk.Radiobutton(
    tab_privacy,
    text="Wszystkie",
    variable=privacy_var,
    value="Wszystkie"
).pack(anchor="w", pady=2)

ttk.Radiobutton(
    tab_privacy,
    text="Anonimowe",
    variable=privacy_var,
    value="Anonimowe"
).pack(anchor="w", pady=2)

ttk.Radiobutton(
    tab_privacy,
    text="Żadne",
    variable=privacy_var,
    value="Żadne"
).pack(anchor="w", pady=2)

pbar = ttk.Progressbar(root, mode="indeterminate", length=300)
pbar.pack(pady=5)

ttk.Button(root, text="Zapisz Ustawienia", command=save_settings).pack(pady=5)

root.mainloop()
