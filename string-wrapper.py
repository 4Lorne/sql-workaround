import tkinter as tk
from tkinter import filedialog

wrap_strings = True

def wrap_strings_with_quotes(file_path=None, values=None):
    if file_path:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    elif values:
        lines = values.split('\n')
    
    if wrap_strings:
        wrapped_strings = [f"'{line.strip()}'," for line in lines[:-1]]
        wrapped_strings.append(f"'{lines[-1].strip()}'")
    else:
        wrapped_strings = [f"{line.strip()}," for line in lines[:-1]]
        wrapped_strings.append(lines[-1].strip())
    
    return wrapped_strings

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        wrapped_strings = wrap_strings_with_quotes(file_path=file_path)
        wrapped_text = '\n'.join(wrapped_strings)
        text_field.delete(1.0, tk.END)  # Clear the text field
        text_field.insert(tk.END, wrapped_text)  # Insert the wrapped strings

def process_values():
    values = text_field.get(1.0, tk.END).strip()
    wrapped_strings = wrap_strings_with_quotes(values=values)
    wrapped_text = '\n'.join(wrapped_strings)
    text_field.delete(1.0, tk.END)  # Clear the text field
    text_field.insert(tk.END, wrapped_text)  # Insert the wrapped strings

def toggle_wrap_strings():
    global wrap_strings
    wrap_strings = not wrap_strings

root = tk.Tk()

# Create a text field
text_field = tk.Text(root)
text_field.pack()

button = tk.Button(root, text='Open File', command=open_file_dialog)
button.pack()

process_button = tk.Button(root, text='Process', command=process_values)
process_button.pack()

wrap_button = tk.Checkbutton(root, text='Strings', command=toggle_wrap_strings)
wrap_button.select()  # Mark the button as checked by default
wrap_button.pack()

root.mainloop()
