# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# Latihan 1: Memahami Kode Program (Insertion Sort) 
# =============================================

def insertion_sort(data): # Fungsi untuk mengurutkan data dengan insertion sort
    for i in range(1, len(data)): # Perulangan mulai dari indeks ke-1
        key = data[i] # Menyimpan nilai yang akan disisipkan
        j = i - 1 # Indeks elemen sebelumnya

        while j >= 0 and data[j] > key: # Jika elemen lebih besar dari key
            data[j + 1] = data[j] # Geser elemen ke kanan
            j -= 1 # Mundur satu indeks
        
        data[j + 1] = key # Letakkan key di posisi yang benar
    
    return data # Mengembalikan data yang sudah terurut

'''
Soal: 
1. Mengapa perulangan dimulai dari indeks 1? 
2. Apa fungsi variabel key? 
3. Mengapa digunakan while, bukan for? 
4. Operasi apa yang terjadi di dalam while? 

Jawab:
1. Perulangan dimulai dari indeks 1 karena elemen pertama (indeks 0) sudah dianggap terurut. Jadi proses penyisipan dimulai dari elemen kedua dengan membandingkannya ke bagian kiri.
2. Variabel key berfungsi untuk menyimpan nilai yang sedang diproses. Nilai ini nantinya akan dimasukkan ke posisi yang sesuai setelah dibandingkan dengan elemen sebelumnya.
3. Digunakan while karena jumlah pergeseran tidak bisa ditentukan dari awal. Perulangan akan terus berjalan selama elemen sebelumnya lebih besar dari key.
4. Di dalam while terjadi proses perbandingan dan pergeseran elemen ke kanan. Pergeseran dilakukan sampai ditemukan posisi yang tepat untuk menempatkan key.
'''