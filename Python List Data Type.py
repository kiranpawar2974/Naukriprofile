# CredenceT1819= [101,"Yusuf",90000,"Pune","CSE"]
# list1 = [1, 2, "Python", "Program", 15.9]
# list2 = ["Amy", "Ryan", "Henry", "Emma"]
# list3 = [101,102,103]
# a=10
#
# # # printing the list
# print(CredenceT1819)
# print(list1)
# print(list2)
# print(list3)
# #
# # # printing the type of list
# print(type(CredenceT1819))
# print(type(list1))
# print(type(list2))
# print(type(list3))
# print(type(a))
#
#
# list1 = [12, 14, 16, 18, 20]
# print(list1)
# print(list1*5)
# print(list1*2)
#
# list1= (list1*5) # it will update list1 becz LISTS are Mutable Data Type.
# print(list1)

# ct18 = list1 * 5
# print(ct18)
# print(type(list1))
# print(type(ct18))
# #
# list1 = [12, 14, 16, 18, 20]
# list2 = [9, 10, 32, 54, 86]
# # print(list1)
# print(list2)
# print(list1*3)
# # # concatenation operator +
# list3 = list1 + list2
# print(list3)

# list1 = [12, 14, 16, 18, 20, 23, 27, 39, 40]
# # # # finding length of the list
# print(len(list1))


list1 = [100, 200, 300, 400, 500]
# print(len(list1))
# # true will be printed if value exists
# # and false if not
#
# print(600 in list1)
# print(700 in list1)
# print(1040 in list1)
# #
# print(300 in list1)
# print(100 in list1)
# print(500 in list1)
# #
# print(600 not in list1)
# print(700 not in list1)
# print(1040 not in list1)
# #
# print(300 not in list1)
# print(100 not in list1)
# print(500 not in list1)


# List checking
# a = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6 ]
# b = [ 1, 2, 5, "Ram", 3.50, "Rahul", 6 ]
# print(a == b)
# # # #
# a = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6]
# b = [ 1, 2, "Ram", 3.50, "Rahul", 5, 6]
# print(a == b)

# List Slicing

emplist = [101,"Yusuf",90000,"Pune","CSE"]
# print(emplist[0])
# print(emplist[1])
# print(emplist[2])
# print(emplist[3])
# print(emplist[4])
# print(emplist[5])
# print(emplist[6])

# my_list = [1, 2, 3, 4, 5]
# #
# print(my_list[:])
# print(my_list[:])
# print(my_list[0:])
# print(my_list[2:])
# print(emplist[:3])
# print(emplist[2:4])
# print(emplist[::1])
# print(emplist[::2])
# print(emplist[::3])
# print(emplist[::4])
# print(emplist[::5])

# negative indexing example
# print(emplist[-1])
# print(emplist[-2])
# print(emplist[-3])
# print(emplist[-4])
# print(emplist[-5])

# print(emplist[-3:])
# print(emplist[:-3])
# print(emplist[-3:-1])
# print(emplist[::-1])
#
# print(emplist[::-2])
# print(emplist[::-3])
# print(emplist[::-4])
# print(emplist[::-5])

# List = [50, 70, 30, 20, 90, 10, 60, 90]
#
# # Display list
# print(List[-7::1])
# print(List[-7::-1])
# print(List[7::-1])
# print(List[1:5])

List = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# #
# # # Show original list
# print("\nOriginal List:\n", List)
#
# print("\nSliced Lists [3:9:2] : ")
# #
# # # Display sliced list
# print(List[3:9:2])
# # #
# # # # Display sliced list
# print(List[::2])
# # #
# # # # Display sliced list
# print(List[::])

emplist = [101,"Yusuf",90000,"Pune","CSE"]
# print(emplist)
# emplist[2]= 190000
# emplist[3]= "Solapur"
# print(emplist)

# emplist[-1] = "Entc"
# print(emplist)

#
# emplist[1:3] = ["Poonam",98000]
# print(emplist)
#
# emplist[1:3] = [98000,"Poonam"]
# print(emplist)

# emplist[-3:-1] = [80000,"Kolhapur"]
# print(emplist)

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
# print(thislist)
# #
# thislist[1:3] = ["blackcurrant", "watermelon"]
# print(thislist)
#
# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# # # # #
# #
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# print(thislist)
# thislist[1:3] = ["watermelon"]
# print(thislist)
# #
# thislist[2:4] = ['a', 'b', 'c', 'd']
# print(thislist) # ['apple', 'banana', 'a', 'b', 'c', 'd']
# thislist[:-1] = []
# print(thislist)



#
# # Initialize list
# List1 = ["Yusuf", 2, 3, 4, 5, 6, 7, 8, 9]
# List2 = ["Tushar",11,12,13,14,15]
# # #
# # # # Show original list
# print("\nOriginal List1:\n", List1)
# print("\nOriginal List2:\n", List2)
# #
# List3=List1+List2
# print("\nConcatinated List3:\n",List3)
#
# print("\nSliced Lists: ")
# #
# # # Creating new List
# newList = List1[:3] + List2[3:]
# print(newList)
#
# newList = List1[0:1] + List2[0:1]
# #
# # # # Display sliced list
# print(newList)
# #
# # # Changing existing List
# List = List1[::2] + List2[1::2]
# #
# # # Display sliced list
# print(List)


# List Method Examples
#
# animals = ['cat', 'dog', 'rabbit']
# print(animals)
# animals.append("Tiger")
# print(animals)

# animals = ['cat', 'dog', 'rabbit']
# # list of wild animals
# wild_animals = ['tiger', 'fox']
# print('Old animals list: ', animals)
# print('Old wildanimals list: ', wild_animals)
#
# # appending wild_animals list to animals
# animals.append(wild_animals)
# wild_animals.append(animals)
#
# #
# #
# print('Updated animals list: ', animals)
# print('Updated Wild_animals list: ', wild_animals)

#
# fruits1 = ['apple', 'banana', 'cherry', 'orange']
# fruits2 = ['apple', 'banana', 'cherry', 'orange']

# print(fruits1)
# fruits1.clear()
# print(fruits1)

# print(fruits2)
# del fruits2[:]
# print(fruits2)

# list = [101,102,"yusuf","Priya"]
# # #
# # # # clearing the list
# print(list)
# # list.clear()
# del list[:]
# print(list)
# print('List:', list)

# mixed list
# my_list = ['cat', 0, 6.7]
# print("Original List:", my_list)
# #
# # # copying a list
# new_list = my_list.copy()
# print('Copied List:', new_list)

# old_list = [1, 2, 3]
# new_list = old_list
# print(old_list)
# print(new_list)
# # # #
# # # #
# new_list.append(4)
# print(new_list)
# print(old_list)

# mixed list
# my_list = ['cat', 0, 6.7]
#
# # copying a list using slicing
# new_list = my_list[:]
#
# print(new_list)
# # Adding an element to the new list
# new_list.append('dog')
# print('New List:', new_list)
#
# #
# # # Printing new and old list
# print('Old List:', my_list)

# create a list
# numbers = [2, 3, 5, 2, 11, 2, 7]
# print(numbers)

# check the count of 2

# print(numbers.count(2))

# cnt= numbers.count(2)
# print(cnt)
# Output: Count of 2: 3

# vowels list
# vowels = ['a', 'e', 'i', 'o', 'i', 'u']

# count element 'i'
# print(vowels.count("i")) # only print krna

# count = vowels.count('i')

# print count
# print('The count of i is:', count)# variable leke print krna

# count element 'p'
# count = vowels.count('p')
#
#
# # print count
# print('The count of p is:', count)
#
# # create a list
# odd_numbers = [1, 3, 5]
# print(odd_numbers)
#
# # create another list
# even_numbers = [2, 4]
# print(even_numbers)
#
# #
# # # add all elements of prime_numbers to numbers
# even_numbers.extend([102,104])
# even_numbers.append([108,110])
#
# # #

# print('List after extend():', even_numbers)
# even_numbers.extend(odd_numbers)
# print('List after extend():', even_numbers)
# odd_numbers.extend(even_numbers)
# print('List after extend():', odd_numbers)


# languages list
# languages_list = ['French']
# # # # languages tuple
# languages_tuple = ('Spanish', 'Portuguese')
# # # # languages set
# languages_set = {'Chinese', 'Japanese'}
# # # # appending language_tuple elements to language
# languages_list.extend(languages_tuple)
# print('New Language List:', languages_list)
# # # # appending language_set elements to language
# languages_list.extend(languages_set)
# print('Newer Languages List:', languages_list)

#
# a1 = [1, 2]
# a2 = [1, 2]
# b  = (3, 4)
# #
# a1.extend(b)
# print(a1)
# # #
# # # a2 = [1, 2, (3, 4)]
# a2.append(b)
#
# print(a2)
# a2.append(a1)
# print(a2)

#
# print(len(a1))
# print(len(a2))

# animals = ['cat', 'dog', 'rabbit', 'horse']
# # get the index of 'dog'
# print(animals.index('dog'))

# second way of printing index value
# Position_Dog = animals.index('dog')  #1
#
# print(Position_Dog)

# vowels = ['a', 'e', 'i', 'o', 'u']

# index of 'p' is vowels
# Position_p = vowels.index('p')
# print(vowels.index('p'))
# print('The index of p:', Position_p)

# alphabets list
# alphabets = ['a', 'e', 'i', 'o', 'g', 'l', 'i', 'u']
# #
# # # index of 'e' in alphabets
# indexOfe = alphabets.index('e')   # 1
# # #
# print('The index of e:', indexOfe)
# # #
# # # # 'i' after the 4th index is searched
# indexofi = alphabets.index('i', 4)   # 6
# # #
# print('The index of i:', indexofi)
# #
# # # 'i' between 3rd and 5th index is searched
# indexofi = alphabets.index('i', 3, 5)   # Error!
# #
# print('The index of i:', indexofi)


# fruits = ['apple', 'banana', 'cherry']
# # #
# fruits[1]= "orange"
# print("Update hoga Orange item list ke banana ko replace krke  using slice: ",fruits)
# #
# fruits = ['apple', 'banana', 'cherry']
# fruits.insert(1, "orange")
# print("insert orange in fruits with position 1 and banana will be moved to next index:",fruits)

# create a list of prime numbers
# prime_numbers = [2, 3, 5, 7]
# # # # insert 11 at index 4
# prime_numbers.insert(4, 11)
# print('List:', prime_numbers)

# mixed_list = [{1, 2}, [5, 6, 7]]
# # # number tuple
# number_tuple = (3, 4)
# # # inserting a tuple to the list
# mixed_list.insert(1, number_tuple)
# print('Updated List:', mixed_list)


# create a list of prime numbers
# prime_numbers = [2, 3, 5, 7]
# print(prime_numbers)
# remove the element at index 2
# print(prime_numbers.pop(2))
# print(prime_numbers)

# removed_element_2 = prime_numbers.pop(2)
# print('Removed Element:', removed_element_2)
# #
# print('Updated List:', prime_numbers)

# languages = ['Python', 'Java', 'C++', 'Ruby', 'C']
# #
# # # remove and return the last item
# print('When index is not passed:')
# print('Deleted Value:', languages.pop())
# # #
# print('Updated List:', languages)
#
# languages = ['Python', 'Java', 'C++', 'Ruby', 'C']
# # remove and return the last item
# print('\nWhen -1 is passed:')
# print('Return Value:', languages.pop(-1))
# # #
# print('Updated List:', languages)
# #
# print('Return Value:', languages.pop(-3))
# print('Updated List:', languages)

# create a list
# prime_numbers = [2, 3, 5, 7, 9, 11]
# #
# # # remove 9 from the list
# prime_numbers.remove(9)
# #
# # # Updated prime_numbers List
# print('Updated List: ', prime_numbers)

# systems = ['Windows', 'macOS', 'Linux']
# print('Original List:', systems)
#
# # # List Reverse
# systems.reverse() # using list methiod
# #
# # # updated list
# print('Updated reversed List:', systems)

# print(systems[::-1]) #using slice

# prime_numbers = [11, 3, 7, 5, 2]
# print(prime_numbers)
# # #
# # # # sorting the list in ascending order
# prime_numbers.sort()
# print("Ascending:",prime_numbers)
# #
# systems.sort()
# print("Ascending:",systems)
# #

# prime_numbers.sort(reverse=True)
# #Logic ---  prime_numbers.sort = 2, 3, 5, 7, 11 -- (reverse=True)----11 7 5 3 2
# print("Descending:",prime_numbers)
#
# vowels list
# vowels = ['e', 'a', 'u', 'o', 'i']
# # #
# # # # sort the vowels
# #
# vowels.sort()
# print("Ascending:",vowels)
# #
# vowels.sort(reverse=True)
# print("Descending:",vowels)
