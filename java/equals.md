# equals mothod override
* As default, Object class uses referencial equality
    * equal if both references point to the same object
* have to override hashCode() too!!!

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

* type casting: `WantedType variable = (WantedType) oldVariable;`

