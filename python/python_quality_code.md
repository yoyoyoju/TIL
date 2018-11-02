### custom class
* example class:
    * name of the class: WordplayStr
    * based on the `str` class (it is a subclass of `str`)
    ```python
    class WordplayStr(str):

        def same_start_and_end(self):
            """ (WordplayStr) -> bool
            Return whether self starts and ends with the same letter.

            >>> s = WordplayStr('abracadabra')
            >>> s.same_start_and_end()
            True
            >>> s = WordplayStr('canoe')
            >>> s.same_start_and_end()
            False
            """

            return self[0] == self[-1]


    if __name__ == '__main__':
        import doctest
        doctest.testmod()
    ```
* methods
    * the first argument is always self
    ```python
    def methodname(self, more_param):
        # body
        return True
    ```
* method `__init__`
    * called to initialize an object
    * creates instance variables that belongs to the object
    ```python
    def __init__(self, input_number):
    """ (ExampleClass, int) -> NoneType
    An ExampleClass with an input_number.
    >>> example = ExampleClass(5)
    >>> example.input_number
    5
    """
    self.input_number = input_number
    ```
* special Methods
    * All classes are built on an existing class called `object`
    * `object` has many special (or magic) methods
    * to see the list: `dir(object)`
    * example: `__eq__`
    ```python
    def __eq__(self, other):
        """ (ExampleClass, ExampleClass) -> bool
        Return True iff this ExampleClass has the same input_number as other.
        >>> ex1 = ExampleClass(1)
        >>> ex2 = ExampleClass(1)
        >>> ex1 == ex2
        True
        """
        return self.input_number == other.input_number
    ```
    * example: `__str__`
        * `print` calls the `__str__` to print
    ```python
    def __str__(self):
        """ (ExampleClass) -> str
        Return a string representation of this ExampleClass
        >>> ex1 = ExampleClass(1)
        >>> ex1.__str__()
        example1
        """
        return 'example' + str(input_number)
    ```

### Method str format
* `str.format` uses placeholders 
* `{0}` correspondes with the first argumnet, and so on
`'{0} and {1} and {2}'.format(1,2,3)`

### Unittest
* import unittest and the module to test
* write separate methods for each test. In each method,
    * write a call on the function being tested,
    * call `self.assertEqual(...)` to compare the actual result to the expected
* to test
    * call `unittest.main()`
* Typically,
    * one TestCase subclass for each function we want to test
    * one test method for each function call (the name starting with 'test')
* when the function mutates things (such as list), check the original (not only the return)
```python
# example
import unittest
import divisors

class TestDivisors(unittest.TestCase):  # TestCase subclass to test divisors
    """Example unittest test methods for get_divisors."""

    def test_divisors_example_1(self):
        """Test get_divisors with 8 and [1, 2, 3]."""
        actual = divisors.get_divisors(8, [1, 2, 3])
        expected = [1, 2]
        self.assertEqual(expected, actual)

    def test_divisors_example_2(self):
        """Test get_divisors with 4 and [-2, 0, 2]."""
        actual = divisors.get_divisors(4, [-2, 0, 2])
        expected = [-2, 2]
        self.assertEqual(expected, actual)
```

### Choosing test cases
* Size (for collections: str, list, tuple, dict)
    * empty collection
    * with 1 item
    * smallest interesting case
    * with several items
* Dichotomies (consider your situation)
    * For example:
        * vowels/non-vowels
        * even/odd
        * positive/negative
        * empty/full
* Boundaries
    * test at the threshold
* Order


### functions as Arguments
```python
def function_runner(f):
    """ (function) -> NoneType

    Call f.
    """
    f()
```

### print
`print(1, 2, 3, sep='..', end='!')`

### Exception Handling
* if you want to handle two kinds of exceptions, and on is a subclass of the other,
    catch the subclass first
```python
try:
    main() 
except ValueError as ve:
    print(ve)
```
* raise Errors
    * `raise ValueError("Bad value")`
* Assertion: assert statement to ensure that preconditions are met
    * `assert 0 <= n < len(L), '{} is out of range.'.format(n)`
------
reference:
* coursera lecture by University of Toronto - [Learn to Program: Crafting Quality Code](https://www.coursera.org/learn/program-code)
