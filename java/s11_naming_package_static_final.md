# naming conventions and packages
# Static and final keywords

### Naming conventions
* packages
    * always lower case
    * unique
    * your internet domain name, reversed, as a prefix for the package name
        * `com.example` and `org.example` for packages will not be distributed
        * `src/com/example/mypack` for `package com.example.mypack;`: have to match
    * [docu](http://docs.oracle.com/javase/specs/jls/se6/html/packages.html#7)
    * invalid characters: `-`, starting with number, java keywords (use `_` front)
    * `java.lang` `java.io`
* classes
    * CamelCase
    * should be nouns
    * start with a capital letter
    * `ArrayList`, `String`, `LinkedList`
* interfaces
    * start with a capital letter
    * CamelCase
    * `List` `Comparable`
* methods
    * mixed case
    * often verbs
    * reflect the function performed or the result returned
    * `size()` `getName()`
* Constants
    * ALL UPPER_CASE
    * separate words with underscore `_`
    * declared using the final keyword
    * `MAX_INT` `PI`
* Variable names (field names)
    * mixedCase 
    * meaningful and indicative
    * start with lower case letter
    * do not use underscores `_`
    * `i` `league` `boxLength`
* Type parameters
    * Single character, capital letters
    * [guidelines](https://docs.orcle.com/javase/tutorial/generics/types.html)
    * `E` (used extensively by the java collections Framework)
    * `K` Key, `T` Type, `V` Value, `S`, `U`, `V` - 2,3,4th Types

### packages
* need to fully specify the package name
* way to manage name spaces of object types
* extends access protection
* how to:
    * `import javafx.scene.Node` : import
    * `javafx.scene.Node` : use fully qualified name
* can use same class name by refering the second way:
```java
import javafx.scene.Node;

Node node = null;
org.w3c.dom.Node anotherNode = null;
// or refer both fully without import
```
```java
import java.awt.*;  
import java.awt.event.WindowAdapter;    // separate java.awt and java.awt.event
import java.awt.event.WindowEvent;

public class MyWindow extends Frame {
    public MyWindow(String title) {
        super(title);
        setSize(500, 140);
        addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent e) {
                System.exit(0);
            }
        });
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        Font sansSerifLarge = new Font("SansSerif", Font.BOLD, 18);
        g.setFont(sansSerifLarge);
        g.drawString("Java", 60, 60);
    }
}

// main
MyWindow myWindow = new MyWindow("a");
myWindow.setVisible(true);
```

#### new artifact
* from IntelliJ
* Jar package
    * file -> project structure -> artifacts -> plus button 
    * -> jar -> from modules with dependencies
    * put Main class to make it excutable
    * Build artifacts
* output file: out artifacts package
* use package
    * file -> project structure -> libraries -> java -> specify the place


### Scope
* visibility
* in scope: accessable variables
```java
public class ScopeCheck {
    public int publicVar = 0;
    private int privateVar = 1;
    private int privateVar2 = 2;

    public void test() {
        int privateVar = 2; // scope is current method
        System.out.println(privateVar); // prints 2 (most local is used)
        for(int i=0; i<2; i++) {
            // i is limited in this block
        }
//        System.out.println(i);      // cannot access to i (out of scope)
        System.out.println(this.privateVar);    // uses class variable 1
    }
    public void test2() {
        System.out.println(privateVar); // prints 1 
    }

    public void useInner() {
        InnerClass innerClass = new InnerClass();
        System.out.println("varInner" + innerClass.varInner);   
        // ScopeCheck can access innerClass.varInner
    }



    public class InnerClase {
        public int privateVar = 3;
        private int varInner = 0;

        public InnerClass() {
            System.out.println(privateVar);
        }

        public void test() {
            ScopeCheck.this.test2();    //  calls the method in the ScopeCheck class
            System.out.println(privateVar); // prints 3
            System.out.println(privateVar2); // prints 2 
            // System.out.println(this.privateVar2); // error
            System.out.println(ScopeCheck.this.privateVar2); // prints 2
        }
    }
}

// main
ScopeCheck.InnerClass innerClass = scopeInstance.new InnerClass();
innerClass.test();

ScopeCheck scopeInstance = new ScopeCheck();
scopeInstance.useInner();       // 0
ScopeCheck.InnerClass innderClass = scopeInstance.new InnerClass();
// innerClass.varInner // not visible
// visible if varInner is public
```





### Access Modifiers
#### Top Level
only classes, interfaces and enums can exist at the top level,
everything else must be included within one of these.
* public
    * the object is visible to all classes everywhere,
     whether they are in the same package or
     have imported the package containing the public class.
    * `public interface Myinterface { //... }`
* package-private:
    * the object is only available within its own package
    * specified by not specifying. (it is default, there is not keyword for this)
    * `class Myclass {//...}`


#### Member Level
* public
    * public class members and methods can be accessed from
    any other class anywhere, even in a different package
* package-private
    * objects with no access modifier
    * visible to every class within the same package
    * not visible to classes in external packages
* private
    * cannot have private class at the top level
    * only visible within the class it is declared
    * not visible anywhere else (including in subclasses of its class)
* protected
    * the object is visible anywhere in its own package (like package-private)
    * also in subclasses even if they are in another package

#### in interface
* everything is public!
* but if interface itself is package-private
the methods in interface are effectively package-private.
(cause the interface itself is not visible to externals)



### static statement
* static is related to the class itself rather than the instances.
* all the instances share one copy 
* if an instance modifies it, it affects all other instances
* good to make a static method for the methods with the static fields
* use class name to access it `Classname.staticmethod()`
* class methods and class variables
* in its own class, static cannot access non-static
```java
public class Main {
    // public int multiplier = 8;  // exist when instance is created
    public static int multiplier = 9;
    public static void main(String[] args) {
        System.out.println(multiplier); // error
    }

    public static int multiply(int num) {
        // without static it does not work
    }
}
```

### final statement
* for constant values
* use when first declare or in constructor
* cannot be anymore modified after construction
```java
public class MyClass {
    private static int ClassCounter = 0;
    public final int instanceNumber;
    private final String name;

    public MyClass(String name) {
        this.name = name;
        ClassCounter++;
        instanceNumber = classCounter;
    }

    public getInstanceNumber() {
        return instanceNumber;
    }
}
//main
MyClass one = new MyClass("one");
one.instanceNumber = 5; // error because it is a final variable
```

* Constance values for static final (do not need to store copies in instances)

* mark constructor as private will prevent to make instances
    * example: `private Main(){}` in `public final class Math`
    * class is final: cannot be extended (no sub-class of final class is possible)
    * method is final: cannot be overriden.

* static initialization block - set static final variables
```java
public class SIBTest {
    public static final String owner;

    static {
        // static initialization block
        owner == "me";
        System.out.println("1 initialization block");
    }

    public SIBTest() {
        // SIB constructor
        System.out.println("constructor");
    }

    static {
        // 2nd initialization block
        System.out.println("2 initialization block");
    }

    public void someMethod() {
        System.out.println("method");

    }
}

// main
System.out.println("main method");
SIBTest test = new SIBTest();
test.someMethod();
/*
 * main method
 * 1 initialization
 * 2 initialization
 * constructor
 * method
 */
```



