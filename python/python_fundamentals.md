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
* count
    * `'syzygy'.count('y')`

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

### while
```python
while expression:
    statements
```
* the statements in the code are excuted if the expression is True
* it excutes again and again until the expression is False
* using lazy evaluation (when the first operand is False, the second is not evaluated:
    ```python
    i = 0
    s = 'xyz'
    while i < len(s) and not (s[i] in 'aeiouAEIOU'):
        print(s[i])
        i = i + 1
    # without the first check it throws IndexError
    ```

### Comments
use `#` (number sign) character

### Type list
`[expr1, expr2, ..., exprN]`
`grades = [80, 90, 80]`
* List Operations
    * index `grades[0]`
    * slice `grades[0:2]`
    * in `90 in gradex`
    * `len(list)`, `min(list)`, `max(list)`, `sum(list)`
* Types of list elements
    * may be of any type
    * can also contain elements of more than one type
* for loops over list
    ```python
    for grade in grades:
        print(grade)
    ```
* list Mothods
    * dir(list)
    * `list.append(object)`
    * `list.extend(list)`
    * `list.pop([index])` Remove the item at the given index (default: at the end)
    * `list.remove(object)` Remove the first occurrence of the object (error if not there)
    * `list.reverse()`
    * `list.sort()`
    * `list.insert(int, object)`
    * `list.count(object)`
    * `list.index(object)` Return the index of first occurrence (error if not there)

### Mutability Aliasing
* mutable: they can be modified
* immutable: they cannot be modified (str, int, float, bool)
* aliasing: refers to the same object
    
### range
`range([start, ] stop[, step]):` 
* stop value is not included
```python
for i in range(10):
    print(i)
```

### Nested Lists
`grades = [['a1', 80], ['a2', 90]]`
`grades[0]`: sublist ['a1', 80]
`grades[0][0]`: 'a1'


### Reading Files
[Reading Files](https://d3c33hcgiwev3.cloudfront.net/_f260744b4347776fd3cd60cf25e73901_read_files.html?Expires=1541116800&Signature=iOv1-S239tZmsqTTt1MKm5dV3V~f3GVTcU-aA6nj9n1pfjp1-DbojuAYklRM9h6Aa8hqNABHVtb68wZ62ZZtNKI3nOD2LNl1zTIoTkC35LBXZOtsKEjIChZYdkksLxJi~xtmuFJk94WPug~mUnUEWIJS8g1m5ysy3FvNs6T-aEs_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)
* `open(filename, mode)`
    * mode: 'r', 'w', 'a'
    * ex) `flanders_file = open('fields.txt', 'r')`
* `flanders_file.close()`
* read
    * `readline()`: 
        * read and return the next line from the file (include the newline character)
        * Return the empty string if there are no more lines in the file
    * `readlines()`
        * read and return all lines in a file in a list
        * includes the newline character
    * `read()`
        * read the whole file as a single string

### Write Files
* `file.write(str)`
* file dialogs
    * Module tkinter 
    ```python
    import tkinter.filedialog
    from_filename = tkinter.filedialog.askopenfilename()
    to_filename = tkinter.filedialog.asksavesasfilename()
    ```
* example
```python
to_file = open(to_filename, 'w')
to_file.write('Copy\n')
to_file.write(contents)
to_file.close()
```

### Tuples
* immutable sequences : cannot be modified
* `tup = ('a', 3, -0.2)`
* index and slice as list
    * `tup[0]`
    * `tup[:2]`
* cannot be modified `tup[0] = 'b'` gives an error
* possible mothods: check `dir(tuple)`
* `for item in tup:`, `len(tup)`, `for i in range(len(tup)):`


### Type dict
* dictionary
* mutable, unordered, can have keys of different types
* `{key1: value1, key2: value2, ..., keyN: valueN}`
* empty dict `d = {}`
* keys must be unique, immutable
    * `d[[1, 2]] = 'banana'` gives an error
    * `d[(1, 2)] = 'banana'` is okay
* operations
    * `object in dict` (`'A1' in asn_to_grade`)
    * `len(dict)` returns number of keys in dict
    * `del dict[key]` (`del asn_to_grade['A1']`)
    * `dick[key] = value` add the key value pair or update the value for the key
---------
reference:
* coursera lecture by University of Toronto - [Learn to Program: The Fundamentals](https://www.coursera.org/learn/learn-to-program)
* [python visualizer](http://pythontutor.com/visualize.html#mode=display)

countinue from week5
