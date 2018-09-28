# notes
To sort out things later

### dictionary safe way
`d.get(key, default)`, where `d` is a dictionary.
It returns `default` when the key does not exist in the `d`.
It does not raise `KeyError` oppose to `d[key]`.


### multiple exception
```python
try:
    try:
        raise Exception("0")
    finally:
        raise Exception("1")
except Exception as ex:
    print(ex)
```
The try block raises both exception, 
but the except block catches the later one (the one with `"1"`)
