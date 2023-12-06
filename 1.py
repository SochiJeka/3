with open('F1.txt', 'w') as f1:
    while True:
        line = input("Введите строку (пустая строка для окончания ввода): ")
        if line == "":
            break
        f1.write(line + '\n')

with open('F1.txt', 'r') as f1, open('F2.txt', 'w') as f2:
    lines = f1.readlines()
    odd_lines = [line for i, line in enumerate(lines) if i % 2 != 0]
    f2.writelines(odd_lines)

import os
f1_size = os.path.getsize('F1.txt')
f2_size = os.path.getsize('F2.txt')

print(f"Размер файла F1: {f1_size} байт")
print(f"Размер файла F2: {  f2_size} байт")