# javaFX

### install and configure
* download [link](https://gluonhq.com/products/javafx/)
* configure in IntelliJ (set global library)
    * configure -> Project default -> Project structure
    * under Platform Settings -> Global Libraries
    * new Global Library -> Java
    * select all the jar files in lib
    * set name

### create javaFX project
* create new Project
* select JavaFX
* right click the project from left navigation menu -> open module settings
* Under project settings: Project
    * check the SDK : 11
    * Project language level : the same as SDK  - 11
* Modules
    * language level : the same as above
* Under Platform Settings : Global Libraries
    * right click the Library (javafx)
    * add to Modules...
    * click okay
* should add javafx-info.java
    * right click src from left navigation menu
    * select New
    * select module-info.jav
    * add inside of the module
    ```java
    requires javafx.fxml;
    requires javafx.controls;

    opens sample;   // package name
    ```
    
### JavaFX Overview
* designed with the MVC(Model-View-Controller) pattern in mind
* this pattern keeps the code that handles an application's data separate form the UI code
* controller is the middleman between the UI and data (do not mix them)
* the files:
    * Controller.java
    * sample.fxml
    * Main.java

### HelloWorld
* no data to deal with -> empty controller
* Main extends Application (javafx.Application)
    * must have a class which extends Application
    * this class will be the entry point for the application
    * the application class manages the lifecycle of a JavaFX application.
    * `init` method `start` method, `stop` method
    * when we run, Application.launch will be called from main method
    * `init` method -> `start` method
        * start method should be overriden as it is abstract
        * in the start method we create the UI
    * when the application finishes, run `stop` method
* Stage:
    * a top-level JavaFX container that extends the window class
    * The JavaFX runtime constructs the initial stage and passes it into the start method
    * requires scene
        * backing each scene is a scene graph 
        * a scene graph:  a tree wich each node corresponds to a UI control or an area of the scene
        * 
    * corresponds to a top level UI container like a window
    * a scene is backed by a scene graph which contains the UI nodes
* FXML:
    * a flavor of XML
* Parent class
    * descend from the node class
```java
@Override
public void start(Stage primaryStage) throws Exception{
    Parent root = FXMLLoader.load(getClass().getResource("sample.fxml");
    // load at the FXML and assign it to a variable of type Parent with the name root
    // the sample.fxml has only GridPane: the only node is the GridPane
    // the GridPane node will be returned by the FXMLLoader.load
    primaryStage.setTitle("Hello World");
    primaryStage.setScene(new Scene(root, 700, 275));
    // we construct the scene (pass the root)
    // the root will back the scene
    // set the width and height of the scene (main window)
    primaryStage.show();
}
```

### Hello World2
* instead of using fxml file, 
```java
// in the start method
// instead of
// Parent root = FXMLLoader.load(getClass().getResource("sample.fxml");
GridPane root = new GridPane();
root.setAlignment(Pos.CENTER);
root.setVgap(10);
root.setHgap(10);
```

* Label
```java
Label greeting = new Label("Welcome");
greeting.setTextFill(Color.GREEN);  // set the color (import Color)
greeting.setFont(Font.font("Times New Roman"), FontWeight.BOLD, 70);
root.getChildren().add(greeting);
```

* fxml with label
    * add label between open and close GridPane
    ```fxml
    <Label text="Welcome" textFill="green">
        <font>
            <Font name="Times New Roman bold" size="70"/>
        </font>
    </Label>
    ```

* better to stick to fxml
    * when changing the looks does not need to touch the java code

### GridPane Layout
* 8 layouts
    * gridpane, anchorpane, stackpane, h box, vbox, flow pane, tilepane, border pane
    * determine how much space I control I ultimately get
    * when the controller is placed int a layout, it becomes a child of that layout
    * layouts ensure their children display at the preferred widths or heights
* preferred size:
    * preferred width and height of the control when it's displayed


* GridPane
    * alignment 
        * "center", "top_center" (no gap above)
    * hgap, vgap (gaps in between rows and columns)
    * `gridLinesVisible="true"` to show the gridLines (z.B. for debugging)
* columnConstranints class in the GridPane
    * ordering is important
        * first is for first column, second is for second column
        * can set pixelwise as well
    ```java
    <columnConstraints>
        <ColumnConstraints percentWidth="50.0"/>
        <ColumnConstraints percentWidth="50.0"/>
    </columnConstraints>
    ```
* add buttons
    * have to add row, column (otherwise they will overlap)
    * each column is the width of the widest column
```java
// fxml file
// in the GridPane
<Button text="Button One" GridPane.rowIndex="0" GridPane.columnIndex="0"/>
<Button text="Button Two" GridPane.rowIndex="0" GridPane.columnIndex="1"/>
```
* comment out
    ```fxml
    <!--<...>-->
    ```

### alignment
* add padding
    ```fxml
    <padding>
        <Insets top="10"/>
    </padding>
    ```
* row span property
    * take up multipul columns
    ```fxml
    <Button text="Button Three" GridPane.rowIndex="3" GridPane.columnIndex="0"
        GridPane.columnSpan="2"/>
    ```
* h alignment property
    ```fxml
    <Button text="Button Three" GridPane.rowIndex="3" GridPane.columnIndex="0"
        GridPane.halignment="RIGHT"/>
    ```


* Hbox Layout
    * commonly used dialogue situation as a child of other layout
    * fillHeight is true for defalut
    * style, using css
    * spacing: add the specified gap in between each child
* padding
```fxml
<HBox fx:controller="sample.Controller"
    xmln:fx="http://javafx.com/fxml" alignment="bottom_right"
    style="-fx-border-color: red; -fx-border-width: 3 -fx-border-style: dashed"
    spacing="10">

    <padding>
        <Insets bottom="10" right="10"/>
    </padding>
    
    <Button text="Okay" prefWidth="90"/>
    <Button text="Cancle" prefWidth="90"/>
```

### BorderPane Layout
* commonly used as top-level window
* has top, left, center, right, bottom

* nested layout
    * layout inside of layout
```fxml
<BorderPane fx:controller="sample.Controller"
    xmlns:fx="http://javafx.com/fxml">

    <top>
        <Label text="This is top" alignment="center"
            BorderPane.alignment="center"
            style="-fx-border-color: blue; -fx-border-width: 3; -fx-border-style: dashed"/>
    </top>

    <center>
        <Label text="center text"/>
    </center>

    <left>
        <Label text="left Label" alignment="center"/>
    </left>

    <right>
        <Label text="right Lebel"/>
    </right>

    <bottom>
        <HBox spacing="10" alignment="top_right">
            <padding>
                <Insets bottom="10" right="10"/>
            </padding>
            <Button text="Okay"/>
        </HBox>
    </bottom>
</BorderPane>
```

### Flow Pane
* similar to HBox, VBox but children won't be cut off wrap the children into the next (row or col)
```fxml
<FlowPane fx:controller="sample.Controller"
    xmlns:fx="http://javafx.com/fxml" orientation="HORIZONTAL">
    <Button text="Button one"/>
</FlowPane>
```

* Tile Pane
    * like flow pane but all the buttons have the same space
* StackPane
    * laying on top of each other
    * first control is on the bottom, last child on the top of the stack
    * (ex) when place text on top of a image
