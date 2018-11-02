# function design recipe

### six steps
1. Examples
    * what should your function do?
    * Type a couple of example calls
    * Pick a name (often a verb or verb phrase): "what does your function do?"
2. Type Contract
    * What are the parameter types?
    * What type of value is returned?
3. Header
    * Pick meaningful parameter names
4. Descriptioin
    * Mention every parameter in your desciption
    * Describe the return value
5. Body
    * Write the body of your function
6. Test
    * run the examples

```python
def convert_to_celsius(fahrenheit):
    ''' (number) -> number

    Return the number of Celsius degrees equivalent to fahrenheit degrees.

    >>> convert_to_celsius(32)
    0
    >>> convert_to_celsius(212)
    100
    '''

    return (fahrenheit - 32) * 5 / 9
```

* reuse functions
* scope (week3)

### using doctest
```python
import doctest
doctest.testmod()
```

### main
* every module has a variable named `__main__`
* use if statement to check whether a module is the main one being executed
* (as opposed to being imported by another module)
```python
if __name__ == '__main__':
    import doctest
    doctest.testmod()
```

------------
reference:
* week2: coursera lecture by University of Toronto - [Learn to Program: The Fundamentals](https://www.coursera.org/learn/learn-to-program)
* week2: coursera lecture by University of Toronto - [Learn to Program: Crafting Quality Code](https://www.coursera.org/learn/program-code)
