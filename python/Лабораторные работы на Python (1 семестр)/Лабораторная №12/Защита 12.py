f = open('ученики.txt', 'r+', encoding='utf-8')
count_string = 0
while True:
    string = f.readline()
    if not string:
        break
    count_string += 1
f.close()
print('количиство строк в файле:', count_string)


f_2 = open('reverse_ученики.txt', 'w', encoding='utf-8')

for i in range(count_string):
    f = open('ученики.txt', 'r+', encoding='utf-8')
    for j in range(count_string - i):
        string = f.readline()
        if not string:
            break
    if '\n' not in string:
        string += '\n'
    f_2.write(string)
    f.close()
    
f_2.close()
