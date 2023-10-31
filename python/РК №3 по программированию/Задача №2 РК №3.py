import struct

f = open('numbers.bin', 'wb')
n = int(input('Введите количество чисел в последовательности: '))
for i in range(n):
    number = int(input(f'Введите {i + 1} число: '))
    pack_object = struct.pack('q', number)
    f.write(pack_object)
f.close()

with open('numbers.bin', 'rb+') as file:
    for i in range(1, n):
        for j in range(i, 0, -1):
            file.seek(j * 8)
            now_number = file.read(8)
            now_number = struct.unpack('q', now_number)
            now_number = now_number[0]

            file.seek((j - 1) * 8)
            previous_number = file.read(8)
            previous_number = struct.unpack('q', previous_number)
            previous_number = previous_number[0]
            if now_number < previous_number:

                file.seek((j - 1) * 8)
                pack_object_1 = struct.pack('q', now_number)
                file.write(pack_object_1)
                pack_object_2 = struct.pack('q', previous_number)
                file.write(pack_object_2)

            else:
                break
    print('То, что в файле по итогу работы сортировки:')

    for i in range(n):
        file.seek(i * 8)
        number = file.read(8)
        number = struct.unpack('q', number)
        number = number[0]
        print(number)









