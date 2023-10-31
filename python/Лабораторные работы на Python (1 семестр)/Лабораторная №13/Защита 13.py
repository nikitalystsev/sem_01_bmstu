import struct

n = int(input('Введите количество чисел:'))
f = open('numbers.bin', 'rb+')
for i in range(n):
    number = int(input('Введите целое число:'))
    pack_object = struct.pack('i', number)
    f.write(pack_object)
    
print('что в файле до:')
for i in range(n):
    f.seek(i * 4)
    now_number = f.read(4)
    now_number = struct.unpack('i', now_number)
    now_number = now_number[0]
    print('Число в файле:', now_number)
print()

for i in range(n, n // 2, -1):
    f.seek((i - 1) * 4)
    number = f.read(4)
    
    f.seek((n - i) * 4)
    number_2 = f.read(4)

    f.seek((i - 1) * 4)
    f.write(number_2)

    f.seek((n - i) * 4)
    f.write(number)
    
print('что в файле после:')
for i in range(n):
    f.seek(i * 4)
    now_number = f.read(4)
    now_number = struct.unpack('i', now_number)
    now_number = now_number[0]
    print('Число в файле:', now_number)    
    
    
    
