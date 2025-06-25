#1. Create a 1D Array (list) with five integer element display the array using a loop. 

arr = [10 , 20 , 30 , 40 , 50 , 60 , [70]]

print("Array Element: ")

for num in arr:
  print(num)

print(len(arr))

# 2. calculate the sum of all array elements in 1D array.abs

list = [10 , 20 , 30 , 40 , 50]

print(sum(list))

list_num = 0

for num in list:
  list_num+=num

print(list_num)

# 3. Find the maximun and minimun number of in 1D array,

list = [10 , 20 , 30 , 40 , 50]

print("Maximun Number" , max(list))
print("Minimum Number" , min(list))

# 4. Insert a new Element at a specific position in a 1D array. 

list = [10 , 20 , 30 , 40 , 50]

list[2] = 60

print(list)

# insert function

position = 2

new_element = 60

list.insert(position , new_element)

print(list)

# 5. Delete an element by its value from a 1D array.

list = [10 , 20 , 30 , 40 , 50]

del list[4]

print(list)

# remove function()

value_ref = 60

list.remove(value_ref)

print(list)

# 6. Update an Element in a 1D array based on it's index.

list = [10 , 20 , 30 , 40 , 50]

list[2] = 60

print(list)

# 7. Search for an element in a 1D array and return it's index.

list = [10 , 20 , 30 , 40 , 50]

search_element = 50

if search_element in list:
  print("Element Found in index : " , list.index(search_element))
else:
  print("Element not Found....")

# 8. concatenate two 1D array into a single array.
 
list_1 = [10 , 20 , 30]

list_2 = [40 , 50 , 60]

combined = list_1 + list_2

print("combined list: " , combined)

#9. sort a list of integer in accending order using a sort() method.

list = [10 , 45 , 23 , 89 , 35 , 101]

list.sort()

print(list)

list.reverse()

print(list)