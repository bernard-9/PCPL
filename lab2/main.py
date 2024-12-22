from colorama import Fore, Style

from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

N = 24

def main():
    rectangle = Rectangle(N, N, "синий")
    circle = Circle(N, "зелёный")
    square = Square(N, "красный")

    print(rectangle)
    print(circle)
    print(square)

    print(Fore.RED + "красный")
    print(Fore.BLUE + "синий")
    print(Fore.GREEN + "зелёный")
    print(Style.RESET_ALL)

if __name__ == "__main__":
    main()
