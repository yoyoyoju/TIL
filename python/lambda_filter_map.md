### Lambda Operator
Create a small anonymous function for one time use.

#### Syntax
```python
lambda argument_list: expression
```

#### example
```python
>>> sum = lambda x, y : x + y
>>> sum(3, 4)
7
```


### map function
`r = map(func, seq)`
* `func`: name of a function
* `seq`: a sequence (a list)
* map applies `func` to all the elements of the `seq`.
* returns an iterator

example:
```python
def fahrenheit(T):
    return (float(9)/5)*T + 32)

temperatures = (36.5, 20, 0, 100)
F = map(celsius, temperatures)
temp_in_fahrenheit = list(map(fahrenheit, temperatures))

# using Lambda:
F = list(map(lambda x: (float(9)/5)*x + 32, temperatures))
```

map can be applied to more than one list:
```python
a = [1, 2, 3, 4]
b = [-1, -2, -3, -4]
list(map(lambda x, y : x + y, a, b))
# [0, 0, 0, 0]

# it works when one is shorter
# stops with the shortes list
a = [1, 2, 3]
b = [-1, -2, -3, -4]
list(map(lambda x, y : x + y, a, b))
# [0, 0, 0]
```


### filtering
`filter(func, seq)`
* `func`: function returns boolean value
* `seq`: a sequence like a list
* to filter out all the elements from the `seq`, which the `func` returns `True`.

example:
```python
aList = [1,3,2,6,4,2]
odd_number = list(filter(lambda x: x % 2, aList))
even_number = list(filter(lambda x: x % 2 - 1, aList))
```
-------
reference: [python-course](https://www.python-course.eu/python3_lambda.php)
