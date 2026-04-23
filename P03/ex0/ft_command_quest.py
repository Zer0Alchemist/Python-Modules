import sys

if __name__ == "__main__":
    print("=== Command Quest ===")

    lenght = len(sys.argv)
    args = len(sys.argv) - 1

    if lenght == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {lenght}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {args}")
        i = 1
        while i <= args:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
        print(f"Total arguments: {lenght}")
