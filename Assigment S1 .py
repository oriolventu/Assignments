# Exercise 1: Write a Python program that prints a greeting message, such as "Hello, Python!".
print('Hello, Python!')

# Exercise 2: Create a program that:
                # Defines two variables, a and b, with numerical values.
                # Prints their sum, difference, product, and quotient.
a = 7 
b = 5

print( a + b)
print( a - b)
print( a * b)
print( a/b )

# Exercise 3: Define a variable name and assign it your name. Write a program that prints a message saying "Hello, [name]!" where [name] is the value of the variable.
name = 'Oriol'
print('Hello,', name)

# Exercise 4: Create a list called universities with at least five different university names.
                # Print the entire list.
                # Print the first and last university in the list.

universities = ['ESADE', 'UAB', 'UIB', 'UOC', 'IE']
universities
universities[0], universities [4]

# Exercise 5: 
                # Create a dictionary called student with keys: name, age, and grade, and assign appropriate values to each key.
                # Write a program that prints each key-value pair in the dictionary.

student = {'name':'Oriol', 'Age': 23, 'Grade': 10}
print("Name:", student["name"])
print("Age:", student["Age"])
print("Grade:", student["Grade"])


# Exercise 6: Tuples 
                # Define a tuple called coordinates with two values representing a point in 2D space (e.g., (x, y)).
                # Print the value of coordinates and access each element by its index.
coordinates = (4, 3)
print(coordinates)
print(coordinates[0], coordinates[1])


# Exercise 7: Sets
                # Create a set called colors with the values: "red", "green", "blue".
                # Add another color to the set.
                # Try adding a duplicate color and observe what happens.
                # Print the set and remove one color from it.
                # Create another set named light_colors and merge colors and light_colors.

colors = {'red', 'green', 'blue'}
colors.add('brown')
colors.add('green')
colors
colors.remove('red')
colors

light_colors = {"light blue", "light green"}
merged_colors = colors.union(light_colors) # .union em serveix per unir els dos sets
merged_colors

# Exercise 8: Conditional Statements
                # Write a program that:
                    # Takes an input number from the user.
                    # Checks if the number is positive, negative, or zero.
                    # Prints an appropriate message based on the result.

number = 5

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")



# Exercise 9: For Loop 
                # Create a list of numbers from 1 to 5.
                # Use a for loop to iterate through the list and print each number.

lista_numeros = [1, 2, 3, 4, 5]

for number in lista_numeros:
    print(number)
else:
    print('Loop Finished')

# Exercise 10: While Loop
                # Write a program that uses a while loop to print numbers from 1 to 5
                # Ensure the loop terminates correctly

counter = 1

while counter <= 5: 
    print(counter)
    counter += 1 
else: 
    print('Loop terminates correctly')


# Exercise 11: Match Statement (Python 3.10+)
                # Asks the user to input a grade (e.g., "A", "B", "C", "D", or "F").
                   #Use a match statement to print a corresponding message for each grade:
                        #"A": "Excellent!"
                        #"B": "Good job!"
                        #"C": "Fair."
                        # "D": "Needs improvement."
                        # "F": "Failing."
                            #Handle invalid input by printing a default message.

command = 'A'

match command:
    case 'A':
        print("Excellent!")
    case 'B':
        print("Good job!")
    case 'C':
        print('Fair')
    case 'D':
        print('Needs improvement')
    case 'F':
        print('Failing')
    case _:
        print('Invalid input. Please enter A, B, C, D, or F.')
 


# Exercise 12: Define a Function
                # Write a function called greet that takes a name as an argument and prints "Hello, [name]!".
                # Call the function with your own name.

def greet(name):
    print(f"Hello, {name}!")

greet('Oriol')

# Exercise 13: Function with Return Value
                # Define a function called square that takes a number as an argument and returns its square.
                # Print the result of calling this function with different numbers.

def square(number):
    return number ** 2

result = square(7)
result

# Exercise 14: Function with Default Parameters
                # Write a function called multiply that takes two parameters, a and b, and returns their product. Set a default value of 1 for the parameter b.
                # Test the function with and without providing the second argument

def multiply(a, b = 1):
    return a * b

resultado_1 = multiply(3) # resultat dona 3 perque tenim b = 1 com a predeterminat
resultado_1

resultado_2 = multiply(3, 8) # en aquest cas hem dit que b = 8 enlloc de 1. pero ho hem hagut d'especificar, sinó ens agafaria b = 1 
resultado_2


# Exercise 15: List Comprehension
                # Create a list of numbers from 1 to 10.
                # Use list comprehension to create a new list that contains the squares of these numbers.
                # Print the new list.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squares = [n ** 2 for n in numeros]
squares

# Exercise 16: Nested Data Structures
                # Create a dictionary where the keys are names of students and the values are lists of their grades
                # Write a function that takes the dictionary and prints the average grade for each student.

notas = {'Marc': [6.5, 4, 7], 
         'Pol': [8, 9.5, 10], 
         'Enric': [2.3, 5, 6.8]}

def nota_media(notas):
    for student, grades_list in notas.items():
        average = sum(grades_list) / len(grades_list)

nota_media(notas)

# Exercise 17: Simple Calculator
                # Write a program that:
                    # Defines a function calculate which takes three parameters: two numbers and an operator (+, -, *, /).
                    # Performs the operation and returns the result.
                    # Ask the user for the two numbers and the operator, then call the function and print the result.

def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division entre cero"
    else:
        return "Error: Invalid operator."

# ejemplo 
num1 = 8
num2 = 5
operator = '*'

resultado = calculate(num1, num2, operator)
resultado
