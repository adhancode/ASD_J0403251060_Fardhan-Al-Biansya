# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# ==========================================================
# Latihan 4: Studi Kasus Jaringan Kabel Antar Gedung
# ==========================================================

# Membuat daftar edge jaringan kabel
# Format: (bobot, node1, node2)
edges = [
    (4, 'GedungA', 'GedungB'),
    (2, 'GedungA', 'GedungC'),
    (3, 'GedungB', 'GedungD'),
    (1, 'GedungC', 'GedungD'),
    (5, 'GedungA', 'GedungD')
]

# Mengurutkan edge dari bobot terkecil
edges.sort()

# Menyimpan hasil MST
mst = []

# Menyimpan total biaya minimum
total_weight = 0

# Menyimpan node yang sudah terhubung
connected = set()

# Perulangan untuk memeriksa edge
for weight, u, v in edges:

    # Memeriksa apakah edge membentuk cycle sederhana
    if u not in connected or v not in connected:

        # Menambahkan edge ke MST
        mst.append((u, v, weight))

        # Menambahkan bobot ke total biaya
        total_weight += weight

        # Menandai node sudah terhubung
        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Jaringan Kabel Minimum:")
for edge in mst:
    # Menampilkan edge yang dipilih
    print(edge)

# Menampilkan total biaya minimum
print("Total biaya minimum =", total_weight)


'''
Pertanyaan Analisis:
1. Algoritma apa yang digunakan?
2. Edge mana saja yang dipilih?
3. Berapa total biaya minimum?
4. Mengapa MST cocok digunakan pada kasus ini?

Jawaban:
1. Algoritma yang digunakan adalah Kruskal.
2. Edge yang dipilih adalah GedungC-GedungD, GedungA-GedungC, dan GedungB-GedungD.
3. Total biaya minimum adalah 6.
4. Karena MST dapat menghubungkan semua gedung dengan biaya paling minimum.
'''