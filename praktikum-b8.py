#pwd_benar = 'si23b'
#a = True
#i = 0
#limit = 3
#while a:
#    i += 1
#    pwd = input('Masukkan Password: ')
#    if pwd == pwd_benar:
#        print('Selamat Anda Login!')
#        a = False
#    else:
#       if i == limit:
#           a = False
#            print('Anda Kehabisan Kesempatan')
#       else:
#            print('Password Salah, Coba lagi!')

###############################################

pwd_benar = 'si23b'
a = True
i = 0
limit = 3
while a:
    i += 1
    pwd = input('Masukkan Password: ')
    if pwd == pwd_benar:
        print('Selamat Anda Login!')
        a = False
    else:
        print('Password Salah!')
        if i == limit:
            a = False
            print('Anda Kehabisan Kesempatan')
        else:
            print(f'Kesempatan anda tersisa {limit-i} kali')

#Komputer memilih angka [ ...5]
#user tebak angka:
#jika salah 1: Tebakan salah, anda memiliki 2 kesempatan lagi
#jika salah 2: Tebakan salah, anda memiliki 1 kesempatan lagi
#jika salah 3: Tebakan salah, belum berhasil
#              Angka yang dicari adalah x
#jika Benar: Anda Benar, angka yang ditebak adalah x (program selesai)

            

