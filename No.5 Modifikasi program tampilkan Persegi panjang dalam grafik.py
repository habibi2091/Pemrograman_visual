import tkinter as tk
from tkinter import Label, Entry, Button, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def hitung_luas_dan_keliling():
    try:
        panjang = float(panjang_entry.get())
        lebar = float(lebar_entry.get())
        
        if panjang <= 0 or lebar <= 0:
            messagebox.showerror("Error", "Panjang dan lebar harus lebih besar dari 0")
            return

        luas = panjang * lebar
        keliling = 2 * (panjang + lebar)

        luas_label.config(text=f"Luas: {luas}")
        keliling_label.config(text=f"Keliling: {keliling}")

        # Menampilkan persegi panjang menggunakan Matplotlib
        fig, ax = plt.subplots()
        ax.add_patch(plt.Rectangle((0, 0), panjang, lebar, fill=None, edgecolor='red'))
        ax.set_xlim(0, panjang + 1)
        ax.set_ylim(0, lebar + 1)
        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.grid(row=5, column=0, columnspan=3)

    except ValueError:
        messagebox.showerror("Error", "Masukkan angka yang valid untuk panjang dan lebar")

# Membuat jendela utama
window = tk.Tk()
window.title("Persegi Panjang Calculator")

# Label dan Entry untuk Panjang
panjang_label = Label(window, text="Panjang:")
panjang_label.grid(row=0, column=0)
panjang_entry = Entry(window)
panjang_entry.grid(row=0, column=1)

# Label dan Entry untuk Lebar
lebar_label = Label(window, text="Lebar:")
lebar_label.grid(row=1, column=0)
lebar_entry = Entry(window)
lebar_entry.grid(row=1, column=1)

# Tombol untuk Menghitung Luas dan Keliling
hitung_button = Button(window, text="Hitung", command=hitung_luas_dan_keliling)
hitung_button.grid(row=2, column=0, columnspan=2)

# Label untuk Menampilkan Luas dan Keliling
luas_label = Label(window, text="Luas: ")
luas_label.grid(row=3, column=0)
keliling_label = Label(window, text="Keliling: ")
keliling_label.grid(row=3, column=1)

window.mainloop()
