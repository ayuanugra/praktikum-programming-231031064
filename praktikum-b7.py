a = True

while a:
    jawab = input('Apakah ingin lanjutkan?(y/n)')
    if jawab == 'y':
        print('Selamat Datang Lagi!')
    elif jawab == 'n':
        print('Sampai Ketemu Lagi :D')
    else:
        print('Jangan aneh-aneh deh :(')
        a = True
