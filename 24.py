numbers = []
for _ in range(10):
    num = int(input("Enter list element: "))
    numbers.append(num)

unique_numbers = []
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)

print("Original List:", numbers)
print("List with Repeated Elements Removed:", unique_numbers)
