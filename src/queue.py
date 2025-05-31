from typing import Union

from src.product import Product

class Queue:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.queue: any = [None] * capacity
        self.front: int = 0
        self.rear: int = -1
        self.size: int = 0

    # Verifica si la cola está llena
    def is_full(self) -> bool:
        return self.size == self.capacity

    # Verifica si la cola está vacía
    def is_empty(self) -> bool:
        return self.size == 0
    
    # Devuelve el tamaño actual de la cola
    def size(self) -> int:
        return self.size

    # Inserta un producto al final de la cola
    def enqueue(self, product: Product) -> any:
        if self.is_full():
            return "\n\tLa cola está llena."
        
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = product
        self.size += 1

        return product

    # Expulsa el producto al frente de la cola
    def dequeue(self) -> any:
        if self.is_empty():
            return "\n\tLa cola está vacía."
        
        product = self.queue[self.front]
        self.queue[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1

        return product

    # Muestra los productos actuales en la cola
    def display(self) -> Union[str, None]:
        if self.is_empty():
            return None
        
        result: str = "\t\n"
        idx: int = self.front

        for product in range(self.size):
            result += "\t - %s\n" % (self.queue[idx])
            idx = (idx + 1) % self.capacity

        return result
