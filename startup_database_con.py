# Vytvorenie dokumentu s prístupovými udajmi na pripojenie k databaze
# Prípadne chybné zadanie a nasledne zhyhanie pripojenia sa rieši v func.py kde sa vyvola tento modul znova a da tak možnosť vyplniť pristupove udaje znovu
# Toto je veľmi jednoduchá verzia
# Tento modul vytvorá textový súbor dbconnect.txt z ktorého nasledne bude čítať modul func.py informacie pre pripojenie do databazy
# Očakava sa že pripojena databaza bude mať 4 stlpce v tomto poradí: popis (je text), hodnota (je cena/decimal kladna alebo záporná), datum (datum bez času), id (automaticky pridaďovane)

import tkinter as tk

main_color = "#bffcce"
insert_localhost = "localhost"
insert_port = "5432"
insert_dbname = "database name"
insert_user = "user name"
insert_password = "password"

file_new = "dbconnect.txt"


def start():
    startup_frame = tk.Tk()
    startup_frame.geometry("300x150")
    startup_frame.config(background=main_color)
    startup_frame.title("Set database")

    def create_doc():
        new_host = "'" + host_entry.get() + "'"
        new_port = "'" + port_entry.get() + "'"
        new_dbname = "'" + dbname_entry.get() + "'"
        new_user = "'" + user_entry.get() + "'"
        new_password = "'" + password_entry.get() + "'"
        connection_string = (
            "host="
            + new_host
            + " port="
            + new_port
            + " dbname="
            + new_dbname
            + " user="
            + new_user
            + " password="
            + new_password
        )
        with open(file_new, "w", encoding="utf-8") as file:
            file.write(connection_string)

        startup_frame.destroy()

    host_entry = tk.Entry()
    host_entry.pack()
    host_entry.insert(tk.END, insert_localhost)

    port_entry = tk.Entry()
    port_entry.pack()
    port_entry.insert(tk.END, insert_port)

    dbname_entry = tk.Entry()
    dbname_entry.pack()
    dbname_entry.insert(tk.END, insert_dbname)

    user_entry = tk.Entry()
    user_entry.pack()
    user_entry.insert(tk.END, insert_user)

    password_entry = tk.Entry()
    password_entry.pack()
    password_entry.insert(tk.END, insert_password)

    create_doc_button = tk.Button(text="Create", command=create_doc)
    create_doc_button.pack()

    startup_frame.wait_window()
