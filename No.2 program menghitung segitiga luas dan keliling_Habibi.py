import tkinter as tk
from tkinter import Label, Entry, Button
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def hitung_luas_dan_keliling():
    alas = float(alas_entry.get())
    tinggi = float(tinggi_entry.get())
    sisi_a = float(sisi_a_entry.get())
    sisi_b = float(sisi_b_entry.get())
    sisi_c = float(sisi_c_entry.get())

    luas = 0.5 * alas * tinggi
    keliling = sisi_a + sisi_b + sisi_c

    luas_label.config(text=f"Luas: {luas}")
    keliling_label.config(text=f"Keliling: {keliling}")

    # Menampilkan segitiga menggunakan Matplotlib
    fig, ax = plt.subplots()
    ax.plot([0, alas, 0, 0], [0, 0, tinggi, 0], 'r-')
    ax.set_xlim(0, max(alas, tinggi) + 1)
    ax.set_ylim(0, max(alas, tinggi) + 1)
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas_widget = canvas.get_tk_widget()
    canvas_widget.grid(row=7, column=0, columnspan=3)

# Membuat jendela utama
window = tk.Tk()
window.title("Segitiga Calculator")

# Label dan Entry untuk Alas
alas_label = Label(window, text="Alas:")
alas_label.grid(row=0, column=0)
alas_entry = Entry(window)
alas_entry.grid(row=0, column=1)

# Label dan Entry untuk Tinggi
tinggi_label = Label(window, text="Tinggi:")
tinggi_label.grid(row=1, column=0)
tinggi_entry = Entry(window)
tinggi_entry.grid(row=1, column=1)

# Label dan Entry untuk Sisi A
sisi_a_label = Label(window, text="Sisi A:")
sisi_a_label.grid(row=2, column=0)
sisi_a_entry = Entry(window)
sisi_a_entry.grid(row=2, column=1)

# Label dan Entry untuk Sisi B
sisi_b_label = Label(window, text="Sisi B:")
sisi_b_label.grid(row=3, column=0)
sisi_b_entry = Entry(window)
sisi_b_entry.grid(row=3, column=1)

# Label dan Entry untuk Sisi C
sisi_c_label = Label(window, text="Sisi C:")
sisi_c_label.grid(row=4, column=0)
sisi_c_entry = Entry(window)
sisi_c_entry.grid(row=4, column=1)

# Tombol untuk Menghitung Luas dan Keliling
hitung_button = Button(window, text="Hitung", command=hitung_luas_dan_keliling)
hitung_button.grid(row=5, column=0, columnspan=2)

# Label untuk Menampilkan Luas dan Keliling
luas_label = Label(window, text="Luas: ")
luas_label.grid(row=6, column=0)
keliling_label = Label(window, text="Keliling: ")
keliling_label.grid(row=6, column=1)

window.mainloop()
