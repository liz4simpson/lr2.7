#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# подсчитайте количество гласных в строке
# введенной с клавиатуры с использованием множеств


if __name__ == "__main__":
    slovar = {'a', 'e', 'i', 'o', 'u', 'y', 'а', 'о', 'у', 'е', 'и', 'я', 'э', 'ы', 'ё', 'ю'}
    word = input('Введите строку: ')

    if word == '':
        print('Вы ничего не ввели')

    else:
        count = 0
        for i in word:
            kost = set(i.lower())
            if len(kost.intersection(slovar)) == 0:
                continue

            elif len(kost.intersection(slovar)) != 0:
                count += 1

    if count == 0:
        print('Гласные не найдены')

    else:
        print(f'Кол-во глассных: {count}')