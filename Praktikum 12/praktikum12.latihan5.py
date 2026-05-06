# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================

# ==========================================================
# Latihan 5: Studi Kasus Shortest Path
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Membuat weighted graph untuk hubungan antar kota
# Bobot menyatakan jarak atau biaya perjalanan
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

def dijkstra(graph, start):
    # Menyimpan jarak minimum dari node awal ke semua node
    # Semua jarak diisi tak hingga terlebih dahulu
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue dipakai untuk memilih node dengan jarak paling kecil
    priority_queue = [(0, start)]

    # Proses berjalan selama masih ada node yang belum diproses
    while priority_queue:
        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak sekarang lebih besar dari jarak yang sudah tercatat,
        # maka node ini tidak perlu diproses lagi
        if current_distance > distances[current_node]:
            continue

        # Mengecek semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Menghitung jarak baru melalui node saat ini
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, maka jarak diperbarui
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    # Mengembalikan hasil jarak terpendek
    return distances

# Menentukan node awal
hasil = dijkstra(graph, 'Bogor')

# Menampilkan hasil jarak terpendek dari Bogor
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"Bogor -> {kota} = {jarak}")
    

'''
Pertanyaan Analisis:
1. Node awal yang digunakan apa?
2. Node mana yang memiliki jarak paling kecil dari node awal?
3. Node mana yang memiliki jarak paling besar dari node awal?
4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.

Jawaban:
1. Node awal yang digunakan adalah Bogor.
2. Node yang memiliki jarak paling kecil dari node awal adalah Depok, dengan jarak 2.
3. Node yang memiliki jarak paling besar dari node awal adalah Bandung, dengan jarak 8.
4. Algoritma Dijkstra bekerja dengan memilih node yang jaraknya paling kecil terlebih dahulu,
   lalu memperbarui jarak ke node tetangga. Proses ini dilakukan sampai semua node diperiksa.
   Pada kasus ini, jalur ke Jakarta lebih kecil melalui Depok, yaitu Bogor -> Depok -> Jakarta
   dengan total jarak 4.
'''