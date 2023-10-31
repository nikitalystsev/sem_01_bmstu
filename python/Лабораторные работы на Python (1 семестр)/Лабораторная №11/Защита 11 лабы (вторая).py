fragment = [
    'афафф а',
    'аааааааа'
]


def test(text):
    a = ';:,.'
    b = 'АаОоУуЭэЫыЯяЕеЁёЮюИи'
    c = 'БбВвГгДдЖжЗзЙйКкЛлМмНнПпРрСсТтФфХхЦцЧчШшЩщ'

    text_str = ' '.join(text)

    text_split = text_str.split()

    for i in range(len(text_split)):
        if text_split[i][-1] in a:
            text_split[i] = text_split[i][:len(text_split[i]) - 1]

    count_elem = []
    for j in range(len(text_split)):
        count = 1
        for k in range(len(text_split[j]) - 1):
            if text_split[j][k] in b and text_split[j][k + 1] in c:
                count += 1
            elif text_split[j][k] in c and text_split[j][k + 1] in b:
                count += 1
        if count == len(text_split[j]):
            if len(text_split[j]) == 1 and (text_split[j] in b or text_split[j] in c):
                count_elem.append(text_split[j])
            elif len(text_split[j]) != 1:
                count_elem.append(text_split[j])
    max_len = float('-inf')
    find_word = ''
    if count_elem:
        for i in range(len(count_elem)):
            if len(count_elem[i]) > max_len:
                max_len = len(count_elem[i])
                find_word = count_elem[i]
        print(find_word)
    else:
        print('Слов с чередующимися гласными и согласными буквами нет.')


test(fragment)
