# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================

# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Membuat graph lokasi kampus
# Bobot pada graph menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    # Menyimpan jarak minimum dari node awal ke semua lokasi
    # Semua jarak diisi tak hingga terlebih dahulu
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue digunakan untuk memilih lokasi dengan jarak terkecil
    priority_queue = [(0, start)]

    # Proses berjalan selama masih ada data di priority queue
    while priority_queue:
        # Mengambil node dengan jarak paling kecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak sekarang lebih besar dari jarak yang sudah tercatat,
        # maka node ini tidak perlu diproses lagi
        if current_distance > distances[current_node]:
            continue

        # Memeriksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Menghitung jarak baru melalui node sekarang
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, maka jarak diperbarui
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Mengembalikan hasil jarak terpendek
    return distances

# Menjalankan algoritma dari Gerbang Kampus
hasil = dijkstra(graph, 'Gerbang')

# Menampilkan hasil jarak terpendek dari Gerbang
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")

'''
Pertanyaan Analisis:
1. Lokasi mana yang paling dekat dari Gerbang?
2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?

Jawaban:
1. Lokasi yang paling dekat dari Gerbang adalah Kantin, dengan jarak 2 menit.
2. Waktu tempuh terpendek dari Gerbang ke Aula adalah 7 menit. Jalurnya bisa melalui Gerbang -> Kantin -> Lab -> Aula.
3. Tidak selalu. Jalur langsung belum tentu paling kecil, karena bisa saja ada jalur lain yang melewati beberapa lokasi tetapi total waktunya lebih singkat.
4. Dijkstra cocok digunakan karena bobot pada graph berupa waktu tempuh positif, sehingga algoritma ini dapat mencari jalur terpendek dengan tepat.
'''