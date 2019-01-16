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
        // graphics can draw:
        graphics.setColor(Color.BLACK);     // set the color
        graphics.fillRect(50, 80, 100, 50); // draw a rectangle
    }
}
```
```java
// add drawing board to UserInterface
// in the method createComponenets
    private void createComponenets(Container container) {
        container.add(new DrawingBoard());
    }
```

* Graphics
    * coordinate system
        * the origin (0,0) is the upper left corner
        * the value of the y axis grows downwards
        * because the size of the window is modified from the bottom right corner
    * fillRect(x-coordinate, y-coordinate, rectangle-width, rectangle-height);
    * setColor(Color.GREEN); 
