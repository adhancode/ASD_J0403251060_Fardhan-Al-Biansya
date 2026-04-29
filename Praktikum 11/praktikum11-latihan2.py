# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Latihan 2: Studi Kasus DFS (Eksplorasi Jalur)
# =============================================

#Definisi graph yang merepresentasikan jalur eksplorasi
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}

#Algoritma DFS menggunakan rekursi
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

#set visited untuk menyimpan node yang sudah pernah dikunjungi
visited = set()

print("DFS dari A:")

#Menjalankan dfs dari A
dfs(graph, 'A', visited)
print("\n") # Menambahkan baris baru agar output rapi

'''
Penjelasan:
Program ini menerapkan metode Depth First Search (DFS) untuk menjelajahi jalur dari satu 
titik ke titik terdalam secara berurutan. Cara kerjanya dimulai dari titik A, di mana 
program akan langsung bergerak masuk ke titik tetangga pertama yang ditemukan, yaitu B, 
lalu lanjut ke D sebelum mengecek cabang lainnya. Proses ini dilakukan menggunakan teknik 
rekursi, yang artinya fungsi akan memanggil dirinya sendiri untuk masuk ke setiap cabang 
hingga buntu, baru kemudian kembali ke atas untuk menyisir sisa jalur yang belum dilewati 
seperti E, C, dan F. Selama proses berjalan, variabel `visited` bertugas sebagai catatan 
agar tidak ada titik yang dikunjungi dua kali, sehingga urutan penelusuran yang muncul di 
layar mencerminkan jalur eksplorasi yang mendalam dan sistematis.
'''

'''
1. Mengapa DFS masuk ke node terdalam terlebih dahulu?
Jawab: Karena implementasi DFS di atas menggunakan rekursi yang mengandalkan Call Stack 
dengan prinsip LIFO (Last In First Out). Saat DFS mengecek tetangga pertama, ia langsung 
memanggil fungsi dfs() lagi untuk tetangga tersebut dan menunda proses pengecekan tetangga 
lainnya. Ini memaksa eksekusi terus turun sedalam mungkin ke satu cabang hingga mencapai 
jalan buntu (node tanpa tetangga baru). Setelah mentok, barulah ia mundur (backtrack) untuk 
mengeksplorasi sisa cabang.

2. Apa yang terjadi jika urutan neighbor diubah?
Jawab: Jalur atau urutan hasil penelusuran (traversal) akan berubah, namun keseluruhan node 
yang terhubung akan tetap berhasil dikunjungi. Sebagai contoh, jika urutan tetangga A diubah 
dari ['B', 'C'] menjadi ['C', 'B'], maka DFS akan mengeksplorasi cabang 'C' sampai habis 
terlebih dahulu sebelum pindah ke cabang 'B'. Outputnya akan berubah menjadi: A C F B D E.

3. Bandingkan hasil DFS dengan BFS pada graph yang sama.
Jawab:
- Hasil penelusuran DFS: A B D E C F
- Hasil penelusuran BFS: A B C D E F
Perbandingan: 
DFS menjelajah vertikal (ke kedalaman). Ia menelusuri cabang B beserta anak-anaknya (D, E) 
sampai tuntas, baru kemudian naik dan pindah ke cabang C beserta anaknya (F). Sedangkan BFS 
menjelajah horizontal (melebar). Ia akan mengunjungi node lapis demi lapis berdasarkan jarak 
terdekat dari titik awal. BFS akan mengunjungi A (level 1), kemudian B dan C (level 2), 
barulah D, E, dan F (level 3).
'''