
days=["Monday", "Tuesday", "Wednesday", 35]

# print(days)
#this is a "for loop"

for apple in days:
    if isinstance(apple, int):
        print("{} is a number".format(apple))
    else:
        print("today is {}".format(apple))


for x in range(1,0, -1):
    print("the number is {} and the next number is {}".format(x, x+1))

#string format syntax example above
#days is a list. Ranges are different from lists in that Ranges only works for numbers. Lists explictly define
#Range is inclusive of the start and exclusive of the end. -1 backwards
#apple is the name of a variable.
#String Interpolation
#If (Condition) Boolean decision. Truthy
#"None" is Python specific same as "Null" in C
#Truthy False includes None. 0, False, [], and "". Truthy True -everything else.




