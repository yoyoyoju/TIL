# pythonic way for getter and setter

For now I will copy and paste from lecture forum:

Getters and Setters are taught as this is a Computer Science course and they are common in other languages like Java. But Python is a language for consenting adults and information hiding by default is not pythonic.

So what do we do in Python?

The pythonic way is to make class attributes public unless there is good reason to do otherwise. So if class Mine has an attribute deep the way we read or write to it in instance SilverDollar is:

```python
class Mine():
    def __init__(self, deep):
        self.deep = deep

SilverDollar = Mine(30)
SilverDollar.deep = 50 # to set x and 
SilverDollar.deep  # to get the value of deep
```

No ugly stuff, just instance_name.variable_name.

But what if some of our users are idiots so we need to check that deep is a positive number but under 2000 (its a mine not a mountain). Similarly, mines deeper than 1000 are dangerous to miners so we need to hide them from the work & safety people - any mines deeper than 1000 will just return 1000. So, what's the pythonic way? Properties. The class looks like this but the user still gets access to it as above preserving the original simple interface:

```python
class Mine():
    def __init__(self, deep):
        self.deep = deep

    @property
    def deep(self):
        if self.__deep > 1000:
            return 1000
        return self.__deep

    @deep.setter
    def deep(self, deep):
        if deep > 2000:
            self.__deep = 2000
        elif deep <= 0:
            self.__deep = 0
        else:
            self.__deep = deep

# and try it out by creating an instance 
SilverDollar = Mine(-400)
print(SilverDollar.deep)
SilverDollar.deep = 5055
print(SilverDollar.deep)

```

So you start out without information hiding. Then you can add it later if needed but without altering your users' interface. Based on - for more information.


#### templates:
```python
class myClass():
    def __init__(self, xxx):
        self.xxx = xxx


# becomes:

class myClass_python():
    def __init__(self, xxx):
        self.xxx = xxx

    @property
    def xxx(self):
        # any required logic & filtering
        #   nefore you return the value
        #   note the double underscore (dunder)
        return self.__xxx

    @xxx.setter
    def xxx(self, xxx):
        # any logic you need to alter xxx
        #   before you save it (note dunder)
        self.__xxx= xxx
```

#### dunder
It creates an attribute that signals that it shouldn't be directly accessed from outside of the class.

So polite Python programmers won't even try. And if you try this code you'll probably find you can't access it without a bit of research :)

```python
class Dunder_demo:
    def __init__(self, x):
        self.__x = x

dd = Dunder_demo(55)
print(dd.__x)
```        




----
reference: [pythonTutor](https://www.python-course.eu/python3_properties.php)


