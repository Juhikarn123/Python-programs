matrix = []
for _ in range(3):
    row = [int(x) for x in input("Enter a row of numbers separated by spaces: ").split()]
    matrix.append(row)

print("Entered matrix:")
for row in matrix:
    for element in row:
        print(element, end=" ")
    print()

transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print("Transposed matrix:")
for row in transpose:
    for element in row:
        print(element, end=" ")
    print()
