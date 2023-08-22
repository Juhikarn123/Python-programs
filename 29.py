input_str = input("Enter a list of numbers separated by spaces: ")
numbers = [int(x) for x in input_str.split()]

total_sum = 0
for num in numbers:
    total_sum += num

print(f"Sum of all elements: {total_sum}")
