### forEach for string
* to loop through a string: `toCharArray()`
```java
public boolean containsAllVowels(String word) {
    String vowels = "aeiou";
    for (char vowel : vowels.toCharArray()) {
        if (!word.contains("" + vowel)) {
            return false;
        }
        return true;
    }
}
```

### methods
* `contains`
* `endsWith`
* `equals`
* `trim`
* `split`

#### split
example:
```java
String line = "word:translation";
String[] parts = line.split(":");
System.out.println(parts[0]);
System.out.println(parts[1]);
```



### format
* numbers to String
    ```java
    double d = 42.5;
    String doubleString = ""+d;
    String anotherWay = Double.toString(d);
    ```
* formatting
    * examples
        ```java
        String.format("%s %.1f", "some String", 1.0002);
        String.format(Locale.ROOT, "%s %.2f", "when the format uses local decimal point (,) to make sure use (.)", 1.2312);
        String.format("the number is %.2f.", 2423.1231); //format the number as a floating point with a precision of two decimal places
        String.format("%,6.1f", 42.000);
        
        ```
    * to use commas
        ```java
        int numberToFormat = 10000000;
        String formattingInstruction = "%, d";  // insert commas and format the number as a decimal integer
        String s = String.format(formattingInstruction, numberToFormat);
        ```
    * the format specifier
        * can have upto five different parts
        * everything in brackets [] below is optional
        * the percent `%` and the type are required
        * the order is also mandatory
        * `%` : insert argument here
        * [argument number] : which argument if there's more than one
        * [flags]: for special formatting options
            * inserting commas
            * putting negative numbers in parentheses
            * make the numbers left justified
        * [width]: defines the minimum bumber of characters that will be used
            * if the number is longer, it will still be used in full
            * if it is less, it will be padded with zeros
        * [.precision]: sets the number of decimal places
        * type: mandatory
            * d: decimal integer (for byte, short, int, char and their wrapper types)
            * f: floating point number (for float, double and BigDecimal)
            * x: hexadecimal (for byte, short, int, long, BigInteger)
            * c: character (for byte, short, char, int)


### Format Date
* use a two-character type that starts with `t`
    * the complete date and time:
        * `%tc`
        * `String.format("%tc", new Date());`
    * just the time
        * `%tr`
        * `String.format("%tr", new Date());`
    * day of the week, month and day
        * day of the week: `%tA`
        * month: `%tB`
        * day of the month: `%td`
        * `Date today=new Date(); String.format("%tA, %tB %td", today, today, today);`
    * day of the week, month and day, without duplicating the arguments
        * using `<` flag : use the previous argument again
        * `String.format("%tA, %<tB %<td", today);`
