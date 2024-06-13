import modul_exercise_11 as modul
while True:
    modul.tampilan()
    masukanInput = input("MAsukan Pilihan : ")

    if masukanInput == '1':
        masukanNama = input('Masukan Nama Pelanggan : ')
        modul.tambah(masukanNama)

    elif masukanInput == '2':
        modul.antrianSelanjutnya()

    elif masukanInput == '3':
        modul.lihat()

    elif masukanInput == '4':
        print('Terimakasih Telah Mengantri')
        quit()

    else:
        print('Pilihan TIdak Ada')