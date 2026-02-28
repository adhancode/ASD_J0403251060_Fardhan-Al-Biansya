# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# Latihan 5: Generator PIN
# Tujuan: Menghasilkan semua kemungkinan PIN 3 digit
# Instruksi: Gunakan angka 0 sampai 2 dengan teknik backtracking
# =============================================

def buat_pin(panjang, hasil=""):
    # Base case
    if len(hasil) == panjang:  
        # Jika panjang PIN sudah sesuai, maka PIN dicetak
        print("PIN:", hasil)
        return
    
    # Recursive case
    for angka in ["0", "1", "2"]:
        # Cek agar angka tidak muncul lebih dari satu kali
        if angka not in hasil:
            buat_pin(panjang, hasil + angka)

# Pemanggilan fungsi
buat_pin(3)

# =============================================
# Penjelasan
# =============================================
# Bagaimana cara mencegah angka yang sama muncul berulang?
#
# Cara mencegah angka yang sama muncul berulang adalah dengan melakukan pengecekan sebelum angka ditambahkan ke dalam variabel hasil.
# Pada program ini digunakan kondisi:
#       if angka not in hasil:
#
# Kondisi tersebut berfungsi untuk memastikan bahwa angka yang akan ditambahkan belum pernah digunakan sebelumnya dalam PIN yang sedang dibentuk.
# Jika angka sudah ada di dalam hasil, maka angka tersebut tidak akan dipakai lagi.
#
# Dengan cara ini, setiap angka hanya dapat digunakan satu kali dalam satu PIN, sehingga tidak ada angka yang berulang.