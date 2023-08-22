List1 = [10, 5, -4, 6, -3, 7, 9]
print("The original list is : " + str(List1))
 
def find_odd(test_list):
  counter = 0
  odd_list = []
  for num in List1:  
    if num % 2 != 0:
        odd_list.append(num)
        counter += 1
 
  print("The odd number list =", odd_list)
  print("The number of odd elements are:", counter)
 
def find_even(test_list):
  counter = 0
  even_list = []
  for num in List1:  
    if num % 2 == 0:
        even_list.append(num)
        counter += 1
 
  print("The odd number list =", even_list)
  print("The number of odd elements are:", counter)
 
find_odd(List1)
find_even(List1)
