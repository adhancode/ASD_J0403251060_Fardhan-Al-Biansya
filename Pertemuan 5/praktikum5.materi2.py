#=============================================
#Nama: Fardhan Al Biansya
#NIM: J0403251060
#Kelas: B1
#=============================================

#=============================================
#Materi Rekursif: Call Stack
#Tracing  bilangan (masuk-keluar)
#Input 3
#Masuk 3-2-1
#Keluar 1-2-3
#=============================================

def hitung(n):

    #Base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk", n)
    hitung(n-1) #Rekursif Case
    print("Keluar", n)

print("===Program Tracing===")
hitung(5)