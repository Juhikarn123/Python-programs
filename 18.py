matrix = []
for _ in range(3):
    row = [int(x) for x in input("Enter a row of numbers: ").split()]
    matrix.append(row)
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()
