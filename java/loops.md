# Loops

### continue
* in addition to the break statement, loops have also continue statement
* skip to the following loop stage
* used especially when the iterable variables got values with which we do not want to handle at all


* example of continue
```java
List<String> names = Arrays.asList("Matti", "Pekka", "Arto");
for(String name : names) {
    if (name.equals("Arto")) {
        continue;
    }
    System.out.println(name);
}
// the printing results are:
// Matti
// Pekka
```

* compare to if statement
```java
List<Integer> values = Arrays.asList(1, 3, 11, 6, 12);
// using if statement:
for(int num : values) {
    if (num > 4 && num % 100 != 0 && num % 40 != 0) {
        System.out.println(num);
    }
}
// using continue:
for (int num : values) {
    if (num < 5) {
        continue;
    }
    if (num % 100 == 0) {
        continue;
    }
    if (num % 40 == 0) {
        continue;
    }
    System.out.println(num);
}
// both prints the same result:
// 11
// 6
```

------
reference
[mooc.fi week12: 54.4 Loops and continue](https://materiaalit.github.io/2013-oo-programming/part2/week-12/)
