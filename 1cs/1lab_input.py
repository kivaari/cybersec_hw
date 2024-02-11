def encode(KEY:str, WORDS:str) -> str:
    # находим кол-во столбцов
    n = len(KEY)

    # находим длинну сообщения
    m = len(WORDS)

    ms = 0

    # находим количество полных строк
    full_strings = m // n

    # находим кол-во слов в неполной строке
    words_in_nf_string = m % n

    # если есть неполная строка, то добавляем еще одну строку в таблицу
    if words_in_nf_string != 0:
        ms = 1

    # кол-во строк в таблице
    rows = full_strings + ms

    # создаем таблицу
    table = [[' ' for _ in range(n)] for _ in range(rows)]

    # если слов меньше чем елементов в таблице
    # то добавляем в пустые элементы знак & 
    if len(WORDS) != rows * n:
        for i in range(n - words_in_nf_string):
            WORDS += "&"

    # счетчик
    index = 0

    # заносим в таблицу слова
    for i in range(rows):
        for j in range(n):
            table[i][j] = WORDS[index]
            index += 1

    output_string = ""

    # добавляем в выводную строку элементы из таблицы в нужном порядке
    for i in range(n):
        k = KEY.find(str(i+1))
        for j in range(rows):
            output_string += table[j][k]

    return  output_string


def decode(KEY:str, encoded:str) -> str:
    # находим кол-во столбцов
    n = len(KEY)

    # находим длинну сообщения
    m = len(encoded)

    # кол-во строк в таблице
    rows = m // n

    # создаем таблицы
    table = [[' ' for _ in range(n)] for _ in range(rows)]
    table_2 = [['' for _ in range(n)] for _ in range(rows)]

    # Заполняем таблицу символами из закодированной строки в порядке столбцов
    index = 0
    for i in range(n):
        for j in range(rows):
            table[j][i] = encoded[index]
            index += 1

    # добавляем элементы из закодированной таблицы в новую таблицу на места, исходя из значений ключа
    for i in range(n):
        replace_column = KEY.find(str(i+1))  # Индекс столбца в который нужно добавить
        for j in range(rows):
            table_2[j][replace_column] += table[j][i]

    # Формируем закодированную строку
    output_string = ""
    for i in range(rows):
        for j in range(n):
            output_string += table_2[i][j]

    return output_string


def main():
    print("Введите предложение: ")
    WORDS = input()

    print("Введите ключ: ")
    KEY = input()

    encoded_string = encode(KEY, WORDS)
    print("Закодированная строка:", encoded_string.replace("&", ""))
    
    decoded_string = decode(KEY, encoded_string)
    print("Раскодированная строка:", decoded_string.replace("&", ""))


if __name__ == "__main__":
    main()
