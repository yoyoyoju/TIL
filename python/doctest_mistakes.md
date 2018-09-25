# Doctest Mistakes
The mistakes I made in doctest.

### newline
new line `\n` should be written in doctest as `\\n'.
```python
def foo():
    '''
    >>> foo()
    'hello\\n'
    '''
    return 'hello\n')
```

