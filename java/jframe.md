 # JFrame
* JFrame is the object that represents a window on the screen
    * where to put all the interface things like buttons, checkboxes, text fields, and so on.
    * it can have a menu bar with menu items
    * it has windowing icons like minimizing, maximizing, and closing the window
    * one can put widgets in it (from javax.swing package such as JButton, JRadioButton, etc)
* making a GUI:
    0. import swing package `import javax.swing.*;`
    1. Make a frame(a JFrame) 
    ```java
    JFrame frame = new JFrame();
    // makes the program quit as soon as you close the window
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    ```
    2. Make a widget(button, text field, etc) `JButton button = new JButton("click me");`
    3. Add the widget to the pane of the frame `frame.getContentPane().add(button);`
    4. Display it (give it a size and make it visible) `frame.setSize(300, 300); frame.setVisible(true);`


### graphics
* three ways to put stuff on the screen
    1. put widgets on a frame `frame.getContentPane().add(myButton);`
    2. Draw 2D graphics on a widget `graphics.fillOval(70, 70, 100, 100);`
    3. Put a JPEG on a widget `graphics.drawImage(myPic, 10, 10, this);`
* drawing widget
    * make a subclass of JPanel and override a method, `paintComponenet(Graphics g)`
    * all the graphics code goes inside the paintComponent method
    * I don't call the paintComponent myslef.


### User event
* event-handling
    * implement a listener interface: call-back method is declared
    * a listener interface is the bridge between the listener and event source
* event source
    * an object that can turn user actions into events
        * events are objects (see java.awt.event package)
    * an evnet source (like a button) creates an event object according to the user action
    * every event type has amatching listener interface
        * MouseEvent - MouseListener interface
        * WindowEvent - WindowListener interface
        * ActionEvent - ActionListener interface
            * actionPerformed(ActionEvent ev)
        * ItemEvent - ItemListener interface
            * itemStateChanged(ItemEvent ev)
        * KeyEvent - KeyListener interface
            * keyPressed(KeyEvent ev)
            * keyReleased(KeyEvent ev)
            * keyTyped(KeyEvent ev)
        * I must implement the interface (implement all the methods in it)
* how it works
    * The Listener
        * implements Listener interface (corresponding to the event)
        * register itself to the Event Source (like button)
            * by `button.addActionListener(this)`
        * has `actionPerformed` method
        * the button calls the method `actionPerformed` when an action event happens
    * The Event Source
        * such as a button
        * has a list of listeners (added by `addActionListener(reference to the Listener object)`)
        * when the event happens, call the `actionPerformed(ActionEvent event)` method on each listener in the list
    * The Event object
        * argument to the event call-back method
        * carry data about the event back to the listener
* how to
    1. implement the ActionListener interface
    2. register with the button (by button.addActionListener)
    3. define the event-handling method (by implementing actionPerformed)
    ```java
    // example code
    // implement the interface
    // register with the button
    // provide the event-handling
    import javax.swing.*;
    import java.awt.event.*;    // for ActionListener and ActionEvent
    public class SimpleGui1B implements ActionListener {
        JButton button;
        public static void main(String[] args) {
            SimpleGui1B gui = new SimpleGui1B();
            gui.go();
        }

        public void go() {
            JFrame frame = new JFrame();
            button = new JButton("click me");
            button.addActionListener(this);
            // the button: event source
            // accept registrations (from listners)
            // get events from the user
            // call the listener's event-handling method

            frame.getContentPane().add(button);
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setSize(300, 300);
            frame.setVisible(true);
        }

        public void actionPerformed(ActionEvent event) {
            button.setText("I've been clicked!");
        }
    }
    ```

--- 
*headfirst java* ch12 getting gui
