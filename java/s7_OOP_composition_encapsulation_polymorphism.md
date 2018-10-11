# OOP part2

### Composition
* 'has' relationship
* modeling parts
* composition vs inheritance:
    * composition: contain different objects of other classes
    * inheritance: only one parent class, 'is one of the kind'

```java
public class Main{
    public static void main(String[] args) {
        Motherboard motherboard = new Motherboard("macPro", 4);
        // can be directed created and passed (without variable name)
        // new Resolution
        Monitor monitor = new Monitor("LG", 100, new Resolution(10,10));

        PC myPC = new PC(monitor, motherboard);
        myPC.powerUp();
        // use getter function to access to the monitor
        thePC.getMonitor().drawPixelAt(10,3);
    }
}
```

```java
public class Motherboard {
    private String model;
    private int ramSlots;

    // constructor , getters setters

    public void loadProgram(String programName) {
        System.out.println("loading " + programName);
    }

    public void pressPowerButton() {
        System.out.println("PowerButton");
    }
}
```

```java
public class Monitor {
    private String model;
    private int size;
    private Resolution nativeResolution;


    public Monitor(String model, int size, Resolution resolution){
        this.model = model;
        this.size = size;
        this.nativeResolution = resolution;
    }

    // getters setters

    public void drawPixelAt(int x, int y) {
        System.out.println("Drawing pixet at " + x "," + y);
    }
}
```

```java
public class Resolution {
    private int width;
    private int height;

    // constructor getters and setters
}
```

```java
public class PC {
    // it has objects of other classes
    private Monitor monitor;
    private Motherboard motherboard;

    //constructor getters

    public void powerUp(){
        motherboard.pressPowerButton();
        drawLogo();
    }
    private void drawLogo() {
        monitor.drawPixelAt(10,10);
    }

    public Monitor getMonitor() {
        return monitor;
    }

```


### Encapsulation
* restrict access to certain components to other codes or classes
1. to prevent unauthorized access
2. do not want to change outside of code to change the class
3. to ensure data is valid: more control
* use private fields and use getters and setters for interact with outside of the code
70, 71: 30min
```java
public class Player {
    private String name;
    private int health = 100;

    public Player(String name; int health){
        this.name = name;
        if (health > 0) {
            this.health = health;
        }
    }
    public void loseHealth(int damage) {
        this.health = this.health - damage;
        if(this.health <= 0) {
            System.out.pritnln("Dead");
        }
    }

    public int healthRemaining() {
        return this.health;
    }
}
```
```java
public class Main {
    public static void main(String[] args) {
        Player player = new Player();
        player.name = "John";
        player.health = 20;
    }
}
```

### Polymorphism
72, 73: 40min

Can create a class within the same file:
```java
class Movie {
}

public class Main {
    Movie movie = new Movie(){
        // here inline modify
        // to the code
        // for example override methods
    }
}
```

### get class name
To refer the class name
`getClass().getSimpleName()`

