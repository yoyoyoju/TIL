# Drawing

### JPanel
* use the class JPanel as a drawing board
* inherits the JPanel class and overrides the method `protected void paintComponenet(Graphics graphics)`
* the user interface calls the `paintComponent` method
* the parameter should be an instance of a class which is subclass of the abstract class `Graphics`
```java
public class DrawingBoard extends JPanel {
    public DrawingBoard() {
        super.setBackground(Color.WHITE);
    }
    @Override
    protected void paintComponent(Graphics graphics) {
        super.paintComponent(graphics);
    }
}
```
