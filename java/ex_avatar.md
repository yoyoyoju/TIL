# Avatar

### draw an object into a UserInterface
* draw a ball in a JPaner
* listen to the key stoke
* move the ball according to the key source

* Avatar class
    * has fields for the location of the object
    * draw method takes Graphics instantce and fillOval
    * move method updates the location
```java
import java.awt.Graphics;
public class Avatar {
    private int x;
    private int y;

    public Avatar(int x, int y) {
        this.x = x;
        this.y = y;
    }
    public int getX() {
        return x;
    }
    public int getY() {
        return y;
    }
    public void move(int movingX, int movingY) {
        this.x += movingX;
        this.y += movingY;
    }
    public void draw(Graphics graphics) {
        graphics.fillOval(x, y, 10, 10);
    }
}
```

* DrawingBoard
    * the constructor takes Avatar object as parameter
    * does not draw itself, but uses the given avatar object to draw
```java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JPanel;

public class DrawingBoard extends JPanel {
    private Avatar avatar;
    public DrawingBoard(Avatar avatar) {
        super();
        super.setBackground(Color.WHITE);
        this.avatar = avatar;
    }
    @Override
    protected void paintComponent(Graphics graphics) {
        super.paintComponent(graphics);
        // let avatar draw
        this.avatar.draw(graphics);
    }
}
```

* UserInterface
    * the constructor takes Avatar object as parameter
    * passes the Avatar object to DrawingBoard object
    * Avatar is independent object and it is drawn in the user interface
```java
public class UserInterface implements Runnable {
    private JFrame frame;
    private Avatar avatar;
    public UserInterface(Avatar avatar) {
        this.avatar = avatar;
    }
// ...
    private void createCompoenets(Container container) {
        DrawingBoard drawingBoard = new DrawingBoard(avatar);
        container.add(drawingBoard);
    }
//...
}
```

* main method
    * create UserInterface object and Avatar object
    * the avatar object is given to the UserInterface as constructor parameter
```java
UserInterface ui = new UserInterface(new Avatar(30, 30));
SwingUtilities.invokeLater(ui);
```


### listen to the keystrokes
* `KeyListener` interface
    * to use key inputs, we need an action listener, who listens to our keyboard
    * interface KeyListener defines the functionality for that:
    * `keyPressed`, `keyReleased`, `keyTyped`
    * these methods receives instance of KeyEvent from the UserInterface
```java
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class KeyboardListener implements KeyListener {
    private Avatar avatar;
    public KeyboardListener(Avatar avatar) {
        this.avatar = avatar;
    }
    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_LEFT) {
            avatar.move(-5, 0);
        } else if(e.getKeyCode() == KeyEvent.VK_RIGHT) {
            avatar.move(5, 0);
        }
    }
    @Override public void keyReleased(KeyEvent e) {} // remains empty
    @Override public void keyTyped(KeyEvent ke) {} // remains empty
}
```
* assign keyboard listener to the JFrame instance
    * we want to listen to the keystrokes directed to our user interface
```java
    private void createComponents(Container container) {
        DrawingBoard drawingBoard = new DrawingBoard(avatar);
        container.add(drawingBoard);
        frame.addKeyListener(new KeyboardListener(avatar));
    }
```

### DrawingBoard Repainting
* some user interface components, such as JButton, hava the functionality to repaint the components
* but our drawing board does not automatically repaint
* we have to ask the drawingboard to paint itself again when needed
* Each subclass of `Component` has the method `public void repaint()`
    * it repaints the component after it is called

* we repaint the ball after the avatar.move
    * so in the class KeyboardListener
    * we need the drawingboard reference
```java
import java.awt.Component;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
public class KeyboardListener implements KeyListener {
    private Component component;
    private Avatar avatar;
    public KeyboardListener(Avatar avatar, Component component) {
        this.avatar = avatar;
        // the drawing board is passed as parameter
        this.component = component;
    }
    @Override
    public void keyPressed(KeyEvent e) {
        if (e.getKeyCode() == KeyEvent.VK_LEFT) {
            avatar.move(-5, 0);
        } else if (e.getKeyCode() == KeyEvent.VK_RIGHT) {
            avatar.move(5, 0);
        }
        // let the board repaint after the movement
        component.repaint();
    }
    // Override keyReleased and keyTyped: do nothing
}
```
* modify the createComponents method in UserInterface to give the DrawingBoard as parameter to the keyListener
```java
private void createComponents(Container container) {
    DrawingBoard drawingBoard = new DrawingBoard(avatar);
    container.add(drawingBoard);
    frame.addKeyListener(new KeyboardListener(avatar, drawingBoard));
}
```

* one can saparate the createComponents and add Listeners
```java
public class UserInterface implements Runnable {
    private JFrame frame;
    private DrawingBoard board;
    private Figure figure;

    public UserInterface(Figure figure) {
        this.figure = figure;
    }
    @Override
    public void run() {
        frame = new JFrame();
        frame.setPreferredSize(new Dimension(400, 400));
        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        createComponents(frame.getContentPane());
        addListeners();
        frame.pack();
        frame.setVisible(true);
    }
    priavet void craeteComponents(Container container) {
        board = new DrawingBoard(figure);
        container.add(board);
    }
    private void addListeners() {
        frame.addKeyListener(new KeyboardListener(board, figure));
    }
    public JFrame getFrame() {
        return frame;
    }
}
```
