# Casting Primitives

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
