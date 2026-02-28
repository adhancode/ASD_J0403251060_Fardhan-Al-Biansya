# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# Materi Rekursif: Menjumlahkan Elemen List
# =============================================

def jumlah_list(data, index=0):
    # Base case
    if index == len(data):
        return 0

    # Recursive case
    return data[index] + jumlah_list(data, index+1)

print("===Program Jumlah Data List===")
print(jumlah_list([2, 4, 5]))