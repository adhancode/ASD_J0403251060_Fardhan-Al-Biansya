# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# Latihan 4: Kombinasi Huruf
# Tujuan: Memahami pola choose dan explore
# Instruksi: Buat kombinasi huruf A dan B
# =============================================

def kombinasi(n, hasil=""):

    # Base case
    if len(hasil) == n: # Jika panjang string sudah sama dengan n, artinya kombinasi sudah lengkap
        print(hasil)
        return

    # Recursive case (Choose + Explore)
    kombinasi(n, hasil + "A") # Pilih huruf "A", lalu lanjutkan eksplorasi
    kombinasi(n, hasil + "B") # Pilih huruf "B", lalu lanjutkan eksplorasi

kombinasi(2)

# ============================================
# Penjelasan
# ============================================
# Bagaimana jumlah kombinasi yang dihasilkan? 
# 
# Jumlah kombinasi yang dihasilkan adalah 2^n.
# Karena setiap posisi hanya punya 2 pilihan, yaitu "A" atau "B".
# Jadi kalau n = 2, jumlahnya 2^2 = 4 kombinasi, kalau n = 3, jumlahnya 2^3 = 8 kombinasi.
# Pola yang dipakai di sini adalah: Choose -> Explore. Kita memilih satu huruf, lalu lanjut rekursi sampai memenuhi panjang n.