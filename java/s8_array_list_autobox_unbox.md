# section8: Array, Java inbuilt List, Autoboxing and Unboxing

### Arrays
* data structure to store sequence of values of one type.
* put `[]` at the end of datatype to indicate it is an array
* index starts from 0 to `length - 1`
* `array.length` for the length of the array: ArrayIndexOutOfBoundsException
* error for out of bounds index
* can be passed as arguments or returned
* defalut values 
    * numeric array elements : zero
    * boolean array elements : false
    * string or other objects: null
```java
int[] myInts = new int[10]; // Array of 10 integers
myInts[5] = 50;             // assign a value to the given index
System.out.println(myInts[5]);  // retrieve the value

int[] myInts2 = {1, 2, 3};  // initialize when create

int[] myInts3 = new int[10];
for (int i=0; i<myInts3.length; i++) {
    myInts3[i] = i * 10;
}

printArray(myInts3);        // without bracket
```
```java
public static void printArray(int[] array) {
    // ...
}
```
```java
private static Scanner scanner = new Scanner(System.in);
int[] myInts = getintegers(5);

public static int[] getIntegers(int number) {
    System.out.println("Enter " + "\r");
    int[]  values = new int[number];
    for(int i=0; i<values.length; i++) {
        values[i] = scanner.nextInt();
    }
    return values;
}
```
`Arrays.copyOf(array, array.length);`

### References Types vs Value Types
* reference types
    * String, classes, arrays
    * new creates new object
    * holds the reference, not the object itself
* value types:
    * primitive types
    * variable directly holds the value
    * when assigned copy the value
* dereference
    * if a new object is assigned to the variable,
    * it now points the new object

```java
// import java.util.Arrays;

int myIntValue = 10;
int anotherIntValue = myIntValue;
anotherIntValue++;
// myIntValue : still 10 unchanged
// anotherIntValue: 11

int[] myIntArray = new int[5]; // reference type
// create an new array and initialize to zero
// stores reference to the array in myIntArray
int[] anotherArray = myIntArray;    
// pointing to the same address

System.out.println("myIntArray= " + Arrays.toString(myIntArray));
System.out.println("AnotherArray= " + Arrays.toString(AnotherArray));

anotherArray[0] = 1;
// both are modified (actually they are pointing to the same objects)
```
* using method:
    passes the reference ( pointing at the same object )
```java
private static main(String[] args) {
    modifyArray(myIntArray);    // passes the reference
}

private static void modifyArray(int[] array) {
    // pointing the same object
    array[0] = 2;
    array = new int[] {1, 2, 3, 4, 5};
    // dereference and points to the new array
}
```

### scanner
`private static Scanner scanner = new Scanner(System.in);`
* static : the other static methods can access without creating instances
* private : other classes cannot access


### List and ArrayList
* array: such as `int[]`
    * type and length was defined as declared.
    * to resize array create a new array with the size and re-assign
```java
int[] original = baseData;  // preserve the original reference
baseData = new int[12]; // create new bigger array
// for loop to copy the original
```

* Collection
* List: ordered collection (List interface)
* Arraylist: inherits from list (AbstractList), class
    * can also hold objects, is defined at declaration `<...>`
    * resizable array (handles resize automatically, capacity)
    * as add more it grows

#### Usage:
```java
// import to use ArrayList
import java.util.ArrayList;     

// Create a new ArrayList:
// specify the type in `<>` blancket
ArrayList<String> arrayList = new ArrayList<String>();
// can also use a Constructor to create a new one and copy an existing ArrayList
ArrayList<String> anotherArrayList = new ArrayList<String>(arrayList);

// another way to copy - addAll(arrayList)
anotherArrayList.addAll(arrayList);

// add a item - add(item)
arrayList.add("add this");
// get the size of ArrayList - size()
arrayList.size();
// get an item by index - get(index)
arrayList.get(0);
// modify an ArrayList - set(index, newItem)
arrayList.set(1, "new entry")
// remove an item by index - remove(index)
arrayList.remove(0)
// check an item is in - contains(item)
// returns true if it is in
arrayList.contains("new entry")
// get the index of the given item - indexOf(item)
// returns -1 if not contain
arrayList.indexOf("new entry")

// convert an ArrayList into Array - toArray()
String[] myArray = new String[arrayList.size()];
myArray = arrayList.toArray();

```


#### example code
```java
import java.util.ArrayList;

public class GroceryList {
private ArrayList<String> groceryList = new ArrayList<String>();

public void addGroceryItem(String item) {
    groceryList.add(item);      // add item and automatically handle size, etc.
}

public void printGroceryList() {
    System.out.println(groceryList.size() + " items");
    for (int i=0; i<groceryList.size(); i++) {
        System.out.println(groceryList.get(i));
    }
}

public void modifyGroceryItem(int position, String newItem) {
    groceryList.set(position, newItem);
}

public void removeGroceryItem(int position) {
    String theItem = groceryList.get(position);
    groceryList.remove(position);
    // move items up to fill the number up
}

public String findItem(String searchItem) {
    // boolean exists = groceryList.contains(searchItem);
    // returns true when it has the item
    
    int position = groceryList.indexOf(searchItem);
    // returns -1 if not contain
    if (position >= 0) {
        return groceryList.get(position);
    }
    return null;

}
}
```


### Autoboxing and Unboxing
We cannot do:
```java
ArrayList<int> intArrayList = new ArrayList<int>();
```
The code above gives an error: "Type argument cannot be of primitive type".
As primitive type is not a class and we need a class reference here.
(Meanwhile String is a class, we can use String here.)
We could create class for `int`.
```java
 class IntClass {
    private int myint;
    // constructor, getters and setters
 }

 ArrayList<IntClass> myArrayList = new ArrayList<IntClass>();
```
but it's messy. neater way to do it is Autoboxing.

* object wrapper (like IntClass above)
```java
Integer integer = new Integer(54);
Double doubleValue = new Double(12.25);
```
`Integer` is a class while `int` is not.
```java
ArrayList<Integer> intArrayList = new ArrayList<Integer>();
for (int i=0; i<10; i++) {
    // Autoboxing (primitive type to Class)
    intArrayList.add(Integer.valueOf(i));
}
for (int i=0; i<10; i++) {
    // unbox (Class to primitive type)
    System.out.println( i + " -----> " + intArrayList.get(i).intValue());
}
```
* Autoboxing and Unboxing
```java
// Autoboxing
// convert primitive type into a class 
Integer.valueOf(56);     // gives Integer object
// two ways:
Integer myInt = Integer.valueOf(56);
Integer myInt = 56;

// Unboxing
// convert class objective into a primitive type
myInt.intValue();       // gives int value
// same as
int i = myInt;
int i = myInt.intValue();
```

#### example for Double
```java
ArrayList<Double> myDoubles = new ArrayList<Double>();
for(double dbl=0.0; dbl<10.0; dbl+=0.5){
    // Autoboxing
    // myDoubles.add(Double.valueOf(dbl));
    myDoubles.add(dbl);
}

for(int i=0; i<myDoubles.size(); i++) {
    // Unboxing
    // double value = myDoubles.get(i).doubleValue();
    double value = myDoubles.get(i);
    System.out.println(i + " ----> " + value);
}
```

50min

### LinkedList
50min

Challengh1,2,3,

