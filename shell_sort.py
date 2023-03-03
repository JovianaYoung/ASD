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