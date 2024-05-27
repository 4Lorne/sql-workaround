import tkinter as tk
from tkinter import filedialog

def wrap_strings_with_quotes(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    wrapped_strings = [f'"{line.strip()}",' for line in lines[:-1]]
    wrapped_strings.append(f'"{lines[-1].strip()}"')
    
    return wrapped_strings

def open_file_dialog():
    file_path = filedialog.askopenfilename(filetypes=[('Text Files', '*.txt')])
    if file_path:
        wrapped_strings = wrap_strings_with_quotes(file_path)
        wrapped_text = '\n'.join(wrapped_strings)
        text_field.delete(1.0, tk.END)  # Clear the text field
        text_field.insert(tk.END, wrapped_text)  # Insert the wrapped strings

root = tk.Tk()

# Create a text field
text_field = tk.Text(root)
text_field.pack()

button = tk.Button(root, text='Open File', command=open_file_dialog)
button.pack()

root.mainloop()