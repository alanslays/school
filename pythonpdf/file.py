import tkinter as tk
from tkinter import filedialog, messagebox
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from datetime import datetime

def generuj_pdf():
    produkt = entry_produkt.get()
    cena = entry_cena.get()
    vat = entry_vat.get()
    notatka = text_notatka.get("1.0", tk.END).strip()

    if not produkt or not cena or not vat:
        messagebox.showwarning("Błąd", "Uzupełnij wszystkie pola produktu!")
        return

    try:
        cena = float(cena)
        vat = float(vat)
    except:
        messagebox.showerror("Błąd", "Cena i VAT muszą być liczbami!")
        return

    wartosc_vat = (cena * vat) / 100
    brutto = cena + wartosc_vat

    sciezka = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("Pliki PDF", "*.pdf")],
        title="Zapisz fakturę jako..."
    )

    if sciezka:
        try:
            c = canvas.Canvas(sciezka, pagesize=A4)
            szerokosc, wysokosc = A4

            data = datetime.now().strftime("%Y-%m-%d %H:%M")

            c.setFont("Helvetica-Bold", 16)
            c.drawString(100, wysokosc - 50, "FAKTURA UPROSZCZONA")

            c.setFont("Helvetica", 10)
            c.drawString(400, wysokosc - 50, f"Data: {data}")

            c.line(100, wysokosc - 60, 500, wysokosc - 60)

            start_y = wysokosc - 120

            c.setFont("Helvetica-Bold", 11)
            c.drawString(100, start_y, "Produkt")
            c.drawString(250, start_y, "Cena Netto")
            c.drawString(350, start_y, "VAT %")
            c.drawString(420, start_y, "Brutto")

            c.line(100, start_y - 5, 500, start_y - 5)

            c.setFont("Helvetica", 11)
            c.drawString(100, start_y - 30, produkt)
            c.drawString(250, start_y - 30, f"{cena:.2f} zł")
            c.drawString(350, start_y - 30, f"{vat:.0f}%")
            c.drawString(420, start_y - 30, f"{brutto:.2f} zł")

            c.setFont("Helvetica", 10)
            c.drawString(100, start_y - 80, f"Wartość VAT: {wartosc_vat:.2f} zł")

            if notatka:
                c.drawString(100, start_y - 120, "Notatka:")
                tekst = c.beginText(100, start_y - 140)
                tekst.setFont("Helvetica", 10)
                tekst.textLines(notatka)
                c.drawText(tekst)

            c.save()

            messagebox.showinfo("Sukces", "Faktura PDF została wygenerowana!")

        except Exception as e:
            messagebox.showerror("Błąd", str(e))


root = tk.Tk()
root.title("Generator Faktur PDF")
root.geometry("400x500")

tk.Label(root, text="Nazwa Produktu:", font=("Arial", 10, "bold")).pack(pady=5)
entry_produkt = tk.Entry(root, width=40)
entry_produkt.pack(pady=5)

tk.Label(root, text="Cena Netto:", font=("Arial", 10, "bold")).pack(pady=5)
entry_cena = tk.Entry(root, width=40)
entry_cena.pack(pady=5)

tk.Label(root, text="Stawka VAT (%):", font=("Arial", 10, "bold")).pack(pady=5)
entry_vat = tk.Entry(root, width=40)
entry_vat.pack(pady=5)

tk.Label(root, text="Notatka:", font=("Arial", 10, "bold")).pack(pady=5)
text_notatka = tk.Text(root, width=40, height=8)
text_notatka.pack(pady=5)

btn_export = tk.Button(root, text="Generuj Fakturę PDF", command=generuj_pdf, bg="#27ae60", fg="white", padx=20)
btn_export.pack(pady=20)

root.mainloop()