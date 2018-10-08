# mooc.fi 
from [mooc.fi](http://moocfi.github.io/courses/2013/programming-part-1/) java lecture part - 1

### w1 input print condition

#### compiler and interpreter
* `javac Hello.java` will compile the java file into _bytecode_. This _bytecode_ is executed using the java interpreter by using `java Hello`.


#### components of commands

* semicolon
    * `;`
    * to separate different commands
    * line breaks are ignored by the compiler and the interpreter.
* parameters
    * information passed to commands
    * passed by placing them between `()` brackets
* comments
    * on a line after two forward slashes `//`


#### print
* `System.out.print();` : without new line
* `System.out.println();` : with new line
* line break `\n` : `System.out.println("First\nSecond\nThird");`

#### main program body
The program is stored in at text file named after the program with the `.java` extension.
```java
public class Example {      // should be stored in Example.java
    public static void main(string[] args) {
        // code
    }
}
```

#### variables and data types
* variable type is written on the first declaration. It keeps its value until it is assigned to a new value.
```java
int myInt = 1;
myInt = 2;
```
* variable data types are immutable. (the type cannot be changed later and cannot be assigned value with different type)
* variable names
    * no: `!`, ` `
    * should not start with number
    * use camelCase notation (the first character is lower)

#### calculation
```java
double whenDividendIsFloat = 3.0 / 2;       // 1.5
double when DivisorIsFloat = 3 / 2.0;       // 1.5

int first = 3;
int second = 2;
double result1 = (double) first / second;   // 1.5
result1 = 1.0 * first / second;             // 1.5  : (1.0 * first) is 3.0
double result2 = (double) (first / second); // 1    calculate is done before the type cast
int integerResultBecauseTypeIsInteger = 3.0 / 2;    // 1
```

#### user input
* use `Scanner` tool to read user input
```java
import java.util.Scanner;

public class Example {
    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        System.out.print("What's your name? ");
        String name = reader.nextLine();
        System.out.println("Hi, " + name);
    }
}
```

* to read integer: `Integer.parseInt` to convert string into an integer.
```java
int number = Integer.parseInt(reader.nextLine());
```

# Resume from Exercise 8
