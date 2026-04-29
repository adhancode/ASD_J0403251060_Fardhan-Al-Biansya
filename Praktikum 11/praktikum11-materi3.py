# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Materi 3: Implementasi DFS
# =============================================

#struktur data untuk membuat antrian, kita gunakan dari library collections bawaan Phyton
from collections import deque

#representasi graph
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

def dfs(graph, node, visited):
#fungsi untuk melakukan penelusuran graph menggunakan DFS
#graph : dictionary yang menyimpan graph
#node : menyimpan node yang sedang dikunjungi
#visited : menyimpan node yang sudah dikunjungi

    #tandai node saat ini sebagai node yang sudah dikunjungi
    visited.add(node)

    #tampilkan node yang sedang dikunjungi
    print(node, end=" ")

    #periksa semua tetangga dari node saat ini
    for neighbor in graph[node]:

        #jika tetangga belum pernah dikunjungi
        if neighbor not in visited:
            #Lakukan dfs secara rekursif ke tetangga tersebut
            dfs(graph, neighbor, visited)

#set visited
visited = set()

#Menjalankan dfs dari A
dfs(graph, "A", visited)

'''
Penjelasan:
Kode ini menerapkan metode Depth First Search (DFS) untuk menelusuri graf dengan cara masuk 
sedalam mungkin ke satu cabang sebelum kembali mengecek cabang lainnya. Secara teknis, fungsi 
ini bekerja secara rekursif, di mana setiap kali titik baru ditemukan, program akan langsung 
melompat ke titik tetangganya yang belum dikunjungi dan menandainya dalam variabel visited
agar tidak terjadi pengulangan. Penggunaan himpunan set untuk mencatat riwayat kunjungan 
memastikan proses berjalan efektif, sehingga hasil akhirnya menampilkan urutan titik yang ditelusuri 
berdasarkan prioritas kedalaman jalur, bukan berdasarkan lebar antrean seperti pada metode BFS.
'''