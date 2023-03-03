import os
import random
# mengimportkan library os dan random

os.system ("cls")
# fungsi untuk membersihkan layar pada program

print("|===================================================================|")
print("|                       NAMA  : JOVIANA YOUNG                       |")
print("|                       NIM   : 2209116012                          |")
print("|                       Kelas : SISTEM INFORMASI A                  |")
print("|                           -POSTTEST 1 ASD-                        |")
print("|===================================================================|")
print()
# biodata diri


#MERGE SORT
young = []
# young adalah variabel untuk list kosong.

for v in range(10):
# untuk v direntang 10.

    c = random.randint(28, 99)
    # fungsi yang akan menghasilkan angka random dari 28 hingga 99.

    young.append(c)
    # menambahkan 10 elemen angka random kedalam variabel young yang berisi list kosong.

def merge_sort(young):
    """
    Fungsi ini akan menerima sebuah list dan mengembalikan list tersebut dalam
    keadaan terurut menggunakan Merge Sort.
    
    Argumen:
        young: list yang akan diurutkan.
    
    pengembalian:
        list dalam keadaan terurut.
    """
    if len(young) <= 1:
    # jika list memiliki satu elemen atau kurang, list tersebut akan dikembalikan.

        return young
        # mengembalikan list dalam keadaan terurut.
    
    # Tentukan indeks tengah list dan pisahkan list menjadi dua bagian yaitu kiri dan kanan.
    tngh = len(young) // 2
    taoq = young[:tngh]     
    ulay = young[tngh:]

    # Pengurutan list bagian kiri dan kanan secara rekursif
    taoq = merge_sort(taoq)
    ulay = merge_sort(ulay)

    # Menggabungkan list bagian kiri dan kanan yang sudah terurut menggunakan fungsi merge.
    return merge(taoq, ulay)

def merge(taoq, ulay):
    """
    Fungsi ini menerima dua list bagian kiri dan kanan yang sudah terurut dan mengembalikan
    gabungan kedua list tersebut dalam keadaan terurut.
    
    Argumen:
        taoq: Sebuah list bagian kiri yang sudah terurut.
        ulay: Sebuah list bagian kanan yang sudah terurut.
    
    pengembalian:
        list dalam keadaan terurut yang merupakan gabungan dari kiri dan kanan list.
    """
    gabungan = [] # Merupakan inisial list kosong untuk menyimpan hasil penggabungan.
    n = 0  # n adalah Indeks untuk list kiri.
    g = 0   # g adalah Indeks untuk list kanan.

    # Selama kedua list memiliki elemen yang belum digabungkan
    while n < len(taoq) and g < len(ulay):
        # ketika elemen pertama kiri lebih kecil dari pada elemen pertama kanan
        if taoq[n] < ulay[g]: # jika elemen list kiri kurang dari list kanan
            gabungan.append(taoq[n]) # Tambahkan elemen pertama left ke hasil penggabungan
            n += 1 # Pindahkan indeks n ke elemen berikutnya di left
        else:
            gabungan.append(ulay[g]) # Tambahkan elemen pertama kanan ke hasil penggabungan
            g += 1 # Pindahkan indeks g ke elemen berikutnya di kanan

    # Jika masih terdapat elemen yang tersisa di kiri, tambahkan semua elemen tersebut ke hasil penggabungan
    gabungan += taoq[n:] 
    # Jika masih ada elemen yang tersisa di kanan, tambahkan semua elemen tersebut ke hasil penggabungan
    gabungan += ulay[g:]
    return gabungan
    # mengembalikan elemen list dalam keadaan terurut.

print("  >>> MERGE SORT <<<  ")
print("----------------------")
print("=====================================================================")
print(f"| Angka Sebelum Diurutkan= {young} |")
print("=====================================================================")
hsl = merge_sort(young) # variabel untuk list yang telah di sorting.
print("=====================================================================")
print(f"| Angka Sesudah Diurutkan= {hsl} |")
print("=====================================================================")

print()


#SHELL SHORT
ana = []
# ana adalah variabel untuk list kosong.

for n in range(10):
# untuk v direntang 10.

    ana.append(random.randint(22, 56))
    """
    fungsi yang akan menghasilkan angka random dari 22 hingga 56 dan akan
    menambahkan 10 elemen angka random kedalam
    variabel ana yang berisi list kosong.

    """
def shellSort(list_array):
    """
    Fungsi ini mengurutkan list dengan cara membandingkan suatu data dengan
    data lain yang memiliki jarak tertentu, kemudian dilakukan penukaran bila diperlukan.
    
    Argumen:
        list_array: parameter list yang akan diurutkan.
    
    """
    y = len(list_array)
    # variabel untuk panjang list
    u = y // 2
    # panjang list dibagi dua sehingga 10//5 = 2
    while u > 0:
    # keika u=5 lebih dari 0
        for i in range(u, y):
        # untuk i di range u, y
            x = list_array[i]
            # variabel untuk list yang ada di i

            z = i
            # variabel z sama dengan i, yang ada di z maka ada di i
            while z >= u and list_array[z - u] > x:
            # ketika z(penomoron angkanya ada 10) >= hasil baginya ada 5 dan parameter list z - u >= x adalah angka dalam list
        
                list_array[z] = list_array[z - u]
                # parameter list z adalah penomoran angka yaitu 10 = hasil bagi list yaitu 5, maka z - u (10-5)
                z -= u #10 - 5 = 5
            list_array[z] = x
            # indeks z = x yaitu 5
        u //= 2
        # u nya adalah 5 dibagi 2 hasilnya 2,5 tetapi dibulatkan menjadi 3
    return list_array
    # mengembalikan list yang telah di sorting

print("  >>> SHELL SORT <<<  ")
print("----------------------")
print("=====================================================================")
print(f"| Angka Sebelum Diurutkan= {ana} |")
print("=====================================================================")
o = shellSort(ana) ##variabel untuk list yang telah di sorting.
print("=====================================================================")
print(f"| Angka Sesudah Diurutkan= {o} |")
print("=====================================================================")


"""
Note:
    penjelasan tiap baris program tertera pada comment.
"""