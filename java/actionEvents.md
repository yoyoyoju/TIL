# Managing Action Events
* Action event listeners listen to the UI components they are assigned to
* according to actions on an UI component, 
 the UI component calls a particular method of all the action event listeners assigned to it
* Action event listeners are classes which implement a particulare interface, 
 and whose instances can be assigned to UI components
* `ActionListener` (interface)
    * defines the method `void actionPerformed(ActionEvent e)`

1. create a class implements ActionListener
```java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MessageListener implements ActionListener {
    @Override
    public void actionPerformed(ActionEvent ae) {
        System.out.println("Message received!");
    }
}
```
2. create a JButton and addActionListener
```java
private void createComponenets(Container container) {
    JButton button = new JButton("Send!");
    button.addActionListener(new MessageListener());
    container.add(button);
}
```


### Handling Objects in the Action Event Listeners
* action event listener to modify states of an object
* to have access to the object in the action event listener,
 the reference to the object should be passed to the constructor of action event listener
```java
private void createComponents(Container container) {
    // GridLayout: like a coordinate system 
    // in the below example: (one line and three column)
    GridLayout layout = new GridLayout(1, 3);
    container.setLayout(layout);

    // JTextArea: user can input text
    JTextArea textAreaLeft = new JTextArea("The Copier");
    JTextArea textAreaRight = new JTextArea();
    JButton copyButton = new JButton("Copy!");

    // AreaCopier defined below
    // when ActionEvent from copyButton occurs
    // copy text from Left to the Right
    AreaCopier copier = new AreaCopier(textAreaLeft, textAreaRight);
    copyButton.addActionListener(copier);

    container.add(textAreaLeft);
    container.add(copyButton);
    container.add(textAreaRight);
}
```
```java
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JTextArea;

public class AreaCopier implements ActionListener {
    private JTextArea origin;
    private JTextArea destination;

    public AreaCopier(JTextArea origin, JTextArea destination) {
        this.origin = origin;
        this.destination = destination;
    }

    @Override
    public void actionPerformed(ActionEvent ae) {
        this.destination.setText(this.origin.getText());
    }
}
```

----
reference
[Mooc.fi week11](https://materiaalit.github.io/2013-oo-programming/part2/week-11/)
