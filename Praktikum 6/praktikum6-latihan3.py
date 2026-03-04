# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# Latihan 3: Tracing Insertion Sort
# =============================================

# Data awal
data = [5, 2, 4, 6, 1, 3] # List yang akan diurutkan

# Proses Insertion Sort
for i in range(1, len(data)): # Perulangan dari indeks ke-1
    key = data[i] # Nilai yang akan disisipkan
    j = i - 1 # Indeks sebelumnya
    pergeseran = 0 # Menghitung pergeseran

    while j >= 0 and data[j] > key: # Jika lebih besar dari key
        data[j + 1] = data[j] # Geser ke kanan
        j -= 1 # Mundur satu indeks
        pergeseran += 1 # Tambah pergeseran

    data[j + 1] = key # Letakkan key di posisi benar

    print(f"Iterasi i = {i}, data = {data}, pergeseran = {pergeseran}") # Tampilkan hasil
    
'''
Soal: 
1. Tuliskan isi list setelah iterasi i = 1. 
2. Tuliskan isi list setelah iterasi i = 3. 
3. Berapa kali pergeseran terjadi pada iterasi i = 4?

Jawab:
1. Pada iterasi ini, angka 2 dibandingkan dengan 5 lalu ditukar posisinya.
Hasilnya: [2, 5, 4, 6, 1, 3]
2. Pada iterasi ini, angka 6 dibandingkan dengan angka sebelumnya. Karena 6 lebih besar, tidak ada pergeseran.
Hasilnya tetap: [2, 4, 5, 6, 1, 3]
3. Pada iterasi ini, angka 1 dibandingkan dengan 6, 5, 4, dan 2.
Semua angka tersebut lebih besar dari 1, jadi terjadi 4 kali pergeseran.
'''