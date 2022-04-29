# В данном случае рассматрвиается куча,где значение в любой веришне больше,чем у потомков(max-heap).
# Min-heap реализуется аналогично
import time
import pickle
import random

with open('dataset_10000.pickle', 'rb') as file:
    data = pickle.load(file)

k = random.randint(1,1000)
t_start = time.perf_counter()
class Heap:
    def __init__(self, massive):
        self.massive = massive
        self.__Build_Heap(self.massive)
        self.max_elem = 0
        self.sort_massive = []

    def __HeapDown(self, massive, i):
        if 2 * i + 1 < len(massive) and massive[2 * i + 1] > massive[i] and 2 * i + 2 < len(massive) and \
                massive[2 * i + 2] > massive[i]:
            if massive[2 * i + 1] > massive[2 * i + 2]:
                massive[i], massive[2 * i + 1] = massive[2 * i + 1], massive[i]
            else:
                massive[i], massive[2 * i + 2] = massive[2 * i + 2], massive[i]
        elif 2 * i + 1 < len(massive) and massive[2 * i + 1] > massive[i]:
            massive[i], massive[2 * i + 1] = massive[2 * i + 1], massive[i]
            self.__HeapDown(massive, 2 * i + 1)
        elif 2 * i + 2 < len(massive) and massive[2 * i + 2] > massive[i]:
            massive[i], massive[2 * i + 2] = massive[2 * i + 2], massive[i]
            self.__HeapDown(massive, 2 * i + 2)

    def __Build_Heap(self, massive):
        for i in range(len(massive) // 2 - 1, -1, -1):
            self.__HeapDown(massive, i)

    def __HeapUp(self, massive, i):
        if massive[i] > massive[i // 2]:
            massive[i], massive[i // 2] = massive[i // 2], massive[i]
            self.__HeapUp(massive, i // 2)

    def Heapsort(self):
        for i in range(len(self.massive)):
            self.sort_massive.append(self.remove())
        return self.sort_massive

    def insert(self, elem):
        self.massive.append(elem)
        self.__HeapUp(self.massive, len(self.massive) - 1)

    # Так как двочная куча не создана для удаления произвольного объекта,
    # метод remove будет удалять и возвращать максимальный объект

    def remove(self):
        if len(self.massive) == 0:
            raise Exception('Данная куча пуста!')
        else:
            self.max_elem = self.massive[0]
            self.massive[0], self.massive[len(self.massive) - 1] = self.massive[len(self.massive) - 1], self.massive[0]
            self.massive.pop(len(self.massive) - 1)
            if self.massive != []:
                self.__HeapDown(self.massive, 0)
            return self.max_elem


a = Heap(data)
a.remove()
all_time = time.perf_counter() - t_start
print('Время: ', all_time)
