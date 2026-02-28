# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# Latihan 2: Tracing Rekursi
# Tujuan: Memahami alur masuk dan keluar fungsi
# Instruksi: Buat fungsi untuk mencari nilai maksimum.
# =============================================

def countdown(n):
    # Base case
    if n == 0:  # Kalau sudah 0, rekursi berhenti
        print("Selesai")
        return

    # Proses saat masuk fungsi
    print("Masuk:", n)

    # Recursive case (fungsi memanggil dirinya sendiri)
    countdown(n - 1)

    # Proses saat keluar fungsi
    print("Keluar:", n)

# Pemanggilan fungsi
countdown(3)

# ============================================
# Penjelasan
# ============================================
# Mengapa "Keluar" muncul terbalik?
#
# Karena proses rekursi menggunakan sistem Call Stack dengan prinsip LIFO (Last In First Out), fungsi yang terakhir dipanggil akan selesai lebih dulu.
# Jadi saat kembali, urutannya jadi dari yang paling kecil dulu.
# "Masuk" dicetak saat fungsi turun ke dalam, dan "Keluar" dicetak saat fungsi naik kembali.
# Makanya urutan "Keluar" terlihat terbalik dibanding "Masuk".