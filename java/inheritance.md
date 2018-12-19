# inheritance
* superclass and subclass
* use `extends` keyword
```java
public class Person {
    private String name;
    public Person(String name) {
        this.name = name;
    }
    @Override
    public String toString() {
        return this.name;
    }
}
public class Student extends Person {
    private int credit;
    public Student(String name, int credit) {
        super(name);
        this.credit = credit;
    }
    @Override
    public String toString() {
        return super.toString() + " : " + this.credit;
    }
    public int credit() {
        return this.credit;
    }
}
```

### polymorphism
```java
Person lucas = new Student("lucas", 1);
lucas.credit(); //NOT WORK
lucas.toString();   // work with toString definded in Student
```
* which methods can be called, is defined through the variable type:
    * `lucas` is a `Person` type: can only use the methods defined in Person class.
* the execution method is chosen based on its real type, regardless of the variable type which is used.
    * Objects are diverse, which means they can be used through different variable types.
    * The execution method does always depend of the object's actual type.
    * if the actual class does not have the method, move to its parent class.
    * `lucas` is actually `Student`: use `Student`'s `toString` method.

### access modifier
* private
    * cannot be seen by its subclasses
    * its subclasses do not have any straight way to access it
* protected
    * access is restricted to only its subclasses
* public
    * subclass can see `public` variables and methods

### superclass
* call `super` in constructor to call the constructor of superclass
    * super call must always be in the first line
* `super` prefix to call the methods defined in the superclass
    ```java
    @Override
    public String toString() {
        return super.toString() + "\n and additional message";
    }
    ```

