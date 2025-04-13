import tkinter as tk
from tkinter import ttk, messagebox
contacts = {}
def add_or_update_contact():
    name = name_var.get().strip()
    phone = phone_var.get().strip()
    email = email_var.get().strip()
    address = address_var.get().strip()

    if not name or not phone:
        messagebox.showwarning("Input Error", "Name and Phone are required.")
        return

    if not phone.isdigit() or len(phone) != 10:
        messagebox.showwarning("Input Error", "Phone must be exactly 10 digits.")
        return
    contacts[phone] = {"Name": name, "Email": email, "Address": address}
    update_table()
    clear_fields()
    messagebox.showinfo("Saved", "Contact added/updated successfully!")

def update_table():
    contact_tree.delete(*contact_tree.get_children())
    for phone, info in contacts.items():
        contact_tree.insert("", "end", iid=phone, values=(info["Name"], phone))

def delete_contact():
    selected = contact_tree.selection()
    if selected:
        phone = selected[0]
        contacts.pop(phone, None)
        update_table()
        clear_fields()
        messagebox.showinfo("Deleted", f"Deleted contact: {phone}")
    else:
        messagebox.showerror("Error", "Please select a contact to delete.")

def search_contact():
    keyword = search_var.get().strip().lower()
    for row in contact_tree.get_children():
        contact_tree.delete(row)

    found = False
    for phone, info in contacts.items():
        if keyword in info["Name"].lower() or keyword in phone:
            contact_tree.insert("", "end", iid=phone, values=(info["Name"], phone))
            highlight_box.configure(bg="light green")
            highlight_box.delete("1.0", tk.END)
            highlight_box.insert(tk.END, f"Name: {info['Name']}\nPhone: {phone}\nEmail: {info['Email']}\nAddress: {info['Address']}")
            found = True
            break

    if not found:
        highlight_box.configure(bg="white")
        highlight_box.delete("1.0", tk.END)
        messagebox.showinfo("Not Found", "No matching contact found.")

def clear_fields():
    name_var.set("")
    phone_var.set("")
    email_var.set("")
    address_var.set("")
    search_var.set("")
    highlight_box.configure(bg="white")
    highlight_box.delete("1.0", tk.END)

def on_row_select(event):
    selected = contact_tree.selection()
    if selected:
        phone = selected[0]
        contact = contacts[phone]
        name_var.set(contact["Name"])
        phone_var.set(phone)
        email_var.set(contact["Email"])
        address_var.set(contact["Address"])
root = tk.Tk()
root.title("Reshma's Contact Book")
root.geometry("800x600")
root.configure(bg="#f0f8ff")
name_var = tk.StringVar()
phone_var = tk.StringVar()
email_var = tk.StringVar()
address_var = tk.StringVar()
search_var = tk.StringVar()

form_frame = tk.Frame(root, bg="#f0f8ff")
form_frame.pack(pady=10)

tk.Label(form_frame, text="Name:", bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=5, sticky='e')
tk.Entry(form_frame, textvariable=name_var, bg="#e6f7ff").grid(row=0, column=1, pady=5)

tk.Label(form_frame, text="Phone:", bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5, sticky='e')
def validate_phone(new_value):
    return new_value.isdigit() and len(new_value) <= 10 or new_value == ""

vcmd = root.register(validate_phone)
tk.Entry(form_frame, textvariable=phone_var, bg="#e6f7ff", validate="key", validatecommand=(vcmd, "%P")).grid(row=1, column=1, pady=5)
tk.Label(form_frame, text="Email:", bg="#f0f8ff").grid(row=2, column=0, padx=10, pady=5, sticky='e')
tk.Entry(form_frame, textvariable=email_var, bg="#e6f7ff").grid(row=2, column=1, pady=5)

tk.Label(form_frame, text="Address:", bg="#f0f8ff").grid(row=3, column=0, padx=10, pady=5, sticky='e')
tk.Entry(form_frame, textvariable=address_var, bg="#e6f7ff").grid(row=3, column=1, pady=5)

button_frame = tk.Frame(root, bg="#f0f8ff")
button_frame.pack()

tk.Button(button_frame, text="Add/Update", bg="#4caf50", fg="white", command=add_or_update_contact).grid(row=0, column=0, padx=10, pady=10)
tk.Button(button_frame, text="Delete", bg="#f44336", fg="white", command=delete_contact).grid(row=0, column=1, padx=10)
tk.Button(button_frame, text="Clear", command=clear_fields).grid(row=0, column=2, padx=10)

search_frame = tk.Frame(root, bg="#f0f8ff")
search_frame.pack(pady=5)
tk.Label(search_frame, text="Search by Name/Phone:", bg="#f0f8ff").pack(side=tk.LEFT)
tk.Entry(search_frame, textvariable=search_var, bg="#fff0f5").pack(side=tk.LEFT, padx=5)
tk.Button(search_frame, text="Search", command=search_contact).pack(side=tk.LEFT)

contact_tree = ttk.Treeview(root, columns=("Name", "Phone"), show="headings", height=8)
contact_tree.heading("Name", text="Name")
contact_tree.heading("Phone", text="Phone")
contact_tree.pack(pady=10)
contact_tree.bind("<<TreeviewSelect>>", on_row_select)

highlight_box = tk.Text(root, height=5, width=60)
highlight_box.pack(pady=10)

root.mainloop()