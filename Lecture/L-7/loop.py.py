# Break Statement in python 
 
# for i in range(1 , 6):
#     if  i == 5:
#         break
#     print("For loop : " , i)

# continue statementin python 

# for i in range(1 ,6):
#     if i == 4:
#         continue 
#     print("for loop : " , i)

# patters print in python 

# for i in range(5):
#     print("i loop: " , i)   
#     for j in range(i):
#         if j == 1:
#             break
#         print("j loop: " , j)

# pattern : * 

# for i in range(1 , 6):
#     for j in range(1 , i):
#         print(f"{j}" , end="")
#     print()

# # Pattern 1: 

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(f"{j}" , end=' ')
#     print()

# # Pattern 2: 

# for i in range(1, 6):
#     for j in range(i, 0, -1):
#         print(f"{j}", end=' ')
#     print()

# # Pattern 3: 

# for i in range(1, 6):
#     for j in range(i):
#         print(f"{j}", end=' ')
#     print()

# # Pattern 4: 

# for i in range(5, 0, -1):
#     for j in range(6 - i):
#         print(f"{j}", end=' ')
#     print()

# # # Pattern 5: 

# for i in range(5, 0, -1):
#     for j in range(i, 6):
#         print(f"{j}", end=' ')
#     print()

# # Pattern 6: 

# for i in range(1, 6):
#      for j in range(5, 5 - i, -1):
#         print(f"{j}", end=' ')
#      print()