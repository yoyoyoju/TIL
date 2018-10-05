# notes
To sort out things later

### dictionary safe way
`d.get(key, default)`, where `d` is a dictionary.
It returns `default` when the key does not exist in the `d`.
It does not raise `KeyError` oppose to `d[key]`.

* `sum(d.values())` or `list(d.values())`


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

### multiple inheritance
```
class A(object):
    def __init__(self):
        self.a = 1
    def x(self):
        print("A.x")
    def y(self):
        print("A.y")
    def z(self):
        print("A.z")

class B(A):
    def __init__(self):
        A.__init__(self)
        self.a = 2
        self.b = 3
    def y(self):
        print("B.y")
    def z(self):
        print("B.z")

class C(object):
    def __init__(self):
        self.a = 4
        self.c = 5
    def y(self):
        print("C.y")
    def z(self):
        print("C.z")

class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
        self.d = 6
    def z(self):
        print("D.z")
```

Which __init__ methods are invoked and in which order is determined by the coding of the individual __init__ methods.

When resolving a reference to an attribute of an object that's an instance of class D, Python first searches the object's instance variables then uses a simple left-to-right, depth first search through the class hierarchy. In this case that would mean searching the class C, followed the class B and its superclasses (ie, class A, and then any superclasses it may have, et cetera).

**reference** : edX 6001x week5 exercise4
