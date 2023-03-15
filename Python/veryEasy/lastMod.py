import os
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

# Initialize dir_path as a global variable
dir_path = ""

# Define the function to get the last modified files in a directory
def get_last_modified_files(num_files):
    try:
        # Get a list of all files in the directory
        files = os.listdir(dir_path)

        # Sort the files by their last modified time in descending order
        files.sort(key=lambda x: os.path.getmtime(os.path.join(dir_path, x)), reverse=True)

        # Get the name and last modified time of the most recently modified files
        last_modified_files = []
        for i in range(num_files):
            if i >= len(files):
                break
            file_path = os.path.join(dir_path, files[i])
            last_modified = os.path.getmtime(file_path)
            last_modified_files.append((files[i], last_modified))

        return last_modified_files

    except FileNotFoundError:
        return []

# Define the function to format the last modified time
def format_last_modified(last_modified):
    return datetime.fromtimestamp(last_modified).strftime('%Y-%m-%d %H:%M:%S')

# Create a GUI window using Tkinter
window = tk.Tk()
window.title('Last Modified Files')

# Add a button to allow the user to select the directory to monitor
def select_dir():
    global dir_path
    dir_path = filedialog.askdirectory()
    if dir_path:
        last_modified_files = get_last_modified_files(5)
        if last_modified_files:
            listbox.delete(0, tk.END)
            for file, last_modified in last_modified_files:
                listbox.insert(tk.END, f'{file} (last modified {format_last_modified(last_modified)})')
        else:
            listbox.delete(0, tk.END)
            listbox.insert(tk.END, 'No files found')

button = tk.Button(window, text='Select Directory', command=select_dir)
button.pack(pady=10)

# Add a listbox to display the last modified files
listbox = tk.Listbox(window, width=70, height=10)
listbox.pack()

# Add a refresh button to update the list of files manually
def refresh():
    last_modified_files = get_last_modified_files(5)
    if last_modified_files:
        listbox.delete(0, tk.END)
        for file, last_modified in last_modified_files:
            listbox.insert(tk.END, f'{file} (last modified {format_last_modified(last_modified)})')
    else:
        listbox.delete(0, tk.END)
        listbox.insert(tk.END, 'No files found')

refresh_button = tk.Button(window, text='Refresh', command=refresh)
refresh_button.pack(pady=10)

# Automatically refresh the list of files every 5 seconds
def auto_refresh():
    refresh()
    window.after(5000, auto_refresh)

# Start auto-refreshing the list of files
auto_refresh()

# Add a button to clear the list of files
def clear_list():
    listbox.delete(0, tk.END)

clear_button = tk.Button(window, text='Clear List', command=clear_list)
clear_button.pack(pady=10)

# Start the GUI main loop
window.mainloop()
