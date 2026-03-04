# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# Latihan 2: Melengkapi Potongan Kode 
# =============================================

def insertion_sort(data): # Fungsi untuk mengurutkan data dengan insertion sort
    for i in range(1, len(data)): # Perulangan dari indeks ke-1
        key = data[i] # Nilai yang akan disisipkan
        j = i - 1 # Indeks sebelumnya
        
        while j >= 0 and data[j] > key: # Jika elemen lebih besar dari key
            data[j + 1] = data[j] # Geser elemen ke kanan
            j -= 1 # Mundur satu indeks
        
        data[j + 1] = key # Letakkan key di posisi yang benar

    return data # Mengembalikan data yang sudah terurut

'''
Soal: 
1. Lengkapi kondisi agar menjadi sorting ascending. 
2. Ubah agar menjadi descending. 

Jawab:
1. Yang diisi pada while di baris 16 adalah: data[j] > key, Lalu ditambahkan baris 20: data[j + 1] = key
2. Yang diubah hanya tanda perbandingannya.
Dari:
data[j] > key
Menjadi:
data[j] < key
'''