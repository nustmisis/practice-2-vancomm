# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:05:53 2023
@author: workk

Упражнение 61. Действительный номерной знак машины? (Решено. 28 строк)

Допустим, в нашей стране старый формат номерных знаков автомобилей состоял
из трех заглавных букв, следом за которыми шли три цифры. После того как
все возможные номера были использованы, формат был изменен на четыре цифры,
предшествующие трем заглавным буквам. Напишите программу, запрашивающую
у пользователя номерной знак машины и оповещающую о том, для какого формата
подходит данная последовательность символов: для старого или нового. Если
введенная последовательность не соответствует ни одному из двух форматов,
укажите это в сообщении.
"""

import re


def main():
    old_pattern_re = re.compile(r"^[А-Я]{3}\d{3}$")
    new_pattern_re = re.compile(r"^\d{4}[А-Я]{3}$")

    plate = input("Введите номерной знак: ")

    if old_pattern_re.match(plate):
        plate_status = "соответствует старому формату"
    elif new_pattern_re.match(plate):
        plate_status = "соответствует новому формату"
    else:
        plate_status = "не соответствует ни одному из известных форматов"

    print(f"Номерной знак {plate} {plate_status}.")


if __name__ == "__main__":
    main()
