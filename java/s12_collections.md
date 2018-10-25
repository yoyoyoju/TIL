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
```


### Sets Symmetric Asymmetric

* challenge

### Sorted Collections

### TreeMap and Unmodifiable Maps

* challenge
