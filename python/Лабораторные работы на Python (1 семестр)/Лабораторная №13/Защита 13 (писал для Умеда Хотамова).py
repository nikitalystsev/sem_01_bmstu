import struct

f = open('numbers.bin', 'wb+')
n = int(input('Введите количество чисел: '))

for i in range(n):
    number = int(input('Введите целое число: '))
    pack_object = struct.pack('i', number)
    f.write(pack_object)
print()
f.close()

f = open('numbers.bin', 'rb+')
print('что в файле до удаления:')
for i in range(n):
    f.seek(i * 4)
    now_number = f.read(4)
    now_number = struct.unpack('i', now_number)
    now_number = now_number[0]
    print('Число в файле:', now_number)
f.close()
print()

f = open('numbers.bin', 'rb+')
i = 0
while True:
    f.seek(i * 4)
    now_number = f.read(4)
    if not now_number:
        break
    now_number = struct.unpack('i', now_number)
    now_number = now_number[0]
    if now_number % 2 != 0:
        for j in range(i, n):
            f.seek((j + 1) * 4)
            next_number = f.read(4)
            f.seek(j * 4)
            f.write(next_number)
        n -= 1
        f.truncate()
    else:
        i += 1

f = open('numbers.bin', 'rb+')
print('что в файле после удаления:')
i = 0
while True:

    f.seek(i * 4)
    now_number = f.read(4)
    if not now_number:
        break
    now_number = struct.unpack('i', now_number)
    now_number = now_number[0]
    print('Число в файле:', now_number)
    i += 1
f.close()
