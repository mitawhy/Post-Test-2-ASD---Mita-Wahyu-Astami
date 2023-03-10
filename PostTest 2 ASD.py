import os
os.system("cls")

def fibonacci(arr, x):
    # Menginisialisasi angka fibonacci / pemberian nilai awal 
    n = len(arr)
    fib2 = 0 
    fib1 = 1
    fib = fib2 + fib1
  
    # Mencari nilai dari fibonacci yang terbesar, lebih kecil, atau sama dengan n
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib2 + fib1
  
    # Indeks awal untuk pencarian
    offset = -1
  
    # Melakukan pencarian
    while fib > 1:
        i = min(offset+fib2, n-1)
  
        # Jika x lebih besar daripada nilai elemen pada indeks i, lakukan pencarian pada subarray sebelah kanan
        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            offset = i
  
        # Jika x lebih kecil daripada nilai elemen pada indeks i, lakukan pencarian pada subarray sebelah kiri
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
  
        # Jika x ditemukan, kembalikan indeks i
        else:
            return i
  
    # Membandingkan elemen terakhir dengan x
    if fib1 and arr[offset+1] == x:
        return offset+1
  
    # Jika elemen tidak ditemukan, maka kembalikan -1
    return -1

def hasil():
    a = fibonacci(data, "Arsel")
    b = fibonacci(data, "Avivah")
    c = fibonacci(data, "Daiva")
    # Menampilkan hasil
    print(f"Arsel di Index {a}, Avivah di Index {b}, Daiva di Index {c}")

    for i in range(len(data)):
        if type(data[i]) == list:
            isi = fibonacci(data[i], "Wahyu")
            isi2 = fibonacci(data[i], "Wibi")
            print("Wahyu di Index",i,"pada kolom",isi)
            print("Wibi di Index",i,"pada kolom",isi2)

data = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]
hasil()