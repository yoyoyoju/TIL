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

### UI Components

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

### Separation Application and UI Logic
* mixing the application logic and user interface in the same classes is not a good idea.
    * it makes harder to test and read. also harder to modify the program
* implement user interface:
1. adding the components to it:
    * which fields do we need?
    * which layout do we use?
2. action event listener:
    * functionality: 
        * an object with functionalities (of an interface) is passed to the constructor
    * which fields are used?: 
        * the neccessary fiedls are passed to the constructor
```java
public interface PersonRecord {
    // interface with neccessary methods
    // to perform the functionality
}

public class PersonRecordListener implements ActionListener {
    // ... fields
    public PersonRecordListener(PersonRecord personRecord, JTextField nameField){
        // set the parameters to the fields
    }
    @Override
    public void actionPerformed(ActionEvent ae) {
        // perform the action
        // using personRecord and nameField
    }
```
3. add action event listener to the ui components
    * the object of PersonRecord should be passed to the constructor of UI
    * create an instance of `PersonRecordListener` and add it to the button
```java
public class UserInterface implements Runnable {
    private JFrame frame;
    private PersonRecord personRecord;
    public UserInterface(PersonRecord personRecord) {
        this.personRecord = personRecord;
    }
    //...

    private void createComponents(Container container) {
        // ...
        PersonRecordListener listener = new PersonRecordListener(personRecord, nameField);
        addButton.addActionListener(listener);
        //...
    }
}
```

### Nested Container Objects
* we can place Container objects insie each other
* class `JPanel` allows for nested Container objects
* one can add an instance of JPanel to a Container object
* example
```java
private void createComponents(Container container) {
    container.add(new JTextArea());
    container.add(createPanel(), BorderLayout.SOUTH);
}

private JPanel createPanel() {
    // layout as constructor parameter
    // can be also set with setLayout method
    JPanel panel = new JPanel(new GridLayout(1, 3));
    panel.add(new JButton("Execute"));
    panel.add(new JButton("Test"));
    panel.add(new JButton("Send"));
    return panel;
}
```
* another way to do
```java
import java.awt.GridLayout;
import javax.swing.JButton;
import javax.swing.JPanel;

public class MenuPanel extends JPanel {
    public MenuPanel() {
        super(new GridLayout(1, 3));
        createComponents();
    }
    private void createComponents() {
        add(new JButton("Execute"));
        add(new JButton("Test"));
        add(new JButton("Send"));
    }
}
// int the ui.createComponents
private void createComponents(Container container) {
    container.add(new JTextArea());
    container.add(new MenuPanel(), BorderLayout.SOUTH);
}
```
-----
references:
[MOOC.fi week11](https://materiaalit.github.io/2013-oo-programming/part2/week-11/)
