##Find max value without max() 

def find_max_value(lst):
  
    max_value = lst[0]
    
    for item in lst:
      if item > max_value:
            max_value = item
    
    return max_value


numbers = [4, 2, 9, 7, 5, 1]
print(find_max_value(numbers))
