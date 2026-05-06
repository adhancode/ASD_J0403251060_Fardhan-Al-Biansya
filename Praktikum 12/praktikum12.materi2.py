# ==========================================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================

# ==========================================================
# Materi 2: Algoritma Bellman Ford
# ==========================================================

def bellman_ford(graph, start): 

    # Membuat dictionary untuk menyimpan jarak minimum dari node awal ke semua node
    # Semua node diinisialisasi dengan nilai tak hingga (∞)
    distances = {node: float('inf') for node in graph} 
    
    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0 

    # Proses relaksasi dilakukan sebanyak (jumlah node - 1)
    # Tujuannya agar semua kemungkinan jalur terpendek dapat diperbarui
    for _ in range(len(graph) - 1): 

        # Mengiterasi setiap node dalam graph
        for node in graph: 

            # Mengiterasi semua edge (node -> neighbor) beserta bobotnya
            for neighbor, weight in graph[node].items(): 

                # Mengecek apakah ditemukan jarak yang lebih kecil
                # (relaksasi edge: memperbarui jarak jika lebih optimal)
                if distances[node] + weight < distances[neighbor]: 

                    # Update jarak minimum ke neighbor
                    distances[neighbor] = distances[node] + weight 

    # Mengembalikan hasil jarak terpendek dari node awal ke semua node
    return distances