print('---Tugas1---')

def tambah_waktu(waktu_awal, jam, menit):
    # Memecah waktu awal menjadi jam dan menit
    jam_awal, menit_awal = map(int, waktu_awal.split(':'))

    # Menambahkan jam dan menit ke waktu awal
    jam_akhir = jam_awal + jam
    menit_akhir = menit_awal + menit

    # Menangani penambahan yang melebihi 60 menit
    if menit_akhir >= 60:
        jam_akhir += 1
        menit_akhir -= 60

    # Menyusun kembali waktu akhir dalam format yang sesuai
    waktu_akhir = f'{jam_akhir:02d}:{menit_akhir:02d}'
    
    return waktu_akhir

# Input waktu awal
waktu_awal = input("Masukkan waktu awal : ")

# Input jam dan menit yang ingin ditambahkan
jam = int(input("Jam yang ingin ditambahkan: "))
menit = int(input("Menit yang ingin ditambahkan: "))

# Memanggil fungsi tambah_waktu
waktu_akhir = tambah_waktu(waktu_awal, jam, menit)

# Menampilkan waktu akhir
print("Waktu akhir:", waktu_akhir)

print()
print('---Tugas2---')
# Mengambil input waktu awal dalam format jam dan menit
waktu_awal = input("Masukkan waktu awal (HH:MM): ")

# Mengambil input selisih waktu dalam jam dan menit
selisih_jam = int(input("Masukkan selisih jam: "))
selisih_menit = int(input("Masukkan selisih menit: "))

# Memisahkan jam dan menit dari input waktu awal
jam_awal, menit_awal = map(int, waktu_awal.split(':'))

# Menghitung waktu sebelumnya
jam_hasil = jam_awal - selisih_jam
menit_hasil = menit_awal - selisih_menit

# Menangani pengurangan menit yang melebihi 60
if menit_hasil < 0:
    jam_hasil -= 1
    menit_hasil += 60

# Menangani jam yang kurang dari 0
if jam_hasil < 0:
    jam_hasil += 24

# Mengonversi hasil ke format HH:MM
hasil_waktu = f"{jam_hasil:02d}:{menit_hasil:02d}"

# Menampilkan hasil
print("Waktu awal:", waktu_awal)
print("Selisih waktu:", selisih_jam, "jam", selisih_menit, "menit sebelumnya")
print("Hasil:", hasil_waktu)
