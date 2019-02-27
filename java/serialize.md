# serialize


### write a serialized object to a file
```java
// 1. make a FileOutputStream
// if the file does not exist, create automatically
FileOutputStream fileStream = new FileOutputStream("MyGame.ser");

// 2. make an ObjectOutpuStream
ObjectOutputStream os = new ObjectOutputStream(fileStream);

// 3. write the object
os.writeObject(one);
os.writeObject(two);

// 4. close the ObjectOutputStream
// it closes ones underneath (FileOutputStream)
os.close();
```

### connection and chain
* Connection streams
    * a connection to a source or destination (file, socket)
    * FileOutputStream: write bytes to a file
* Chain streams
    * should be chained to connection streams
    * ObjectOutputStream: flattens (serialize) objects


### Serializable
* Serializable interface
    * marker or tag interface (doesn't have to implement any methods)
    * to announce that the class is serializable
    * to be able to serialize, the entire object graph is serialized
    * mark an instance variable as `transient` if it shouldn't be saved


### deserialize
* when the superclass is a non-serializable
    * the superclass constructor will run just as though a new object of that type were being created
* when a variable is transient
    * they will brought back as null(object references) or default value (primitives)
    * reinitialize the variable
```java
// 1. make a FileInputStream
// if the file does not exist, throw an exception
FileInputStream fileStream = new FileInputStream("MyGame.ser");

// 2. make an ObjectInputStream
ObjectInputStream os = new ObjectInputStream(fileStream);

// 3. read the objects
// read back in the same order in which they were written
// throw exception if try to read more objects than you wrote
Object one = os.readObject();
Object two = os.readObject();

// 4. Cast the object
GameCharacter elf = (GameCharacter) one;
GameCharacter troll = (GameCharacter) two;

// 5. close the ObjectInputStream
// close the ones underneath
os.close();
```
* what happens
    1. the object is read from the stream
    2. the JVM determines the object's class type
    3. the JVM attempts to find and load the object's class. If the JVM cannot, throws an exception
    4. a new object is given space on the heap, but the serialized object's constructor does not run
    5. if the object has a non-serializable class somewhere up its inheritance tree,
        the constructor for that non-serializable class will run along with any constructors above that.
    6. the object's instance varibales are given the values from the serialized state.
        Transient variables are given a value of null for object references and defaults for primitives.
    7. static variables are not saved, and when an object is deserialized, it will have whatever static variable its class currently has.
