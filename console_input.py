def read_sequence():
    raw = input("Enter a sequence of numbers separated by spaces: ")
    numbers = [int(x) for x in raw.split()]
    print("Sequence:", numbers)


def read_array():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    array = []
    print("Enter the numbers row by row:")

    for r in range(rows):
        row = [int(x) for x in input(f"Row {r+1}: ").split()]
        if len(row) != cols:
            print("Error: row does not match required number of columns.")
            return
        array.append(row)

    print("Array:")
    for row in array:
        print(row)


if __name__ == "__main__":
    print("=== Requirement 1 ===")
    read_sequence()
    read_array()
