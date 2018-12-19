# inheritance
* superclass and subclass
* use `extends` keyword
```java
public class Component {
    private String id;
    public Component(String id) {
        this.id = id;
    }
}

public class Motor extends Component {
    private String motorType;
    public Motor(String motorType, String id) {
    super(id);
    this.motorType = motorType;
    }
}
```

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
