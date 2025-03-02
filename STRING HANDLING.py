# STRING HANDLING
# Write a program to concatenate two strings.
string_1 = input("ENTER THE INPUT:")
string_2 = input("ENTER THE INPUT:")
ADD = string_1 + string_2
print(ADD)

# Write a program to find the length of a string.
A = input("ENTER THE INPUT :")
print(len(A))

# Write a program to reverse a string.
A = input("ENTER THE INPUT :")
B = A[::-1]
print(B)

# Write a program to check if a string is a palindrome.

a = input("ENTER YOUR INPUT IN UPPER CLASS :")
a = a.upper()
b= a[::-1]
if(a == b):
   print("THE WORD" ,a, "IS A PALINDROME")
else:
    print("THE WORD" ,a, "IS NOT A PALINDROME")

# Write a program to count the number of vowels in a string.
String = input('Enter the string :')
count = 0
#to check for less conditions
#keep string in lowercase
String = String.lower()
   if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        #if True
       count+=1
#check if any vowel found
if count == 0:
    print('No vowels found')
else:
   print('Total vowels are :' + str(count))

a = input("ENTER YOUR INPUT :")
a = a.lower()
count = 0
vowels = ['a' , 'e' , 'i' , 'o' , 'u']
for char in a:
    if char in vowels:
        count = count+1
        print("THE TOT NUM OF VOWELS ARE" ,count)
        
# Write a program to convert a string to uppercase.

a = input("ENTER A STRING :")
a = a.upper()
print(a)

# Write a program to convert a string to lowercase.
a = input("ENTER A STRING :")
a = a.lower()
print(a)

# Write a program to replace a substring in a string.
main = input("ENTER THE MAIN STRING :")
sub = input("ENTER THE OLD SUB STRING :")
new = input("ENTER THE NEW SUBSTRING :")
main = main.upper()
sub = sub.upper()
new = new.upper()
op = main.replace(sub,new)
print("THE UPDATED STRING IS",op)

# Write a program to check if a string starts with a specific prefix.
string = input("ENTER THE STRING :")
string = string.upper()
prefix = input("ENTER THE PREFIX :")
prefix = prefix.upper()
if string.startswith(prefix):
    print("YES")
else:
    print("NO")
# Write a program to check if a string ends with a specific suffix.

string = input("ENTER THE STRING :")
string = string.upper()
sufix = input("ENTER THE SUFIX :")
sufix = sufix.upper()
if string.endswith(sufix):
    print("YES")
else:
    print("NO")
