input_str = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in input_str.split()]
smallest = largest = numbers[0]
for num in numbers:
    if num < smallest:
        smallest = num
    elif num > largest:
        largest = num
print(f"Smallest element: {smallest}")
print(f"Largest element: {largest}")
