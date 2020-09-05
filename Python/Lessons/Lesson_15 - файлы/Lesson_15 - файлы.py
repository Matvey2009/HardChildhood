# Урок № 15 по Python - файлы

## r (Read) чтение, w (Write) запись(создание), a (Append) дозапись, b (Binary) бинарник + w / r
file = open("Test.txt", "w")
file.write("hello world")
file.close()

with open("Test.txt", "w") as myFile:
    myFile.write("Hello World!")

with open("Test.txt", "a") as myFile:
    myFile.write("\nGood bye, World")
    print("\nЗапись через print", file = myFile)

## readline() - чтение строки (по-умолчанию), read() - все строки в одну, readlines() - все строки в список строк
print(" -= чтение файла readline (по умолчанию) в цикле =-")
with open("Test.txt", "r") as myFile:
    for i in myFile:
        print(i, end="")
print()

print(" -= чтение файла readline построчно =-")
with open("Test.txt", "r") as myFile:
    str1 = myFile.readline()
    print(str1, end="")
    str2 = myFile.readline()
    print(str2)
print()

print(" -= чтение файла циклом readline в цикле =-")
with open("Test.txt", "r") as myFile:
    line = myFile.readline()
    while line:
        print(line, end="")
        line = myFile.readline()
print()

print(" -= чтение файла целиком read =-")
with open("Test.txt", "r") as myFile:
    ctx = myFile.read()
    print(ctx)
print()

print(" -= чтение файла в список readlines =-")
with open("Test.txt", "r") as myFile:
    ctx = myFile.readlines()
    str1 = ctx[0]
    str2 = ctx[1]
    print(str1, end="")
    print(str2)
print()

# print(" -= если кодировка не ASCII, то заменяем к примеру на UTF8 =-")
# FileName = "Test.txt"
# with open(FileName, encoding="utf8") as myFile:
#     text = myFile.read()
#     print(text)

import os

## создаем папку по относительному пути (в этом же месте), абсолютный путь ("c://Folder1/Folder2/NewFolder")
os.mkdir("NewFolder")

input()
## удаление папки
os.rmdir("NewFolder")

## переименование файла
os.rename("Test.txt", "Test-2.txt")

input()
## и обратно
os.rename("Test-2.txt", "Test.txt")

## текущая рабочая директория
print(os.getcwd())
print()

## список файлов и директорий в папке
print(os.listdir(path="."))
print()

## удаляем файл
os.remove("Test.txt")

input()