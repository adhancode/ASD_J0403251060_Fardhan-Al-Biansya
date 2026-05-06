# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================

# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur 
# ==========================================================

# Membuat weighted graph dengan dictionary bersarang
# Setiap node menyimpan tetangga dan bobot hubungan antar node
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
# Jalur 1: A -> B -> D
jalur_1 = graph['A']['B'] + graph['B']['D']

# Jalur 2: A -> C -> D
jalur_2 = graph['A']['C'] + graph['C']['D']

# Menampilkan hasil perhitungan masing-masing jalur
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# Membandingkan total bobot kedua jalur
# Jalur dengan bobot lebih kecil dipilih sebagai jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")

'''
Pertanyaan Analisis:
1. Berapa total bobot jalur A -> B -> D?
2. Berapa total bobot jalur A -> C -> D?
3. Jalur mana yang dipilih sebagai jalur terpendek?
4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?

Jawaban:
1. Total bobot jalur A -> B -> D adalah 9.
2. Total bobot jalur A -> C -> D adalah 3.
3. Jalur terpendek yang dipilih adalah A -> C -> D.
4. Jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit, 
karena yang diperhatikan adalah total bobot terkecil, bukan banyaknya langkah.
'''