def possible_arrangments(list1):
      for x in range(3):
        for y in range(3):
            for z in range(3):  
                if (x!=y and y!=z and x!=z):
                    print(list1[x], list1[y], list1[z])
 

List3 = ['A', 'B', 'C']
possible_arrangments(List3)
