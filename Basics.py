from math import *
# * Variables :
#The variable just hold one value!
char_Name = "ahmed"
print("there was a boy called "+ char_Name)
print("He liked his name "+ char_Name)
print(char_Name +" has one brother")

# * Numbers

print(3/6)
my_num= 5
print(str(my_num)+ " is my fav number") #converted into String!

my_num2 = -5
print(abs(my_num2))
print(max(2,3))
print(min(2,3))
print(round(3.8))
print(floor(3.6))
print(ceil(3.6))
print(sqrt(9))

# * Getting inputs :

name = input("Enter your name:")
major = input("Enter your Major: ")
print("Name is : "+ name+" ,Major is: "+ major)


# * Lists : holds more than one value!

family_members = ["Seham","Alya", "Shatha","Mona" ,"Hakim"]
print(family_members[0])
# First element is at index 0!
# -1 last element in list !
print(family_members[1:3]) # start from index 1(one is included!) to 3 , but 3 isnt concluded!
print(family_members[0:])
# Change values!
family_members[0] = "Sara"
Neibours = ["Ahmed", "Dourah"]

print(family_members, Neibours) # print 2 lists together!

# 1- Concatenation of two lists:
family_members.extend(Neibours)
print(family_members)
family_members += Neibours
print(family_members)

# 2-Append :
family_members.append("Cat")
print(family_members)

# 3- Insert: to a specific place!
family_members.insert(0,"Dog")
print(family_members)

# 4- delete a certain value from the list !
family_members.remove("Sara")
print(family_members)
# 5- delete all the list
Neibours.clear()
# 6- delete last value from list!
what_was_popped = family_members.pop()
print(family_members)
print(what_was_popped)
# 7-Checks if the value in the list or not
print(family_members.index("Dog")) #at index 0!
# 8- the function count ,counts how many the word "Mona" in my list !
print(family_members.count("Mona"))

# 9- sorting
family_members.sort()
print(family_members) # sorting here alphabetically!

nums = [3,6,4,1,9,0]
nums.sort()
print(nums)


# 10- copy of my list :

# nothing will happen to the copy!
new_list = family_members.copy()
family_members.append("David")
print(new_list)
print(family_members)

# if two lists are equal the copy will be the exact, any changes will inflict the two of them !
new_list = family_members
family_members.append(1)
print(family_members)
print(new_list)


# * Tuples : cannot be changed after making it  ! like lists adding or deleting or replace it with new value!

coordinates = (23,45)
print(coordinates[0])

# list of tuples!
list_of_tuples = [(2,4), (3,6) ,(8,0)] # CANNOT BE CHANGED !


# * FUNCTIONS :
def say_hi (name, age):
    print("Hi !" + name + " Your're age is :" +str(age) ) # CAST
    # you cannot print a number with string! all of the above is  STRING!

# call the function :
say_hi("Seham",21)


# Return statement :
def cube(number):
    return number * number * number
print(cube(3))

result = cube(4)
print(result)

def sum(number1 , number2):
    return number1 + number2

print(sum(2,6))

def sub(number1 , number2):
    return number1 - number2
    # any statement after return will not appear!
print(sub(2,6))


#  * If statemets :
is_hungry= False
wants_to_eat = True
if is_hungry and wants_to_eat : # if one of them true the if part will exist
    print("Go eat")
elif is_hungry and not wants_to_eat:
    print("Eat to survive! ")
elif not is_hungry and wants_to_eat:
    print("do not eat too much!")
else :
    print("Do not eat, Go do sport")


# * Dictionaries :
convert_month = { "jan" : "january" , "feb": "febraury" , "mar":"march"}
# Every key should be uniqe!
print(convert_month["mar"]) # march will be printed


