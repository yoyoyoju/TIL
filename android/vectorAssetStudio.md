# Vector Asset Studio

How to import svg file as drawble:

1. Add to `build.gradle` (Module:app)
```gradle
android{
    defaultConfig {
        vectorDrawables.useSupportLibrary = true
    }
}
```

2. Add a SVG file
Right click on `res` and select `New > Vector Asset`.
Choose Local file as Asset Type and set the path for the svg file, as well as the name.

3. Use the added drawable
Refer the drawable like "@drawable/name", using the name set in the above step 
