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
```


### generics

* note from headFirst java chapter 16
* convention for type parameter
    * `T`
    * `E`: for a collection class, type of the Element the collection will hold
* `extends` keyword in generics means `extends` or `implements`.
    * it means "is-a"
    * `<T extends Comparable<? super T>>`: Comparable is interface, but uses `extends` keyword


#### Using generic Classes

* class declaration includes a type parameter
* example: ArrayList
    ```java
    // E represents the type used to create an instance of ArrayList
    public class ArrayLIst<E> extends AbstractList<E> implements List<E> ... {
        public boolean add(E o) 
        
        // more code
    }
    ```
    * using type parameters with ArrayList
    ```java
    // in this example, the element E is String
    ArrayList<String> alist = new ArrayList<>();
    ```


#### Using generic Methods

* method declaration uses a type parameter in its signature
* defferent ways to use it
    1. using a type parameter defined in the class declaration
        `public boolean add (E e)` like the ArrayList case above
    2. using a type parameter that was not defined in the class declaration
        ```java
        // declare the type before the return type
        // T can be any subtype of Animal
        // i.e. ArrayList<Animal>, ArrayList<Dog>, ArrayList<Cat>, etc.
        public <T extends Animal> void takeThing(ArrayList<T> list)

        // compare to this
        // this method can only take ArrayList<Animal>
        public void takeOnlyAnimal(ArrayList<Ainmal> list)

        ```



### Array and Collection

* in Array
    ```java
    // let's say Dog and Cat are subtype of Animal
    public void takeAnimals(Animal[] animals) {
        for (Animal a : animals) {
            // if Dog override the eat method, the overriden method will executed.
            a.eat();
        }
    }

    // one can pass Animal[] as well as Dog[]
    public void go() {
        Animal[] animals = {new Dog(), new Cat()};
        Dog[] dogs = {new Dog()};
        takeAnimals(animals);
        takeAnimals(dogs);  // this works, too.
    }

    public void replaceToCat(Animal[] animals) {
        // the type was checked in runtime
        // if Dog[] was passed, it will give an error:
        // ArrayStoreException
        animals[0] = new Cat();
    }
    ```
* in ArrayList
    ```java
    public void takeAnimals(ArrayList<Animal> animals) {
        // ...
    }

    // one cannot pass ArrayList<Dog>
    public void go() {
        ArrayList<Animal> animals = new ArrayList<>();
        animals.add(new Dog());
        takeAnimals(animals);

        ArrayList<Dog> dogs = new ArrayList<>();
        takeAnimals(dogs);  // NOT WORK
    }

    // cannot pass ArrayList<Dog> to this.
    // collection type checks happen only when you compile.
    // If it were possible to pass ArrayList<Dog>, nothing will stop to add a Cat here
    // because there is no runtime type check for ArrayList.
    // So, it is not allowed to pass ArrayList<Dog> here.
    public void addCat(ArrayList<Animal> animals) {
        animals.add(new Cat());
    }
    ```
* generic with a wildcard
    * what if you want a method for `ArrayList<Dog>` and `ArrayList<Cat>`?
        ```java
        // can invoke methods on the elements in the list
        // the compiler will stop you from add elements to the list
        public void takeAnimals(ArrayList<? extends Animal> animals) {
            // this is ok
            for (Animal a : animals) {
                a.eat();
            }

            // this is not ok
            animals.add(new Cat());
        }
        ```
    * another way to write it
        ```java
        public <T extends Animal> void takeThing(ArrayList<T> list)
        ```

