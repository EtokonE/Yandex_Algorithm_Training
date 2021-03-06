#➡️ Python:

#Считать строку (до перевода строки):
s = input()

#Считать число из строки (если в ней всего одно число):
x = int(input())

#Считать несколько чисел из одной строки:
x, y = map(int, input().split())

#Считать список чисел из одной строки:
lst = list(map(int, input().split()))

#Нарезать строку на слова:
words = input().split()

#Удалить пробелы в начале и конце строки:
s = s.strip()

#Чтение неизвестного количества строк лучше делать из файла (в тестирующей системе обычно файл называется input.txt).

#Например, в первой строке записано какое-то число, а в следующих строках какой-то текст неизвестной длины. Тогда чтение лучше сделать так:
with fin as open('input.txt', 'r'):
    x = fin.readline() # число из первой строки
    lines = fin.readlines() # все остальные строки