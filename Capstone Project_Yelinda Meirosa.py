print('==== TIARA BOOK STORE ====')

buku = []

def read():
    index=0
    if len(buku)<=0:
        print('Buku masih kosong')
    else: 
        for book in buku :
            print(str(index)+". "+book)
            index= index+1

def create():
    judul = input('Masukan Judul buku :')
    buku.append(judul)
    print('Buku telah ditambahkan')

def update():
    read()
    index=int(input('Masukan Index :'))
    judul_lama = buku[index]
    judul_baru = input('Masukan judul baru :')
    buku[index] = judul_baru
    print(judul_lama+ ' telah diganti menjadi '+judul_baru)


def delete():
    read()
    index=int(input('Masukan Index :'))
    judul = buku[index]
    del buku[index]
    print(judul +'telah dihapus' )

def main_menu():
    print('[1] Read Menu')
    print('[2] Create Menu')
    print('[3] Update Menu')
    print('[4] Delete Menu')

    menu = input('Pilih Menu : ')
    if menu == '1':
        read()
    elif menu == '2':
        create()
    elif menu == '3':
        update()
    elif menu == '4':
        delete()
    else :
        print('Menu Tidak Tersedia')

while(True):
    main_menu()

