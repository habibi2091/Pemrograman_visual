import tkinter as tk
from tkinter
import simpledialog, messagebox
import math

def hitung_luas(jari_jari):
    return math.pi * (jari_jari**2)

def hitung_keliling(jari_jari):
    return 2 * math.pi * jari_jari

def tampilkan_hasil(luas, keliling):
    hasil_str = f"Luas lingkaran: {luas:.2f}\nKeliling lingkaran: {keliling:.2f}"
    messagebox.showinfo("Hasil", hasil_str)

def main():
    window = tk.Tk()
    window.title("Program Menghitung Lingkaran")

    jari_jari = simpledialog.askfloat("Input", "Masukkan panjang jari-jari lingkaran:")

    if jari_jari is not None:  # Menangani pengguna membatalkan dialog
        luas = hitung_luas(jari_jari)
        keliling = hitung_keliling(jari_jari)

        tampilkan_hasil(luas, keliling)

    window.mainloop()

if __name__ == "__main__":
    main()
