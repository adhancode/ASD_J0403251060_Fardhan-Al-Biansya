# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# Latihan 4: Memahami Kode Program (Merge Sort) 
# =============================================

def merge_sort(data): # Fungsi untuk mengurutkan list dengan metode merge sort
    if len(data) <= 1: # Jika data 0 atau 1 elemen (sudah terurut)
        return data # Kembalikan data apa adanya
    
    mid = len(data) // 2 # Menentukan titik tengah
    left = data[:mid] # Membagi bagian kiri
    right = data[mid:] # Membagi bagian kanan
    
    left_sorted = merge_sort(left) # Mengurutkan bagian kiri (rekursif)
    right_sorted = merge_sort(right) # Mengurutkan bagian kanan (rekursif)
    
    return merge(left_sorted, right_sorted) # Menggabungkan dua bagian yang sudah terurut

'''
Soal: 
1. Apa yang dimaksud dengan base case? 
2. Mengapa fungsi memanggil dirinya sendiri? 
3. Apa tujuan fungsi merge()? 

Jawab:
1. Base case adalah kondisi berhenti pada rekursi. Pada kode ini yaitu `if len(data) <= 1`, artinya jika data hanya satu elemen atau kosong, maka langsung dikembalikan karena sudah terurut.
2. Untuk membagi data menjadi bagian yang lebih kecil sampai mencapai base case, sehingga proses pengurutan lebih mudah dilakukan.
3. Untuk menggabungkan dua list yang sudah terurut menjadi satu list yang tetap terurut.
'''