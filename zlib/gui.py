import tkinter as tk
from tkinter import messagebox  # Correctly import messagebox
import zlib, base64

def compress(inputfile, outputfile):
    with open(inputfile, 'r') as file:
        data = file.read()
    data_bytes = bytes(data, 'utf-8')
    compressed_data = base64.b64encode(zlib.compress(data_bytes, 9))
    decoded_data = compressed_data.decode('utf-8')
    with open(outputfile, 'w') as compressed_file:
        compressed_file.write(decoded_data)

def decompress(inputfile, outputfile):
    with open(inputfile, 'r') as file:
        file_content = file.read()
    encoded_data = file_content.encode('utf-8')
    decompressed_data = zlib.decompress(base64.b64decode(encoded_data))
    decoded_data = decompressed_data.decode('utf-8')
    with open(outputfile, 'w') as file:
        file.write(decoded_data)

def perform_compression():
    input_path = input_entry.get()
    output_path = output_entry.get()
    if input_path and output_path:
        compress(input_path, output_path)
        messagebox.showinfo("Success", "Compression completed successfully!")
    else:
        messagebox.showerror("Error", "Please enter both input and output file paths")

def perform_decompression():
    input_path = dentry.get()
    output_path = dout.get()
    if input_path and output_path:
        decompress(input_path, output_path)
        messagebox.showinfo("Success", "Decompression completed successfully!")
    else:
        messagebox.showerror("Error", "Please enter both input and output file paths")

def setup_compression_ui():
    clear_window()
    global input_entry, output_entry
    input_entry = tk.Entry(window)
    output_entry = tk.Entry(window)
    
    input_label = tk.Label(window, text="File to be compressed")
    output_label = tk.Label(window, text="Compressed file")
    compress_button = tk.Button(window, text="Compress", command=perform_compression)
    back_button = tk.Button(window, text="Back", command=initial_ui)
    
    input_label.grid(row=0, column=0)
    input_entry.grid(row=0, column=1)
    output_label.grid(row=1, column=0)
    output_entry.grid(row=1, column=1)
    compress_button.grid(row=2, column=1)
    back_button.grid(row=3, column=0)

def setup_decompression_ui():
    clear_window()
    global dentry, dout
    dentry = tk.Entry(window)
    dout = tk.Entry(window)
    
    dinput = tk.Label(window, text="Compressed File")
    doutput = tk.Label(window, text="Decompressed File")
    decompress_button = tk.Button(window, text="Decompress", command=perform_decompression)
    back_button = tk.Button(window, text="Back", command=initial_ui)
    
    dinput.grid(row=0, column=0)
    dentry.grid(row=0, column=1)
    doutput.grid(row=1, column=0)
    dout.grid(row=1, column=1)
    decompress_button.grid(row=2, column=1)
    back_button.grid(row=3, column=0)

def clear_window():
    for widget in window.winfo_children():
        widget.destroy()

def initial_ui():
    clear_window()
    compress_button = tk.Button(window, text="Compress", command=setup_compression_ui)
    decompress_button = tk.Button(window, text="Decompress", command=setup_decompression_ui)
    compress_button.pack()
    decompress_button.pack()

window = tk.Tk()
window.title("Compressor and Decompressor")
window.geometry("300x200")

initial_ui()

window.mainloop()
