import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def hitung_luas_dan_keliling():
    panjang = float(entry_panjang.get())
    lebar = float(entry_lebar.get())
    
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    
    label_hasil.config(text=f'Luas: {luas}, Keliling: {keliling}')
    
    # Menampilkan hasil dalam grafik
    figure = Figure(figsize=(4, 3), dpi=100)
    plot = figure.add_subplot(1, 1, 1)
    plot.bar(['Luas', 'Keliling'], [luas, keliling])
    
    canvas = FigureCanvasTkAgg(figure, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()

window = tk.Tk()
window.title("Perhitungan Persegi Panjang")

label_panjang = tk.Label(window, text="Panjang:")
label_panjang.pack()
entry_panjang = tk.Entry(window)
entry_panjang.pack()

label_lebar = tk.Label(window, text="Lebar:")
label_lebar.pack()
entry_lebar = tk.Entry(window)
entry_lebar.pack()

button_hitung = tk.Button(window, text="Hitung", command=hitung_luas_dan_keliling)
button_hitung.pack()

label_hasil = tk.Label(window, text="")
label_hasil.pack()

window.mainloop()
