#Data types and operators
#Q1
NUM_1 = float(input("Enter the Number : "))
NUM_2 = float(input("Enter the Number : "))
ADD = NUM_1 + NUM_2
print(ADD)

#Q2
NUM_1 = float(input("ENTER A NUMBER :"))
NUM_2 = float(input("ENTER A NUMBER :"))
SUB = NUM_1 - NUM_2
print(SUB)

#Q3
NUM_1 = float(input("ENTER A NUMBER :"))
NUM_2 = float(input("ENTER A NUMBER :"))
MUL = NUM_1 * NUM_2
print(MUL)

#Q4
NUM_1 = float(input("ENTER A NUMBER :"))
NUM_2 = float(input("ENTER A NUMBer ;"))
if(NUM_1 == 0):
    print("Numorator cannot be zero")
elif(NUM_2 == 0):
    print("ZERO")
else:
  print(NUM_1 / NUM_2)
    
#Q5
NUM_1 = float(input("ENTER A NUMBER :"))
NUM_2 = float(input("ENTER A NUMBER :"))
DIFF = NUM_1 % NUM_2
print("THE REMAINDER OF TWO NUMBERS ARE",DIFF)

#Q6
num1 = int(input("ENTER A NUMBER :"))
num2 = int(input("ENTER A NUMBER :"))
num1 = num1 + num2#adds both num and assign a new value for num1
num2 = num1 - num2#sub the num2 value with the newly assigned num1 value and assign a new num2 value
num1 = num1 - num2#sub the newely assigned values and prints the output
print("NUM_1 =",num1)
print("NUM_2 =",num2)

#Q7
num = int(input("ENTER A NUMBER :"))
if(num%2 == 0):
    print("THE GIVEN NUMBER" ,num, "IS EVEN")
elif(num%2 == 1):
    print("THE GIVEN NUMBER" ,num, "IS ODD")

#Q8
num = int(input("ENTER A NUMBER :"))
SQUARE = num**2
print("THE SQUARE VALUE OF" ,num, "is" ,SQUARE)

#Q9
num = int(input("ENTER A NUMBER :"))
CUBE = num**3
print("THE CUBE VALUE OF" ,num, "is" ,CUBE)

#Q10
celcius = float(input("ENTER THE TEMPERATURE IN CELCIUS :"))
fahrenhit = (celcius * 1.8) + 32
print("THE TEMP IN FARHENHIT IS" ,fahrenhit,"F")
































