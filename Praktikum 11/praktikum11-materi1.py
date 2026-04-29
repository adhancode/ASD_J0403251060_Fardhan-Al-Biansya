# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B P1
# =============================================

# =============================================
# Materi 1: Implementasi Dasar Graph
# =============================================

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}

for node in graph:    
    print(node, "->", graph[node])

'''
Penjelasan:
Graph di atas merepresentasikan sebuah struktur data graph dengan 4 node (A, B, C, D) 
dan hubungan antar node yang ditunjukkan dalam bentuk list.
'''