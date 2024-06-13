from collections import deque

# Deklarasi Queue
antrian = deque()

# ===PENAMBAHAN DATA===
# Fungsi enqueue
def enqueue(item):
    antrian.appendleft(item)
    # fungsi appendleft sama seperti append namun data yang pertama masuk diubah menjadi data yang terakhir masuk

# pemanggilan fungsi
enqueue('iqbal')
enqueue('epan')
enqueue('supra')

# output
print(antrian)
print('\n')

# ===PENHAPUSAN DATA===
# Fungsi dequeue
def dequeue():
    antrian.popleft()
    # fungsi popleft sama seperti pop (menghapus) namun data yang pertama masuk diubah menjadi data yang terakhir masuk


# pemanggilan fungsi
dequeue()

# output
print(antrian)