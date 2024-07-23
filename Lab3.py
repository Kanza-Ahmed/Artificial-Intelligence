#Kinza Iftikhar
#BCS21016

#divisible by 7 and multiple of 5
print("Following numbers are the divisible by 7 and multiples of 5: \n")
for number in range(1500, 2701):
    if number%7==0 and number%5==0:
        print(number)

#temperature conversion
def celsius_to_farhrenheit(celsius):
    """Takes temperature in celsius and converts to Fahrenheit"""
    fahrenheit = (celsius * 9/5)+32
    return fahrenheit

def farhrenheit_to_celsius(fahrenheit):
    """Takes temperature in fahrenheit and converts to celsius """
    #f = (c * 9/5) + 32
    celsius = (fahrenheit - 32) * 5/9
    return celsius

x = farhrenheit_to_celsius(45)
print(f"Fahrenheit to Celsius: {x}")
y = celsius_to_farhrenheit(7)
print(f"Celsius to Fahrenheit: {y}")

#Guess a number
import random
our_number = random.randint(1, 9)

while True:
    users_guess = int(input("Guess a number between 1 to 9: "))
    if users_guess==our_number:
        print("Well guessed ! ")
        break
    else:
        print("Wrong Guess! Try Again")

#print the pattern
rows = 5
columns = 5
for i in range(rows):
    # nested loop
    for j in range(i):
        print("*", end=' ')
    print('')

rows = 5
b = 0
for i in range(rows, 0, -1):
    b += 1
    for j in range(1, i + 1):
        print("*", end=' ')
    print('\r')

#reverse the word
user_string=input("Enter a string you want to reverse! ")
print(user_string[::-1])

#no. of even and odd numbers
def count_even_numbers(series):
    """Counts even numbers in a series of numbers"""
    even_number=0
    odd_number=0
    for number in series:
        if number%2==0:
            even_number+=1
        else:
            odd_number +=1
    return even_number, odd_number

number_series =(1, 2, 3, 4, 5, 6, 7, 8, 9)  
x, y = count_even_numbers(number_series)
print(f"No of even numbers: {x}")
print(f"No of odd numbers: {y}")

#prints item and type
datalist = [1452, 11.32, 1+2j, True, 'w3resource', (0, -1), [5, 12], {"class":'V', "section":'A'}]

for data in datalist:
    print(f"The datatype of {data} is {type(data)}")

#print except 3 and 6
for number in range(0,7):
    if number==3 or number==6:
        continue
    else:
        print(number)

#accepts sequence of lines
user_string= ""
while True:
    new_string = input("Enter a line: ")
    if new_string:
        user_string+=new_string+ "\n"
    else:
        break        

print(user_string.lower())

#binary div by 5
def divisible_by_five(numbers):
    """Accepts a sequence of CSV binary numbers and returns a string of numbers that are divisible by 5"""
    number = numbers.split(',')
    for n in number:
        n_dec = int(n, 2)
        if n_dec % 5 == 0:
            print(n)


numbers = "0100, 0011, 1010, 1001, 1100, 1001"
divisible_by_five(numbers)

#calculate the number of digits and letters
string = input("Enter a string: ")
letter=0
digit = 0
for character in string:
    if character.isalpha():
        letter+=1
    elif character.isdigit():
        digit+=1 
    

print(f"The number of letters is: {letter}")
print(f"The number of digits is: {digit}")

