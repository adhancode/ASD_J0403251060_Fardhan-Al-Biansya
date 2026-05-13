# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 13 - Graph III: Spanning Tree
# ==========================================================

# ==========================================================
# Materi 2: Implementasi Algoritma Prim
# ==========================================================

# Mengimpor heapq untuk membuat priority queue
import heapq

# Membuat weighted graph
graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},  # Node A terhubung ke B, C, dan D
    'B': {'A': 4, 'D': 3},          # Node B terhubung ke A dan D
    'C': {'A': 2, 'D': 1},          # Node C terhubung ke A dan D
    'D': {'A': 5, 'B': 3, 'C': 1}   # Node D terhubung ke A, B, dan C
}

# Fungsi algoritma Prim
def prim(graph, start):

    # Menyimpan node yang sudah dikunjungi
    visited = set([start])

    # List untuk menyimpan edge sementara
    edges = []

    # Memasukkan edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    # List untuk menyimpan hasil MST
    mst = []

    # Variabel total bobot
    total_weight = 0

    # Perulangan selama masih ada edge
    while edges:

        # Mengambil edge dengan bobot terkecil
        weight, u, v = heapq.heappop(edges)

        # Jika node tujuan belum dikunjungi
        if v not in visited:

            # Menandai node sudah dikunjungi
            visited.add(v)

            # Menambahkan edge ke MST
            mst.append((u, v, weight))

            # Menambahkan bobot ke total
            total_weight += weight

            # Memeriksa tetangga dari node baru
            for neighbor, w in graph[v].items():

                # Jika tetangga belum dikunjungi
                if neighbor not in visited:

                    # Menambahkan edge ke priority queue
                    heapq.heappush(edges, (w, v, neighbor))

    # Mengembalikan hasil MST dan total bobot
    return mst, total_weight

# Menjalankan algoritma Prim dari node A
mst, total = prim(graph, 'A')

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

# Menampilkan edge yang dipilih
for edge in mst:
    print(edge)

# Menampilkan total bobot
print("Total bobot =", total)

'''
Penjelasan:
Program ini menggunakan algoritma Prim untuk mencari
Minimum Spanning Tree (MST).

Proses dimulai dari node A, lalu program memilih edge
dengan bobot paling kecil yang terhubung ke node
yang belum dikunjungi.

Edge yang dipilih:
A-C = 2
C-D = 1
D-B = 3

Total bobot MST adalah 6.

Perbedaan Prim dan Kruskal adalah Prim membangun
tree mulai dari satu node awal, sedangkan Kruskal
memilih edge terkecil dari seluruh graph.
'''