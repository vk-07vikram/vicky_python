# print() formaatting using sep and end

print("Apple" , "banana" , "cherry" , sep= " , " ,end="<--- end of list\n")

#formatted message for user input 

name = input("Enter your name: ")
age = input("Enter your age: ")
hobby = input("Enter your hobby: ")

#print( "my name is" + name +" and my age is " + "and hobby is " + hobby )
 
print(f"hello ,{name}! at {age} , enjoying {hobby} sounds fun!!")