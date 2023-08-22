List1 = ['XYZ', 'ABC', 'xyz', 'abc']
print("Original List:", str(List1))
 
List1[0], List1[-1] = List1[-1], List1[0]
print("List after swapping:", str(List1))
