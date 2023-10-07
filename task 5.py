# -*- coding: utf-8 -*-
"""
Задана строка S и символ С. За один ход можно поменять местами два соседних
символа. Сколько потребуется ходов чтобы переместить все символы С в строке
в начало строки, не меняя при этом порядок следования между остальными
символами?

Например, имеется строка abcabcabc, и задан символ b. После перемещения всех
символов b в начало строки, получится строка bbbacacac, на это уйдёт 9 ходов,
ниже указаны строки получившиеся после кажого хода.

1. bacabcabc
2. bacbacabc
3. babcacabe
4. bbacacabc
5. bbacacbac
6. bbacabcac 
7. bbacbacac
8. bbabcacac 
9. bbbacacac

Входные данные

Задана строка 5, состоящая из прописных букв латинского алфавита, и символ С
через пробел.
Длина строки не превышает 100 символов.
Гарантируется, что символ С встречается в строке 5.

Выходные данные

Выведите единственное числе количество ходов, которое потребуется, чтобы
переместить все символы "C" в начало строки.

Примеры

входные данные

аbrahcabe b

выходные данные
9

@author: workk
"""


def solve(text: str, target: str) -> int:
    steps = 0
    offset = 0

    for i in range(len(text)):
        if text[i] != target:
            continue

        if i != offset:
            text = text[:offset] + target + text[offset:i] + text[i + 1 :]
            steps += i - offset

        offset += 1

    return steps


def main():
    text, target = input().split()
    print(solve(text, target))


if __name__ == "__main__":
    main()
