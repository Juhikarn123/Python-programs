List1 = [22, 24, 30, 22, 45, 67, 22, 30, 45]
item_to_remove = 22
 
print("The original list is : " + str(List1))
 
def remove_an_item(test_list, value):
 
  for x in test_list:
    if(x == value):
      test_list.remove(x)
  return test_list
 
res_list = remove_an_item(List1, item_to_remove)
 
print("Updated list after remove operation: " + str(res_list))
 
