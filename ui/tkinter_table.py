import tkinter as tk
from tkinter import ttk


def get_search_results_table(rows):
    root = tk.Tk()
    root.title('Search Results')
    table = ttk.Treeview(root, columns=('Lyrics', 'Lyricist', 'Year', 'Metaphor',
                                        'Source', 'Target', 'Meaning', 'Gender', 'Resourse'), show='headings', height=50)

    style = ttk.Style()
    style.configure("Treeview", font=('Iskoola Pota', 12))
    style.configure('Treeview', rowheight=150)

    table.heading("#1", text="Lyrics")
    table.heading("#2", text="Lyricist")
    table.heading("#3", text="Year")
    table.heading("#4", text="Metaphor")
    table.heading("#5", text="Source")
    table.heading("#6", text="Target")
    table.heading("#7", text="Meaning")
    table.heading("#8", text="Gender")
    table.heading("#9", text="Resourse")


    for row in rows:
        table.insert('', 'end', values=row)

    table.pack()

    # Set the width of the 'Year', 'Source', 'Target', and 'Gender' columns to less than 20
    table.column('#3', width=50)
    # table.column('#5', width=100)
    # table.column('#6', width=100)
    table.column('#8', width=60)

    # Set the width of other columns to 100
    # table.column('#1', width=400)
    # table.column('#2', width=100)
    # table.column('#4', width=400)
    # table.column('#7', width=100)

    return root
