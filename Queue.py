class Queue:
    def __init__(self):
        self.queue = []

    def add(self, data):
        self.queue.append(data)

    def pop(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError("Fronta je prazdna.")

    def count(self):
        return len(self.queue)

    def clear(self):
        self.queue = []

    def popAll(self):
        data = list(self.queue)
        self.clear()
        return data

    def is_empty(self):
        return len(self.queue) == 0

queue = Queue()
queue.add(1)
queue.add(2)
queue.add(3)

print("Pocet prvku ve fronte:", queue.count())

fronta_obsah = queue.popAll()
print("Obsah:", fronta_obsah)
print("Pocet prvku po vyprazdneni:", queue.count())
