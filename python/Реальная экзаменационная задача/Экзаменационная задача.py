def rezult(str_: str):
    a = ['+', '*', '/', '-']
    b = {0: lambda x, y: x + y, 1: lambda x, y: x * y, 2: lambda x, y: x / y, 3: lambda x, y: x - y}
    for i in range(len(str_)):
        if str_[i] in a:
            k = i - 1
            j = i + 1
            num1 = ''
            num2 = ''
            while str_[j] == ' ' or str_[j].isdigit():
                num2 += str_[j]
                j += 1
            while str_[k] == ' ' or str_[k].isdigit():
                num1 += str_[k]
                k -= 1
            num1 = num1[::-1]
            num1 = num1.strip()
            num2 = num2.strip()
            if num1 and num2:
                int_n1 = int(num1)
                int_n2 = int(num2)
            ind = a.index(str_[i])
            c = b[ind](int_n1, int_n2)
            return c


def check(str_: str):
    a = ['+', '*', '/', '-']
    print('переданная в check строка:', str_)
    for i in range(len(str_)):
        if str_[i] in a:
            print('нашло символ арифметического выражения')
            k = i - 1
            j = i + 1
            num1 = ''
            num2 = ''
            while str_[j] == ' ' or str_[j].isdigit():
                num2 += str_[j]
                j += 1
            while str_[k] == ' ' or str_[k].isdigit():
                num1 += str_[k]
                k -= 1
            num1 = num1[::-1]
            print('первое число:', num1)
            print('второе число:', num2)
            num1 = num1.strip()
            num2 = num2.strip()
            if num1 and num2:
                return True
            return False


def main():
    fin = open('in.txt')
    fout = open('out.txt', 'w')
    string = fin.readline()
    print('первая считанная строка:', string)
    next_str = fin.readline()
    print('следующая строка:', next_str)
    while string != '':
        if check(next_str):
            print('прошло проверку check')
            count = rezult(next_str)
            print('результат выражения', count)
            if count > 0:
                count = int(count)
                for i in range(count):
                    if '\n' not in string:
                        string += '\n'
                    fout.write(string)
        else:
            fout.write(string)
        string = next_str
        print('переприсвоенная следующая строка:', string)
        next_str = fin.readline()
        print('следующая считанная строка:', next_str)
    fin.close()
    fout.close()


main()
