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


challenge: 13

### Scope
1,2: 30
challenge: 7

### Access Modifiers

### static statement

### final statement


