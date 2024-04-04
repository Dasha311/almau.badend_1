from list import MyList
a1 = MyList()
a1.append(1)
a1.append(5)
a1.append(6)
a1.append(4)

a2 = MyList()
a2.append(8)
a2.append(9)
a2.append(3)

print(a1)  # Вывод: [1, 5, 6, 4]
print(a2)  # Вывод: [8, 9, 3]

print(a1.max())  # Вывод: 6
print(a2.min())  # Вывод: 3

a3 = a1 + a2
print(a3)  # Вывод: [9, 14, 9, 4]

a4 = a1 - a2
print(a4)  # Вывод: [-8, -7, -6, 4]

print(len(a1))  # Вывод: 4
print(len(a2))  # Вывод: 3

print(a1 < a2)  # Вывод: False