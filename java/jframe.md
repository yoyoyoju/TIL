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
    ```java
    public void go() {
        JFrame frame = new JFrame();
        JButton button = new JButton("Click");
        Font bigFont = new Font("serif", Font.BOLD, 28);
        button.setFont(bigFont);
        frame.getContentPane().add(BorderLayout.NORTH, button);
        frame.setSize(200, 200);
        frame.setVisible(true);
    }
    ```



### graphics
* three ways to put stuff on the screen
    1. put widgets on a frame `frame.getContentPane().add(myButton);`
    2. Draw 2D graphics on a widget `graphics.fillOval(70, 70, 100, 100);`
    3. Put a JPEG on a widget `graphics.drawImage(myPic, 10, 10, this);`
* drawing widget
    * make a subclass of JPanel and override a method, `paintComponenet(Graphics g)`
    * all the graphics code goes inside the paintComponent method
    * I don't call the paintComponent myslef.
* Graphics and Graphics2D
    * methods for Graphics
        * drawImage()
        * drawLine()
        * drawPolygon
        * drawRect()
        * drawOval()
        * fillRect()
        * fillRoundRect()
        * setColor()
    * Graphics2D g2d = (Graphics2D) g;
        * fill3DRect()
        * draw3DRect()
        * rotate()
        * scale()
        * shear()
        * transform()
        * setRenderingHints()
* examples
    ```java
    import java.awt.*;
    import javax.swing.*;

    class MyDrawPanel extends JPanel {
        public void paintComponent(Graphics g) {
            g.setColor(Color.orange);
            g.fillRect(20, 50, 100, 100);

            // jpg file
            Image image = new ImageIcon("catzilla.jpg").getImage();
            // or, for IDE
            // Image image = new ImageIcon(getClass().getResource("catzilla.jpg")).getImage();
            g.drawImage(image, 3, 4, this); // 3 pixel from the left edge of the panel, 4 pixel from the top

            // randomly-colored circle on a black background
            g.fillRect(0, 0, this.getWidth(), this.getHeight()); // fill with default(black) color
            int red = (int) (Math.random() * 256);
            int green = (int) (Math.random() * 256);
            int blue = (int) (Math.random() * 256);
            Color randomColor = new Color(red, green, blue);
            g.setColor(randomColor);
            g.fillOval(70,70,100,100);
        }
    }
    ```


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


### two buttons
* How to deal with two different buttons: options
    1. Register the same listener with both buttons
        ```java
        class MyGui implements ActionListener {
            public void go() {
                colorButton = new JButton();
                labelButton = new JButton();
                colorButton.addActionListener(this);
                labelButton.addActionListener(this);
            }
            public void actionPerformed(ActionEvent event) {
                if(event.getSource() == colorButton) {
                    frame.repaint();
                } else {
                    label.setText("new text");
                }
            }
        }
        ```
    2. Create two separate ActionListener classes
    ```java
    public class TwoButtons {
        JFrame frame;
        JLabel label;
        public static void main(String[] args) {
            TwoButtons gui = new TwoButtons();
            gui.go();
        }

        public void go() {
            frame = new JFrame();
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

            JButton labelButton = new JButton("Change Label");
            labelButton.addActionListener(new LabelListener());

            JButton colorButton = new JButton("Change Circle");
            colorButton.addActionListener(new ColorListener());

            label = new JLabel("label");
            MyDrawPanel drawPanel = new MyDrawPanel();

            frame.getContentPane().add(BorderLayout.SOUTH, colorButton);
            frame.getContentPane().add(BorderLayout.CENTER, drawPanel);
            frame.getContentPane().add(BorderLayout.EAST, labelButton);
            frame.getContentPane().add(BorderLayout.WEST, label);

            frame.setSize(300, 300);
            frame.setVisible(true);
        }

        class LabelListener implements ActionListener {
            public void actionPerformed(ActionEvent event) {
                label.setText("changed");
            }
        }

        class ColorListener implements ActionListener {
            public void actionPerformed(ActionEvent event) {
                frame.repaint();
            }
        }
    }
    ```


### Layout
* *headfirst java* ch13
* Big three layout managers:
    * BorderLayout
        * default layout for a frame `frame.getContentPane().add(BorderLayout.EAST, button);`
        * five regions, one component per region
            * BorderLayout.EAST, WEST: preferred width, height is upto layout manager
            * NORTH, SOUTH: get preferred height, width is upto layout manager
            * CENTER: gets left over space (unless you use pack())
    * FlowLayout
        * each components added left to right (or top to bottom)
        * in order they were addded
        * wrapping to a new line when needed
        * each component is the size it wants to be
        * default layout for a panel (use panel.setLayout() on the panel to set something else)
    * BoxLayout
        * stack the components vertically (or horizontally)
        * each component gets to have its own size
        * placed in the order in which they're added
        ```java
        public void go() {
            JFrame frame = new JFrame();
            JPanel panel = new JPanel();
            panel.setBackground(Color.darkGray);
            panel.setLayout(new BoxLayout(panel, BoxLayout.Y_AXIS));
            JButton button = new JButton("one");
            JButton buttonTwo = new JButton("two");
            panel.add(button);
            panel.add(buttonTwo);
            frame.getContentPane().add(BorderLayout.EAST, panel);
            frame.setSize(250, 200);
            frame.setVisible(true);
        }
        ```


### swing components
* JTextField
    * `JTextField field = new JTextField(20); // 20 columns of the preferred width`
    * `JTextField field = new JTextField("name");`
    * methods
        * field.getText(): get text out of it
        * field.setText("text"): put text in it; setText(""): clears the field
        * field.addActionListener(myActionListener); 
            * get an actionevent when the user presses return or enter
            * can also register for keyevents if want to hear about it every time the user presses a key
        * field.selectAll(); select/highlight the text in the field
        * field.requestFocus(); put the cursor back in the field
* JTextArea
    * can have more than one line of text
    * to make a JTextArea scroll, have to stick it in a ScrollPane
    * `JTextArea text = new JTextArea(10, 20);` 10 lines, 20 columns
    * methods
        * make it have a vertical scrollbar only
            ```java
            JScrollPane scroller = new JScrollPane(text); // text is a JTextArea
            text.setLineWrap(true);
            scroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
            scroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
            panel.add(scroller);
            ```
        * replace the text that's in it `text.setText("...");`
        * append to the text that's int it `text.append("...");`
        * select/highlight the text in the field `text.selectAll();`
        * put the cursor back in the field `text.requestFocus();`
* JCheckBox
    * `JCheckBox check = new JCheckBox("...");`
    * methods
        * listen for an item event(when it is selected or deselected)
            `check.addItemListener(this);`
        * handle the event (and find out whether or not it's selected)
            ```java
            public void itemStateChanged(ItemEvent ev) {
                String onOrOff = "off";
                if (check.isSelected()) onOrOff = "on";
                System.out.println("check bos is " + onOrOff);
            }
            ```
        * select or deselect it in code `check.setSelected(true);`
* JList
    * constructor takes an array of any object type
    ```java
    String[] listEntries = {"one", "two"};
    JList list = new JList(listEntries);
    ```
    * methods
        * make it have a vertical scrollbar
        ```java
        JScrollPane scroller = new JScrollPane(list);
        scroller.setVerticalScrollBarPolicy(ScrollPaneConstants.VERTICAL_SCROLLBAR_ALWAYS);
        scroller.setHorizontalScrollBarPolicy(ScrollPaneConstants.HORIZONTAL_SCROLLBAR_NEVER);
        panel.add(scroller);
        ```
        * set the number of lines to show before scrolling `list.setVisibleRowCount(4);`
        * restrict the user to select only one thing at a time `list.setSelectionMode(ListSelectionModel.SINGLE_SELECTION);`
        * register for list selection events `list.addListSelectionListener(this);`
        * handle event (find out which thing in the list was selected)
        ```java
        public void valueChanged(ListSelectionEvent lse) {
            if (!lse.getValueIsAdjusting()) {
                String selection = (String) list.getSelectedValue();
                System.out.println(selection);
            }
        }
        ```
--- 
*headfirst java* ch12 getting gui
