import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def polacz():
    return mysql.connector.connect(
        host="localhost",
        user="Twoj_User",
        password="Twoje_Haslo",
        database="mojabaza"
    )

def dodaj_film(t, r, y, o):
    db = polacz()
    c = db.cursor()
    c.execute(
        "INSERT INTO filmy (tytul, rezyser, rok, ocena) VALUES (%s,%s,%s,%s)",
        (t, r, y, o)
    )
    db.commit()
    c.close()
    db.close()

def pobierz_filmy(fraza=""):
    db = polacz()
    c = db.cursor()
    if fraza:
        c.execute(
            "SELECT * FROM filmy WHERE tytul LIKE %s",
            (f"%{fraza}%",)
        )
    else:
        c.execute("SELECT * FROM filmy")
    dane = c.fetchall()
    c.close()
    db.close()
    return dane

def usun_film(fid):
    db = polacz()
    c = db.cursor()
    c.execute("DELETE FROM filmy WHERE id=%s", (fid,))
    db.commit()
    c.close()
    db.close()

def aktualizuj_film(fid, t, r, y, o):
    db = polacz()
    c = db.cursor()
    c.execute(
        "UPDATE filmy SET tytul=%s, rezyser=%s, rok=%s, ocena=%s WHERE id=%s",
        (t, r, y, o, fid)
    )
    db.commit()
    c.close()
    db.close()

def odswiez():
    for i in tree.get_children():
        tree.delete(i)
    for f in pobierz_filmy(search_var.get()):
        tree.insert("", tk.END, values=f)

def dodaj():
    try:
        dodaj_film(
            tytul_var.get(),
            rezyser_var.get(),
            int(rok_var.get()),
            float(ocena_var.get())
        )
        odswiez()
    except:
        messagebox.showerror("Błąd", "Nieprawidłowe dane")

def usun():
    sel = tree.selection()
    if not sel:
        return
    fid = tree.item(sel)["values"][0]
    usun_film(fid)
    odswiez()

def edytuj(event):
    sel = tree.selection()
    if not sel:
        return
    dane = tree.item(sel)["values"]

    win = tk.Toplevel(root)
    win.title("Edytuj")

    tv = tk.StringVar(value=dane[1])
    rv = tk.StringVar(value=dane[2])
    yv = tk.StringVar(value=dane[3])
    ov = tk.StringVar(value=dane[4])

    ttk.Entry(win, textvariable=tv).pack(padx=5, pady=5)
    ttk.Entry(win, textvariable=rv).pack(padx=5, pady=5)
    ttk.Entry(win, textvariable=yv).pack(padx=5, pady=5)
    ttk.Entry(win, textvariable=ov).pack(padx=5, pady=5)

    def zapisz():
        try:
            aktualizuj_film(
                dane[0],
                tv.get(),
                rv.get(),
                int(yv.get()),
                float(ov.get())
            )
            win.destroy()
            odswiez()
        except:
            messagebox.showerror("Błąd", "Nieprawidłowe dane")

    ttk.Button(win, text="Zapisz", command=zapisz).pack(pady=5)

root = tk.Tk()
root.title("Katalog Filmów")

tytul_var = tk.StringVar()
rezyser_var = tk.StringVar()
rok_var = tk.StringVar()
ocena_var = tk.StringVar()
search_var = tk.StringVar()

form = ttk.Frame(root, padding=10)
form.pack(fill="x")

ttk.Entry(form, textvariable=tytul_var, width=20).grid(row=0, column=0, padx=5)
ttk.Entry(form, textvariable=rezyser_var, width=20).grid(row=0, column=1, padx=5)
ttk.Entry(form, textvariable=rok_var, width=10).grid(row=0, column=2, padx=5)
ttk.Entry(form, textvariable=ocena_var, width=10).grid(row=0, column=3, padx=5)
ttk.Button(form, text="Dodaj Film", command=dodaj).grid(row=0, column=4, padx=5)

ttk.Entry(form, textvariable=search_var, width=20).grid(row=1, column=0, padx=5, pady=5)
ttk.Button(form, text="Szukaj", command=odswiez).grid(row=1, column=1, padx=5)

cols = ("id", "tytul", "rezyser", "rok", "ocena")
tree = ttk.Treeview(root, columns=cols, show="headings")
for c in cols:
    tree.heading(c, text=c.capitalize())
tree.pack(expand=True, fill="both", padx=10, pady=10)

tree.bind("<Double-1>", edytuj)

ttk.Button(root, text="Usuń Wybrany", command=usun).pack(pady=5)

odswiez()
root.mainloop()
