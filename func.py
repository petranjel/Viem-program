# Sem zapíšem zakladne funkcie

import psycopg2
import startup_database_con as sdc

file_name = "dbconnect.txt"

# Zoznam stringov

connect_string = ""  # string s parametramy pripojenia na databazu
select_string = "SELECT description, value_data, to_char(c_time,'DD.MM.YYYY'),row_id FROM pokladna"  # vyber stlpcov z databazy
select_where_time = "SELECT description, value_data, to_char(c_time,'DD.MM.YYYY'),row_id FROM pokladna WHERE c_time = %s"  # vyber stlpcov z databazy podľa konkretneho datumu
update_string = "UPDATE pokladna SET description=%s,value_data=%s WHERE row_id=%s"  # oprava riadku v databaze indentifikovaneho IDčkom
delete_string = "DELETE FROM pokladna WHERE row_id=%s"  # vymazanie riadku v databaze na indentifikovaneho IDčkom
insert_string = "INSERT INTO pokladna (description,value_data,c_time) VALUES (%s,%s,NOW()) RETURNING row_id"  # vloženie riadku do databazy s aktualnym dátumom a vracia hodnotu ID stplca
select_value_from_time = "SELECT value_data FROM pokladna WHERE c_time=%s"  # vyber riadkov jedneho stlpca z databazy podľa konkretneho datumu

# Zoznam premenných
description = ""
value = float()
row_id = int()
selected_rows = list()


# čítanie suboru a uloženie do stringu v prípade zlihania spustí vytvorenie suboru v mudule startup_database_con.py
def conn_read_from_file():
    global connect_string
    try:
        with open(file_name, "r", encoding="utf-8") as con_file:
            connect_string = con_file.read()
    except:
        sdc.start()
        conn_read_from_file()


# vytvorý spojenie a cursor nad databazou
def connect_open():
    global conn, cursor
    try:
        conn_read_from_file()
        conn = psycopg2.connect(connect_string)
        cursor = conn.cursor()
    except:
        sdc.start()
        connect_open()


# zatvorý spojenie s databazou
def connect_close():
    conn.close()
    cursor.close()


# označanie riadkov v databaze a vloženie da stringu
def select():
    global selected_rows
    cursor.execute(select_string)
    selected_rows = cursor.fetchall()


# pridanie riadku do databazy
def add_row(description, value):
    global row_id
    if description == str(""):
        print("error Popis nevlozeny")
    elif value == str(""):
        print("error Hodnota nevlozena")
    else:
        try:
            value = value.replace(",", ".")
        except:
            pass
        value = float(value)
        connect_open()
        cursor.execute(insert_string, (description, value))
        row_id = cursor.fetchone()
        conn.commit()
        connect_close()
        return row_id, value, description


# oprava riadku v databaze
def update(description, value, row_id):
    connect_open()
    if description == str(""):
        print("error Popis nevlozeny")
    elif value == str(""):
        print("error Hodnota nevlozena")
    try:
        value = value.replace(",", ".")
    except:
        pass
    cursor.execute(update_string, (description, value, row_id))
    conn.commit()
    connect_close()


# vymazanie riadku z databazy
def delete(row_id):
    connect_open()
    cursor.execute(delete_string, (row_id,))
    conn.commit()
    connect_close()
