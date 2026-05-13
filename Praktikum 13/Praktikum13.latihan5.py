# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# ==========================================================
# Latihan 5: Tugas Mandiri Program Minimum Spanning Tree
# ==========================================================

# Kasus yang dipilih:
# Jaringan Jalan Antar Kota

# Membuat daftar edge jalan antar kota
# Format: (bobot, kota1, kota2)
edges = [
    (5, 'Bogor', 'Jakarta'),
    (2, 'Bogor', 'Depok'),
    (3, 'Depok', 'Jakarta'),
    (6, 'Jakarta', 'Bandung'),
    (4, 'Depok', 'Bandung')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

# Menyimpan hasil MST
mst = []

# Menyimpan total bobot minimum
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Perulangan untuk memeriksa setiap edge
for weight, u, v in edges:

    # Memeriksa apakah edge membentuk cycle sederhana
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot ke total
        total_weight += weight

        # Menandai node sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")
for edge in mst:
    # Menampilkan edge yang dipilih
    print(edge)

# Menampilkan total bobot MST
print("Total bobot minimum =", total_weight)


'''
Pertanyaan Analisis:
1. Kasus apa yang dipilih?
2. Algoritma apa yang digunakan?
3. Edge mana saja yang dipilih dalam MST?
4. Berapa total bobot MST?
5. Mengapa edge tertentu tidak dipilih?

Jawaban:
1. Kasus yang dipilih adalah jaringan jalan antar kota.
2. Algoritma yang digunakan adalah Kruskal.
3. Edge yang dipilih adalah Bogor-Depok, Depok-Jakarta, dan Depok-Bandung.
4. Total bobot MST adalah 9.
5. Karena edge tersebut memiliki bobot lebih besar dan dapat membentuk cycle.
'''