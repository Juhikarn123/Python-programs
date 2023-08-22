numbers = [int(x) for x in input("Enter a list of numbers: ").split()]
squared_even = [x ** 2 for x in numbers if x % 2 == 0]
print("Squared even numbers:", squared_even)
