size = int(input("Enter the size of the pattern: "))

inline = size
while size > 0:
    for line in range(0, inline):
        print("*", end="")
    print()
    size -= 1