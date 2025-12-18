import tkinter as tk
from tkinter import ttk, messagebox

class KwadratModel:
    def oblicz(self, liczba):
        return liczba * liczba

class KwadratView(tk.Tk):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.title("Kalkulator Kwadratu (MVC)")
        self.geometry("300x150")

        self.wejscie_var = tk.StringVar()
        self.wynik_var = tk.StringVar(value="Wynik:")

        ttk.Label(self, text="Podaj liczbę:").pack(pady=5)
        self.entry = ttk.Entry(self, textvariable=self.wejscie_var)
        self.entry.pack(pady=5)

        ttk.Button(self, text="Oblicz", command=self.controller.obsluz_oblicz).pack(pady=5)

        ttk.Label(self, textvariable=self.wynik_var, font=("Arial", 12)).pack(pady=5)

    def pobierz_liczbe(self):
        return self.wejscie_var.get()

    def ustaw_wynik(self, wartosc):
        self.wynik_var.set(f"Wynik: {wartosc}")

    def wyczysc_wejscie(self):
        self.wejscie_var.set("")

class KwadratController:
    def __init__(self, model, view=None):
        self.model = model
        self.view = view

    def obsluz_oblicz(self):
        tekst = self.view.pobierz_liczbe()
        try:
            liczba = int(tekst)
            wynik = self.model.oblicz(liczba)
            self.view.ustaw_wynik(wynik)
        except ValueError:
            messagebox.showerror("Błąd", "Podaj poprawną liczbę całkowitą")
            self.view.wyczysc_wejscie()

if __name__ == "__main__":
    model = KwadratModel()
    controller = KwadratController(model)
    view = KwadratView(controller)
    controller.view = view
    view.mainloop()
