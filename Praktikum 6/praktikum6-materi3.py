# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# #Insertion Sort dengan Tracking
# =============================================

def merge_sort(data):
    
    #Divide: Membagu data menjadi 2 bagian
    mid = len(data) //2
    left = data[:mid] #Slicing bagian kiri
    right = data[mid:]

