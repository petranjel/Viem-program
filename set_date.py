import tkinter as tk
from tkinter import messagebox
from tkcalendar import Calendar
import datetime

formatted_date = ""  # Premenná pre formátovaný dátum


def set_date_ui(on_date_confirmed=None):
    """Vytvorí užívateľské prostredie na nastavenie konkrétneho dátumu pomocou kalendára."""
    global formatted_date  # Premenná pre formátovaný dátum
    def confirm_date():

        try:
            selected_date = calendar.get_date()
            specific_date = datetime.datetime.strptime(selected_date, "%d.%m.%Y").date()
            formatted_date = specific_date.strftime("%d.%m.%Y")
            messagebox.showinfo("Úspech", f"Nastavený dátum: {formatted_date}")
            print(f"Nastavený dátum: {formatted_date}")  # Tu môžete pridať kód na spracovanie dátumu
            if on_date_confirmed:
                on_date_confirmed(formatted_date)
            root.destroy()  # Zatvorenie okna po potvrdení dátumu
        except ValueError as e:
            messagebox.showerror("Chyba", f"Neplatný dátum: {e}")

    # Hlavné okno
    root = tk.Tk()
    root.title("Nastavenie dátumu")
    root.geometry("400x300")

    # Kalendár
    calendar = Calendar(root, date_pattern="dd.mm.yyyy")
    calendar.pack(pady=20)

    # Tlačidlo na potvrdenie
    tk.Button(root, text="Potvrdiť", command=confirm_date).pack(pady=10)

    root.mainloop()


# Spustenie užívateľského prostredia
if __name__ == "__main__":
    set_date_ui()
