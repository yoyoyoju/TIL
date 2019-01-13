# User Interfaces

### Swing
* swing library
    * class JFrame
        * user interface contains a JFrame object
        * All user interface components are added to the JFrame object component container
        * object variables cannot be initiated outside the methods
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

###

-----
references:
[MOOC.fi week11](https://materiaalit.github.io/2013-oo-programming/part2/week-11/)
