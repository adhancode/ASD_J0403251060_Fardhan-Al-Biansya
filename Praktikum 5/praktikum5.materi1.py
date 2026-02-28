# =============================================
# Nama: Fardhan Al Biansya
# NIM: J0403251060
# Kelas: B1
# =============================================

# =============================================
# Materi Rekursif: Faktorial
# Recursive Case => 3! = 3 x 2 x 1
# Base Case => 0 berhenti
# =============================================

def faktorial(n):
    if n == 0:
        return 1

    # Recursive case
    return n*faktorial(n-1)  # n-1*n-2*n-3 .................. n-?


print("===Program Faktorial===")
print("Hasil Faktorial: ", faktorial(3))
