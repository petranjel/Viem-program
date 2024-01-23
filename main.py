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

# Premenne z gui.py


fu.connect_open()
fu.select()
gui.frame_up()
gui.start_pro()
gui.make_tree()
for row in fu.selected_rows:
    state_value = "positive" if row[1] >= 0 else "negative"
    gui.tree.insert("", tk.END, values=row, tags=state_value)
fu.connect_close()


gui.frame_main.mainloop()
