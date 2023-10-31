fragment = [
    'hhh.',
    'bc abc.'


]


def split_text(text):
    text = ''.join(text)
    text_split_point = text.split('.')
    print('Текст, разбитый на предложения: ')
    for i in text_split_point:
        print(i)
    print()
    symbol = input('Введите букву: ')
    k1 = 0
    find_i = 0
    for i in range(len(text_split_point)):
        split_word = text_split_point[i].split()
        c = 0
        c1 = 0
        for j in range(len(split_word) - 1):
            if split_word[j][0] == symbol and split_word[j + 1][0] == symbol:
                c += 1
                c1 = max(c, c1)
            elif split_word[j][0] == symbol:
                c += 1
                c1 = max(c, c1)
            elif split_word[j + 1][0] == symbol:
                c = 0
                c += 1
                c1 = max((c, c1))
            else:
                c = 0

        if c1 > k1:
            k1 = c1
            find_i = i
    print(text_split_point[find_i])


split_text(fragment)
