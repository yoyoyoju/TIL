# Mistakes
The mistakes I made

### newline
new line `\n` should be written in doctest as `\\n`.
```python
def foo():
    '''
    >>> foo()
    'hello\\n'
    '''
    return 'hello\n'
```


### loop over dictionary
* `for key in dictionary:` for keys
* `for key, value in dictionary.items():` for keys
* `for key, value in dictionary.iteritems():` for Python2.x 

