# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# Latihan 3: Mencari Nilai Maksimum
# Tujuan: Mengolah struktur data list menggunakan rekursi
# Instruksi: Buat fungsi untuk mencari nilai maksimum.
# =============================================

def cari_maks(data, index=0):

    # Base case
    if index == len(data) - 1:  
        # Jika index sudah di elemen terakhir,maka langsung kembalikan nilai tersebut
        return data[index]

    # Recursive case
    maks_sisa = cari_maks(data, index + 1)  # Fungsi memanggil dirinya sendiri untuk mencari nilai maksimum dari sisa elemen setelah index sekarang

    # Bandingkan elemen sekarang dengan hasil dari sisa elemen
    if data[index] > maks_sisa:  # Jika elemen sekarang lebih besar, kembalikan elemen sekarang
        return data[index]  
    else:                        # Jika tidak, kembalikan maksimum dari sisa list
        return maks_sisa

angka = [3, 7, 2, 9, 5] 
print("Nilai maksimum:", cari_maks(angka)) 

# =============================================
# Alur Program
# =============================================
# 1. Program membuat list angka.
#    Contoh: angka = [3, 7, 2, 9, 5]
# 2. Program memanggil fungsi:
#       cari_maks(angka, 0)
#    Artinya pencarian dimulai dari index 0.
# 3. Jika index belum berada di elemen terakhir, maka fungsi masuk ke recursive case.
# 4. Fungsi akan terus memanggil dirinya sendiri dengan index + 1.
#    Contoh urutan pemanggilan jika data = [3, 7, 2, 9, 5]:
#       cari_maks([3,7,2,9,5], 0)
#       cari_maks([3,7,2,9,5], 1)
#       cari_maks([3,7,2,9,5], 2)
#       cari_maks([3,7,2,9,5], 3)
#       cari_maks([3,7,2,9,5], 4) -> base case (mengembalikan 5)
# 5. Saat sudah sampai di elemen terakhir, kondisi base case terpenuhi:
#       index == len(data) - 1
#    Maka fungsi langsung mengembalikan nilai terakhir.
# 6. Setelah itu proses kembali ke atas (unwinding).
#    Setiap langkah akan membandingkan nilai sekarang dengan nilai maksimum dari sisa elemen.
#       9 dibanding 5 -> ambil 9
#       2 dibanding 9 -> ambil 9
#       7 dibanding 9 -> ambil 9
#       3 dibanding 9 -> ambil 9
# 7. Nilai yang terus dibawa ke atas adalah 9, akhirnya fungsi pertama menerima hasil 9.
# 8. Program mencetak:
#       Nilai maksimum: 9

# Kesimpulan:
# Base case      : index == len(data) - 1
# Recursive call : cari_maks(data, index + 1)
# Fungsi ini bekerja dengan cara turun ke elemen terakhir lalu naik kembali sambil membandingkan setiap elemen sampai ditemukan nilai yang paling besar.