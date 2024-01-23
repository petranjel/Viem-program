# tento modul rieši komunikaciu s text. dokumentom cbox_value.txt v ktorom sa ukladaju rýchle volby pre cbox v mudule gui.py

c_value = str()
fast_offer = []
fast_offer_without = []
c_box = []
import tkinter as tk
from tkinter import messagebox

file_cbox = "cbox_value.txt"


def save_cbox_values():
    try:
        with open(file_cbox, "a+", encoding="utf-8") as file:
            for value in fast_offer_without:
                file.seek(0)
                content = file.read()
                if value not in content:
                    if value.endswith("\n"):
                        file.write(value)
                    else:
                        file.write(value + "\n")
                else:
                    print("Rýchla voľba už existuje")
    except:
        print("Chyba zapisu do cbox_value.txt")


def load_cbox_values():
    try:
        with open(file_cbox, "r", encoding="utf-8") as file:
            for c_value in file:
                if c_value.endswith("\n"):
                    fast_offer.append(c_value)
                    c_value = c_value.replace("\n", "")
                    fast_offer_without.append(c_value)
    except:
        print("Neviem načítať cbox hodnoty zo súboru cbox_value.txt")


def update_cbox_value(old_value, new_value):
    try:
        with open(file_cbox, "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open(file_cbox, "w", encoding="utf-8") as file:
            for line in lines:
                if old_value in line:
                    line = line.replace(old_value, new_value)
                file.write(line)
    except:
        print("Chyba pri aktualizácii hodnoty")


def delete_cbox_value(delete_value):
    try:
        with open(file_cbox, "r", encoding="utf-8") as file:
            lines = file.readlines()

        with open(file_cbox, "w", encoding="utf-8") as file:
            for line in lines:
                if delete_value not in line:
                    file.write(line)
    except:
        print("Chyba pri odstraňovaní hodnoty")


def delete_lists():
    fast_offer.clear()
    fast_offer_without.clear()


def repair_or_delete_cbox_value():
    frame_c_box_config = tk.Tk()
    frame_c_box_config.geometry("600x200")
    frame_c_box_config.config(background="#bffcce")
    frame_c_box_config.title("Pridaj rýchlu voľbu")
    delete_lists()
    load_cbox_values()

    def execute_update_cbox_value():
        def ok():
            new_value = cbox_entry.get()
            update_cbox_value(old_value, new_value)
            frame_c_box_config.destroy()
            delete_lists()
            load_cbox_values()

        def cancel():
            cbox_entry.destroy()
            ok_button.destroy()
            cancel_button.destroy()
            cbox_button_update = tk.Button(
                frame_c_box_config,
                text="Oprav",
                width=18,
                background="#779eff",
                command=execute_update_cbox_value,
            )
            cbox_button_update.grid(column=1, row=0)

        selected_indices = show_fs.curselection()
        if not selected_indices:
            print("Nebola vybraná žiadna hodnota.")
            return
        old_value = show_fs.get(tk.ANCHOR)
        cbox_entry = tk.Entry(frame_c_box_config, width=25)
        cbox_entry.grid(column=0, row=0)
        cbox_entry.insert(tk.END, old_value)
        cbox_button_update.destroy()
        ok_button = tk.Button(
            frame_c_box_config,
            text="Oprav",
            width=18,
            background="#779eff",
            command=ok,
        )
        ok_button.grid(column=1, row=0)
        cancel_button = tk.Button(
            frame_c_box_config,
            text="Zrušiť",
            width=18,
            background="#779eff",
            command=cancel,
        )
        cancel_button.grid(column=2, row=0)

    def execute_remove_cbox_value():
        selected_indices = show_fs.curselection()
        if not selected_indices:
            print("Nebola vybraná žiadna hodnota.")
            return
        delete_value = show_fs.get(tk.ANCHOR)
        if messagebox.askyesno("Vymazať", "Chceš naozaj vymazať rýchlu voľbu?"):
            delete_cbox_value(delete_value)
            frame_c_box_config.destroy()
            delete_lists()
            load_cbox_values()

    show_fs = tk.Listbox(frame_c_box_config, width=30, background="#779eff")
    show_fs.grid(column=0, row=1)
    for val in fast_offer_without:
        show_fs.insert(tk.END, val)

    cbox_button_update = tk.Button(
        frame_c_box_config,
        text="Oprav",
        width=18,
        background="#779eff",
        command=execute_update_cbox_value,
    )
    cbox_button_update.grid(column=1, row=0)
    cbox_button_delete = tk.Button(
        frame_c_box_config,
        text="Vymazať",
        width=18,
        background="#779eff",
        command=execute_remove_cbox_value,
    )
    cbox_button_delete.grid(column=2, row=0)
    frame_c_box_config.wait_window()


def add_c_box_value():
    frame_c_box_config = tk.Tk()
    frame_c_box_config.geometry("600x200")
    frame_c_box_config.config(background="#bffcce")
    frame_c_box_config.title("Pridaj rýchlu voľbu")
    delete_lists()
    load_cbox_values()

    def execute_add_cbox():
        value = cbox_entry.get()
        if value == "":
            print("")
        else:
            if value not in fast_offer_without:
                fast_offer.append(value + "\n")
                fast_offer_without.append(value)

            else:
                print("Táto hodnota už existuje")
            frame_c_box_config.destroy()
            save_cbox_values()

    show_fs = tk.Listbox(frame_c_box_config, width=30, background="#779eff")
    show_fs.grid(column=0, row=1)
    for val in fast_offer_without:
        show_fs.insert(tk.END, val)
    cbox_entry = tk.Entry(frame_c_box_config, width=25)
    cbox_entry.grid(column=0, row=0)
    cbox_button_add = tk.Button(
        frame_c_box_config,
        text="Pridaj do rýchlej voľby",
        width=18,
        background="#779eff",
        command=execute_add_cbox,
    )
    cbox_button_add.grid(column=1, row=0)
    frame_c_box_config.wait_window()


# repair_or_delete_cbox_value()
