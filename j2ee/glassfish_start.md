# GlassFish
* Open Source Java EE Reference Implementation

### configure to start
* GlassFish5 works upto JDK8 (currently January 2019)
* configure to let the GlassFish use the right version of JDK
* if it is not connected to the right version, it gives some error
* one way to set the JDK version is using `glassfish/config/asenv.conf` file
* example: in the `asenv.conf` file add
    `AS_JAVA="/Library/Java/JavaVirtualMachines/jdk1.8.0_201.jdk/Contents/Home"`

* modify the environment variabl `JAVA_HOME` in the `.bash_profile` file
* to see run `echo $JAVA_HOME` to see the current value
[ref](https://matthiashoys.wordpress.com/2012/09/10/how-to-modify-the-version-of-java-used-for-glassfish-3-1-2-2/)

### first start
* in the directory where the glassfish is,
    ```shell
    $ glassfish5/glassfish/bin/asadmin start-domain
    ```
* in the brower, go to `http://localhost:8080`
* to manage, go to `http://localhost:4848`
* to stop, 
    ```shell
    $ glassfish5/glassfish/bin/asadmin stop-domain
    ```


