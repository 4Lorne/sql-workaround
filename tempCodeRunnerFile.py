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

root.mainloop()