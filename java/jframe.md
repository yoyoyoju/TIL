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


### User event
* event-handling


--- 
*headfirst java* ch12 getting gui
