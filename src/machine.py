from src.product import Product
from src.queue import Queue

class Machine:

    def __init__(self, rows: int, columns: int, capacity: int) -> None:
        self.rows = rows
        self.columns = columns
        self.capacity = capacity
        self.vending_machine = [[Queue(capacity) for product in range(columns)] for product in range(rows)]
        
    def insert_product(self, row: int, column: int, product: Product) -> any:
        if 0 <= row < len(self.vending_machine) and 0 <= column < len(self.vending_machine[0]):
            return self.vending_machine[row][column].enqueue(product)
        else:
            return "\t\tFila o columna fuera de rango."

    def dispense_product(self, row: int, column: int) -> any:
        if 0 <= row < len(self.vending_machine) and 0 <= column < len(self.vending_machine[0]):
            return self.vending_machine[row][column].dequeue()
        else:
            return "\t\tFila o columna fuera de rango."
        
    def display_column(self, row: int, column: int) -> any:
        if 0 <= row < len(self.vending_machine) and 0 <= column < len(self.vending_machine[0]):
            result = self.vending_machine[row][column].display()

            if result is None:
                return "\n\tLa cola está vacía."
            else:
                return f"\n\tProductos en la fila {row}, columna {column}: {result}" 
        else:
            return "\n\tFila o columna fuera de rango."
        
    def display(self, spacing: int):
        body: str = "\n\t"

        for row in range(self.rows):
            for column in range(self.columns):
                body += "%s" % (f"{self.vending_machine[row][column].size}".center(spacing, " "))
            
            body += "\n\t"
                
        return body
