#Python Assignment 1: Data Structures - Strings & Tuples#

#1. String Concatenation:#

string1 ='hello '
string2 = input('what is your name?')     # taking input from user #
result = string1 + string2                # storing the concatenated string into result #
print(result)
string3 =', welcome to Python programming'
result2 = result  +  string3              # storing the concatenated string into result2 #
print(result2)

#2. String Slicing and Indexing:#

print(result2[0:1])   #first character of the string.#
print(result2[-1])    #last character of the string.#
print(result2[0:5])   #first 5 characters of the string.#
print(result2[0:-11]) #last 11 characters of the string.#
print(result2[::-1])  #string in reverse.#
print(result2.index("Python"))# to get the strings index number#
print(result2[23:29])        #printing specific string #

#3. String Methods:#

strM='Python beginner tutorial'
print(strM.upper())          #upper case#
print(strM.lower())          #lowe case#
print(strM.capitalize())     #Capitalize#
print(strM.count('t'))       # number of t in the string#

new_strM ='Machine Learning' + strM[6:]  #change  python to machine learning#
print(new_strM)

#Tuples (Creation, Modification and Access) :#

t1 = (10,20,30)  # creation of tuple #
t2 = (40,50,60)
t_combine = (t1 + t2)
print(t_combine)
print(t_combine *3)    # repeating the elements 3 times#
print(t_combine[2])    # access the 3rd element#
print(t_combine[0:3])  # first three elements#
print(t_combine[-3:])  # last three elements#