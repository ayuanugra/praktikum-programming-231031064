import os
os.system('clear')

nim = [2,3,1,0,3,1,0,6,4]
print(nim)

# akses item
print('---akses item---')
print('item indeks 0:',nim[0])
print('item indeks 3:',nim[3])
print('item indeks terakhir:',nim[len(nim)-1])
print()

# akses indeks negatif
print('---akses indeks negatif---')
print('item indeks terakhir:',nim[-1])
print('item indeks pertama:',nim[-len(nim)])
print('item indeks 3: [-6] ',nim[-6])
print('item indeks 5: [-4] ',nim[-4])
print('item indeks -7: [2] ',nim[2])
print('item indeks 2: [-7] ',nim[-7])
print()

# akses indeks batas
print('---akses indeks negatif---')
print(f'item indeks 1,2,....: {nim[1:]}')
print(f'item indeks 3,4,....: {nim[3:]}')
print(f'item indeks 0,1,2,3: {nim[:4]}')
print(f'item indeks 0: {nim[:1]}')
print(f'item indeks semua: {nim[:]}')
print(f'item indeks [:8]: {nim[:-1]}')
print(f'item indeks [:4]: {nim[:-5]}')
print()

# pengirisan
print('---pengirisan---')
print(f'item indeks 1,2: {nim[1:3]}')
print(f'item indeks []: {nim[3:3]}')
print(f'item indeks 2,3,4: {nim[2:5]}')
print(f'item indeks [1:8]: {nim[1:-1]}')
print(f'item indeks [2:7]: {nim[2:-2]}')
print()

# Nested List
print('---Nested List---')
kelas = [('PTI',2),
         ('Prog',3)]
kelas.append(('Sains',2))
kelas.append(('Cinta',2))
kelas.append(('Kalkulus',2))

# tambahkan matkul 4 dan 5 dan sksnya

# Mata kuliah 1: Matkul1 dengan 2 sks
print(f'Mata Kuliah 1: {kelas[0][0]} dengan {kelas[0][1]} sks')
# Mata kuliah 2: Matkul2 dengan 3 sks
print(f'Mata Kuliah 2: {kelas[1][0]} dengan {kelas[1][1]} sks')
# Mata kuliah 3: Matkul3 dengan 2 sks
print(f'Mata Kuliah 3: {kelas[2][0]} dengan {kelas[2][1]} sks')
# Mata kuliah 4: Matkul4 dengan 2 sks
print(f'Mata Kuliah 4: {kelas[3][0]} dengan {kelas[3][1]} sks')
# Mata kuliah 5: Matkul5 dengan 2 sks
print(f'Mata Kuliah 5: {kelas[4][0]} dengan {kelas[4][1]} sks')

data = [('Ayu',2023,'Aktif'),
        (76,98,89,97,99),
        [2,3,2,2,2],
        ('S1-Reguler','Sistem Informasi B','Ganjil')]
print()
print('Nama mahasiswa:',data[0][0])
print('Inisial',data[0][0],':',data[0][0][0])
print('NIM Ayu:',str(nim).replace('[','').replace(']','').replace(',','').replace(' ',''))
print('Program',data[0][0],':',data[3][0],data[3][1])
print(f'Angkatan {data[0][0]} : {data[3][2]}-{data[0][1]}')
print(f'Total sks {data[0][0]} adalah: {sum(data[2])}')
print(f'Jumlah Nilai {data[0][0]}: {len(data[2])}')
print(f'Nilai tertinggi {data[0][0]}: {max(data[1])}')
print(f'Nilai terendah {data[0][0]}: {min(data[1])}')
x_bar = sum(data[1]) / len(data[1])
print(f'Rata-rata nilai {data[0][0]}: {x_bar}')


# Nama mahasiswa: Ayu
# Inisial Ayu: A
# NIM Ayu: 231031064
# Program Ayu: S1-Reguler Sistem Informasi B
# Angkatan Ayu: Ganjil-2023
# Total sks Ayu adalah: 11
# Jumlah Nilai Ayu: 5
# Nilai tertinggi Ayu: 99
# Nilai terendah Ayu: 76
# Rata-rata nilai Ayu: 91.8
