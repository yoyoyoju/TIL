# Collections

### Collections
* collections class
```java
int lastRow = 'A' + (numPows -1);
for (char row = 'A'; row <= lastRow; row++) { //... }
String.format("%02d", myInt);
private List<Seat> seats = new ArrayList<>();
for(Seat seat : seats) {// ...}
```
* Collection
    * Set
        * SortedSet
    * List
    * Queue
    * Deque

* Set
    * HashSet, LinkedHashSet
* SortedSet     // elements should be Comparable
    * TreeSet

### Binary search
```java
// change ArrayList to LinkedList -> still work
private List<Seat> seats = new LinkedList<>();

// more general
private Collection<Seat> seats = new HashSet<>();
```


* To do Binary search need to implement Comparable
```java
private List<Seat> seats = new ArrayList<>();


public boolean researveSeat(String seatNumber) {
    Seat requestedSeat = new Seat(seatNumber);
    int foundSeat = Collections.binarySearch(seats, requestedSeat, null);
    if(foundSeat >= 0) {
        return seats.get(foundSeat).reserve();
    } else {
        return false;
    }
}



private class Seat implements Comparable<Seat> {
    //...
    @Override
    public int compareTo(Seat seat) {
        return this.seatNumber.compareToIgnoreCase(seat.getSeatNumber());
    }
}
```

### Collections List Methods
```java
// when the inner class Seat of Theater is public
Theatre theatre = new Theatre("O", 8, 12);
// shallow copy 
// if we modify a seat by reserve, the original is also changed
// actually they are pointing the same seat objects
List<Theatre.Seat> seatCopy = new ArrayList<>(theatre.seats);
seatCopy.get(1).reserve();
theatre.reserveSeat("A02"); // already reserved from the line above

Collections.reverse(seatCopy);
printList(seatCopy);        // reversed order
printList(theatre.seats);   // still in the original order

Collections.shuffle(seatCopy);   // psudo-random order


// does not need to be sorted
Theatre.Seat minSeat = Collections.min(seatCopy);
Theatre.Seat maxSeat = Collections.max(seatCopy);

sortList(seatCopy); // bouble sort


// to copy
// does not work:
// only gives capacity, actually need to have the objects before copy
List<Theatre.Seat> newList = new ArrayList<>(theatre.seats.size());
Collections.copy(newList, theatre.seats);

public static void printList(List<Theatre.Seat> list) {
    for(Theatre.Seat seat : list) }
        System.out.println(" " + seat.getSeatNumber());
    }
}

public static void sortList(List<? extends Theatre.Seat> list) {
    for(int i=0; i<list.size() -1; i++) {
        for(int j = i+1; j<list.size(); j++) {
            if(list.get(i).compareTo(list.get(j)) >0) {
                Collections.swap(list, i, j);
            }
        }
    }
}
```


### Comparable and Comparator
```java
public Collection<Seat> getSeats() {
    return seats;
}

```
* create a comparator object within an existing class
```java
public class Theatre {
    
    // ...
    // in the constructor, set prices as Seat objects are created

    static final Comparator<Seat> PRICE_ORDER = new Comparator<Seat>() {
        // anonymous inner class
        @Override
        public int compare(Seat seat1, Seat seat2) {
            if (seat1.getPrice() < seat2.getPrice()) {
                return -1;
            } else if (seat1.getPrice() > seat2.getPrice()) {
                return 1;
            } else {
                return 0;
            }
        }
    };
    
    // ..
    // the inner class Seat has now price field
}

// main
List<Theatre.Seat> priceSeats = new ArrayList<>(theatre.getSeats());
priceSeats.add(theatre.new Seat("B00", 13.00));
priceSeats.add(theatre.new Seat("A00", 13.00));
Collections.sort(priceSeats, Theatre.PRICE_ORDER);
printList(priceSeats);
```
    * when it is static can be initialized in static initialization block
    ```java
    public class Theatre {
        // fields

        static final Comparator<Seat> PRICE_ORDER;

        static {
            PRICE_ORDER = new Comparator<Seat>() {
                @Override
                public int compare(Seat seat1, Seat seat2) {
                    if (seat1.getPrice() < seat2.getPrice()) {
                        return -1;
                    } else if (seat1.getPrice() > seat2.getPrice()) {
                        return 1;
                    } else {
                        return 0;
                    }
                }
            }
        }

        // ..
    }
    ```
    * compareTo return 0 only when equals return true. consistency with equals
    * the PRICE_ORDER will raise error, since it is not consistent with equals:
        gives 0 even when it is not equals
* create a new class of implements that compare at out interface

### Maps
* not part of collection
* dictionary-like
* two types: key and value
* keys should be unique
* keys does not need to be immutable (but need to be careful)
* key/ values can be Classes
* methods:
    * `.put("key", "value")` : returns the previous value and set the data
    * `.get("key")`
    * `.containsKey("key")`
    * `.ketSet()`   : returns key set - no specific order
    * `.remove("key")`, `.remove("key", "value')`
    * `.replace("key", "new entry")`, `.replace("key", "old", "new")`
```java
public class Map {
    public static void main(String[] args) {
        // use the complete decoration
        java.util.Map<String, String> languages = new HashMap<>();
    }
}
```

```java
import java.util.HashMap;
import java.util.Map;

public class MapProg {
    public static void main(String[] args) {
        Map<String, String> languages = new HashMap<>();
        languages.put("key", "value");
        languages.put("key2", "value--2");
        System.out.println(languages.get("key"));
        languages.put("key", "another value");  // over-write the previous entry
            // returns the previous entry which is "value" in this case
            // returns null if there was no entry
        if(languages.containsKey("key")) {
            System.out.println("key is already in it");
        }

        // looping through the contents
        for(String key: languages.keySet()) {
            System.out.println(key + ":" + languages.get(key));
        }

        // removing
        if (!languages.remove("key2", "value2")) {
            System.out.println("not removed, key/value value not founc);
        }
        languages.remove("key2");
        
        // replace
        languages.replace("key", "if oldvalue matches ", "value replaced");
        languages.replace("key", "value replaced");
        languages.replace("key3", "does not exist");    // not added
    }
}
```

#### example
v135
```java
// class Location
Map<String, Integer> exits;

this.exits = new HashMap<String, Integer>();

public void addExit(String direction, int location) {
    exits.put(direction, location);
}

public Map<String, Integer> getExits() {
    // copy the exits and return the copy
    // the outside cannot change this.exits
    return new HashMap<String, Integer>(exits);
}


```
* split string
    ```java
    String[] road = "string this that".split(" ");
    String[] road2 = "string, this, that".split(", ");
    ```


### Immutable Classes
* [document](https://docs.oracle.com/javase/tutorial/essential/concurrency/imstrat.html)
* cannot be changed once it is created
* `private final`
    * final: the field shouldn't be changed
```java
public class Location {
    private final Map<String, Integer> exits;
    public Location(Map<String, Integer> exits) {
        this.exits = exits;
        this.exits.put("Q", 0);
    }
}

// main
private static Map<Integer, Location> locations = new HashMap<~>();
Map<String, Integer> tempExit = new HashMap<String, Integer>();
tempExit.put("W", 2);

locations.put(1, new Location(tempExit));
// I can still change tempExit
// because it is pointing the same object which is in the Location
tempExit.remove("W");   // like this
```
```java
// change in the Location constructor:
        // this.exits = exits;
        this.exits = new HashMap<String, Integer>(exits);
```
* problem with the constructor:
    * crash when `null` is passed
    * test before initialize
```java
if(exits != null) {
    this.exits = new HashMap<String, Integer>(exits);
} else {
    this.exits = new HashMap<String, Integer>();
}
```

* Regular expression: IntelliJ
    * Edit, Find, Replace..., tick Regex
    * `location.get\(\d\).addExit`
    * `tempExit.put`


### sets Hashset
* Sets:
    * no defined order (chaotic)
    * cannot contain duplicates
    * [compressed Oops](https://docs.oracle.com/javase/8/docs/technotes/guides/vm/performance-enhancements-7.html)
* methods:
    * `.addAll()`

In this example, the HeavenlyBody is mutable because moons can be added
but they do not affect the equals and hashCode. So it is okay to be used as key
```java
import java.util.Set;

public final class HeavenlyBody {
    private final String name;
    private final double orbitalPeriod;
    private final Set<HeavenlyBody> satellites;

    public HeavenlyBody(String name, double orbitalPeriod) {
        this.name = name;
        this.orbitalPeriod = orbitalPeriod;
        this.satellites = new HashSet<>()
    }

    // getters and setters

    public boolean addMoon(HeavenlyBody moon) {
        return this.satellites.add(moon);
    }

    public Set<HeavenlyBody> getSatellites() {
        return new HashSet<>(this.satellites);
    }
}

// main
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;
private static Map<String, HeavenlyBody> solarSystem = new HashMap<>();
private static Set<HeavenlyBody> planets = new HashSet<>();

HeavenlyBody temp = new HeavenlyBody("Earth", 365);
SolarSystem.put(temp.getName(), temp);
planets.add(temp);

HeavenlyBody tempMoon = new HeavenlyBody("Moon", 27);
solarSystem.put(tempMoon.getName(), tempMoon);
temp.addMoon(tempMoon);

for(HeavenlyBody planet : planets) {
    System.out.println(planet.getName());
    for(HeavenlyBody planetMoon : planet.getSatellites()) {
        System.out.println("\t" + planetMoon.getName());
    }
}

set<HeavenlyBody> moons = new HashSet<>();
for(HeavenlyBody planet : planets) {
    moons.addAll(planet.getSatellites());
}

// two plutos 
HeavenlyBody pluto = new HeavenlyBody("Pluto", 248);
plantes.add(pluto);
pluto = new HeavenlyBody("Pluto", 842);
plantes.add(pluto);
```
### equals hashcode
* without overriden: 
    * Object class uses referencial equality (it is default)
    * equal if both references point to the same object
    * othewise they are not equal
* Objects that are equal should have the same hashcode!!!
* [documentation on equals](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html#equals-java.lang.Object-)
```java
Object o = new Object();
o.equals(o);        // equals from Object class
"pluto".equals(""); // equals from String class (Overriden)
```
```java
// Override euqals and hashCode of HeavenlyBody
@Override
public boolean equals(Object obj) {
    if (this == obj) {
        return true;
    }
    if (( obj == null) || (obj.getClass() != this.getClass())) {
        return false;
    }

    String objName = ((HeavenlyBody) obj).getName();
    return this.name.equals(objName);
}

@Override
public int hashCode() {
    // 57 is small enough not to cause overflow
    // it make the hash different from String
    return this.name.hashCode() + 57;
}
```

### instanceOf geetClass
* compare getClass make sure it is not subclass
* when the class is final, do not need to worry too much

```java
public class Dog {
    private final String name;
    public Dog(String name) {
        this.name = name;
    }
    //getter getName

    @Override
    public final boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }

        if(obj instanceof Dog) {
            String objName = ((Dog) obj).getName();
            return this.name.equals(objName);
        }
        return false;
    }
}

public class Labrador extends Dog {
    public Labrador(String name) {
        super(name);
    }

    // should not override
    /* 
    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }

        if(obj instanceof Labrador) {
            String objName = ((Labrador) obj).getName();
            return this.getName().equals(objName);
        }
        return false;
    }
    */
}

public class DogMain {
    public static void main(String[] args) {
        Labrador rover = new Labrador("Rover");
        Dog rover2 = new Dog("Rover");

        System.out.println(rover2.equals(rover));   // true
        // Labrador is a Dog
        System.out.println(rover.equals(rover2));   // false
        // Dog is not a Labrador
    }
}
```
* How to fix? 
    * do not override equals in Labrador class
    * mark the equals final -> cannot be overriden

### Sets methods
* [set interface](https://docs.oracle.com/javase/tutorial/collections/interfaces/set.html)
* Set Interface Bulk Operations
    * destructive: modify the set they are called upon
    * `addAll`, `retainAll`, `containsAll`, `removeAll`
* all the Collections can take argument and initialize from it.
    * no argument creates an empty collection
* `asList`
    * returns a fixed-size list backed by the specified array
    * acts as bridge between array-based and collection-based APIs
```java
import java.util.HashSet;
import java.util.Set;
// main
Set<Integer> squares = new HashSet<>();
Set<Integer> cubes = new HashSet<>();

// union
for(int i = 1; i<=100; i++) {
    squares.add(i*i);
    cubes.add(i*i*i);
}
Set<Integer> union = new HashSet<>(squares);
union.addAll(cubes);

// intersection
Set<Integer> intersection = new HashSet<>(squares);
intersection.retainAll(cubes);
for(int i: intersection) {
    System.out.println(i + " : " + Math.sqrt(i) + " : " + Math.cbrt(i));
}

// using asList
Set<String> words = new HashSet<>();
String sentence = "one day in the ";
String[] arrayWords = sentence.split(" ");
words.addAll(Arrays.asList(arrayWords));
for (String s : words) {
    System.out.println(s);
}

// asymmetric difference
// nature takes divine
// devine takses nature
Set<String> nature = new HashSet<>();
Set<String> divine = new HashSet<>();
String[] natureWords = {"all", "nature", "is", "but"};
nature.addAll(Arrays.asList(natureWords));
String[] divineWords = {"is", "err", "human"};
devine.addAll(Arrays.asList(divineWords));
// nature takes divine
System.out.println("nature - divine: ");
Set<String diff1 = new HashSet<>(nature);
diff1.removeAll(divine);
printSet(diff1);


// symmetric difference
// union - intersection
Set<String> unionTest = new HashSet<>(nature);
unionTest.addAll(divine);
Set<String> intersectionTest = new HashSet<>(nature);
intersectionTest.removeAll(divine);
unionTest.removeAll(intersectionTest);
printSet(unionTest);

// containsAll
// non destructive
// check one is superset
if (nature.containsAll(divine)) {
    System.out.println("divine is a subset of nature");
}
```

```java
private static void printSet(Set<String> set) {
    System.out.println("\t");
    for(String s : set) {
        System.out.print(s + " ");
    }
    System.out.println();
}
```

### Example
* v148

```java
private final BodyTypes bodyType;

public enum BodyTypes {
    STAR,
    PLANET,
    MOON
}

public HeavenlyBody(BodyTypes bodyType) {
    this.bodyType = bodyType;
}

public BodyTypes getBodyType() {
    return bodyType;
}

public boolean addSatellite(HeavenlyBody moon) {
    return this.satellites.add(moon);
}

@Override
public final boolean equals(Object obj) {
    if (this == obj) {
        return true;
    }
    if(obj instanceof HeavenlyBody) {
        HeavenlyBody the Object = (HeavenlyBody) obj;
        if(this.name.equals(theObject.getName())) {
            return this.bodyType == theObject.getBodyType();
        }
    }
    return false;
}

@Override
public final int hashCode() {
    return this.name.hashCode() + 57 + this.bodyType.hashCode();
}
```
```java
// Planet subclass
public class Planet extends HeavenlyBody {
    public Planet(String name, double orbitalPeriod) {
        super(name, orbitalPeriod, BodyTypes.PLANET);
    }

    @Override
    public boolean addSatellite(HeavenlyBody moon) {
        if(moon.getBodyType() == BodyTypes.MOON) {
            return super.addSatellite(moon);
        } else {
            return false;
        }
    }
}
```
* for the key, create a inner class Key inside of HeavenlyBody
```java
public static final class Key {
    private String name;
    private BodyTypes bodyType;

    private Key(String name, BodyTypes bodyType) {
        this.name = name;
        this.bodyType = bodyType;
    }

    // getters

    @Override
    public boolean equals(Object obj) {
        Key key = (Key) obj;
        if(this.name.equals(key.getName())) {
            return (this.bodyType == key.getBodyType());
        }
        return false;
    }

    @Override
    public int hashCode() {
        return this.name.hashCode() + 57 + this.bodyType.hashCode();
    }
}


// use the inner class
private final Key key;

this.key = new Key(name, bodyType);

// in the equals code
if(obj instanceof HeavenlyBody) {
    HeavenlyBody theObject = (HeavenlyBody) obj;
    return this.key.equals(theObject.getKey());
}

// in the hashCode
return this.key.hashCode();
```

### Sorted Collections
* linked hash set, linked hash map
    * loop in order it based on comparTo
    * the items should implement Comparable
    * `new LinkedHashMap<>();`
* methods
    * `getOrDefault`
    * `Collections.unmodifiableMap(list);`
* linked hash map example: v150, v151
```java
public class StockItem implements Comparable<StockItem> {
    private final String name;
    private double price;
    private int quantityStock = 0;

    //... 
    @Override
    public boolean equals(Object obj) {
        if(obj == this) {
            return true;
        }

        if ((obj == null) || (obj.getClass() != this.getClass())) {
            return false;
        }

        String objName = ((StockItem) obj).getName();
        return this.name.equals(objName);
    }

    @Override
    public int hashCode() {
        return this.name.hashCode() + 31;
    }

    @Override
    public int compareTo(StockItem o) {
        if(this == o) {
            return 0;
        }
        
        if(o != null) {
            return this.name.compareTo(o.getName());
        }
        throw new NullPointerException();
    }
    //...
}
```
```java
// another class using the StockItem
private final Map<String, StockItem> list;
StockItem inStock = list.getOrDefault(item.getName() ,item);
public Map<String, StockItem> Items() {
    // read only view
    return Collections.unmodifiableMap(list);
}

// for loop
for (Map.Entry<String, StockItem> item : list.entrySet()) {
    StockItem stockItem = item.getValue();
    //...
 }
```


### TreeMap and Unmodifiable Maps
* `TreeMap`
    * alphabetical order
* un modifiable maps
    * the individual object in the collection can still be modified
    * if I don't have get method for the item, I don't want to have get method for the Collection either.
    ```java
    public Map<String, Double> PriceList() {
        Map<String, Double> prices = new LinkedHashMap<>();
        for(Map.Entry<String, StockItem> item : list.entrySet()) {
            prices.put(item.getKey(), item.getValue().getPrice());
        }
        return Collections.unmodifiableMap(prices);
    }
    ```

* challenge
