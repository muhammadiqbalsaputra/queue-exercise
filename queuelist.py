# ---MEMANGGIL FUNGSI DENGAN MENGGUNAKAN VAIABEL LOKAL---
# deklarasi queue
queue = []

# fungsi untuk menambahan queue
def enqueue():
    data = 'saiful'
    data2 = 'bagus'
    data3 = 'jarot'
    data4 = 'cikal'
    queue.append(data)
    queue.append(data2)
    queue.append(data3)
    queue.append(data4)

# memanggil fungsi. *apabila tidak dipanggil hasil tidak akan memproses apa-apa
enqueue()

# output
print(queue)
print('\n')

# ---MEMANGGIL FUNGSI DENGAN PARAMETER---
# deklarasi queueParameter
queueParameter = []

# fungsi untuk menambahkan queue dengan menggunakan parameter
def enqueueParam(item):
    queueParameter.append(item)

# memanggil fungsi. dengan menambahkan nilai enqueueParam(nilai), misal: enqueueParam('fajri')
enqueueParam('Joko')
print(queueParameter)

# ---MENGHAPUS DATA---
# fungsi menghapus data
def dequeue():
    if len(queue) == 0:
        return 'Data Kosong'
    else:
        queue.pop(0)

# memanggil fungsi dequeue
dequeue()

# output
print('===Hasil dequeue===')
print(queue) # hasil akan menghilangkan saiful karena saiful pada variabel queue merupakan data yang pertama kali masuk 

# ---MEMANGGIL DATA TERDEPAN ATAU DATA FRONT---
# fungsi mengakses data terdepan atau data front
def front():
    if len(queue) < 1:
        print('Queue Kosong')
    else:
        return queue[0]
    
    # deskripsi apabila jumlah data dari queue kurang dari 1 atau 0 maka akan menghasilkan 'queue kosong' dan jika tidak menampilkan data front.

# output
print(f'Data Front : {front()}')

# ---MENAMPILKAN DATA TERAKHIR---
# Fungsi Data Tail
def tail():
    if len(queue) < 1:
        return 'Queue Kosong'
    else:
        return queue[-1]

# output
print(f'Data Tail : {tail()}')

# ---MEMANGGIL DATA DARI STACK KOSONG ATAU TIDAK---
# fungsi Memanggil IsEmpty
def isEmpty():
    if len(queue) == 0:
        return 'Queue Kosong'
    else:
        return 'Queue Tidak Kosong'

# output
print(f'Apa Queue Kosong? : {isEmpty()}') # output seharusnya menampilkan tidak kosong karena terdapat data yang menempel pada variabel queue antara lain ['bagus', 'jarot', 'cikal']

