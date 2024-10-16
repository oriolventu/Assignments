# Exercise 1: FizzBuzz
    # 1. Write a FizzBuzz Function: Create a function fizzbuzz(n) that takes an integer n as a parameter.
    # 2. Implement FizzBuzz Logic: The function should print:
        # "Fizz" for multiples of 3
        # "Buzz" for multiples of 5
        # "FizzBuzz" for multiples of both 3 and 5
        # The number itself for other numbers
    # 3. Call the Function: Call the function for numbers 1 to 20.
    #

def fizzbuzz(n):
    for i in range (n, n + 1):
        if i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        else:
            print(i)

fizzbuzz(20) 

# Exercise 2: Basic Data Filtering
    # 1. Create a List of Mixed Data Types: Create a list that contains a mix of integers, strings, and floats.
    # 2. Filter the List: Use list comprehension to create a new list that contains only the integers from the original list.
    # 3. Print the New List: Output the filtered list of integers.

mixed_list = [7, 4, 'Manzana', 2.2, 'Ramon', 8.3]
mixed_list_2 = [mix for mix in mixed_list if isinstance(mix, int)] # 
mixed_list_2

# Exercise 3: Simple To-Do List
    # Create an Empty List: Start with an empty list called todo_list.
    # Define Functions:
        #  A function add_task(task) that adds a task to the list.
        #  A function show_tasks() that prints all tasks in the list.

todo_list = []

def add_task(task):
    todo_list.append(task)
    print(f'Task added: "{task}"')

def show_tasks():
    if not todo_list:
        print('No hay tareas')
    else: 
        print('Cosas por hacer:')
        for idx, task in enumerate(todo_list, start=1): 
            print(f"{idx}. {task}") 

# ponemos un par de ejemplos: 
add_task('comprar leche')
add_task('pasear al perro')

show_tasks()

# Exercise 4: Temperature Converter
    # 1. Define a Conversion Function: Write a function celsius_to_fahrenheit(celsius) that converts Celsius to Fahrenheit.
    # 2. Print the Result: Output the converted temperature for 22ºF, 46ºF, 51ºF and 76ºF.

def celsius_to_fahrenheit(celsius): 
    fahrenheit = (celsius * 9/5) + 32 # formula de celsius a fahrenheit 
    return fahrenheit

temperatura_celsius = [22, 46, 51, 76]

for temperatura in temperatura_celsius:
    temperatura_fahrenheit = celsius_to_fahrenheit(temperatura)
    print(f"{temperatura}°C es equivalente a {temperatura_fahrenheit:.2f}°F.")


    