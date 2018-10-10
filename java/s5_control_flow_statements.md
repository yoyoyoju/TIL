# section: 5 - Control Flow statements

### switch statement
* to test one variable for different values
* without break the code continues to the next case 
* primitive types (byte, short, char, int) can be used as test variable
```java
int switchValue = 1;

switch(switchValue) {
    case 1:
        System.out.println("Value was 1");
        break;  // get out of switch block
    
    case 2:
        System.out.println("Value was 2");
        break;

    case 3:case 4:case 5: // test for multiple
        System.out.println("was a 3, or a 4, or a 5");
        break;

    default:    // for any other cases
        System.out.println("Was not 1 or 2");
        break;
}
```

* String can be also used (for later version than JDK7)
* it is case sensitive : use `.toLowerCase()` or `.toUpperCase()`
```java
String month = "January";
switch(month) {
    case "January":
        System.out.println("Jan");
        break;
    case "June":
        System.out.println("Jun");
        break;
    default:
        System.out.println("Not sure");
}

switch(month.toLowerCase()) {   // to test case insensitive
    case "january":
        System.out.println("Jan");
        break;
    default:
        System.out.println("Not sure");
}
```

### for statement
* to make a loop
* `break;` to break out for the loop
```java
for(init; termination; increment){
// initialize : init
// terminate when termination is false
// everytime : increment (iteration step)
// between {} body 
}
```
1. initialize by init
2. check termination condition
    * if true do the body
    * if false terminate (jump to out of the body)
3. do the increment
4. go back to step 2.

```java
for(int i=0; i<5; i++){
// i is created only for this loop. afterwards it is not accessable
    System.out.println("Loop " + i + " hello!");
    // print out 0, 1, 2, 3, 4
    // 5 times starting from 0
}
```

### format string
`String.format("%.2f", 700.0000000001);`
convert number to String until 2 decimal point


### while loop
* when I don't know when to stop before hand
* should set the init, increment manually
* `while(condition) { ... }`
```java
int count = 1;
while(count !=6) {
    // ...
    count++;
}

// equavalent for loop to the above while loop
for (int i=1; i<7; i++) {
// ...
}
```

can use break
```java
while(true) {       // go forever until break
    if(count == 6) {
        break;
    }
    // ...
    count++;        // should variable increment
}
```

may not be excuted at all.
```java
int count = 6;
while(count != 6) {
    // not excuted
    count++;
}

for (int i=6; i!=6; i++) {
    // not excuted
}
```

* continue ignore code down do again from the beginning.
* continue from the test (next iteration)
* test condition at the top
```java
int number = 4;
int finishNumber = 20;

while (number <= finishNumber) {
    number++;
    if(!isEvenNumber(number)) {
        continue;
    }

    System.out.println("Even number " + number);
}
```


### do while
* excuted at least once
* test condition at the bottom
* `do { ... } while (condition);` - semicolon at the end!
```java
int count = 1;
do {
    //excuted at least onec
    count++;
    if (count > 100) {
        break;
    }
} while(count !=6);
```

### parsing values from a string
* parse String as other primitive datatypes
* Integer: wrapper class of int
* if it fails gives an error ( it should be possible the type to convert to )
```java
String numberAsString = "2018";
int number = Integer.parseInt(numberAsString);
numberAsString += 1;    // concatenate string '1'  = '20181'
number += 1;            // arithmatic add 1 = 2019

String numberAsString2 = "2018a";
number = Integer.parseInt(numberAsString);
// gives an error
```
* parse into double type
```java
String numberAsString = "2018.125";
double number = Double.parseDouble(numberAsString);
numberAsString += 1;    // concatenate string '1'  = '2018.1251'
number += 1;            // arithmatic add 1 = 2019.125

String numberAsString2 = "2018.125a";
number = Double.parseDouble(numberAsString);
// gives an error
```

### user input
* use Scanner class
    * `import java.util.Scanner;`: import Scanner
    * `Scanner scanner = new Scanner(System.in);` create an instance
    * `scanner.nextLine();`
    * `scanner.nextInt();` : parse the user input, (enter should be handled after)
* should close after we use (release the underline memory)
    * `scanner.close();`
* common mistake:
    * after you read a number using `nextInt()`,
     the enter key should be handled by `nextLine()`.
     otherwise the next userinput will be skipped

```java
import java.util.Scanner;
public class Main {
    public static void main(String[] args) {
        // create instance of the class Scanner
        Scanner scanner = new Scanner(System.in);


        System.out.println("Enter your year of birth: ");
        // get user input and parse it into int
        int yearOfBirth = scanner.nextInt();
        scanner.nextLine(); // handle next line character (enter key)
        int age = 2018 - yearOfBirth;


        System.out.println("Enter your name: ");
        // read a line of input
        String name = scanner.nextLine();
        

        System.out.println("Your name is " + name);
        System.out.println("You are " + age + " years old.");

        scanner.close();
    }
}
```

### problems and solutions
* add some condition to the user input
    * print error if it is not in the range
    * InputMismatchException: when input is wrong type
        * use `hasNextInt()`
```java
// check next input is number
// allow to avoid type error
boolean hasNextInt = scanner.hasNextInt();
if (hasNextInt) {
    int yearOfBirth = scanner.nextInt();
    scanner.nextLine();

    int age = 2018 - yearOfBirth;
    if(age >= 0 && age <= 100) {
        System.out.println("age is " + age);
    } else {
        System.out.println("Invalid year of birth");
    }
} else {
    System.out.println("Unable to parse year of birth.");
}
```


### MIN MAX Constant
From min and max challenge:
```java
int min = Integer.MAX_VALUE;
int max = Integer.MIN_VALUE;
```
by initializing this, all the possible numbers are bigger than or equal to `min`
and all the possible numbers are smaller than or equal to `max`.

