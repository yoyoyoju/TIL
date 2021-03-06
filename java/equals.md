# equals mothod override

* As default, Object class uses referencial equality
    * equal if both references point to the same object
* have to override hashCode() too!!!


### equality

* Reference equality
    * two references that refer to the same object on the heap are equal.
    * the default behavior of `equal`
    * to see two references are referring to the same object, use `==` operator
    * hashCode is based on the object's memory address on the heap
* Object equality
    * two references, two objects on the heap. they are meaningfully equivalent.
    * the hashCode and equals should be override


### Rules for equals and hashCode

* If two objects are equal, they must have matching hashCode
* if two objects are equals, calling equals on either object must return true
* if two objects have the same hashcode value, they are not required to be equals


### equals

* object class's equals: compare whether they have the same reference
    * ArrayList: uses `equals` for `contains`
* example:
```java
@Override
public boolean equals(Object object) {
    if (object == null) {
        return false;
    }
    if (this.getClass() != object.getClass()) {
        return false;
    }
    Book compared = (Book) object;
    if (this.publishingYear != compared.getPublishingYear()) {
        return false;
    }
    if (this.name == null || !this.name.equals(compared.getName())) {
        return false;
    }
    return true;
}
```

* Another example using `instanceof`: when the class is final
```java
// when the class is final
@Override
public boolean equals(Object object) {
    if (object == this)
        return true;

    if (!(object instanceof Coordinate))
        return false;

    Coordinate other = (Coordinate) object;

    return (this.width == other.getWidth()) &&
            (this.height == other.getHeight());
}
```

### hashCode
* hashCode: returns hash value
    * used for HashMap keys
    * same (based on the `equals` method) objects should return the same hash value
* example hashMap
```java
public int hashCode() {
    if (this.name == null) {
        return 7;
    }
    return this.name.hashCode() + this.publishingYear;
}
```

* another example with two fields
```java
@Override
public int hashCode() {
    int result = Integer.hashCode(this.width);
    result = 31 * result + Integer.hashCode(this.height);
    return result;
}
```


* type casting: `WantedType variable = (WantedType) oldVariable;`


---
reference: **headfirst java** chapter 16
