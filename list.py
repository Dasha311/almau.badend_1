class MyList:
    def __init__(self):
        self.elements = []  # Пустой атрибут листа 

    def append(self, n):
        self.elements.append(n)  # Добавления элемента в конец списка 

    def pop(self):
        self.elements.pop()  # Удаления элемента в конец списка 

    def max(self):
        return max(self.elements)  # Максимальной число 

    def min(self):
        return min(self.elements)  # Мин число

    def __str__(self):
        return str(self.elements)  # Вызывает элемент из списка

    def __add__(self, other):
        result = MyList()
        for i in range(max(len(self.elements), len(other.elements))):  # Создает цикл потом беред длину листа делет еше один лист он нулевой 
            n1 = self.elements[i] if i < len(self.elements) else 0      
            n2 = other.elements[i] if i < len(other.elements) else 0
            result.append(n1 + n2)  # Добавляем эту сумму в новый список 
        return result

    def __sub__(self, other):
        result = MyList()
        for i in range(max(len(self.elements), len(other.elements))):  # Делаем еще один цикл как в прошлый раз 
            n1 = self.elements[i] if i < len(self.elements) else 0
            n2 = other.elements[i] if i < len(other.elements) else 0
            result.append(n1 - n2)  # Так же добовляем в список 
        return result

    def __len__(self):
        return len(self.elements)  # Показыват числа эдемента списка

    def __lt__(self, other):
        return len(self.elements) < len(other.elements)  #Сравнения чисел 