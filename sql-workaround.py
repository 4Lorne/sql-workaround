import tkinter as tk
from tkinter import filedialog

# Function definitions
def select_input_file():
    input_file = filedialog.askopenfilename()
    input_file_entry.delete(0, tk.END)
    input_file_entry.insert(0, input_file)

def copy_output():
    root.clipboard_clear()
    root.clipboard_append(output_text.get(1.0, tk.END))

def save_output():
    output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    with open(output_file, "w") as f:
        f.write(output_text.get(1.0, tk.END))

def process_file():
    input_file = input_file_entry.get()

    table_name = table_name_entry.get()
    columns_to_search = columns_to_search_entry.get().split(',')
    value_to_find = value_to_find_entry.get()

    initial_query = "select {} from {} where ({}, 0) in (".format(",".join(columns_to_search), table_name, value_to_find)

    with open(input_file, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    chunks = [lines[i:i + 900] for i in range(0, len(lines), 900)]

    output_lines = []
    for i, chunk in enumerate(chunks):
        ids = [line for line in chunk]
        if strings_var.get():
            ids = ['"{}"'.format(id) for id in ids]
        tuples = ["({}, 0)".format(id) for id in ids]
        if i != 0:
            output_lines.append('OR ({}, 0) in ({})'.format(value_to_find, ",".join(tuples)))
        else:
            output_lines.append(initial_query + ",".join(tuples) + ")")

    output_string = "\n".join(output_lines)
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, output_string)

# Creates the window
root = tk.Tk()
root.geometry("425x450")

# Places the widgets
tk.Label(root, text="Input File").grid(row=0, column=0)
input_file_entry = tk.Entry(root)
input_file_entry.grid(row=0, column=1)
input_file_button = tk.Button(root, text="Browse", command=select_input_file)
input_file_button.grid(row=0, column=2)

strings_var = tk.BooleanVar()
strings_checkbox = tk.Checkbutton(root, text="Strings", variable=strings_var)
strings_checkbox.grid(row=1, column=0)

tk.Label(root, text="Table Name").grid(row=2, column=0)
table_name_entry = tk.Entry(root)
table_name_entry.grid(row=2, column=1, padx=(10, 10), pady=(10, 10))
table_name_entry.insert(0, "table1")

tk.Label(root, text="Columns").grid(row=3, column=0)
columns_to_search_entry = tk.Entry(root)
columns_to_search_entry.grid(row=3, column=1, padx=(10, 10), pady=(10, 10))
columns_to_search_entry.insert(0, "column1, column2, column3")

tk.Label(root, text="Value to Find").grid(row=4, column=0)
value_to_find_entry = tk.Entry(root)
value_to_find_entry.grid(row=4, column=1, padx=(10, 10), pady=(10, 10))
value_to_find_entry.insert(0, "value1")

process_button = tk.Button(root, text="Process File", command=process_file)
process_button.grid(row=5, column=0, columnspan=5, padx=(10, 10), pady=(10, 10))

output_text = tk.Text(root, height=10, width=50)
output_text.grid(row=6, column=0, columnspan=5, padx=(10, 10), pady=(10, 10))

copy_button = tk.Button(root, text="Copy Output", command=copy_output)
copy_button.grid(row=7, column=0, columnspan=2, padx=(10, 10), pady=(10, 10))

save_button = tk.Button(root, text="Save Output", command=save_output)
save_button.grid(row=7, column=1, columnspan=2, padx=(10, 10), pady=(10, 10))

# Begins the application
root.mainloop()