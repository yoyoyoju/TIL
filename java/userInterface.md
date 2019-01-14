# User Interfaces

### Swing
* swing library
    * class JFrame
        * user interface contains a JFrame object
        * All user interface components are added to the JFrame object component container
        * object variables cannot be initiated outside the methods
            * ui object variables should be initiated either in the constructor or methods
            * for example `private JFrame frame = new JFrame()` in the class definition
             would evade user interface thread execution order,
             and it can lead to a breakdown.
    * interface Runnable 
        * which allows us to execute a threaded program
        * started in main program
        * defines the method `public void run()`
```java
import java.awt.Container;
import java.awt.Dimension;
import javax.swing.JFrame;
import javax.swing.WindowConstants;

public class UserInterface implements Runnable {
    private JFrame frame;

    public UserInterface() {
    }

    @Override
    public void run() {
        // create a new JFrame
        frame = new JFrame("Title");
        // define the frame size with width 200 pixels and height 100 pixels
        frame.setPreferredSize(new Dimension(200, 100));
        // the user interface has to close when the user presses the cross icon
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        createComponents(frame.getContentPane());
        // packs the JFrame object as defined before and 
        // sorts the user interface components of the Container object contained by JFrame
        frame.pack();
        // show the user interface to the user
        frema.setVisible(true);
    }

    private void createComponents(Container container) {
        // add user interface components to the JFrame's container
    }

    public JFrame getFrame() {
        // returns the JFrame object 
        return frame;
    }
}
```
* swing user interface are started through the method `invokeLater`
    * provided by the class SwingUtilities
    * recieves a `Runnable` as a parameter
    * adds the Runnable object to the execution queue and calls it ASAP.
    * with class `SwingUtilities` we can start new threads when we need them
```java
import javax.swing.SwingUtilities;

public class Main {
    public static void main(String[] args) {
        UserInterface ui = new UserInterface();
        SwingUtilities.invokeLater(ui);
    }
}
```

#### UI Components

* User Interfaces are composed of
    * a background window (JFrame)
    * a component Container
    * UI components 
        * are set into the container
        * different kinds of buttons, texts and other items
        * Every component has its own class
        * [Oracle visual sequence of components](https://docs.oracle.com/javase/tutorial/uiswing/components/index.html)


* Text
    * added to the container as an object of class `JLabel`
    * text is set in the constructor
    * text can also be set by `setText` method
```java
private void createComponents(Container container) {
    JLabel text = new JLabel("Text field");
    container.add(text);
}
```

* Buttons
    * class JButton
```java
private void createComponents(Container container) {
    JButton button = new JButton("Click!");
    container.add(button);
}
```

* setting up UI Components
    * the component location is defined by the UI Layout Manager
    * the default UI layout manager of every Container object: BorderLayout
        * can be set like `container.setLayout(new BorderLayout());`
        * [more about layout](http://docs.oracle.com/javase/tutorial/uiswing/layout/visual.html)
    * additional parameter for `add`: (for BorderLayout class)
        * BorderLayout.NORTH, .EAST, .SOUTH, .WEST, .CENTER

```java
private void createComponents(Container container) {
    container.setLayout(new BorderLayout());
    container.add(new JButton("North"), BorderLayout.NORTH);
    // button Center is not visible because Default(Center) is assigned to center too
    container.add(new JButton("Center"), BorderLayout.CENTER);
    container.add(new JButton("Default (Center)"));
}
```

* BoxLayout
    * UI components are added either horizontally or vertically (given in the constructor)
    * `new BoxLayout(container, BoxLayout.X_AXIS);`: components are set up horizontally
    * `new BoxLayout(container, BoxLayout.Y_AXIS);`: vertically
    * do not have a limitied number of places
```java
private void createComponents(Container container) {
    BoxLayout layout = new BoxLayout(container, BoxLayout.X_AXIS);
    container.setLayout(layout);
    container.add(new JLabel("First"));
    container.add(new JLabel("Second"));
```

* ButtonGroup and JRadioButton
    * create a multiple-exclusion scope
```java
private void createComponents(Container container) {
    BoxLayout layout = new BoxLayout(container, BoxLayout.Y_AXIS);
    container.setLayout(layout);
    container.add(new JLabel("Choose meat or fish:"));

    JRadioButton meat = new JRadioButton("Meat");
    JRadioButton fish = new JRadioButton("Fish");

    ButtonGroup buttonGroup = new ButtonGroup();
    buttonGroup.add(mean);
    buttonGroup.add(fist);

    container.add(meat);
    container.add(fist);
```

-----
references:
[MOOC.fi week11](https://materiaalit.github.io/2013-oo-programming/part2/week-11/)
