### Setting and using Color resource


setting color in `res/values/colors.xml`:
```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
    <color name="opaque_red">#f00</color>
</resources>
```

Using color resource in java code:
```java
Resources res = getResources();
int color = res.getColor(R.color.opaque_red);
```

---
[ref](https://developer.android.com/guide/topics/resources/more-resources#Color) 


