# Generics

### intro
* Generic type parameter
    * when we define a class
    * define the types that have to be chosen when an object is created
    * set up the number of type parameters we want (after the class name <T>)

```java
public class Slot<T> {
    private T key;

    public void setValue(T key) {
        this.key = key;
    }
    public T getValue() {
        return key;
    }
}

Slot<String> string = new Slot<String>();
string.setValue(":)");
System.out.println(string.getValue());
```

### interface with generics
* interfaces which uses generics
    * Comparable:
        * compareTo method
        * used in `Collections.sort`

Example:
```java
public class ClubMember implements Comparable<ClubMember> {
    private String name;
    private int height;
    
    public ClubMember(String name, int height) {
        this.name = name;
        this.height = height;
    }
    public int getHeight() {
        return this.height;
    }

    @Override
    public int compareTo(ClubMember clubMember) {
        return this.height - clubMember.getHeight();
    }
}
