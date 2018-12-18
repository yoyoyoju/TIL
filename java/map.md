# Map interface

### iteration
1. iterator and Map.Entry
```java
long i = 0;
Iterator<Map.Entry<Integer, Integer>> it = map.entrySet().iterator();
while (it.hasNext()) {
    Map.Entry<Integer, Integer> pair = it.next();
    i += pair.getKey() + pair.getValue();
}
```
2. foreach and Map.Entry
```java
long i = 0;
for (Map.Entry<Integer, Integer> pair : map.entrySet()) {
    i += pair.getKey() + pair.getValue();
}
```
3. foreach from java8
```java
final long[] i = {0};
map.forEach((k, v) -> i[0] += k + v);
```
4. keySet and foreach
```java
long i = 0;
for (Integer key : map.keySet()) {
    i += key + map.get(key);
}
```
5. keySet and iterator
```java
long i = 0;
iterator<Integer> itr2 = map.keySet().iterator();
while (itr2.hasNext()) {
    Integer key = itr2.next();
    i += key + map.get(key);
}
```
6. for and Map.Entryo
```java
long i = 0;
for (Iterator<Map.Entry<Integer, Integer>> entries = map. entrySet().iterator(); entries.hasNext(); ) {
    Map.Entry<Integer, Integer> entry = entries.next();
    i += entry.getKey() + entry.getValue();
}
```
7. Stream API (java8)
```java
final long[] i = {0};
map.entrySet().stream().forEach(e -> i[0] += e.getKey() + e.getValue());
```
8. Stream API parallel
```java
final long[] i = {0};
map.entrySet().stream().parallel().forEach(e -> i[0] += e.getKey() + e.getValue());
```
9. IterableMap of Apache Collections
```java
long i = 0;
MapIterator<Integer, Integer> it = iterableMap.mapIterator();
while (it.hasNext()) {
    i += it.next() + it.getValue();
}
```
10. MutableMap of Eclipse collections
```java
final long[] i = {0};
mutableMap.forEachKeyValue((key, value) -> {
    i[0] += key + value;
});
```


---
from [stackoverflow](https://stackoverflow.com/questions/46898/how-to-efficiently-iterate-over-each-entry-in-a-java-map)
