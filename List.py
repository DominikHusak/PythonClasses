class List:
    def __init__(self):
        self.stack = []

    def add(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("Zasobnik je prazdny.")

    def count(self):
        return len(self.stack)

    def clear(self):
        self.stack = []

    def popAll(self):
        data = list(self.stack)
        self.clear()
        return data

    def is_empty(self):
        return len(self.stack) == 0

stack = List()
stack.add(1)
stack.add(2)
stack.add(3)

print("Pocet prvku v zasobniku:", stack.count())
zasobnik_obsah = stack.popAll()
print("Obsah:", zasobnik_obsah)
print("Pocet prvku po vyprazdneni:", stack.count())
