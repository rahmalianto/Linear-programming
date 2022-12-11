import tkinter as tk
from tkinter import ttk

import numpy as np
from scipy.optimize import linprog



window = tk.Tk()
window.geometry("875x350") # windows size
window.resizable(False, False)
window.title("Optimasi lele sumber mina - Nurhidayah Alfianty")


PAKAN_1MM_LELE_KECIL_VAR = tk.DoubleVar()
PAKAN_1MM_LELE_SEDANG_VAR = tk.DoubleVar()
PAKAN_1MM_LELE_BESAR_VAR = tk.DoubleVar()
BATAS_PAKAN_1MM = tk.DoubleVar()

PAKAN_05MM_LELE_KECIL_VAR = tk.DoubleVar()
PAKAN_05MM_LELE_SEDANG_VAR = tk.DoubleVar()
PAKAN_05MM_LELE_BESAR_VAR = tk.DoubleVar()
BATAS_PAKAN_05MM = tk.DoubleVar()

PAKAN_HALUS_LELE_KECIL_VAR = tk.DoubleVar()
PAKAN_HALUS_LELE_SEDANG_VAR = tk.DoubleVar()
PAKAN_HALUS_LELE_BESAR_VAR = tk.DoubleVar()
BATAS_PAKAN_HALUS = tk.DoubleVar()

HARGA_LELE_KECIL_VAR = tk.DoubleVar()
HARGA_LELE_SEDANG_VAR = tk.DoubleVar()
HARGA_LELE_BESAR_VAR = tk.DoubleVar()




frame1 = ttk.Frame(window)
frame1.grid(pady=10, row=0, column=0)


pakan_1mm_label = ttk.Label(frame1, text="Pakan 1mm")
pakan_1mm_label.grid(padx=10, row=0, column=0)

lele_kecil_label = ttk.Label(frame1, text="Kecil")
lele_kecil_label.grid(padx=10, row=1, column=0)
pakan_1mm_lele_kecil_entry = ttk.Entry(frame1, textvariable=PAKAN_1MM_LELE_KECIL_VAR)
pakan_1mm_lele_kecil_entry.grid(padx=10, row=1, column=1)

lele_sedang_label = ttk.Label(frame1, text="Sedang")
lele_sedang_label.grid(padx=10, row=1, column=2)
pakan_1mm_lele_sedang_entry = ttk.Entry(frame1, textvariable=PAKAN_1MM_LELE_SEDANG_VAR)
pakan_1mm_lele_sedang_entry.grid(padx=10, row=1, column=3)

lele_besar_label = ttk.Label(frame1, text="Besar")
lele_besar_label.grid(padx=10, row=1, column=4)
pakan_1mm_lele_besar_entry = ttk.Entry(frame1, textvariable=PAKAN_1MM_LELE_BESAR_VAR)
pakan_1mm_lele_besar_entry.grid(padx=10, row=1, column=5)

batasan_pakan_1mm_label = ttk.Label(frame1, text="Batasan")
batasan_pakan_1mm_label.grid(padx=10, row=1, column=6)
batasan_pakan_1mm_entry = ttk.Entry(frame1, textvariable=BATAS_PAKAN_1MM)
batasan_pakan_1mm_entry.grid(padx=10, row=1, column=7)



pakan_05mm_label = ttk.Label(frame1, text="Pakan 05mm")
pakan_05mm_label.grid(padx=10, row=2, column=0)

lele_kecil_label = ttk.Label(frame1, text="Kecil")
lele_kecil_label.grid(padx=10, row=3, column=0)
pakan_05mm_lele_kecil_entry = ttk.Entry(frame1, textvariable=PAKAN_05MM_LELE_KECIL_VAR)
pakan_05mm_lele_kecil_entry.grid(padx=10, row=3, column=1)

lele_sedang_label = ttk.Label(frame1, text="Sedang")
lele_sedang_label.grid(padx=10, row=3, column=2)
pakan_05mm_lele_sedang_entry = ttk.Entry(frame1, textvariable=PAKAN_05MM_LELE_SEDANG_VAR)
pakan_05mm_lele_sedang_entry.grid(padx=10, row=3, column=3)

lele_besar_label = ttk.Label(frame1, text="Besar")
lele_besar_label.grid(padx=10, row=3, column=4)
pakan_05mm_lele_besar_entry = ttk.Entry(frame1, textvariable=PAKAN_05MM_LELE_BESAR_VAR)
pakan_05mm_lele_besar_entry.grid(padx=10, row=3, column=5)

batasan_pakan_05mm_label = ttk.Label(frame1, text="Batasan")
batasan_pakan_05mm_label.grid(padx=10, row=3, column=6)
batasan_pakan_05mm_entry = ttk.Entry(frame1, textvariable=BATAS_PAKAN_05MM)
batasan_pakan_05mm_entry.grid(padx=10, row=3, column=7)



pakan_halus_label = ttk.Label(frame1, text="Pakan halus")
pakan_halus_label.grid(padx=10, row=4, column=0)

lele_kecil_label = ttk.Label(frame1, text="Kecil")
lele_kecil_label.grid(padx=10, row=5, column=0)
pakan_halus_lele_kecil_entry = ttk.Entry(frame1, textvariable=PAKAN_HALUS_LELE_KECIL_VAR)
pakan_halus_lele_kecil_entry.grid(padx=10, row=5, column=1)

lele_sedang_label = ttk.Label(frame1, text="Sedang")
lele_sedang_label.grid(padx=10, row=5, column=2)
pakan_halus_lele_sedang_entry = ttk.Entry(frame1, textvariable=PAKAN_HALUS_LELE_SEDANG_VAR)
pakan_halus_lele_sedang_entry.grid(padx=10, row=5, column=3)

lele_besar_label = ttk.Label(frame1, text="Besar")
lele_besar_label.grid(padx=10, row=5, column=4)
pakan_halus_lele_besar_entry = ttk.Entry(frame1, textvariable=PAKAN_HALUS_LELE_BESAR_VAR)
pakan_halus_lele_besar_entry.grid(padx=10, row=5, column=5)

batasan_pakan_halus_label = ttk.Label(frame1, text="Batasan")
batasan_pakan_halus_label.grid(padx=10, row=5, column=6)
batasan_pakan_halus_entry = ttk.Entry(frame1, textvariable=BATAS_PAKAN_HALUS)
batasan_pakan_halus_entry.grid(padx=10, row=5, column=7)



harga_label = ttk.Label(frame1, text="Harga jual")
harga_label.grid(padx=10, row=6, column=0)

harga_lele_kecil_label = ttk.Label(frame1, text="Kecil")
harga_lele_kecil_label.grid(padx=10, row=7, column=0)
harga_lele_kecil_entry = ttk.Entry(frame1, textvariable=HARGA_LELE_KECIL_VAR)
harga_lele_kecil_entry.grid(padx=10, row=7, column=1)

harga_lele_sedang_label = ttk.Label(frame1, text="Sedang")
harga_lele_sedang_label.grid(padx=10, row=7, column=2)
harga_lele_sedang_entry = ttk.Entry(frame1, textvariable=HARGA_LELE_SEDANG_VAR)
harga_lele_sedang_entry.grid(padx=10, row=7, column=3)

harga_lele_besar_label = ttk.Label(frame1, text="Besar")
harga_lele_besar_label.grid(padx=10, row=7, column=4)
harga_lele_besar_entry = ttk.Entry(frame1, textvariable=HARGA_LELE_BESAR_VAR)
harga_lele_besar_entry.grid(padx=10, row=7, column=5)


output_frame = tk.Text(window, height=7)
output_frame.grid(pady=10, row=2, column=0)


def tombol_hitung():
    res = None

    try:
        pakan_1mm = [PAKAN_1MM_LELE_KECIL_VAR.get(), PAKAN_1MM_LELE_SEDANG_VAR.get(), PAKAN_1MM_LELE_BESAR_VAR.get()]
        pakan_05mm = [PAKAN_05MM_LELE_KECIL_VAR.get(), PAKAN_05MM_LELE_SEDANG_VAR.get(), PAKAN_05MM_LELE_BESAR_VAR.get()]
        pakan_halus = [PAKAN_HALUS_LELE_KECIL_VAR.get(), PAKAN_HALUS_LELE_SEDANG_VAR.get(), PAKAN_HALUS_LELE_BESAR_VAR.get()]
        batasan_pakan = [BATAS_PAKAN_1MM.get(), BATAS_PAKAN_05MM.get(), BATAS_PAKAN_HALUS.get()]
        harga_lele = [HARGA_LELE_KECIL_VAR.get()*-1, HARGA_LELE_SEDANG_VAR.get()*-1, HARGA_LELE_BESAR_VAR.get()*-1]
        
        A = np.array([pakan_1mm, pakan_05mm, pakan_halus, [-1, 0, 0], [0, -1, 0], [0, 0, -1]])
        b = np.array(batasan_pakan + [0, 0, 0])
        c = np.array(harga_lele)

        res = linprog(c, A_ub=A, b_ub=b, method='simplex')
        print(res)
        optimal_pakan_1mm = round(res.x[0],1)
        optimal_pakan_05mm = round(res.x[1],1)
        optimal_pakan_halus = round(res.x[2],1)
        optimal_keuntungan = round(res.fun*-1,1)

        print_value = 'Jumlah optimal untuk masing2 ikan adalah: \n - Ikan kecil: ' + str(optimal_pakan_1mm) + \
            ' kg \n - Ikan sedang: ' + str(optimal_pakan_05mm) + \
            ' kg \n - Ikan besar ' + str(optimal_pakan_halus) + \
            ' kg \n\n Sehingga keuntungan optimal yang diperoleh adalah senilai: Rp. ' + str(optimal_keuntungan)
    except Exception as e:
        print_value = 'Terjadi error: ' + str(e)

    print(print_value)
    output_frame.delete('1.0', tk.END)
    output_frame.insert(tk.END, print_value)

    return res

tombol_enter = ttk.Button(frame1, text="Hitung", command=tombol_hitung)
tombol_enter.grid(padx=10, row=8, column=7)

window.mainloop()