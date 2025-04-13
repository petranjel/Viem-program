# V tomto module sa rieši hlavne uživateľske prostretie ktoré je riešene pomocou knižnice tkinter

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import quick_choice as quick
import func as fu
import datetime
import set_date as sd # import modulu pre nastavenie datumu

main_color = "#bffcce"
first_start = True
add_com = False
upd_com = False

today = datetime.date.today() # ziskanie aktualneho datumu
today_form = today.strftime("%d.%m.%Y") # premenna pre format datumu


def on_closing():
    if messagebox.askyesno(
        "Ukončiť?", "Na nič sa nezabudlo?\nJe pridaná uzávierka a výber z pokladne?"
    ):
        frame_main.destroy()


# Vytvorenie pracovneho okna
def frame_up():
    global frame_main, frame_one, frame_two, frame_three
    frame_main = tk.Tk()
    frame_main.geometry("900x700")
    frame_main.config(background=main_color)
    frame_main.title("Viem")
    frame_main.protocol("WM_DELETE_WINDOW", on_closing)

    frame_one = tk.Frame(frame_main, background=main_color)
    frame_two = tk.Frame(frame_main, background=main_color)
    frame_three = tk.Frame(frame_main, background=main_color)
    frame_one.pack()
    frame_two.pack()
    frame_three.pack()


# vytvorenie tabulky
def make_tree():
    global tree
    tree = ttk.Treeview(
        frame_three,
        columns=("c1", "c2", "c3", "c4"),
        show="headings",
        height=15,
    )

    style = ttk.Style(tree)
    style.configure("Treeview", font=(None, 14), rowheight=30)
    tree.column("c1", anchor=tk.CENTER, width=400)
    tree.heading("c1", text="Popis")
    tree.column("c2", anchor=tk.CENTER, width=150)
    tree.heading("c2", text="Hodnota (EUR)")
    tree.column("c3", anchor=tk.CENTER, width=250)
    tree.heading("c3", text="Datum")
    tree.column("c4", anchor=tk.CENTER, width=100)
    tree.heading("c4", text="ID")
    tree.tag_configure("positive", background="#76ff76")
    tree.tag_configure("negative", background="#f66")
    tree.grid(column=0, row=0)
    tree["displaycolumns"] = ["c1", "c2", "c3"]
    scroll_tree = tk.Scrollbar(
        frame_three, orient=tk.VERTICAL, command=tree.yview, width=30
    )
    scroll_tree.grid(column=1, row=0, sticky="ns")
    tree.configure(yscrollcommand=scroll_tree.set)


# vytvorenie niekoľkých tlačitiel  s rôznymi funkciamy
def button_add_create():
    global button_add
    button_add = tk.Button(
        frame_one,
        text=("Pridaj"),
        background="#59c919",
        width=6,
        height=3,
        command=add_command,
    )
    button_add.grid(column=0, row=0, padx=5, pady=5, ipadx=3)


def button_repair_create():
    global button_repair
    button_repair = tk.Button(
        frame_one,
        text=("Oprav"),
        background="#59c919",
        width=6,
        height=3,
        command=update_command,
    )
    button_repair.grid(column=1, row=0, padx=5, pady=5, ipadx=3)


def button_delete_create():
    global button_delete
    button_delete = tk.Button(
        frame_one,
        text=("Vymaž"),
        background="#59c919",
        width=6,
        height=3,
        command=delete_event,
    )
    button_delete.grid(column=2, row=0, padx=5, pady=5, ipadx=3)


# tlačidlo zatial bez funkcie
def button_time_create():
    global button_time
    button_time = tk.Button(
        frame_one,
        text=("Nastav deň"),
        background="#59c919",
        width=8,
        height=3,
        command=set_date_event,  
    )
    button_time.grid(column=3, row=0, padx=5, pady=5, ipadx=3)


# tlačidlo zatial bez funkcie
def button_filter_as_create():
    global button_filter_as
    button_filter_as = tk.Button(
        frame_one,
        text=("Filtruj podľa\nnové okno"),
        background="#59c919",
        width=10,
        height=3,
    )
    button_filter_as.grid(column=5, row=0, padx=5, pady=5, ipadx=3)


# tlačidlo zatial bez funkcie
def button_coin_create():
    global button_coin
    button_coin = tk.Button(
        frame_one,
        text=("Mincovník"),
        background="#59c919",
        width=8,
        height=3,
    )
    button_coin.grid(column=6, row=0, padx=5, pady=5, ipadx=3)


# zobrazene texty v uživateľskom prostredí
def label_today_create():
    global label_today
    label_today = tk.Label(
        frame_two,
        text=("Dnes je " + " " + today_form),
        background=main_color,
        font=(None, 16),
    )
    label_today.grid(column=1, row=3, sticky="n")


def label_time_set_create():
    global label_time_set
    label_time_set = tk.Label(
        frame_two, text=("Nastavený deň je"), background=main_color, font=(None, 16)
    )
    label_time_set.grid(column=1, row=4)


def sum_label_create():
    global sum_label
    sum_label = tk.Label(
        frame_three, text=("SPOLU 0.0 EUR"), background=main_color, font=(None, 20)
    )
    sum_label.grid(row=1, column=0, ipadx=20)


# tlačidlo pre supustenie časti modulu quick_choice.py ktorý prida rýchlu voľbu
def button_add_c_box_value_create():
    global button_add_c_box_value
    button_add_c_box_value = tk.Button(
        frame_one,
        text="Pridaj rýchlu voľbu",
        background="#779eff",
        width=15,
        height=3,
        command=add_cbox_seq,
    )
    button_add_c_box_value.grid(column=3, row=0, padx=5, pady=5, ipadx=3)


def add_cbox_seq():
    quick.add_c_box_value()
    c_box["values"] = quick.fast_offer_without


# tlačidlo pre supustenie časti modulu quick_choice.py ktorým opravý alebo vymaže rýchlu voľbu
def button_repdel_c_box_value_create():
    global button_repdel_c_box_value
    button_repdel_c_box_value = tk.Button(
        frame_one,
        text="Oprav/vymaž rýchlu voľbu",
        background="#779eff",
        width=20,
        height=3,
        command=update_or_delete_cbox_value,
    )
    button_repdel_c_box_value.grid(column=4, row=0, padx=5, pady=5, ipadx=3)


def update_or_delete_cbox_value():
    quick.repair_or_delete_cbox_value()
    c_box["values"] = quick.fast_offer_without


# vstup pre zadanie hodnoty/sumy
def field_value_create():
    global field_value
    field_value = tk.Entry(frame_two, width=15)
    field_value.grid(column=3, row=2, sticky="n")


# tlačidlo pre pridanie noveho alebo úprava riadku v tabulke
def button_ready_create():
    global button_ready
    button_ready = tk.Button(
        frame_two, text=("Hotovo"), background="#59c919", command=add_event
    )
    button_ready.grid(column=4, row=2, sticky="n")


# vstup pre zadanie popisu s rýchlou voľbou
def c_box_create():
    global c_box
    c_box = ttk.Combobox(frame_two, width=40)
    c_box.grid(column=1, row=2, sticky="n")


# tlačidlo zrušiť/navrat
def button_cancel_create():
    global button_cancel
    button_cancel = tk.Button(
        frame_two, text=("Zrušiť"), background="#59c919", command=cancel
    )
    button_cancel.grid(column=5, row=2, sticky="n")


# tlaťidlo bez funkcie
def asfd_button_create():
    global asfd_button
    asfd_button = tk.Button(
        frame_two, text=("Pridaj hodnotu pokladne"), background="#59c919"
    )
    asfd_button.grid(column=0, row=2, sticky="e")


# vyrvorenie tlačidiel
def start_pro():
    global first_start
    button_add_create()
    button_repair_create()
    button_delete_create()
    button_time_create()
    button_filter_as_create()
    button_coin_create()
    if first_start == True:
        label_today_create()
        label_time_set_create()
        sum_label_create()
        quick.load_cbox_values()
    if first_start == False:
        calculate_sum()

    first_start = False


# vymazanie tlačidiel
def destroy_start():
    button_add.destroy()
    button_repair.destroy()
    button_delete.destroy()
    button_time.destroy()
    button_filter_as.destroy()
    button_coin.destroy()


# tlačidlo pridaj
def add_command():
    global add_com
    destroy_start()
    button_add_c_box_value_create()
    button_repdel_c_box_value_create()
    field_value_create()
    button_ready_create()
    c_box_create()
    button_cancel_create()
    asfd_button_create()
    add_com = True
    c_box.set("Rýchla voľba")
    c_box["values"] = quick.fast_offer_without
    # print(quick.fast_offer_without)


# tlačidlo opraviť
def update_command():
    global upd_com, row, selected_item
    try:    
        selected_item = tree.focus()
        if not selected_item or not selected_item.isidentifier():
            raise ValueError("Nie je vybraná žiadna položka na úpravu.")
        
        destroy_start()
        button_add_c_box_value_create()
        button_repdel_c_box_value_create()
        field_value_create()
        button_ready_create()
        c_box_create()
        button_cancel_create()
        upd_com = True
        c_box["values"] = quick.fast_offer_without
        c_box.insert(tk.END, tree.item(selected_item, "values")[0])
        field_value.insert(tk.END, tree.item(selected_item, "values")[1])
        row = tree.item(
            selected_item,
        )["values"]

    except ValueError as ve:
        messagebox.showerror("Chyba", f"Chyba výberu: {ve}")
    except Exception as e:
        messagebox.showerror("Chyba", f"Neočakávaná chyba: {e}")


# tlačidlo zrušiť
def cancel():
    global add_com, upd_com
    if add_com == True:
        reset_ui()
        add_com = False
    if upd_com == True:
        reset_ui()
        upd_com = False


def add_event():
    global add_com, upd_com
    try:    
        fu.description = c_box.get()
        fu.value = field_value.get()
        if not fu.description or not fu.value:
            raise ValueError("Popis a hodnota musia byť vyplnené.")

        # pridanie novej položky
        if add_com == True:
            fu.add_row(fu.description, fu.value)
            row_tag = "positive" if int(fu.value) >= 0 else "negative"
            tree.insert(
                "",
                tk.END,
                values=(fu.description, fu.value, today_form, fu.row_id),
                tags=row_tag,
            )
            reset_ui()
            add_com = False
        # oprava existujucej polozky
        if upd_com == True:
            fu.row_id = row[3]
            fu.update(fu.description, fu.value, fu.row_id)
            row_tag = "positive" if float(fu.value) >= 0 else "negative"
            tree.item(
                selected_item,
                values=(fu.description, fu.value, row[2], fu.row_id),
                tags=row_tag,
            )
            reset_ui()
            upd_com = False
    except ValueError as ve:
        messagebox.showerror("Chyba", f"Chyba vstupu: {ve}")
    except Exception as e:
        messagebox.showerror("Chyba", f"Neočakávaná chyba: {e}")


# tlačidlo vymazať
def delete_event():
    try:
        selected_item = tree.focus()
        if not selected_item or not selected_item.isidentifier():
            raise ValueError("Nie je vybraná žiadna položka na vymazanie.")

        # Dialogove okno pre potvrdenie vymazania
        confirm = messagebox.askyesno(
            "Potvrdenie vymazania",
            "Naozaj chcete vymazať vybranú položku?"
            + "\n"
            + str(tree.item(selected_item, "values")[0])
            + "\n"
            + str(tree.item(selected_item, "values")[1])+ " eur"
            + "\n" 
            + str(tree.item(selected_item, "values")[2]),
        )
        if not confirm:
            return  # Zruši ak používateľ nepotvrdí

        fu.row_id = tree.item(selected_item, "values")[3]
        fu.delete(fu.row_id)
        tree.delete(selected_item)

    except ValueError as ve:
        messagebox.showerror("Chyba", f"Chyba výberu: {ve}")
    except Exception as e:
        messagebox.showerror("Chyba", f"Neočakávaná chyba: {e}")


# zmazanie tlačidiel
def reset_ui():
    """Reset the UI by destroying all dynamically created widgets and restarting the main UI."""
    widgets = [
        "button_add_c_box_value",
        "button_repdel_c_box_value",
        "field_value",
        "button_ready",
        "c_box",
        "button_cancel",
        "asfd_button",
    ]
    for widget in widgets:
        try:
            globals()[widget].destroy()
        except NameError:
            pass  # Ignore if the widget does not exist
    start_pro()

def set_date_event():

    def update_label_time_set(new_date):
        global label_time_set
        label_time_set.config(text=f"Nastavený deň je {new_date}")

    sd.set_date_ui(on_date_confirmed=update_label_time_set) # Spustenie užívateľského prostredia na nastavenie dátumu s callback funkciou


# Vypočíta súčet hodnôt v stĺpci c2 a aktualizuje sum_label.
def calculate_sum(): 
    try:
        total = 0.0
        for child in tree.get_children():
            value = tree.item(child, "values")[1]  # Získanie hodnoty zo stĺpca c2
            total += float(value)
        sum_label.config(text=f"SPOLU {total:.2f} EUR")
    except ValueError as e:
        messagebox.showerror("Chyba", f"Neplatná hodnota v stĺpci: {e}")
    except Exception as e:
        messagebox.showerror("Chyba", f"Neočakávaná chyba: {e}")
