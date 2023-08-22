List1 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 5, 5, 5, 6, 7]
k = 2
print("Original List:", str(List1))
 
res_list = []
 
for i in List1:
   counter = List1.count(i)
   if counter > k and i not in res_list:
     res_list.append(i)
 
print("The list items with count > k = ", res_list)
