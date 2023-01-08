# GUI -> Graphical User Interface

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# init
window = tk.Tk()
window.configure(bg="white")
window.geometry("900x900")
#window.resizable(False,False)
window.title("Siapa Dia!")

# Variabel dan Fungsi
NAMA_DEPAN = tk.StringVar()
NAMA_BELAKANG = tk.StringVar()
ALAMAT = tk.StringVar()
GENDER = tk.StringVar()
TEMPAT_LAHIR = tk.StringVar()
TANGGAL_LAHIR = tk.StringVar()
NAMA_PANGGILAN = tk.StringVar()
NAMA_ADEK = tk.StringVar()
NAMA_AYAH = tk.StringVar()
NAMA_IBU = tk.StringVar()
NAMA_SAHABAT = tk.StringVar()
NAMA_HEWAN = tk.StringVar()
NAMA_MAKANAN = tk.StringVar()
NAMA_MINUMAN = tk.StringVar()
HOBI = tk.StringVar()

def tombol_click():
    '''fungsi ini akan dipanggil oleh tombol'''
    pesan = f"Hallo {NAMA_DEPAN.get()} {NAMA_BELAKANG.get()} {ALAMAT.get()} {GENDER.get()} {TEMPAT_LAHIR.get()} {TANGGAL_LAHIR.get()} {NAMA_PANGGILAN.get()} {NAMA_ADEK.get()} {NAMA_AYAH.get()} {NAMA_IBU.get()} {NAMA_SAHABAT.get()} {NAMA_HEWAN.get()} {NAMA_MAKANAN.get()} {NAMA_MINUMAN.get()} {HOBI.get()}, Chuaaaaaks!"
    showinfo(title="Hey Yo",message=pesan)

# frame input
input_frame = ttk.Frame(window)
# penempatan Grid, Pack, Place
input_frame.pack(padx=10,pady=1,fill="x",expand=True)

# komponen-komponen
# 1. label nama depan
nama_depan_label = ttk.Label(input_frame,text="Nama Depan:")
nama_depan_label.pack(padx=10,pady=1,fill="x",expand=True)
# 2. entry nama depan
nama_depan_entry = ttk.Entry(input_frame,textvariable=NAMA_DEPAN)
nama_depan_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 3. label nama belakang
nama_belakang_label = ttk.Label(input_frame,text="Nama Belakang:")
nama_belakang_label.pack(padx=10,pady=1,fill="x",expand=True)
# 4. entry nama belakang
nama_belakang_entry = ttk.Entry(input_frame,textvariable=NAMA_BELAKANG)
nama_belakang_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 5. label alamat
alamat_label = ttk.Label(input_frame,text="Alamat:")
alamat_label.pack(padx=10,pady=1,fill="x",expand=True)
# 6. entry alamat
alamat_entry = ttk.Entry(input_frame,textvariable=ALAMAT)
alamat_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 7. label gender
gender_label = ttk.Label(input_frame,text="Gender:")
gender_label.pack(padx=10,pady=1,fill="x",expand=True)
# 8. entry gender
gender_entry = ttk.Entry(input_frame,textvariable=GENDER)
gender_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 9. label tempat lahir
tempat_lahir_label = ttk.Label(input_frame,text="Tempat Lahir:")
tempat_lahir_label.pack(padx=10,pady=1,fill="x",expand=True)
# 10. entry tempat lahir
tempat_lahir_entry = ttk.Entry(input_frame,textvariable=TEMPAT_LAHIR)
tempat_lahir_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 11. label nama panggilan
nama_panggilan_label = ttk.Label(input_frame,text="Panggilan:")
nama_panggilan_label.pack(padx=10,pady=1,fill="x",expand=True)
# 12. entry nama panggilan
nama_panggilan_entry = ttk.Entry(input_frame,textvariable=NAMA_PANGGILAN)
nama_panggilan_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 13. label nama adek
nama_adek_label = ttk.Label(input_frame,text="Nama Adek:")
nama_adek_label.pack(padx=10,pady=1,fill="x",expand=True)
# 14. entry nama adek
nama_adek_entry = ttk.Entry(input_frame,textvariable=NAMA_ADEK)
nama_adek_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 15. label nama ayah
nama_ayah_label = ttk.Label(input_frame,text="Nama Ayah:")
nama_ayah_label.pack(padx=10,pady=1,fill="x",expand=True)
# 16. entry nama ayah
nama_ayah_entry = ttk.Entry(input_frame,textvariable=NAMA_AYAH)
nama_ayah_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 17. label nama ibu
nama_ibu_label = ttk.Label(input_frame,text="Nama Ibu:")
nama_ibu_label.pack(padx=10,pady=1,fill="x",expand=True)
# 18. entry nama ibu
nama_ibu_entry = ttk.Entry(input_frame,textvariable=NAMA_IBU)
nama_ibu_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 19. label nama sahabat
nama_sahabat_label = ttk.Label(input_frame,text="Nama Sahabat:")
nama_sahabat_label.pack(padx=10,pady=1,fill="x",expand=True)
# 20. entry nama sahabat
nama_sahabat_entry = ttk.Entry(input_frame,textvariable=NAMA_SAHABAT)
nama_sahabat_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 21. label hewan
nama_hewan_label = ttk.Label(input_frame,text="Nama Hewan:")
nama_hewan_label.pack(padx=10,pady=1,fill="x",expand=True)
# 22. entry nama hewan
nama_hewan_entry = ttk.Entry(input_frame,textvariable=NAMA_HEWAN)
nama_hewan_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 23. label nama makanan
nama_makanan_label = ttk.Label(input_frame,text="Nama Makanan:")
nama_makanan_label.pack(padx=10,pady=1,fill="x",expand=True)
# 24. entry nama makanan
nama_makanan_entry = ttk.Entry(input_frame,textvariable=NAMA_MAKANAN)
nama_makanan_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 25. label nama minuman
nama_minuman_label = ttk.Label(input_frame,text="Nama Minuman:")
nama_minuman_label.pack(padx=10,pady=1,fill="x",expand=True)
# 26. entry nama minuman
nama_minuman_entry = ttk.Entry(input_frame,textvariable=NAMA_MINUMAN)
nama_minuman_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 27. label hobi
nama_hobi_label = ttk.Label(input_frame,text="Hobi:")
nama_hobi_label.pack(padx=10,pady=1,fill="x",expand=True)
# 28. entry hobi
hobi_entry = ttk.Entry(input_frame,textvariable=HOBI)
hobi_entry.pack(padx=10,pady=1,fill="x",expand=True)
# 29. Tombol
tombol_sapa = ttk.Button(input_frame,text="Sapa!",command=tombol_click)
tombol_sapa.pack(fill="x",expand=True,padx=10,pady=10)

# Main Loop window
window.mainloop()