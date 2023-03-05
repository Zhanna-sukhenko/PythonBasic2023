def print_triangle(height: int, fill_symbol=" 0 ", outer_symbol=" . ", border_symbol=" * ") -> None:
    for i in range(height - 1):
        print(
            outer_symbol * (height - i - 1),
            border_symbol,
            fill_symbol * ((i-1) if i > 0 else 0),
            border_symbol if i > i+1 else "   ",
            fill_symbol * ((i-1) if i > 0 else 0),
            border_symbol if i > 0 else "",
            outer_symbol * (height - i - 1),
            sep=""
        )
    print(border_symbol * (height * 2 - 1))

if __name__ == "__main__":
    input_height = int(input("input height: "))
    print("A")
    print_triangle(height=input_height, fill_symbol="   ", outer_symbol="   ")

def print_triangle(height: int, fill_symbol=" 0 ", outer_symbol=" . ", border_symbol=" * ") -> None:
    for i in range(height - 1):
        print(
            outer_symbol * (height - i - 1),
            border_symbol,
            fill_symbol * ((i-1) if i > 0 else 0),
            border_symbol if i > 0 else "",
            fill_symbol * ((i-1) if i > 0 else 0),
            border_symbol if i > 0 else "",
            outer_symbol * (height - i - 1),
            sep=""
        )
    print(border_symbol * (height * 2 - 1))

if __name__ == "__main__":
    input_height = int(input("input height: "))
    print("B")
    print_triangle(height=input_height, fill_symbol=" * ", outer_symbol="   ")

def print_triangle(height: int, fill_symbol1=" * ", fill_symbol2=" * ", outer_symbol=" . ", border_symbol=" * ") -> None:
    for i in range(height - 1):
        print(
            outer_symbol * (height - i - 1),
            border_symbol,
            fill_symbol1 * ((i-1) if i > 0 else 0),
            border_symbol if i > 0 else "",
            fill_symbol1 * ((i-1) if i > 0 else 0),
            border_symbol if i > 0 else "",
            outer_symbol * (height - i - 1),
            sep=""
        )
    print(border_symbol * (height * 2 - 1))
    for i in reversed(range(0, input_height - 1)):
        print(
            outer_symbol * (height - i - 1),
            border_symbol,
            fill_symbol2 * ((i - 1) if i > 0 else 0),
            border_symbol if i > i + 1 else "   ",
            fill_symbol2 * ((i - 1) if i > 0 else 0),
            border_symbol if i > 0 else "",
            outer_symbol * (height - i - 1),
            sep=""
        )
if __name__ == "__main__":
    input_height = int(input("input height: "))
    print("C")
    print_triangle(height=input_height, fill_symbol2="   ", outer_symbol="   ")

def print_triangle(height: int, fill_symbol1=" * ", fill_symbol2=" * ", outer_symbol=" . ", border_symbol=" * ") -> None:
    for i in range(height - 1):
        print(
            outer_symbol * (height - i - 1),
            border_symbol,
            fill_symbol1 * ((i-1) if i > 0 else 0),
            border_symbol if i > 0 else "",
            fill_symbol1 * ((i-1) if i > 0 else 0),
            border_symbol if i > 0 else "",
            outer_symbol * (height - i - 1),
            sep=""
        )
    print(border_symbol * (height * 2 - 1))
    for i in reversed(range(0, input_height - 1)):
        print(
            outer_symbol * (height - i - 1),
            border_symbol,
            fill_symbol2 * ((i - 1) if i > 0 else 0),
            border_symbol if i > 0 else "",
            fill_symbol2 * ((i - 1) if i > 0 else 0),
            border_symbol if i > 0 else "",
            outer_symbol * (height - i - 1),
            sep=""
        )

if __name__ == "__main__":
    input_height = int(input("input height: "))
    print("D")
    print_triangle(height=input_height, fill_symbol2="   ", outer_symbol="   ")
