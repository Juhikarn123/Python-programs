list1 = [int(x) for x in input("Enter the first list of numbers: ").split()]
list2 = [int(x) for x in input("Enter the second list of numbers: ").split()]
common_elements = [x for x in list1 if x in list2]
print("Common elements:", common_elements)
