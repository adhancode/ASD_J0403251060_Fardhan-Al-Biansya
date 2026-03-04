# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# Latihan 5: Melengkapi Fungsi Merge 
# =============================================

def merge(left, right):
    result = [] # List untuk menyimpan hasil penggabungan
    i = 0       # Indeks untuk list left
    j = 0       # Indeks untuk list right
    
    while i < len(left) and j < len(right): # Selama kedua list masih ada elemen
        if left[i] <= right[j]:             # Jika elemen left lebih kecil atau sama (ascending)
            result.append(left[i])          # Masukkan elemen left ke result
            i += 1                          # Pindah ke elemen berikutnya di left
        else:
            result.append(right[j])  # Masukkan elemen right ke result
            j += 1                   # Pindah ke elemen berikutnya di right
    
    result.extend(left[i:])   # Tambahkan sisa elemen left (jika ada)
    result.extend(right[j:])  # Tambahkan sisa elemen right (jika ada)
    
    return result # Kembalikan hasil penggabungan yang sudah terurut

'''
Soal: 
1. Lengkapi kondisi agar menjadi ascending. 
2. Jelaskan fungsi result.extend().

Jawab:
1. Yang diisi pada kondisi if di baris 17 adalah: left[i] <= right[j]
2. Fungsi result.extend() digunakan untuk menambahkan sisa elemen yang belum diproses ke dalam result.
Jadi, jika masih ada data yang tersisa di left atau right, semuanya langsung ditambahkan agar tidak ada data yang tertinggal.
'''