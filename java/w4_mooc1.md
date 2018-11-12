# w4: basics of objects

### Methods and copying parameters
* primitive data types are copied as passed to a method
* references are copied as well. (the object itself is NOT copied)

* `String.format("%.2f", floatnum);`
* `String.format("%02d", intnum);`

### Randomness
```java
import java.util.Random;
Random randomizer = new Random();
randomizer.nextInt(10);     // random number [0, 9]
randomizer.nextDouble();    // random double [0..1]
randomizer.nextGaussian();
```

