#Conditional Statements
#Write a program to find the largest of three numbers.
NUM_1 = int(input("ENTER THE NUMBER :"))
NUM_2 = int(input("ENTER THE NUMBER :"))
NUM_3 = int(input("ENTER THE NUMBER :"))
if(NUM_1 > NUM_2 and NUM_1 > NUM_3):
    print("NUM_1 IS GREATER")
elif(NUM_2 > NUM_1 and NUM_2 > NUM_3):
    print("NUM_2 IS GREATER")
elif(NUM_3 > NUM_1 and NUM_3 > NUM_2):
    print("NUM_3 IS GREATER")
#Write a program to check if a number is positive, negative, or zero.
    
num = int(input("ENTER A NUMBER :"))
if(num < 0):
    print("THE NUM IS NEGATIVE")
elif(num > 0):
    print("THE NUM IS POsITIVE")
elif(num == 0):
    print("THE NUM IS ZERO")    
#Write a program to check if a year is a leap year.
    
year = int(input("ENTER THE YEAR :"))
if(year % 4 == 0):
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
#2000, 2004, 2008, 2012, 2016, 2020, 2024, 2028, 2032, 2036, and so on

#Write a program to check if a number is divisible by both 3 and 5
num = int(input("ENTER A NUMBER :"))
if(num % 3 == 0 and num % 5 ==0):
     print("DIVISIBLE")
else:
   print("NOT DIVISIBLE")
   
#Write a program to check if a character is a vowel or consonant.
A = input("ENTER A CHRACTER :")
VOW = ['a' , 'e' , 'i' , 'o' , 'u']
if(A in VOW):
    print("VOWEL")
else:
    print("CONSONANT")
#Write a program to check if a number is within a given range.
A = int(input("ENTER A NUMBER :"))
if(A in range(1,9)):
    print(f"{A} is in range")
else:
    print(f"{A} is not in range")

#Write a program to compare two strings and print the larger one.
STR_1 = input("ENTER A STRING :")
STR_1 = STR_1.upper()
STR_2 = input("ENTER A STRING :")
STR_2 = STR_2.upper()
if(len(STR_1 ) > len(STR_2)):
    print(f"{STR_1} is greater")
elif(len(STR_2) > len(STR_1)):
    print(f"{STR_2} is greater")
else:
    print("BOTH ARE EQUAL")
    
#Write a program to calculate the grade based on a student's score.
MARK = int(input("ENTER YOUR MARK :"))
if(MARK <= 100 and MARK >=90):
   print("YOUR GRADE IS O")
elif(MARK <= 89 and MARK >=80):
    print("YOUR GRADE IS A")
elif(MARK <= 79 and MARK >=70):
    print("YOUR GRADE IS B")
elif(MARK <= 69 and MARK >= 60):
    print("YOUR GRADE IS C")
elif(MARK <= 59 and MARK >=50):
    print("YOUR GRADE IS D")
elif(MARK < 50 and MARK >= 0):
    print("YOU ARE FAILED")
else:
    print("ENTER VALID MARK")

#Write a program to check if a number is a prime number.
NUM = int(input("ENTER A NUMBER :"))
if(NUM <= 1):
    print(f"{NUM} IS NOT A PRIME NUMBER")
elif( NUM%2 == 0 or NUM % 3 == 0):
    print(f"{NUM} IS NOT A PRIME NUMBER")
else:
    print(f"{NUM} IS NOT A PRIME NUMBER")



































































































