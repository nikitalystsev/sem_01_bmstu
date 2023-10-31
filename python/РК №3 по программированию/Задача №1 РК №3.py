file_1 = open('in1.txt', 'r')
file_2 = open('in2.txt', 'r')
file_3 = open('out.txt', 'w')

line_1 = file_1.readline()
line_2 = file_2.readline()

while line_1 != '' and line_2 != '':
    print(f"сейчас сравнивается {line_1} c {line_2}")
    if int(line_1) > int(line_2):
        file_3.write(line_2)
        line_2 = file_2.readline()
    elif int(line_1) == int(line_2):
        file_3.write(line_1)
        file_3.write(line_2)
        line_1 = file_1.readline()
        line_2 = file_2.readline()
    elif int(line_1) < int(line_2):
        file_3.write(line_1)
        line_1 = file_1.readline()

while True:
    file_3.write(line_1)
    line_1 = file_1.readline()
    print('Считанная строка из первого файла дополнительным циклом:', line_1)
    print('Её длина:', len(line_1))
    print()
    if not line_1:
        break

while True:
    file_3.write(line_2)
    line_2 = file_2.readline()
    print('Считанная строка из второго файла дополнительным циклом:', line_2)
    print('Её длина:', len(line_2))
    print()
    if not line_2:
        break

file_1.close()
file_2.close()
file_3.close()
