import tkinter as tk
from tkinter import simpledialog, messagebox

def hitung_volume_kubus(sisi):
    return sisi ** 3

def tampilkan_hasil(volume):
    hasil_str = f"Volume kubus: {volume:.2f}"
    messagebox.showinfo("Hasil", hasil_str)

def main():
    window = tk.Tk()
    window.title("Program Menghitung Volume Kubus")

    sisi = simpledialog.askfloat("Input", "Masukkan panjang sisi ke kubus:")
    
    if sisi is not None:  # Menangani pengguna membatalkan dialog
        volume = hitung_volume_kubus(sisi)
        tampilkan_hasil(volume)

    window.mainloop()

if __name__ == "__main__":
    main()
