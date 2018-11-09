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
        * holds references to objects
* where to use variables:
    * as object state, as local variables, as arguments, as return types
