# Mistakes
The mistakes I made

### doctest newline
new line `\n` should be written in doctest as `\\n`.
```python
def foo():
    '''
    >>> foo()
    'hello\\n'
    '''
    return 'hello\n'
```


### doctest NORMALIZE WHITESPACE
`````python
def foo():
    '''
    >>> foo()   # doctest: +NORMALIZE_WHITESPACE
    a b c
    '''
    print("a b c ")
`````
to normalize the white space


### loop over dictionary
* `for key in dictionary:` for keys
* `for key, value in dictionary.items():` for Python3.x
* `for key, value in dictionary.iteritems():` for Python2.x 

