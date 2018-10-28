# python fundamentals

### python as a calculator
* +, -, *
* `**`  : exponentiation (`2 ** 5` is `32`)
* `/`   : division  (`9 / 2` is `4.5`)
* `//`  : integer division (`9 // 2` is `4`)
* `%`   : modulo, remainder (`9 % 2` is `1`)

* Arithmetic Operator Precedence
    * `**`  highest
    * `-`(negation)
    * `*`, `/`, `//`, `%`
    * `+`, `-`(subtraction) lowest

### python and computer memory
* A value has a memory address
* A variable contains a memory address
* A variable refers to a value
* A variable points to a value
* examples:
    * Value `8.5` has memory address `id34`
    * Variable `shoe_size` contains memory address `id34`
    * The value of `shoe_size` is `8.5`
    * `shoe_size` refers to value `8.5`
    * `shoe_size` points to value `8.5`

### Variables
1. Evaluate the expression. This produces a memory address.
2. Store the memory address in the variable

### builtin Functions
* `dir(__builtins__)` , `dir(str)`
* `help(abs)`: display the docstring from the function definition

### defining Functions
```python
def function_name(parameters):
    body
```
```python
def f(x):
    return x ** 2
```
* return statement
    1. Evaluate the expression. This produces a memory address.
    2. Pass back that memory address to the caller. Exit the function
* functions Calls (`function_name(arguments)`)
    1. Evaluate the arguments to produce memory addresses.
    2. Store those memory addresses in the corresponding parameters.
    3. Execute the body of the function.

### Type str
* string literal: sequence of characters
* use single quotes(') or double quotes(")
* cannot change a str
* Escape Sequences(\)
    * `'wow, you\'re dripping wet.'`
    * `"wow, you're dripping wet."`
* string operators
    * `str1 + str2`: concatenate
    * `str1 * int1` or `int1 * str1`: concatenate int1 copies of str1
    * `==`, `!=`, `<`, `>`, `<=`, `>=`, `in`, `len(s)`
* indexing and slicing
    * `s[0]`: the first, `s[-1]`: the last letter
    * `s[0:5]` gives substring
    * `s[0:len(s)]` means `s[:]`
* looping
    * `for char in s:`  (s is a str)

### Input Output
* print
    * triple-quoted string: can span multiple lines
    * Excape Sequences
        * `\n`, `\t`, `\\` (backslash \), `\'`, `\"`
    ```python
    print("hello")
    print(3 + 8 - 5)            # evalute the expression and display the result
    print("hello", "there")     # space is inserted in between
    print(''' How
    are
    you?''')                    # triple-quoted string
    ```
* input: prompts the user to enter some input, returns the input as string
    ```python
    name = input("What is your name? ")
    ```

### Booleans
* Type `bool`: `True` or `False`
* Comparison operators:
    * `<`, `>`, `==`, `>=`, `<=` ,`!=`
* Logical operators
    * `not`, `and`, `or` in the Precedence order

### converting between types
* `str`: value to string, example `str(47.2)`
* `int`: string with only digits, float to int 
    * `int('123')` or `int(-99.9)`
    * `int('99.9')` does not work since it contains '.'
* `float`: string with digits with one or zero decimal points (possibly '-'), int to float
    * `float('-43.2')`
    * `float(4)`
    * `float(-9.9.9)` : ValueError


### Import
* module: a file containing function definitions and other statements
* `import mudule_name`
* `module_name.function_name`

### if
```python
if expression1:
    body
[elif expression2:
    body2]
[else:
    bodyN]
```
```python
def report_status(scheduled_time, estimated_time):
    """ (float, float) -> str """
    if scheduled_time == estimated_time:
        return 'on time'
    elif scheduled_time > estimated_time:
        return 'early'
    else:
        return 'delayed'
```
```python
def is_even(num):
    """ (int) -> bool
    Return whether num is even.
    """

    return num % 2 == 0
```

#### None
* NoneType
* when a function body ends without having executed a return statement,
 the function returns value None.




---------
reference:
* coursera lecture by University of Toronto - [Learn to Program: The Fundamentals](https://www.coursera.org/learn/learn-to-program)
* [python visualizer](http://pythontutor.com/visualize.html#mode=display)

countinue from week5
