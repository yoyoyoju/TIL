# Abstract Class
* class that cannot be instantiated
    * abstract classes cannot produce instances
    * can use abstract type as a reference type
    * the class must be extended
    * *concrete* class: it's okay to make objects of that type
* abstract class can contain normal and abstract methods
* use keyword `abstract` for abstract classes or abstract method
    * `public abstract class ClassName`
    * `public abstract returnType methodName`
* example codes
    ```java
    abstract public class Canine extends Animal {...}
    public class MakeCanine {
        public void go() {
            Canine c;   // abstract class as a reference type
            c = new Dog();  // Dog is a concrete class
            c = new Canine();   // compile error, as Canine is abstract
            ...
        }
    }

```java
public abstract class Operation {
    private String name;

    public Operation(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    public abstract void execute(Scanner reader);
}

public class Addition extends Operation {
    public Addition() {
        super("Addition");
    }

    @Override
    public void execute(Scanner reader) {
        System.out.print("number: ");
        int first = Integer.parseInt(reader.nextLine());
        System.out.print("number: ");
        int second = Integer.parseInt(reader.nextLine());
        System.out.println("sum: " + (first + second));
    }
}
```
```java
public class UserInterface {

    private Scanner reader;
    private List<Operation> operations;

    public UserInterface(Scanner reader) {
        this.reader = reader;
        this.operations = new ArrayList<Operation>();
    }

    public void addOperation(Operation operation) {
        this.operations.add(operation);
    }

    public void start() {
        while (true) {
            printOperations();
            System.out.println("Choice: ");

            String choice = this.reader.nextLine();
            if (choice.equals("0")) {
                break;
            }

            executeOperation(choice);
            System.out.println();
        }
    }

    private void printOperations() {
        System.out.println("\t0: Quit");
        for (int i = 0; i < this.operations.size(); i++) {
            String operationName = this.operations.get(i).getName();
            System.out.println("\t" + (i + 1) + ": " + operationName);
        }
    }

    private void executeOperation(String choice) {
        int operation = Integer.parseInt(choice);

        Operation chosen = this.operations.get(operation - 1);
        chosen.execute(reader);
    }
}
```
usage:
```java
UserInterface ui = new UserInterface(new Scanner(System.in));
ui.addOperation(new Addition());
ui.start();
```


### abstract method
* method can also be abstract
    * the method must be overridden to be used
    * the class must be abstract too
    * for methods that there is no proper generic method implementation
    * abstract methods have not body
        `public abstract void eat();`

-----------
Codes from [mooc.fi](https://materiaalit.github.io/2013-oo-programming/part2/week-10/)
