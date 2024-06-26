import customtkinter as ctk
from PIL import Image
import tkinter.constants as ctkk
import tkinter as tk
from tkinter import ttk
from CTkMessagebox import CTkMessagebox
from BPlusTree import *
from graphviz import Digraph



# Redirecting stdout
ctk.set_appearance_mode("dark")

app = ctk.CTk()
app.geometry('1200x1000')
app.iconbitmap('images/icon.ico')
app.title('Les algorithmes de hachage')

# les fonction d'Essai Lineare:




def hash_function(key, size):
    return key % size

def insert(table, key, value, size):
    index = hash_function(key, size)

    while table[index] is not None:
        index = (index + 1) % size

    table[index] = (index, value)

def display_table(table):
    return [(i, table[i]) for i in range(len(table))]

def insert_value1(entry, treeview):
    table = hash_table
    size = size_table
    value = entry.get()
    if value.isdigit():
        key = int(value)
        insert(table, key, value, size)
        display_and_update_treeview(table, treeview)
    else:
        key = sum(ord(char) for char in value)
        insert(table, key, value, size)
        display_and_update_treeview(table, treeview)

def delete_value1(entry, treeview):
    table = hash_table
    size = size_table
    value = entry.get()

    # Create a list to store indices of matching values
    indices_to_delete = []

    for i, item in enumerate(table):
        if item is not None and item[1] == value:
            indices_to_delete.append(i)

    # Delete the values at the identified indices
    table[indices_to_delete[0]] = None

    display_and_update_treeview(table, treeview)


def display_and_update_treeview(table, treeview):
    treeview.delete(*treeview.get_children())
    for i, item in enumerate(table):
        if item is not None:
            treeview.insert("", "end", values=(item))
        else:
            treeview.insert("", "end", values=(i, ""))


# les fonction de Hachage quadratique:

def insert_quadratic(entry, treeview):
    table = hash_table
    size = size_table
    value = entry.get()
    if value.isdigit():
        key = int(value)
        index = hash_quadratic(key, size, table)
        table[index] = (index, value)
        display_and_update_treeview(table, treeview)
    else:
        key = sum(ord(char) for char in value)
        index = hash_quadratic(key, size, table)
        table[index] = (index, value)
        display_and_update_treeview(table, treeview)

def hash_quadratic(key, size, table):
    index = key % size
    i = 1
    while table[index] is not None:
        index = (index + i ** 2) % size
        i += 1
    return index


# les fonction de Hachage double:

def insert_double(entry, treeview):
    table = hash_table
    size = size_table
    value = entry.get()
    if value.isdigit():
        key = int(value)
        index = hash_double(key, size, table)
        table[index] = (index, value)
        display_and_update_treeview(table, treeview)
    else:
        key = sum(ord(char) for char in value)
        index = hash_double(key, size, table)
        table[index] = (index, value)
        display_and_update_treeview(table, treeview)

def hash_double(key, size, table):
    prime = 7  # Choose a prime number for double hashing
    index = key % size
    i = 1
    while table[index] is not None:
        index = (index + i * (prime - (key % prime))) % size
        i += 1
    return index
# les fonction de chainage interne:

def insert_internal_chaining(entry, treeview):
    table = hash_table
    size = size_table
    value = entry.get()
    if value.isdigit():
        key = int(value)
        index = hash_function(key, size)
        if table[index] is None:
            table[index] = (index, value, "")
        else:
            # Handle collision by finding an empty space for the linked list
            link_index = find_empty_space(table, index, size)
            table[link_index] = (link_index, value, table[index][0])
            table[index] = (index, table[index][1], link_index)

        display_and_update_treeview_internal_chaining(table, treeview)
    else:
        key = sum(ord(char) for char in value)
        index = hash_function(key, size)
        if table[index] is None:
            table[index] = (index, value, "")
        else:
            link_index = find_empty_space(table, index, size)
            table[link_index] = (link_index, value, table[index][0])
            table[index] = (index, table[index][1], link_index)

        display_and_update_treeview_internal_chaining(table, treeview)

def find_empty_space(table, start_index, size):
    index = (start_index + 1) % size
    while table[index] is not None:
        index = (index + 1) % size
    return index

def display_and_update_treeview_internal_chaining(table, treeview):
    treeview.delete(*treeview.get_children())
    for i, item in enumerate(table):
        if item is not None:
            treeview.insert("", "end", values=(item))
        else:
            treeview.insert("", "end", values=(i, "", ""))


# Les fonctiones de CHAINAGE SEPARE:
def hash_chainage_separe(a,n) :
    if isinstance(a, int):
        return a%n
    else :
      key=sum(ord(char) for char in a)
      return key%n
        
    
def is_cell_not_empty(parent_widget, row, column):
    widget = parent_widget.grid_slaves(row, column)
    return widget

def insert_chainage_separe(entry,scrollable_frame,Xicon) :
    global size_separer
    size = size_separer
    value = entry.get()
    if value.isdigit() :
     value = int(value)
     ind = hash_chainage_separe(value,size)
    else :
     ind = hash_chainage_separe(value,size)
    n=0
    while is_cell_not_empty(scrollable_frame, ind, n) : 
        n = n+1

    ArrowIcon = ctk.CTkImage(Image.open("icons/rightarrow-icon.png"), size=(25, 25))
    icon_label = ctk.CTkLabel(scrollable_frame, image=ArrowIcon, fg_color="transparent", text="" , width=25, padx=5,pady=5)
    icon_label.grid(row=ind, column=n, padx=5, pady=5)


    label_frame = ctk.CTkFrame(scrollable_frame)
    label_frame.grid(row=ind, column=n+1, padx=10, pady=10)
    value_label = ctk.CTkLabel(label_frame, fg_color="white", text=value, text_color="black" , width=25, padx=5,pady=5)
    value_label.pack(side=tk.LEFT)
    separator = ttk.Separator(label_frame, orient="vertical")
    separator.pack(side=tk.LEFT, fill="y", padx=1)
    newX_label = ctk.CTkLabel(label_frame, image=Xicon, fg_color="white", text="", text_color="black" , width=25, padx=5,pady=5)
    newX_label.pack(side=tk.LEFT)
    if n == 1 :
        label_frame = scrollable_frame.grid_slaves(row=ind, column=0)[0]
        label_frame.winfo_children()[2].configure(image="")
    else : 
        label_frame = scrollable_frame.grid_slaves(row=ind, column=n - 1)[0]
        label_frame.winfo_children()[2].configure(image="")
        
def suppress_chainage_separe(entry, scrollable_frame, Xicon):
    global size_separer
    size = size_separer
    value = entry.get()
    if value.isdigit():
        value = int(value)
        ind = hash_chainage_separe(value, size)
    else:
        ind = hash_chainage_separe(value, size)

    n = 1  # Start from column=1
    found = False

    while is_cell_not_empty(scrollable_frame, ind, n) :
        label_frame = scrollable_frame.grid_slaves(row=ind, column=n)[0]
        children = label_frame.winfo_children()
        for child in children:
            if isinstance(child, ctk.CTkLabel):
                label_text = child.cget("text")
                if label_text == value:
                    label_frame.destroy()  # Remove the label 
                    label_frame2 = scrollable_frame.grid_slaves(row=ind, column=n-1)[0]
                    if label_frame2:
                     label_frame2.destroy() 
                    label_value_prev = scrollable_frame.grid_slaves(row=ind, column=n-2)[0].winfo_children()[2]
                    label_value_next = scrollable_frame.grid_slaves(row=ind, column=n+2)
                    if not label_value_next : 
                         label_value_prev.configure(image=Xicon)
                    found = True
                   # Shift columns to the left
                    shift_columns_to_left(scrollable_frame, ind, n+1)
                    break
            
        if found:
            break
        n += 1
    if not found:
        print(f"Value {value} not found.")

def shift_columns_to_left(scrollable_frame, row, start_column):
    # Move columns to the left
    for col in range(start_column, scrollable_frame.grid_size()[0]+1):
        widget = scrollable_frame.grid_slaves(row=row, column=col)
        if widget:
            widget = widget[0]
            widget.grid(row=row, column=col-2)
 

# Les fonction d'Arbre B+:

def generate_dot(node, dot):
    if node.check_leaf:
        dot.node(str(node.values), shape='record')
    else:
        dot.node(str(node.values), shape='ellipse')
        for child in node.keys:
            dot.edge(str(node.values), str(child.values))
            generate_dot(child, dot)

def visualize_bplustree(bplustree, canvas):
    dot = Digraph(comment='B+ Tree')
    dot.attr(rankdir='TB')
    generate_dot(bplustree.root, dot)

    dot.render('bplustree', format='png', cleanup=True)
    
    img = tk.PhotoImage(file='bplustree.png')
    canvas.config(width=img.width(), height=img.height())
    canvas.create_image(0, 0, anchor=tk.NW, image=img)
    canvas.image = img


def insert_value(entry_value, canvas):
    global bplustree, record_len
    value = entry_value.get().strip()
    key = value  # For simplicity, using the value as the key
    bplustree.insert(value, key)
    visualize_bplustree(bplustree, canvas)

def delete_value(entry_value, canvas):
    value = entry_value.get().strip()
    key = value  # For simplicity, using the value as the key
    bplustree.delete(value, key)
    visualize_bplustree(bplustree, canvas)

record_len = None
bplustree = bplustree = BplusTree(3)
def update_record_len(c):
    global record_len, bplustree
    record_len = int(c)
    print(record_len)
    bplustree = BplusTree(record_len)


head_frame = ctk.CTkFrame(master=app, height=100, fg_color='#5e2c59', bg_color='#5e2c59')
head_frame.pack(side='top', fill='x')

bg_head_img = ctk.CTkImage(light_image=Image.open("images/head-bg.png"), dark_image=Image.open("images/head-bg.png"),
                           size=(1700, 100))

image_head_label = ctk.CTkLabel(master=head_frame, image=bg_head_img, text="")
image_head_label.place(relx=0.5, rely=0.46, anchor='center')

head_separator = ctk.CTkLabel(head_frame, text="", height=1, width=1700, fg_color='#5e2c59')
head_separator.place(relx=0.5, rely=1, anchor='center')

def set_table_size(entry, treeview):
    global hash_table, size_table
    size_table = entry.get()
    size_table = int(size_table)
    hash_table = [None] * size_table
    display_and_update_treeview(hash_table, treeview)
# Les fonctions des pages
size_table = None  # initializer un table de 30 elements
hash_table = [None]
def Essai_Lineaire():
    
    global hash_table, size_table
    hash_table = [None]
    
    top_content = ctk.CTkFrame(content_page, height=150)
    top_content.pack(side='top', fill='both', expand='True')
    
    bottom_content = ctk.CTkFrame(content_page)
    bottom_content.pack(side='bottom', fill='both', expand='True')

    size_label = ctk.CTkLabel(top_content, text="Choisissez la taille de votre table :")
    size_label.place(relx=0.15, rely=0.2, anchor="center")

    size_entry = ctk.CTkEntry(top_content)
    size_entry.place(relx=0.15, rely=0.4, anchor="center")

    size_button = ctk.CTkButton(top_content, text="Appliquer", command=lambda: set_table_size(size_entry,treeview))
    size_button.place(relx=0.15, rely=0.6, anchor="center")


    insert_label = ctk.CTkLabel(top_content, text="Insérer une valeur :")
    insert_label.place(relx=0.4, rely=0.2, anchor="center")

    insert_entry = ctk.CTkEntry(top_content)
    insert_entry.place(relx=0.6, rely=0.2, anchor="center")

    insert_button = ctk.CTkButton(top_content, text="Insérer", command=lambda: insert_value1(insert_entry, treeview))
    insert_button.place(relx=0.8, rely=0.2, anchor="center")

    delete_label = ctk.CTkLabel(top_content, text="Supprimer la valeur :")
    delete_label.place(relx=0.4, rely=0.5, anchor="center")

    delete_entry = ctk.CTkEntry(top_content)
    delete_entry.place(relx=0.6, rely=0.5, anchor="center")

    delete_button = ctk.CTkButton(top_content, text="Supprimer", command=lambda: delete_value1(delete_entry, treeview))
    delete_button.place(relx=0.8, rely=0.5, anchor="center")



    table_label = ctk.CTkLabel(top_content, text="Tableau de Hachage:")
    table_label.place(relx=0.5, rely=0.9, anchor="center")


    # Styling the Treeview
    #style = ttk.Style(content_page)
    #style.configure("Treeview", font=('Arial', 12), rowheight=30, fieldbackground='#E3E3E3')
    style = ttk.Style()
    style.configure('Alternate.Treeview', background='lightblue', fieldbackground='white', font=('Courier', 15))

    # Configure the separator style for columns
    style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])

    # Treeview widget
    treeview = ttk.Treeview(bottom_content, columns=("Index", "Donnée"), show="headings", height=100)
    treeview.config(style='Alternate.Treeview')
    treeview.grid(row=3, column=0, columnspan=3, pady=10, sticky="nsew")

    treeview.heading("Index", text="Index")
    treeview.heading("Donnée", text="Donnée")

    # Center the Treeview
    bottom_content.grid_rowconfigure(3, weight=1)
    bottom_content.grid_columnconfigure(0, weight=1)

    display_and_update_treeview(hash_table, treeview)
    for col in ("Index", "Donnée"):
        treeview.column(col,width=100, anchor=tk.CENTER)

def Hachage_Quadratique():
    global hash_table, size_table
    hash_table = [None]

    top_content = ctk.CTkFrame(content_page, height=150)
    top_content.pack(side='top', fill='both', expand='True')
    
    bottom_content = ctk.CTkFrame(content_page)
    bottom_content.pack(side='bottom', fill='both', expand='True')


    size_label = ctk.CTkLabel(top_content, text="Choisissez la taille de votre table :")
    size_label.place(relx=0.15, rely=0.2, anchor="center")

    size_entry = ctk.CTkEntry(top_content)
    size_entry.place(relx=0.15, rely=0.4, anchor="center")

    size_button = ctk.CTkButton(top_content, text="Appliquer", command=lambda: set_table_size(size_entry,treeview))
    size_button.place(relx=0.15, rely=0.6, anchor="center")


    insert_label = ctk.CTkLabel(top_content, text="Insérer une valeur :")
    insert_label.place(relx=0.4, rely=0.2, anchor="center")

    insert_entry = ctk.CTkEntry(top_content)
    insert_entry.place(relx=0.6, rely=0.2, anchor="center")

    insert_button = ctk.CTkButton(top_content, text="Insérer", command=lambda: insert_quadratic(insert_entry, treeview))
    insert_button.place(relx=0.8, rely=0.2, anchor="center")

    delete_label = ctk.CTkLabel(top_content, text="Supprimer la valeur :")
    delete_label.place(relx=0.4, rely=0.5, anchor="center")

    delete_entry = ctk.CTkEntry(top_content)
    delete_entry.place(relx=0.6, rely=0.5, anchor="center")

    delete_button = ctk.CTkButton(top_content, text="Supprimer", command=lambda: delete_value1(delete_entry, treeview))
    delete_button.place(relx=0.8, rely=0.5, anchor="center")

    table_label = ctk.CTkLabel(top_content, text="Tableau de Hachage:")
    table_label.place(relx=0.5, rely=0.9, anchor="center")

    # Styling the Treeview
    style = ttk.Style()
    style.configure('Alternate.Treeview', background='lightblue', fieldbackground='white', font=('Courier', 15))
    style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])

    # Treeview widget
    treeview = ttk.Treeview(bottom_content, columns=("Index", "Donnée"), show="headings", height=100)
    treeview.config(style='Alternate.Treeview')
    treeview.grid(row=3, column=0, columnspan=3, pady=10, sticky="nsew")

    treeview.heading("Index", text="Index")
    treeview.heading("Donnée", text="Donnée")

    # Center the Treeview
    bottom_content.grid_rowconfigure(3, weight=1)
    bottom_content.grid_columnconfigure(0, weight=1)

    display_and_update_treeview(hash_table, treeview)
    for col in ("Index", "Donnée"):
        treeview.column(col, width=100, anchor=tk.CENTER)



def Double_Hachage():
    global hash_table, size_table
    hash_table = [None]

    top_content = ctk.CTkFrame(content_page, height=150)
    top_content.pack(side='top', fill='both', expand='True')
    
    bottom_content = ctk.CTkFrame(content_page)
    bottom_content.pack(side='bottom', fill='both', expand='True')



    size_label = ctk.CTkLabel(top_content, text="Choisissez la taille de votre table :")
    size_label.place(relx=0.15, rely=0.2, anchor="center")

    size_entry = ctk.CTkEntry(top_content)
    size_entry.place(relx=0.15, rely=0.4, anchor="center")

    size_button = ctk.CTkButton(top_content, text="Appliquer", command=lambda: set_table_size(size_entry,treeview))
    size_button.place(relx=0.15, rely=0.6, anchor="center")


    insert_label = ctk.CTkLabel(top_content, text="Insérer une valeur :")
    insert_label.place(relx=0.4, rely=0.2, anchor="center")

    insert_entry = ctk.CTkEntry(top_content)
    insert_entry.place(relx=0.6, rely=0.2, anchor="center")

    insert_button = ctk.CTkButton(top_content, text="Insérer", command=lambda: insert_double(insert_entry, treeview))
    insert_button.place(relx=0.8, rely=0.2, anchor="center")

    delete_label = ctk.CTkLabel(top_content, text="Supprimer la valeur :")
    delete_label.place(relx=0.4, rely=0.5, anchor="center")

    delete_entry = ctk.CTkEntry(top_content)
    delete_entry.place(relx=0.6, rely=0.5, anchor="center")

    delete_button = ctk.CTkButton(top_content, text="Supprimer", command=lambda: delete_value1(delete_entry, treeview))
    delete_button.place(relx=0.8, rely=0.5, anchor="center")

    table_label = ctk.CTkLabel(top_content, text="Tableau de Hachage:")
    table_label.place(relx=0.5, rely=0.9, anchor="center")

    # Styling the Treeview
    style = ttk.Style()
    style.configure('Alternate.Treeview', background='lightblue', fieldbackground='white', font=('Courier', 15))
    style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])

    # Treeview widget
    treeview = ttk.Treeview(bottom_content, columns=("Index", "Donnée"), show="headings", height=100)
    treeview.config(style='Alternate.Treeview')
    treeview.grid(row=3, column=0, columnspan=3, pady=10, sticky="nsew")

    treeview.heading("Index", text="Index")
    treeview.heading("Donnée", text="Donnée")

    # Center the Treeview
    bottom_content.grid_rowconfigure(3, weight=1)
    bottom_content.grid_columnconfigure(0, weight=1)

    display_and_update_treeview(hash_table, treeview)
    for col in ("Index", "Donnée"):
        treeview.column(col, width=100, anchor=tk.CENTER)



def Chainage_intern_page():
    global hash_table, size_table
    hash_table = [None]

    top_content = ctk.CTkFrame(content_page, height=150)
    top_content.pack(side='top', fill='both', expand='True')
    
    bottom_content = ctk.CTkFrame(content_page)
    bottom_content.pack(side='bottom', fill='both', expand='True')

    size_label = ctk.CTkLabel(top_content, text="Choisissez la taille de votre table :")
    size_label.place(relx=0.15, rely=0.2, anchor="center")

    size_entry = ctk.CTkEntry(top_content)
    size_entry.place(relx=0.15, rely=0.4, anchor="center")

    size_button = ctk.CTkButton(top_content, text="Appliquer", command=lambda: set_table_size(size_entry,treeview))
    size_button.place(relx=0.15, rely=0.6, anchor="center")


    insert_label = ctk.CTkLabel(top_content, text="Insérer une valeur :")
    insert_label.place(relx=0.4, rely=0.2, anchor="center")

    insert_entry = ctk.CTkEntry(top_content)
    insert_entry.place(relx=0.6, rely=0.2, anchor="center")

    insert_button = ctk.CTkButton(top_content, text="Insérer", command=lambda: insert_internal_chaining(insert_entry, treeview))
    insert_button.place(relx=0.8, rely=0.2, anchor="center")

    delete_label = ctk.CTkLabel(top_content, text="Supprimer la valeur :")
    delete_label.place(relx=0.4, rely=0.5, anchor="center")

    delete_entry = ctk.CTkEntry(top_content)
    delete_entry.place(relx=0.6, rely=0.5, anchor="center")

    delete_button = ctk.CTkButton(top_content, text="Supprimer", command=lambda: delete_value1(delete_entry, treeview))
    delete_button.place(relx=0.8, rely=0.5, anchor="center")

    table_label = ctk.CTkLabel(top_content, text="Tableau de Hachage:")
    table_label.place(relx=0.5, rely=0.9, anchor="center")
    # Styling the Treeview
    style = ttk.Style()
    style.configure('Alternate.Treeview', background='lightblue', fieldbackground='white', font=('Courier', 15))
    style.layout('Treeview', [('Treeview.treearea', {'sticky': 'nswe'})])

    # Treeview widget
    treeview = ttk.Treeview(bottom_content, columns=("Index", "Donnée", "Lien"), show="headings", height=100)
    treeview.config(style='Alternate.Treeview')
    treeview.grid(row=3, column=0, columnspan=4, pady=10, sticky="nsew")

    treeview.heading("Index", text="Index")
    treeview.heading("Donnée", text="Donnée")
    treeview.heading("Lien", text="Lien")

    # Center the Treeview
    bottom_content.grid_rowconfigure(3, weight=1)
    bottom_content.grid_columnconfigure(0, weight=1)

    display_and_update_treeview_internal_chaining(hash_table, treeview)
    for col in ("Index", "Donnée", "Lien"):
        treeview.column(col, width=100, anchor=tk.CENTER)

def set_separer_size(entry,scrollable_frame):
    global  size_separer
    for frame in scrollable_frame.winfo_children():
        frame.destroy()
    size_separer = entry.get()
    size_separer = int(size_separer)
    Xicon = ctk.CTkImage(Image.open("icons/X-icon.png"), size=(25, 25))
    for i in range(size_separer):
        

        label_frame = ctk.CTkFrame(scrollable_frame)
        label_frame.grid(row=i, column=0, padx=10, pady=10)

        index_label = ctk.CTkLabel(label_frame, text=f"{i}", fg_color="transparent", width=5, padx=5,pady=5)
        index_label.pack(side=tk.LEFT)

        separator = ttk.Separator(label_frame, orient="vertical")
        separator.pack(side=tk.LEFT, fill="y", padx=0)

        X_label = ctk.CTkLabel(label_frame, image=Xicon, fg_color="white", text="", text_color="black" , width=25, padx=5,pady=5)
        X_label.pack(side=tk.LEFT)
    
    

size_separer = None
def Chainage_separer_page():
    
    global size_separer 
    size_separer = None
    top_content = ctk.CTkFrame(content_page, height=150)
    top_content.pack(side='top', fill='both')
    
    bottom_content = ctk.CTkFrame(content_page)
    bottom_content.pack(side='bottom', fill='both', expand='True')

    Xicon = ctk.CTkImage(Image.open("icons/X-icon.png"), size=(25, 25))

    size_label = ctk.CTkLabel(top_content, text="Choisissez la taille de votre table :")
    size_label.place(relx=0.15, rely=0.2, anchor="center")

    size_entry = ctk.CTkEntry(top_content)
    size_entry.place(relx=0.15, rely=0.4, anchor="center")

    size_button = ctk.CTkButton(top_content, text="Appliquer", command=lambda:set_separer_size(size_entry,scrollable_frame))
    size_button.place(relx=0.15, rely=0.6, anchor="center")

    insert_label = ctk.CTkLabel(top_content, text="Insérer une valeur :")
    insert_label.place(relx=0.4, rely=0.2, anchor="center")

    insert_entry = ctk.CTkEntry(top_content)
    insert_entry.place(relx=0.6, rely=0.2, anchor="center")

    insert_button = ctk.CTkButton(top_content, text="Insérer", command=lambda: insert_chainage_separe(insert_entry,scrollable_frame,Xicon))
    insert_button.place(relx=0.8, rely=0.2, anchor="center")

    delete_label = ctk.CTkLabel(top_content, text="Supprimer une valeur :")
    delete_label.place(relx=0.4, rely=0.5, anchor="center")

    delete_entry = ctk.CTkEntry(top_content)
    delete_entry.place(relx=0.6, rely=0.5, anchor="center")

    delete_button = ctk.CTkButton(top_content, text="Supprimer", command=lambda: suppress_chainage_separe(delete_entry,scrollable_frame, Xicon))
    delete_button.place(relx=0.8, rely=0.5, anchor="center")

    table_label = ctk.CTkLabel(top_content, text="Chaînage séparé:")
    table_label.place(relx=0.5, rely=0.9, anchor="center")

    scrollable_frame = ctk.CTkScrollableFrame(bottom_content,  height=100)
    scrollable_frame.pack(fill='both', expand='True')

    
    for i in range(size_separer):
        

        label_frame = ctk.CTkFrame(scrollable_frame)
        label_frame.grid(row=i, column=0, padx=10, pady=10)

        index_label = ctk.CTkLabel(label_frame, text=f"{i}", fg_color="transparent", width=5, padx=5,pady=5)
        index_label.pack(side=tk.LEFT)

        separator = ttk.Separator(label_frame, orient="vertical")
        separator.pack(side=tk.LEFT, fill="y", padx=0)

        X_label = ctk.CTkLabel(label_frame, image=Xicon, fg_color="white", text="", text_color="black" , width=25, padx=5,pady=5)
        X_label.pack(side=tk.LEFT)

def bplus_tree_page():
    global bplustree, record_len
    top_content = ctk.CTkFrame(content_page, height=150)
    top_content.pack(side='top', fill='both')
    
    bottom_content = ctk.CTkFrame(content_page, fg_color="white")
    bottom_content.pack(side='bottom', fill='both', expand='True')

    # Combobox for record_len
    label_record_len = ctk.CTkLabel(top_content, text="Choisir le degree d'arbre:")
    label_record_len.place(relx=0.3, rely=0.25, anchor="center")
    
    combobox_var = ctk.StringVar(value="3")
    combobox = ctk.CTkComboBox(top_content, values=["3", "4", "5", "6", "7"], command=update_record_len, variable=combobox_var)
    combobox.place(relx=0.3, rely=0.55, anchor="center")


    label_insert = ctk.CTkLabel(top_content, text="Insert Value:")
    label_insert.place(relx=0.5, rely=0.25, anchor="center")

    entry_insert = ctk.CTkEntry(top_content)
    entry_insert.place(relx=0.5, rely=0.45, anchor="center")

    button_insert = ctk.CTkButton(top_content, text="Insert", command=lambda: insert_value(entry_insert, canvas))
    button_insert.place(relx=0.5, rely=0.7, anchor="center")

    label_delete = ctk.CTkLabel(top_content, text="Delete Value:")
    label_delete.place(relx=0.7, rely=0.25, anchor="center")

    entry_delete = ctk.CTkEntry(top_content)
    entry_delete.place(relx=0.7, rely=0.45, anchor="center")

    button_delete = ctk.CTkButton(top_content, text="Delete", command=lambda: delete_value(entry_delete, canvas))
    button_delete.place(relx=0.7, rely=0.7, anchor="center")
    
    canvas = ctk.CTkCanvas(bottom_content)
    canvas.place(relx=0.5, rely=0.5, anchor="center")

    visualize_bplustree(bplustree, canvas)


def delet_frame():
    for frame in content_page.winfo_children():
        frame.destroy()

# indicate function
def hide_indicator():
    import_indicate.configure(bg_color='#4D1230')
    ml_indicate.configure(bg_color='#4D1230')
    process_indicate.configure(bg_color='#4D1230')
    vise_indicate.configure(bg_color='#4D1230')
    doc_indicate.configure(bg_color='#4D1230')
    tut_indicate.configure(bg_color='#4D1230')

def indicate(lb, page):
    hide_indicator()
    lb.configure(bg_color='#e06d14')
    delet_frame()
    page()
# Dashboard farme
dashboard_frame = ctk.CTkFrame(master=app, width=250, fg_color='#4D1230', bg_color='#4D1230')
dashboard_frame.pack(side='left', fill='y')

dash_label = ctk.CTkLabel(master=dashboard_frame, text="Dashboard", font=('bold', 30), text_color='white')
dash_label.place(relx=0.5, rely=0.05, anchor='center')

dash_label2 = ctk.CTkLabel(master=dashboard_frame, text="", height=1, width=150, fg_color='#e06d14', corner_radius=30)
dash_label2.place(relx=0.5, rely=0.09, anchor='center')
# Dashboard Buttons

Essai_Lineaire_btn = ctk.CTkButton(master=dashboard_frame, font=('bold', 18), text='Essai Linéaire', compound='left' ,text_color='#e06d14',
                           fg_color='transparent', border_color='#e06d14', border_width=4, width=200, height=50, command=lambda: indicate(import_indicate, Essai_Lineaire))
Essai_Lineaire_btn.place(relx=0.5, rely=0.2, anchor='center', )

import_indicate = ctk.CTkLabel(master=dashboard_frame, text='', bg_color='#4D1230', width=5, height=50)
import_indicate.place(relx=0.04, rely=0.2, anchor='center')

Hachage_Quadratique_btn = ctk.CTkButton(master=dashboard_frame, font=('bold', 16), text='Hachage Quadratique', text_color='#e06d14',
                         fg_color='transparent', border_color='#e06d14', border_width=4, compound='left',width=200, height=50,
                         command=lambda: indicate(vise_indicate, Hachage_Quadratique))
Hachage_Quadratique_btn.place(relx=0.5, rely=0.3, anchor='center')

vise_indicate = ctk.CTkLabel(master=dashboard_frame, text='', bg_color='#4D1230', width=5, height=50)
vise_indicate.place(relx=0.04, rely=0.3, anchor='center')

Double_Hachage_btn = ctk.CTkButton(master=dashboard_frame, font=('bold', 18), text='Double Hachage', text_color='#e06d14',
                            fg_color='transparent', border_color='#e06d14', border_width=4, compound='left', width=200, height=50,
                            command=lambda: indicate(process_indicate, Double_Hachage))
Double_Hachage_btn.place(relx=0.5, rely=0.4, anchor='center')

process_indicate = ctk.CTkLabel(master=dashboard_frame, text='', bg_color='#4D1230', width=5, height=50)
process_indicate.place(relx=0.04, rely=0.4, anchor='center')

Chainage_intern_btn = ctk.CTkButton(master=dashboard_frame, font=('bold', 18), text='Chaînage interne', text_color='#e06d14',
                       fg_color='transparent', border_color='#e06d14', border_width=4, compound='left', width=200, height=50,
                       command=lambda: indicate(ml_indicate, Chainage_intern_page))
Chainage_intern_btn.place(relx=0.5, rely=0.5, anchor='center')

ml_indicate = ctk.CTkLabel(master=dashboard_frame, text='', bg_color='#4D1230', width=5, height=50)
ml_indicate.place(relx=0.04, rely=0.5, anchor='center')


Chainage_separer_btn = ctk.CTkButton(master=dashboard_frame, font=('bold', 18), text='Chaînage séparé', text_color='#e06d14',
                        fg_color='transparent', border_color='#e06d14', border_width=4, compound='left', width=200, height=50,
                        command=lambda: indicate(tut_indicate, Chainage_separer_page))
Chainage_separer_btn.place(relx=0.5, rely=0.6, anchor='center')

tut_indicate = ctk.CTkLabel(master=dashboard_frame, text='', bg_color='#4D1230', width=5, height=50)
tut_indicate.place(relx=0.04, rely=0.6, anchor='center')


bplus_tree_btn = ctk.CTkButton(master=dashboard_frame, font=('bold', 18), text='Arbre b+', text_color='#e06d14',
                        fg_color='transparent', border_color='#e06d14', border_width=4, compound='left',width=200, height=50,
                        command=lambda: indicate(doc_indicate, bplus_tree_page))
bplus_tree_btn.place(relx=0.5, rely=0.7, anchor='center')

doc_indicate = ctk.CTkLabel(master=dashboard_frame, text='', bg_color='#4D1230', width=5, height=50)
doc_indicate.place(relx=0.04, rely=0.7, anchor='center')
content_page = ctk.CTkFrame(master=app)
content_page.pack(side='right', fill="both", expand=True)

team_frame = ctk.CTkFrame(master=content_page)
team_frame.pack(fill='both', expand=True)

bg_img = ctk.CTkImage(light_image=Image.open("images/bag-img.png"), dark_image=Image.open("images/bag-img.png"), size=(1300, 750))
image_label = ctk.CTkLabel(master=team_frame, image=bg_img, text="")
image_label.pack(fill="both", expand=True)

team_img = ctk.CTkImage(light_image=Image.open("images/team.png"), dark_image=Image.open("images/team.png"), size=(400, 400))
team_img_label = ctk.CTkLabel(master=team_frame, image=team_img, text="", corner_radius=10, width=420, height=420, fg_color='#4D1230')
team_img_label.place(relx=0.5, rely=0.5, anchor='center')

app.mainloop()
