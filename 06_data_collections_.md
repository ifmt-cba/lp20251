# Chapter 6: Data Collections

Welcome back! In the [previous chapter](05_iteration__loops__.md), we learned about **Iteration (Loops)**, which allows your program to repeat actions, like performing a calculation for every student or printing numbers in a sequence. This is great for doing something *to* multiple pieces of data, but how do we store and manage those multiple pieces of data *together* in the first place?

Imagine you need to keep track of a list of groceries you need to buy, or the names and phone numbers of your friends. You could store each item or number in a separate variable (`item1 = "milk"`, `item2 = "eggs"`, `friend1_name = "Alice"`, `friend1_phone = "555-1234"`), but this quickly becomes messy and unmanageable if you have more than a few items. How would you loop through a thousand separate variables?

This is where **Data Collections** come in. In programming, data collections (also known as data structures) are ways to store and organize groups of related data under a single name. They are crucial for handling lists of items, sets of properties, and other situations where you deal with more than just one or two isolated pieces of information.

In Python, two of the most common and useful built-in data collections for beginners are **Lists** and **Dictionaries**. You'll see these used extensively in `lista4.py`, as it focuses heavily on exercises that require managing groups of data.

Let's explore these two fundamental collection types.

## Lists: Ordered Sequences

Think of a **List** in Python like a shopping list, a todo list, or a list of student names. It's an ordered sequence of items. Each item in the list has a position, starting from 0.

Lists are defined using square brackets `[]`, with items separated by commas.

```python
# An empty list
shopping_list = []

# A list of strings (groceries)
shopping_list = ["bread", "milk", "eggs", "cheese"]

# A list of numbers (student grades)
grades = [85, 90, 78, 92]

# A list can even hold different types of data, although it's often best to keep items related
mixed_list = ["Alice", 25, True, 9.5]
```

You can access individual items in a list using their position, called an **index**. Remember that the first item is at index `0`, the second at index `1`, and so on.

```python
shopping_list = ["bread", "milk", "eggs", "cheese"]

print(shopping_list[0]) # Output: bread
print(shopping_list[2]) # Output: eggs

# You can also use negative indices to count from the end
print(shopping_list[-1]) # Output: cheese (the last item)
print(shopping_list[-2]) # Output: eggs (the second to last item)
```

Lists are **mutable**, meaning you can change, add, or remove items after the list is created.

```python
shopping_list = ["bread", "milk", "eggs", "cheese"]

# Change an item
shopping_list[1] = "yogurt"
print(shopping_list) # Output: ['bread', 'yogurt', 'eggs', 'cheese']

# Add an item to the end
shopping_list.append("fruit")
print(shopping_list) # Output: ['bread', 'yogurt', 'eggs', 'cheese', 'fruit']

# Remove an item by its value
shopping_list.remove("eggs")
print(shopping_list) # Output: ['bread', 'yogurt', 'cheese', 'fruit']

# Get the number of items in the list
print(len(shopping_list)) # Output: 4
```

Lists are frequently used with loops ([Chapter 5: Iteration (Loops)](05_iteration__loops__.md)) to process each item.

```python
grades = [85, 90, 78, 92]

# Calculate the sum of grades using a loop
total_grade = 0
for grade in grades:
    total_grade = total_grade + grade
    # Shorthand: total_grade += grade

print(f"Total grade: {total_grade}") # Output: Total grade: 345
```

Look at `q1` in `lista4.py`. It creates a list, fills it with numbers using a `for` loop, and then uses the list's `.index()` method (which can raise a `ValueError` if the item isn't found, hence the `try...except`) to find an item's position:

```python
# From lista4.py, q1 (simplified)
def q1():
    lista = [] # Start with an empty list
    # Use a loop to add 15 random numbers to the list
    for _ in range(15):
        lista.append(random.randrange(100)) # Add an item to the end
    print(lista) # Print the whole list

    numero = int(input_int('Digite um número a ser buscado: ',0,100))

    # Check if the number is in the list and find its position
    try:
        posicao = lista.index(numero) # Find the index of the number
        print(f'Localizado na posição: {posicao}')
    except ValueError: # If .index() doesn't find the number, it raises an error
        print(f'{numero} não localizado na lista')
```

This demonstrates creating a list and then performing actions (like adding items or searching) on it. `q2` also uses a list to store characters.

## Dictionaries: Key-Value Pairs

Think of a **Dictionary** in Python like a real-world dictionary or a phone book. Instead of using a numbered position (index) to find information, you use a **key** to look up a corresponding **value**. In a phone book, the name (key) gets you the phone number (value). In a dictionary, the word (key) gets you the definition (value).

Dictionaries are defined using curly braces `{}`. Each item is a `key: value` pair, and pairs are separated by commas.

```python
# An empty dictionary
empty_dict = {}

# A dictionary storing personal information
person = {"name": "Alice", "age": 25, "city": "New York"}

# A dictionary storing student grades for different subjects
student_grades = {"Math": 90, "Science": 85, "History": 78}
```

You access values in a dictionary using their keys, enclosed in square brackets `[]`.

```python
person = {"name": "Alice", "age": 25, "city": "New York"}

print(person["name"]) # Output: Alice
print(person["age"])  # Output: 25

# Trying to access a key that doesn't exist will cause an error (KeyError)
# print(person["job"]) # This would cause an error
```

You can add new key-value pairs or change the value for an existing key using the same square bracket notation.

```python
person = {"name": "Alice", "age": 25, "city": "New York"}

# Add a new key-value pair
person["job"] = "Engineer"
print(person) # Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'job': 'Engineer'}

# Change an existing value
person["age"] = 26
print(person) # Output: {'name': 'Alice', 'age': 26, 'city': 'New York', 'job': 'Engineer'}

# Get the number of key-value pairs
print(len(person)) # Output: 4
```

You can loop through dictionaries in various ways, commonly iterating through their keys, values, or both.

```python
student_grades = {"Math": 90, "Science": 85, "History": 78}

# Loop through keys
print("Subjects:")
for subject in student_grades.keys(): # or just 'for subject in student_grades:'
    print(subject)
# Output:
# Subjects:
# Math
# Science
# History

# Loop through values
print("\nGrades:")
for grade in student_grades.values():
    print(grade)
# Output:
# Grades:
# 90
# 85
# 78

# Loop through both keys and values
print("\nSubject Grades:")
for subject, grade in student_grades.items():
    print(f"{subject}: {grade}")
# Output:
# Subject Grades:
# Math: 90
# Science: 85
# History: 78
```

Dictionaries are excellent for storing information that has descriptive labels (keys) associated with values, like configuration settings, database records, or the properties of an object.

Look at `q5` in `lista4.py`. It uses dictionaries to represent individual student records (each student has a name, grades, media, situation) and then stores these student dictionaries in a list called `diario`.

```python
# From lista4.py, q5 (simplified structure)
def q5():
    diario = [] # This is a LIST to hold multiple student records

    # Loop to create records for 15 students
    for i in range(15):
        aluno = dict() # Create an empty DICTIONARY for ONE student
        # Store student data using keys and values
        aluno['nome'] = f'Aluno {i+1}' # Example name
        aluno['n1'] = random.randrange(0,11) # Example grade
        aluno['n2'] = random.randrange(0,11) # Example grade
        aluno['media'] = round((aluno['n1'] + aluno['n2'])/2,1)
        aluno['situacao'] = 'AP' if aluno['media']>=6 else 'RP' # Using conditional logic!

        diario.append(aluno) # Add the student DICTIONARY to the LIST

    # Now 'diario' is a list of dictionaries!
    # You can loop through the list to access each student's dictionary
    print("Example: Accessing data for the first student in the list")
    first_student = diario[0] # Get the first dictionary from the list
    print(f"Name: {first_student['nome']}") # Access value using key from the dictionary
    print(f"Media: {first_student['media']}") # Access another value
```

This simplified example from `q5` shows how lists and dictionaries can be combined: a list (`diario`) containing multiple dictionary items (`aluno`), where each dictionary represents one complex item (a student record). This is a very common and powerful way to structure data in programming.

## How Data Collections Fit in `lp20251`

`lista4.py` is dedicated to exercises that involve working with these data collections. The `qXX` functions ([Chapter 2: Exercise/Question (qXX Function)](02_exercise_question__qxx_function__.md)) in this file contain the specific code for creating, manipulating, and processing lists and dictionaries to solve the problems described in the exercise comments.

You'll use the [Exercise Runner](01_exercise_runner_.md) ([Chapter 1: Exercise Runner](01_exercise_runner_.md)) at the end of `lista4.py` (as described in [Chapter 3: Exercise List File (listaX.py)](03_exercise_list_file__listax_py__.md)) to select and run the `qXX` function corresponding to the exercise you want to work on. The code inside that chosen `qXX` function will then use lists or dictionaries (often along with loops and conditional logic) to accomplish its task.

Here's a simplified sequence diagram showing how a `qXX` function might interact with a list:

```mermaid
sequenceDiagram
    participant User
    participant Exercise Runner
    participant qXX Function
    participant List Object

    User->>Exercise Runner: Runs lista4.py
    Exercise Runner->>User: Ask for exercise number
    User->>Exercise Runner: Type number (e.g., 1)
    Exercise Runner->>qXX Function: Call q1()
    qXX Function->>List Object: Create an empty List []
    Loop qXX Function->>List Object: Call append() method
    qXX Function->>List Object: Add an item to the list
    Note over qXX Function: (Repeats inside a loop)
    qXX Function->>List Object: Call index() method (or other list operations)
    List Object-->>qXX Function: Return result (e.g., position or error)
    qXX Function->>User: (May print output)
    qXX Function-->>Exercise Runner: Function finishes
    Exercise Runner-->>User: Program finishes
```

This diagram shows that the `qXX` function directs the actions, using the List (or Dictionary) object to store and manage the actual data collection.

## Internal Implementation (Simplified)

At a high level, when you create a list or a dictionary, Python sets aside a space in the computer's memory to hold the collection.

*   For a **List**, Python keeps track of the items in a specific order. When you access an item by its index (like `my_list[0]`), Python knows exactly where the data for that item is stored because of its position in the internal sequence. When you `append` an item, Python adds it to the end and updates its internal record of the order.
*   For a **Dictionary**, Python uses a clever technique (often called hashing) to quickly find where a value is stored based on its key, without having to look through the items in order. This is why accessing items by key is very fast, even in large dictionaries, but dictionaries don't inherently maintain the order you added the items (though in modern Python versions, they remember the order of insertion).

You don't need to understand the deep technical details of how Python manages memory for these collections right now. The important concept is the difference in how you access data: by **ordered position** (index) for Lists, and by **descriptive label** (key) for Dictionaries.

## Conclusion

In this chapter, you learned about **Data Collections**, essential structures for grouping and managing multiple pieces of data in your programs. You explored two fundamental Python collections:

*   **Lists**, which are ordered sequences of items, accessed by index, and are mutable.
*   **Dictionaries**, which are unordered collections of key-value pairs, accessed by key, and are also mutable.

You saw how these collections are used within the `qXX` functions in `lista4.py` to handle tasks involving multiple data points, and how they can even be combined (like a list of dictionaries) to represent more complex data structures.

Understanding lists and dictionaries is vital, as they are used in almost every non-trivial program to organize information. In the next chapter, you'll learn about creating functions to help ensure that the input you get from a user is valid, a process that might involve checking input against values stored in collections.

[Next Chapter: Input Validation Functions](07_input_validation_functions_.md)

---

<sub><sup>Generated by [AI Codebase Knowledge Builder](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge).</sup></sub> <sub><sup>**References**: [[1]](https://github.com/ifmt-cba/lp20251/blob/2353bfea16374996818c71298b449a71933ddc9f/lista4.py)</sup></sub>