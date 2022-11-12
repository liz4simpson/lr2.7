#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# определите общие символы в двух строках
# введенных с клавиатуры


if __name__ == "__main__":
    slovo1 = set(input('Введите первую строку: '))
    slovo2 = set(input('Введите вторую строку: '))

    if len(slovo1.intersection(slovo2)) == 0:
        print('Совпадений нет')

    else:
        print("Общие символы = ",
              slovo1.intersection(slovo2))