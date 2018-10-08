# session3 - Variables, Datatypes and Operators

### Variable
Have to datatype and name and assign a value to it.
Generally start with lowercase.
```java
int myFirstNumber = 5;
System.out.println(myFirstNumber);  # print out the variable
```

### Whole numbers


#### int
* standard for whole number
* width of 32 (4 bytes)
* roughly, -2.147 billion to 2.147 billion: (-2147483648 to 2147483647)
* expressions (for example `(a*b)`) convert to int

#### byte
* for smaller numbers more efficient
* width of 8
* -128 to 127
```java
byte myByteValue = 10;
byte myNewByte = (myByteValue/2);           // converted to int -> error
byte myNewByte = (byte) (myByteValue/2);    // cast into byte
System.out.println("myNewByte = " + myNewByte);
```
#### short
* width of 16
* -32768 to 32767
```java
short myShortValue = -32768;                
short myNewShort = (short) (myShortValue/2); // should cast into short
```

#### long
* for larger numbers
* width of 64 
* at the end of the number should be `l` or `L`
* do not need to cast
```java
long mylongValue = 100L;                                    // at the end `L`
byte myByte = 10;
short myShort = 10000;
int myInt = 19038323;
long myLong = 50000L + 10L * (myByte + myShort + myInt);    // do not need to cast
System.out.println("my long = " + myLong);
```

### comment
After `//` will be ignored.



### decimal numbers

#### double
* double precision number 
* width of 64 (8 bytes)
* number with decimal point in default is assumed to be double
* recommended to use:
    * more precise than `float` (double precision)
    * faster in modern computers
    * more built-in functions
```java
double myDoubleValue1 = 5d;           // put d for double
double myDoubleValue2 = 5.25;         // assumes it is double
double myDoubleValue3 = 5d / 3d       // 1.6666666666666667
float myFloatValue3 = 5f / 3f         // 1.6666666
int myIntValue = 5 / 3                // gives 1 (dont' handle reminder)
```

#### float
* single precision number
* width of 32 (4 bytes)
* need to put `f` at the end of the number (or cast)
```java
float myFloatValue1 = 5.4f;         // put `f` at the end for float
float myFloatValue2 = (float) 5.4;  // cast
float myFloatValue3 = 5f / 3f       // 1.6666666
```


### char bool

#### char
* width is 16 (2byte)
* store one letter or one character (more than one gives an error)
* unicode character is supported ([unicode-table](unicode-table.com))
```java
char myChar1 = 'D';
char myChar2 = '$';
char myChar3 = '\u00A9';        // unicode character for copyright symbol
```

#### bool
* only two values: `true` and `false`.
```java
boolean myBoolean1 = true;
boolean myBoolean2 = false;
```

### primitive types
8 primitive types built-in to the language.
* byte
* short
* int
* long
* float
* double
* char
* boolean


### strings
* sequence of characters
* double quote around the string
* not primitive type (but a Class)
```java
String myString = "This is a string";
myString = myString + ", and this is more.";        // append to the string
myStirng = myString + "\u00A9 2018";                // unicode character
String numberString = "250.55";                     // numbers as string
String lastString = "10";
int myInt = 50;
lastString = lastString + myInt;                    // converts int to String (gives back "1050")
double doubleNumber = 120.47;
lastString = lastString + doubleNumber;             // converted double to String ("1010120.47")
```

### Operators
* operands: parameters
* common operators
    * `=` (assignment), `+`,  `-`, `*`, `/`, `%` (remainder), `++` (increment by 1), `--`
    * `+=`, `*=`, `-=`, `/=`
* test operators (for conditional code, return boolean)
    * `==` 'is equal'
    * `!=`, `>=`, `>`, `<`, `<=`
* conditional operators
    * `&&` (and), `||` (or)
* ternary operator
    ` boolean wasCar = isCar ? true : false;` 
    ```java
    if isCar == true
        wasCar = true
    else
        wasCar = false
    ```
[summary of operators](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/opsummary.html)
[operator precedence table](http://cs.bilkent.edu.tr/~guvenir/courses/CS101/op_precedence.html)
```java
int result = 1 + 2;  
result = result - 1;
result += 2;            // add 2 to the result

boolean isAlien = false;
if (isAlien == false)   // if `isAlien` is flase
    System.out.println("It is not an alien!");

int topScore = 100;
if (topScore != 100)
    System.out.println("not 100");

if secScore = 60;
if ((topScore > secScore) && (topScore < 100))
    System.out.println("Greater than top score and less then 100")

boolean isCar = false;
if (isCar = true)       // returns whatever the values which is assigned to (true)
    System.out.println("This is not supposed to happen")    // this will print out
if (isCar = false)       // returns whatever the values which is assigned to (false)
    System.out.println("This does not print out")

if (isCar)              // better way
    System.out.println("This is not supposed to happen")    

boolean wasCar = isCar ? true : false;
if (wasCar)
    System.out.println("wasCar is true");

```




-------
### IntelliJ
* type `sout` (templete for IntelliJ) for `System.out.println`.
