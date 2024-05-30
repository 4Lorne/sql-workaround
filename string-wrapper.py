import tkinter as tk
from tkinter import ttk

from tkinter import filedialog

wrap_strings = True

def wrap_strings_with_quotes(file_path=None, values=None):
    if file_path:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    elif values:
        lines = values.split('\n')
    
    wrapped_strings = []
    for line in lines:
        stripped_line = line.strip()
        # Check if the string is already wrapped in single quotes
        if stripped_line.startswith("'") and (stripped_line.endswith("',") or stripped_line.endswith("'")):
            wrapped_strings.append(stripped_line)
        else:
            # Check if the string is a number
            if stripped_line.isdigit():
                wrapped_strings.append(f"{stripped_line},")
            else:
                if wrap_strings:
                    wrapped_strings.append(f"'{stripped_line}',")
                else:
                    wrapped_strings.append(f"{stripped_line},")
    
    # Remove the comma from the last value
    if wrapped_strings:
        wrapped_strings[-1] = wrapped_strings[-1].rstrip(',')
    
    return wrapped_strings

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        wrapped_strings = wrap_strings_with_quotes(file_path=file_path)
        wrapped_text = '\n'.join(wrapped_strings)
        text_field.delete(1.0, tk.END)  # Clear the text field
        text_field.insert(tk.END, wrapped_text)  # Insert the wrapped strings

root = tk.Tk()

notebook = ttk.Notebook(root)
notebook.pack()

def process_values():
    values = text_field.get(1.0, tk.END).strip()
    if not values:  # Check if the text field is empty
        print("Text field is empty. Please enter some text.")
        return  # If it is, return without doing anything
    wrapped_strings = wrap_strings_with_quotes(values=values)
    wrapped_text = '\n'.join(wrapped_strings)
    query = query_entry.get()
    query_with_values = query.replace('{}', wrapped_text)
    
    # Create a new tab with a new text field
    new_tab = tk.Frame(notebook)
    new_text_field = tk.Text(new_tab)
    new_text_field.pack()
    new_text_field.insert(tk.END, query_with_values)  # Insert the query with values

    # Add a button that closes the tab
    close_button = tk.Button(new_tab, text="Close", command=lambda: notebook.forget(new_tab))
    close_button.pack()

    notebook.add(new_tab, text=f'Tab {notebook.index("end")+1}')  # Add the new tab to the notebook

    # Copy the processed text to the clipboard
    root.clipboard_clear()
    root.clipboard_append(query_with_values)

def toggle_wrap_strings():
    global wrap_strings
    wrap_strings = not wrap_strings



# Create a text field
text_field = tk.Text(root)
text_field.pack()

# Create an entry for the query
query_entry = tk.Entry(root)
query_entry.pack()
query_entry.insert(0, "SELECT * IN Example1 WHERE ({})")  # Default query

button = tk.Button(root, text='Open File', command=open_file_dialog)
button.pack()

process_button = tk.Button(root, text='Process', command=process_values)
process_button.pack()

wrap_button = tk.Checkbutton(root, text='Strings', command=toggle_wrap_strings)
wrap_button.select()  # Mark the button as checked by default
wrap_button.pack()

root.mainloop()