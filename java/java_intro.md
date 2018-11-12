### Java
* Java is platform indepecdent
* how the java works:
    * source code -> [Java Compiler] -> bytecode
    * The bytecode is distributed
    * interpreter depending on the machine translates the bytecode into Machine code
* how to:
    * source code (.java file)
    * compile by `javac java_file.java`
    * -> output (.class file)
    * ran by JVM (java virtual machine) `java java_file.class`
* Object oriented
* strongly-typed language
* multithreaded


* no boolean test on an integer

#### example
```java
String[] pets = {"Zitrone", "Zero", "Zack"};
int i = (int) (Math.random() * pets.length);
System.out.println(pets[i] + " is at home");
```

### class
* think about
    * what the object knows : instance variables
    * what does the object do : methods
* objects lives in the heap (Garbage-Collectible Heap)

#### how to
* class (Dog) : the class I want to write
* testdrive (DogTestDrive) : has main method, to test my class

### Variables
* primitive and reference
    * primitive
        * holds fundamental values
        * including integers, booleans, floating point numbers
    * object reference
        * holds references to objects (bit depth not relevant)
        * the reference variable is bits representing a way to get to the object
        * objects live in the garbage collectible heap
* where to use variables:
    * as object state, as local variables, as arguments, as return types

#### Primitive Types
Type | Bit Depth | Value Range
-----|-----------|------------
boolean | JVM-specific | true or false
char | 16 bits | 0 to 65535
byte|8 bits | -128 to 127
short | 16 bits | -32768 to 32767
int | 32 bits | -2147483648 to 2147483647
lone | 64 bits | -huge to huge
float | 32 bits | varies
double|64 bits | varies

* `float f = 32.5f` : at the end of float f

#### reference
```java
Dog mydog = new Dog();
```
* `Dog myDog` part
    * to allocate space for a reference variable
    * name that variable myDog
    * The reference variable is of type Dog (and cannot be changed)
* `new Dog();` part
    * to allocate space for a new Dog object on the heap
* `=` part
    * assigns the new Dog to the reference variable myDog
```java
Dog john = mydog;
```
* john and mydog are refering to the same object
* there is one object and two references. (I can call the dog as mydog or john)


#### Array
* an array variable is a remote control to an array object
`int[] nums;`
* create a new int array with a length of 3 and assign it to nums: `nums = new int[3];`
* give each element an int value : `nums[0] = 1; nums[1] = 5; nums[2] = 49;`
* Arrays can hold primitive variables or references `Dog[] pets = new Dog[3]; pets[0] = new Dog();`

#### Objects and Classes
* A method uses parameters. A caller passes arguments.
* instance variables : declared inside a class (but not within a method)
    * always get a default value
        * integers: 0
        * floating points : 0.0
        * booleans: false
        * references: null
* local variables are declared within a method
    * must be initialized before use
