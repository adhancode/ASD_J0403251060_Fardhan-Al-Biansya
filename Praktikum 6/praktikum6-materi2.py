# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# #Insertion Sort dengan Tracking
# =============================================

def insertion_sort(data):
    #Melihat data awal
    print("Data awal: ", data)
    print("="*50)

    #Loop mulai dari data ke 2 (index array ke 1)
    for i in range(1, len(data)):

        key = data[i] #Simpan nilai yang disisipkan
        j = i-1 #Index elemen terakhir di bagian kiri

    print("Iterasi ke-",i)
    print("Nilai key =",key)
    print("Bagian Kiri (Terurut):", data[:1])
    print("Bagian Kanan (Belum Terurut):", data[i:])

    #Geser
    while j>=0 and data[j] > key:
        data[j+1] = data[j]
        j -= 1

    #Sisipkan key ke posisi yang benar
    data[j+1] = key

    print("Setelah disisipkan:", data)
    print("-"*50)

    return data
angka = [7,8,5,2,4,6]
print("Hasil Sorting:", insertion_sort(angka))