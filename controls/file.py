import tkinter as tk

root = tk.Tk()
root.title("Konwerter Jednostek")
root.geometry("300x200")

tk.Label(root, text="Wprowadź wartość (metry):").pack(pady=10)

entry_metry = tk.Entry(root)
entry_metry.pack(pady=5)

tk.Button(root, text="Konwertuj na stopy").pack(pady=10)

tk.Label(root, text="Wynik: 0.0 stóp").pack(pady=10)

root.mainloop()
