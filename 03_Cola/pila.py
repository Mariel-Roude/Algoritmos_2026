from typing import Any
from copy import copy

class Stack:

    def __init__(self):
        self.__elements = []

    def push(self, value: Any) -> None:
        self.__elements.append(value)

    def pop(self) -> Any:
        if self.size() > 0:
            return self.__elements.pop()
        return None
   
    def on_top(self) -> Any:
        if self.size() > 0:
            return self.__elements[-1]
        return None

    def size(self) -> int:
        return len(self.__elements)

    def is_empty(self) -> bool:
        return self.size() == 0

    def show(self) -> None:
        stack_aux = Stack()
        stack_aux.__elements = copy(self.__elements)

        while not stack_aux.is_empty():
            print(stack_aux.pop())