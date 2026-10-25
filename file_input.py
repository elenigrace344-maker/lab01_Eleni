def read_from_file():
    filename = input("Enter the name of the text file: ")

    try:
        with open(filename, "r") as f:
            content = f.read().strip()
            numbers = [int(x) for x in content.split()]
            print("Numbers read from file:", numbers)
    except FileNotFoundError:
        print("Error: The file does not exist.")


if __name__ == "__main__":
    print("=== Requirement 2 ===")
    read_from_file()

