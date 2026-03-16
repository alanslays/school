import customtkinter as ctk
import requests
import threading

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Przelicznik walut")
        self.geometry("400x300")

        self.kwota = ctk.CTkEntry(self, placeholder_text="Kwota w PLN")
        self.kwota.pack(pady=10)

        self.waluta = ctk.CTkOptionMenu(self, values=["EUR", "USD", "GBP", "UAH", "CAD", "AUD"])
        self.waluta.pack(pady=10)

        self.przycisk = ctk.CTkButton(self, text="Przelicz", command=self.start_thread)
        self.przycisk.pack(pady=10)

        self.wynik = ctk.CTkLabel(self, text="")
        self.wynik.pack(pady=10)

    def start_thread(self):
        t = threading.Thread(target=self.przelicz)
        t.start()

    def przelicz(self):
        try:
            kwota_pln = float(self.kwota.get())
            wybrana = self.waluta.get()

            url = "http://api.nbp.pl/api/exchangerates/tables/A/?format=json"
            response = requests.get(url)
            data = response.json()

            waluty = data[0]["rates"]
            kurs = [x["mid"] for x in waluty if x["code"] == wybrana][0]

            wynik = kwota_pln / kurs
            tekst = f"{wynik:.2f} {wybrana}"

            self.wynik.configure(text=tekst)

        except Exception as e:
            self.wynik.configure(text="Błąd")

app = App()
app.mainloop()