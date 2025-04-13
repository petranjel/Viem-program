# Sem zapíšem základ programu

import func as fu

# Premenne z func.py
fu.description  # spojene so stlpcom description z databazy
fu.value  # spojene so stlpcom value_data z databazy
fu.row_id  # spojene so stlpcom row_id z databazy
fu.selected_rows  # vracia hodnotu row_id z databazy noveho pridaneho riadku

import quick_choice as quick

# Premenne z quick_choice.py
quick.c_value  # spojene s hodnotou ktora sa ma zapisat alebo precitat zo suboru so zoznamom
quick.fast_offer_without  # spojene s listom zoznamu bez \n

import gui
import tkinter as tk


fu.connect_open()       # vytvorenie spojenia s databazou
fu.select()             # pripojenie dat z databazy do stringu
gui.frame_up()          # vytoverenie pracovneho okna
gui.start_pro()         # vytvorenie tlačidiel a dalšie pomocne časti
gui.make_tree()         # vytvorenie tabulky
for row in fu.selected_rows:  # pripojenie dat z databazy
    state_value = "positive" if row[1] >= 0 else "negative"
    gui.tree.insert("", tk.END, values=row, tags=state_value)
fu.connect_close()      # zatvorenie spojenia s databazou
print("Ukončenie programu prebehlo úspešne")  # vypis do konzoly

gui.frame_main.mainloop()
