#
# Fabio Nicolai Lagos Padilla
# 32341166
#
# Estructuras de Datos
# Sección 1168
#
# Foro 1
# Atria Vending Machine
# 
# Vending Machine
# V.0.00.09
#

import os

from src.machine import Machine
from src.product import Product

# Crea una máquina expendedora con 6 filas, 10 columnas y una capacidad de 5 productos por columna.
rows: int = 6
columns: int = 10
capacity: int = 5

# Importa la clase Machine y crea una instancia de la máquina expendedora con los parámetros.
vending_machine: Machine = Machine(rows, columns, capacity)

# Variables globales.
spacing: int = 5
length: int = columns * spacing
continueProgram: bool = True

def print_header():
    return "\n%s%s%s%s%s%s%s%s" % (
        "%s%s" % ("\t", "-" * length),
        "\n",
        "\n\t%s\n" % ("ATRIA VENDING MACHINE".center(length, " ")),
        "\n\t%s" % ("Creado por: ".center(length, " ")),
        "\n\t%s" % ("[Fabio Lagos]".center(length, " ")),
        "\n\t%s\n" % ("V 0.00.09".center(length, " ")),
        "\n",
        "%s%s" % ("\t", "-" * length)
    )

def print_menu():
    return "%s%s%s%s%s%s%s" % (
        "%s%s" % ("\t", "-" * length),
        "\n\t%s" % ("1. Insertar producto"),
        "\n\t%s" % ("2. Expulsar producto"),
        "\n\t%s" % ("3. Ver productos de una columna"),
        "\n\t%s" % ("4. Salir"),
        "\n",
        "%s%s" % ("\t", "-" * length)
    )

if (__name__ == "__main__"):
    while continueProgram:
        #os.system("clear")
        print(print_header())
        print(vending_machine.display(spacing))
        print(print_menu())

        option: str = input("\tSeleccione una opción: ")

        if (option == "1"):
            print("")
            name: str = input("\tIngrese el nombre del producto: ")
            price: float = float(input("\tIngrese el precio del producto: "))
            row: int = int(input(f"\tIngrese la fila (1-{rows}): "))
            column: int = int(input(f"\tIngrese la columna (1-{columns}): "))

            product: any = vending_machine.insert_product(row - 1, column - 1, Product(name, price))
            
            if isinstance(product, Product):
                print(f"\n\tProducto agregado correctamente: {product}")
            else:
                print(product)
        elif (option == "2"):
            print("")
            row: int = int(input(f"\tIngrese la fila (1-{rows}): "))
            column: int = int(input(f"\tIngrese la columna (1-{columns}): "))

            product: any = vending_machine.dispense_product(row - 1, column - 1)

            if isinstance(product, Product):
                print(f"\n\tProducto expulsado: {product}")
            else:
                print(product)
        elif (option == "3"):
            print("")
            row: int = int(input(f"\tIngrese la fila (1-{rows}): "))
            column: int = int(input(f"\tIngrese la columna (1-{columns}): "))

            products: any = vending_machine.display_column(row - 1, column - 1)

            print(products)
        elif (option == "4"):
            continueProgram = False
        else:
            print("\n\tOpción no válida, intente nuevamente.")

        #os.system("pause")
