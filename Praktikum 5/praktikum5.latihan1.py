# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# Latihan 1: Rekursi Pangkat
# Tujuan: Memahami base case dan recursive case
# Instruksi: Buat fungsi rekursif untuk menghitung nilai pangkat.
# =============================================

def pangkat(a, n): 
    # Base case 
    if n == 0: # Jika nilai n sama dengan 0, maka fungsi langsung mengembalikan nilai (Karena secara matematika, a^0 = 1)
        return 1
    
    # Recursive case 
    return a * pangkat(a, n - 1) # Jika n tidak sama dengan 0, maka fungsi akan mengembalikan nilai a dikali dengan hasil dari pangkat(a, n-1), fungsi memanggil dirinya sendiri dengan nilai n yang dikurangi 1

print(pangkat(2, 4))  # Output: 16

# =============================================
# Alur Program
# =============================================
# 1. Program memanggil pangkat(2, 4)
# 2. Karena n != 0, fungsi masuk recursive case
# 3. Fungsi terus memanggil dirinya:
#       pangkat(2,4)
#       pangkat(2,3)
#       pangkat(2,2)
#       pangkat(2,1)
#       pangkat(2,0) -> base case
# 4. Saat n == 0, fungsi mengembalikan 1
# 5. Nilai kemudian dikalikan saat proses kembali (unwinding):
#       2 × 2 × 2 × 2 = 16
#
# Kesimpulan:
# Base case: if n == 0
# Recursive call: pangkat(a, n - 1)