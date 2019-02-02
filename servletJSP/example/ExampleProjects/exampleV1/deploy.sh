TOMCAT_EXAMPLEV1=~/TIL/servletJSP/example/tomcat/webapps/Example-v1
DEV_EXAMPLEV1=~/TIL/servletJSP/example/ExampleProjects/exampleV1

# compile the project
# modify
# javac -classpath /the/path/to/the/jar -d classes src/something
javac -classpath ~/TIL/servletJSP/example/tomcat/lib/servlet-api.jar:classes:. -d classes $DEV_EXAMPLEV1/src/com/example/web/*.java
javac -classpath ~/TIL/servletJSP/example/tomcat/lib/servlet-api.jar:classes:. -d classes $DEV_EXAMPLEV1/src/com/example/model/*.java

# copy the classes into WEB-INF/classes
cp -r $DEV_EXAMPLEV1/classes $TOMCAT_EXAMPLEV1/WEB-INF/

# copy the web.xml file to WEB-INF
cp $DEV_EXAMPLEV1/etc/web.xml $TOMCAT_EXAMPLEV1/WEB-INF/web.xml

# copy *.jsp *.html in web into the deployment environment
cp $DEV_EXAMPLEV1/web/*.jsp $TOMCAT_EXAMPLEV1/
cp $DEV_EXAMPLEV1/web/*.html $TOMCAT_EXAMPLEV1/

# additional:
# file to be downloaded goes into the root
cp $DEV_EXAMPLEV1/etc/example_picture.jpg $TOMCAT_EXAMPLEV1/
