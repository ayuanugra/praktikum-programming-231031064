# Fungsi Rekursif Fibonacci
def fibonacci(n):
    if n < 0:
        print('Tidak ada bilangan yang bernilai negatif')
        return None
    elif n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Fungsi untuk mendapatkan input nilai
def inputan():
        nilai = int(input('Masukkan Sebuah Bilangan : '))
        return nilai

# Fungsi untuk menampilkan hasil
def tampilan(nilai, hasil):
    print('Fibonacci(%d)=%d' % (nilai, hasil))

# Program Utama
nilai = inputan()
hasil = fibonacci(nilai)
tampilan(nilai, hasil)
