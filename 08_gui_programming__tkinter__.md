# Chapter 8: GUI Programming (Tkinter)

Welcome back! In the [previous chapter](07_input_validation_functions_.md), we learned about **Input Validation Functions**, which help us get reliable numerical input from the user, ensuring it's the correct type and within a valid range, all while working with text in the console.

So far, all our programs have been text-based. We input text on a command line and get text output back. This is functional, but wouldn't it be nice if our programs had visual interfaces, with windows, buttons you can click, and boxes where you can type?

This is where **GUI Programming** comes in! GUI stands for Graphical User Interface. Instead of just talking to your computer through text in a console, a GUI lets you interact using graphical elements like windows, buttons, text fields, checkboxes, and more. It's like building a small control panel for your program instead of having a text-based conversation with it.

In Python, a popular library for creating simple GUIs is called **Tkinter**. It's usually included with Python, so you don't need to install anything extra! Tkinter is used in some exercises in `lista2.py` (specifically `q12` and `q13`) to give them a graphical feel instead of just using console input/output.

Let's explore the basics of Tkinter to understand how these exercises create visual windows.

## What is a GUI? (Beyond the Console)

A Graphical User Interface (GUI) provides visual elements that users interact with directly.

*   **Console Program:**
    *   User types commands/input.
    *   Program prints text output.
    *   Example: `input('Enter your name: ')` followed by `print(f'Hello, {name}!')`.
*   **GUI Program:**
    *   Program opens a **window**.
    *   The window contains **widgets** (buttons, text fields, labels).
    *   User clicks buttons, types in text fields, etc.
    *   Program responds visually (shows a message in a box, changes text on the screen) and might perform actions based on user interaction.
    *   Example: A window with a label "Enter your name:", a text box to type in, and a "Submit" button. When the button is clicked, a message box pops up saying "Hello, [name you typed]!".

This is much more user-friendly for many types of applications.

## Tkinter Basics: The Window and the Event Loop

To start building a GUI with Tkinter, you need a main window.

1.  **Import:** First, you import the necessary parts of the Tkinter library. We usually import `tkinter` itself and sometimes specific widgets or helper modules like `messagebox`.

    ```python
    import tkinter as tk
    from tkinter import messagebox # Used for pop-up messages
    # Or specifically import things you need:
    # from tkinter import Tk, Label, Button, Entry
    ```

    The line `import tkinter as tk` is a common convention, allowing you to refer to Tkinter functions using `tk.` prefix (e.g., `tk.Tk()`). The `from tkinter import ...` style lets you use names like `Tk`, `Label`, `messagebox` directly without the `tk.` prefix. Both styles are used. `lista2.py` uses the `from tkinter import ...` style.

2.  **Create the Main Window:** This creates the basic window object.

    ```python
    # Create the main window
    window = tk.Tk() # Or just Tk() if you used 'from tkinter import Tk'
    window.title("My First GUI") # Give the window a title
    ```

    `window = tk.Tk()` creates the top-level window for your application.

3.  **Start the Event Loop:** This is the most important step after creating the window and adding all your widgets. The `mainloop()` method starts Tkinter's event loop.

    ```python
    # Keep the window open and listen for events
    window.mainloop()
    ```

    Think of `mainloop()` as the program entering a waiting state. It sits there, displaying the window, and constantly *listens* for events: mouse clicks, key presses, window resizing, etc. When an event occurs, it figures out which widget was involved and runs the corresponding code you've told it to run (like calling a function when a button is clicked). Without `mainloop()`, the window would just pop up and disappear immediately as the program finishes.

Any code you write *after* `window.mainloop()` will only run *after* the GUI window is closed.

## Widgets: The Building Blocks

Widgets are the interactive elements you place inside a window. Common widgets include:

*   `Label`: Displays text or images.
*   `Entry`: A single-line text box for user input.
*   `Button`: A clickable button that can trigger an action.
*   `Frame`: A container to group and organize other widgets.
*   `messagebox`: Not a widget *inside* the window, but a separate pop-up window for messages (like errors or information).

You create widgets by creating an instance of the widget class and usually passing the window (or parent widget) it belongs to as the first argument.

```python
# Create a label widget
my_label = tk.Label(window, text="Hello, GUI!")

# Create an entry widget for text input
my_entry = tk.Entry(window, width=20) # width is in text characters

# Create a button widget
my_button = tk.Button(window, text="Click Me")
```

Creating a widget isn't enough; you also need to tell Tkinter *where* to place it in the window. This is done using **Layout Managers**.

## Layout: Arranging Widgets (`grid`)

Layout managers determine the position and size of widgets within their parent window or frame. Tkinter has a few (pack, grid, place). For beginners, `grid` is often intuitive as it arranges widgets in a grid of rows and columns, similar to a spreadsheet.

You use the `.grid()` method on a widget to place it.

```python
my_label = tk.Label(window, text="Hello, GUI!")
my_entry = tk.Entry(window, width=20)
my_button = tk.Button(window, text="Click Me")

# Place the widgets using grid
my_label.grid(row=0, column=0) # Put label in the first row (0), first column (0)
my_entry.grid(row=0, column=1) # Put entry in the first row (0), second column (1)
my_button.grid(row=1, column=0, columnspan=2) # Put button in the second row (1), spanning 2 columns
```

*   `row`: Specifies the row number (starts from 0).
*   `column`: Specifies the column number (starts from 0).
*   `columnspan`: Makes a widget span across multiple columns.
*   `sticky`: Used to align the widget within its grid cell (e.g., `'W'` for West/left, `'E'` for East/right, `'N'` for North/top, `'S'` for South/bottom, `'NSEW'` to fill the cell).

You need to call a layout method (`.grid()`, `.pack()`, or `.place()`) for *every* widget you want to appear in the window.

## Event Handling: Making Widgets Do Things (`command`)

A GUI program is driven by **events**. Nothing happens until the user (or the system) triggers an event. The most common event you'll deal with is a button click. You make a button *do* something by linking its `command` property to a Python function.

The function you link to a button's `command` should *not* take any arguments and should be defined *before* you create the button.

```python
def on_button_click():
    print("Button clicked!")
    # This function runs whenever the button is clicked

my_button = tk.Button(window, text="Click Me", command=on_button_click)
my_button.grid(row=1, column=0)

# Important: The function name is passed WITHOUT parentheses ()
# If you write command=on_button_click(), the function will run immediately
# when the button is CREATED, not when it's clicked!
```

When the button is clicked, Tkinter's `mainloop` detects the click event on that button and automatically calls the function assigned to its `command`.

## Tkinter in `lista2.py` (`q12`, `q13`)

Now let's see how these concepts appear in `lista2.py`. Exercises `q12` and `q13` are examples where the standard console input/output is replaced by a simple Tkinter GUI. This means when you run `lista2.py` and select `12` or `13` in the [Exercise Runner](01_exercise_runner_.md), a graphical window will pop up instead of the console asking for input.

Let's look at a simplified structure of `q12` (you can compare it to the full code provided in the context):

```python
# From lista2.py, q12 (Simplified Tkinter parts)
def q12():
    # Function that runs when the button is clicked
    def show_idade():
        # 1. Get text from the Entry widget
        idade_str = txt_idade.get() # Use .get() to retrieve text

        # 2. Validate/Convert input (similar to input validation chapter!)
        try:
            idade = int(idade_str) # Try converting to integer
            msg = '' # Message to display

            # 3. Apply conditional logic based on age
            if (idade < 18):
                msg = 'Menor de Idade'
            elif (idade > 65):
                msg = 'Maior de 65 anos'
            else:
                msg = 'Maior de Idade'

            # 4. Display result in a graphical message box
            messagebox.showinfo(
                title='Situação da Idade!',
                message=f'{msg}')

        except ValueError:
            # Handle non-integer input gracefully
            messagebox.showerror("Input Error", "Please enter a valid integer for age.")

        # 5. Clear the Entry field for the next input (optional but good UX)
        txt_idade.delete(0, tk.END) # tk.END means delete up to the end
        txt_idade.focus() # Put cursor back in the field

    # --- GUI Setup ---
    window = tk.Tk() # 1. Create the main window
    window.title('Questão 12')
    window.config(padx=10, pady=10) # Add some padding around content

    # 2. Create widgets
    lbl_idade = tk.Label(window, text='Idade:') # Label
    # Entry widget - Note the 'global' in original q12
    # 'global txt_idade' is needed inside show_idade to modify
    # the txt_idade variable defined here. A slightly better way
    # in larger apps is to pass widgets as arguments or use classes,
    # but 'global' works for simple examples like this.
    global txt_idade # Makes this variable accessible in show_idade
    txt_idade = tk.Entry(window, width=4)

    # Button widget - linked to the show_idade function
    btn_ok = tk.Button(window, text="OK", width=5, command=show_idade)

    # 3. Arrange widgets using grid
    lbl_idade.grid(row=0, column=0)
    txt_idade.grid(row=0, column=1, columnspan=2, sticky='W')
    btn_ok.grid(row=1, column=0, columnspan=3)

    txt_idade.focus() # Put cursor in the entry field when window opens

    # 4. Start the event loop - keeps window open and responsive
    window.mainloop()
```

**Explanation of `q12`'s Tkinter usage:**

1.  It imports necessary Tkinter components.
2.  It defines a function `show_idade()` that contains the core logic: getting input from the text field (`txt_idade.get()`), performing calculations/conditional checks ([Chapter 4: Conditional Logic](04_conditional_logic_.md)), and showing the result. It also includes basic error handling for non-integer input using `try...except` (inspired by [Chapter 7: Input Validation Functions](07_input_validation_functions_.md)).
3.  It creates the main `window` object.
4.  It creates `Label`, `Entry`, and `Button` widgets, associating them with the `window`. The `Entry` widget (`txt_idade`) is declared `global` so the `show_idade` function can access it.
5.  The `btn_ok` button's `command` is set to the `show_idade` function, so clicking the button runs that code.
6.  Widgets are placed using the `.grid()` layout manager.
7.  `window.mainloop()` is called to display the window and start listening for events (like the button click).

`q13` follows a very similar pattern but uses multiple `Entry` widgets for name and two grades, calculates a media, applies conditional logic for student status, and displays the result in a `messagebox`.

Instead of the program running sequentially and finishing after printing output, Tkinter programs are *interactive*. They wait for user actions (events) and respond accordingly, running small pieces of code (like the `show_idade` function) only when triggered by an event (like clicking the button).

## How Tkinter Works Internally (Simplified)

When you run a Tkinter application and call `window.mainloop()`, here's a simplified idea of what happens:

1.  **Setup:** Tkinter communicates with your computer's operating system (OS). It tells the OS to create a window with specific properties (title, size, etc.).
2.  **Draw Widgets:** Tkinter calculates where each widget should go based on the layout managers (`grid`, `pack`, etc.) and tells the OS to draw them inside the window.
3.  **Enter Event Loop:** The program enters the `mainloop()`. It's now mostly idle, consuming very little processing power, waiting.
4.  **Listen for Events:** The `mainloop` constantly listens for messages (events) from the OS windowing system. "The mouse was clicked at these coordinates," "A key was pressed," "The window was resized," "The 'OK' button was clicked."
5.  **Dispatch Event:** When an event occurs, the `mainloop` identifies which widget received the event (e.g., `btn_ok`).
6.  **Call Command:** If that widget has a `command` linked to it for that type of event (like a button having a function for a click), the `mainloop` *pauses* its listening briefly and calls the linked Python function (e.g., `show_idade()`).
7.  **Execute Function:** Your function (`show_idade`) runs. It might get data from `Entry` widgets (`.get()`), perform calculations, update `Label` widgets (`.config(text=...)`), or show a pop-up `messagebox`.
8.  **Update Display:** If your function changed anything visual (like updating a label or showing a message box), Tkinter tells the OS to redraw parts of the window.
9.  **Resume Listening:** Once your function finishes, the `mainloop` resumes listening for the next event.

This cycle continues until the window is closed, which signals the `mainloop` to finish, and the program exits the loop and terminates.

Here's a simple sequence diagram for the button click flow:

```mermaid
sequenceDiagram
    participant User
    participant OS Window System
    participant Tkinter Mainloop
    participant Button Widget
    participant Command Function (e.g., show_idade)

    User->>OS Window System: Clicks the button visually
    OS Window System->>Tkinter Mainloop: Sends "Button Clicked" event message
    Tkinter Mainloop->>Button Widget: Identify the widget clicked
    Button Widget->>Tkinter Mainloop: Report its linked command function
    Tkinter Mainloop->>Command Function: Call the linked function (show_idade())
    Command Function->>Command Function: Perform logic (get entry text, calculate)
    Command Function->>OS Window System: Request to show Message Box (via Tkinter)
    OS Window System->>User: Display Message Box
    User->>OS Window System: Clicks OK on Message Box
    OS Window System->>Command Function: Report Message Box closed (via Tkinter)
    Command Function-->>Tkinter Mainloop: Function finishes
    Tkinter Mainloop->>Tkinter Mainloop: Resume listening for events
```

This event-driven model is different from the sequential console programs we've seen so far and is fundamental to how most modern graphical applications work.

## Conclusion

In this chapter, you were introduced to **GUI Programming** using the **Tkinter** library. You learned how it allows you to create visual windows with interactive elements called **widgets** (like `Label`, `Entry`, `Button`). You saw how to arrange these widgets using **layout managers** like `grid` and how to make buttons trigger actions by linking them to functions using the `command` option.

You also got a peek into the **event loop** (`mainloop`), which is the core of a GUI application, listening for user interactions and calling the appropriate code in response. This interactive, event-driven approach is different from the sequential execution of simple console programs.

Exercises like `q12` and `q13` in `lista2.py` use these Tkinter concepts to provide a more visual way to interact with the program, building on concepts like conditional logic ([Chapter 4: Conditional Logic](04_conditional_logic_.md)) and input handling (now done through `Entry` widgets and processed in button command functions, often with validation logic similar to [Chapter 7: Input Validation Functions](07_input_validation_functions_.md)).

This concludes our exploration of the core concepts in the `lp20251` project's early exercises. You now have a foundation to understand the structure of the exercise files (`listaX.py`), how to run specific exercises (`qXX` functions using the [Exercise Runner](01_exercise_runner_.md)), and the fundamental programming ideas they teach (conditional logic, loops, data collections, input validation, and basic GUI).

---

<sub><sup>Generated by [AI Codebase Knowledge Builder](https://github.com/The-Pocket/Tutorial-Codebase-Knowledge).</sup></sub> <sub><sup>**References**: [[1]](https://github.com/ifmt-cba/lp20251/blob/2353bfea16374996818c71298b449a71933ddc9f/lista2.py)</sup></sub>