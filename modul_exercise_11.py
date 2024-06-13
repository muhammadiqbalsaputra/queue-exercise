antrian = []

def tampilan():
    if len(antrian) == 0:
        print('Antrian Sekarang : Kosong')
    else:
        print(f'Antrian Sekarang : {antrian[0]}') 

    if len(antrian) < 2:
        print('Tidak Ada Pelanggan Selanjutnya')
    else:
        print(f'Antrian Selanjutnya : Pelanggan {antrian[1]}')

    print(f'Jumlah Antrian : {len(antrian)}')
    print('Pilihan')
    print('1. Tambah Antrian ')
    print('2. Antrian Selanjutnya')
    print('3. Lihat Antrian')
    print('4. Keluar')

def tambah(nama):
    print(f'{nama} Berhasil Ditambahkan Ke Antrian')
    print('='*30)
    antrian.append(nama)


def antrianSelanjutnya():
    if len(antrian) <= 1:
        antrian.pop(0)
        print('='*30)
        print('Antrian Kosong')
        print('='*30)
        print('\n')
    else:
        print('='*30)
        print(f'Pelanggan Selanjutnya {antrian[1]}')
        antrian.pop(0)
        print('='*30)
        print('\n')

def lihat():
    if len(antrian) == 0:
        print('='*30)
        print('Antrian Kosong')
        print('='*30)
        print('\n')
    else:
        print('---Daftar Antrian---')
        for angka,daftar in enumerate(antrian):
            print(f'{angka+1}, {daftar}')
        print('='*30)
        print('\n')

