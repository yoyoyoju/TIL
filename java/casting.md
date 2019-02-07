### Casting
* cast an object reference back to its real type
    * see also [inheritance](inheritance.md#polymorphism)
    * to call a class-specific methods, the reference type should match
    ```java
    // example by custom Class Dog
    Object dog = new Dog(); // the reference type is not dog
    // Dog-specific methods does not work, such as
    // dog.bark(); // NOT work!

    Dog realDog = (Dog) dog;    // cast the object back to a Dog
    realDog.bark(); //works now
    ```
    * to make sure:
        * when it goes wrong, ClassCastException at runtime
    ```java
    if (o instanceof Dog) {
        Dog d = (Dog) dog;
    }
    ```




### Casting Primitives

* shove bigger size primitive into smaller size (without casting) won't work
```java
long y = 42;
int x = y; // does not work
```
* to force it use the **cast** operator
```java
long y = 42;
int x = (int) y; // works now
```
* the values will be chop down, though
```java
long y = 40002;
// 40002 exceeds the 16-bit linit of a short
short x = (short) y; // x is not -25534
```
```java
float f = 3.14f;
int x = (int) f;    // x is 3
```

-----
reference
*headfirst java* chapter 5
