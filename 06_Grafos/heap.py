from typing import Any

class HeapMax():
    def __init__(self):
        self.elements = []

    def add_element(self, value: Any) -> None:
        self.elements.append(value)
        self.float(self.size() - 1)

    def delete_element(self) -> Any:
        if self.size() == 0:
            return None
        self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
        value = self.elements.pop()
        if self.size() > 0:
            self.sink(0)
        return value

    def size(self) -> int:
        return len(self.elements)

    def float(self, index: int) -> None:
        while index > 0 and self.elements[index] > self.elements[(index - 1) // 2]:
            father = (index - 1) // 2
            self.elements[index], self.elements[father] = self.elements[father], self.elements[index]
            index = father

    def sink(self, index: int) -> None:
        left = (index * 2) + 1
        control = True
        while control and left < self.size():
            right = (index * 2) + 2
            max_child = left
            if right < self.size():
                max_child = max_child if self.elements[max_child] > self.elements[right] else right

            if self.elements[index] < self.elements[max_child]:
                self.elements[index], self.elements[max_child] = self.elements[max_child], self.elements[index]
                index = max_child
                left = (index * 2) + 1
            else:
                control = False

    def arrive(self, value: Any, priority: Any) -> None:
        self.add_element([priority, value])

    def attention(self) -> Any:
        result = None
        if self.size() > 0:
            result = self.delete_element()
        return result

    def convert_to_heap(self) -> None:
        # Optimizado O(n): hundir desde el último padre hasta la raíz
        for i in range((self.size() // 2) - 1, -1, -1):
            self.sink(i)

    def heap_sort(self) -> list:
        result = []
        while self.size() > 0:
            value = self.delete_element()
            result.append(value)
        return result


class HeapMin():
    def __init__(self):
        self.elements = []

    def add_element(self, value: Any) -> None:
        self.elements.append(value)
        self.float(self.size() - 1)

    def delete_element(self) -> Any:
        if self.size() == 0:
            return None
        self.elements[0], self.elements[-1] = self.elements[-1], self.elements[0]
        value = self.elements.pop()
        if self.size() > 0:
            self.sink(0)
        return value

    def size(self) -> int:
        return len(self.elements)

    def float(self, index: int) -> None:
        while index > 0 and self.elements[index] < self.elements[(index - 1) // 2]:
            father = (index - 1) // 2
            self.elements[index], self.elements[father] = self.elements[father], self.elements[index]
            index = father

    def sink(self, index: int) -> None:
        left = (index * 2) + 1
        control = True
        while control and left < self.size():
            right = (index * 2) + 2
            min_child = left
            if right < self.size():
                min_child = min_child if self.elements[min_child] < self.elements[right] else right

            if self.elements[index] > self.elements[min_child]:
                self.elements[index], self.elements[min_child] = self.elements[min_child], self.elements[index]
                index = min_child
                left = (index * 2) + 1
            else:
                control = False

    def arrive(self, value: Any, priority: Any) -> None:
        self.add_element([priority, value])

    def search(self, value: Any) -> int:
        for index, element in enumerate(self.elements):
            if element[1][0] == value:
                return index
        return -1

    def attention(self) -> Any:
        result = None
        if self.size() > 0:
            result = self.delete_element()
        return result

    def convert_to_heap(self) -> None:
        # Optimizado O(n): hundir desde el último padre hasta la raíz
        for i in range((self.size() // 2) - 1, -1, -1):
            self.sink(i)

    def heap_sort(self) -> list:
        result = []
        while self.size() > 0:
            value = self.delete_element()
            result.append(value)
        return result

    def change_priority(self, index: int, new_priority: Any) -> None:
        if index < len(self.elements):
            previous_priority = self.elements[index][0]
            self.elements[index][0] = new_priority
            if new_priority > previous_priority:
                self.sink(index)
            elif new_priority < previous_priority:
                self.float(index)