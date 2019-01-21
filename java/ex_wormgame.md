# Example code
### Worm Game

#### wormgame
* Main Class
* enum Direction
```java
// Main Class
public static void main(String[] args) {
        // write test code here
        WormGame game = new WormGame(20, 20);

        UserInterface ui = new UserInterface(game, 20);
        SwingUtilities.invokeLater(ui);

        while (ui.getUpdatable() == null) {
            try {
                Thread.sleep(100);
            } catch (InterruptedException ex) {
                System.out.println("The drawing board hasn't been created yet.");
            }
        }

        game.setUpdatable(ui.getUpdatable());
        game.start();
    }
```

```java
package wormgame;

import java.awt.event.KeyEvent;

public enum Direction {

    UP(0, -1, KeyEvent.VK_UP),
    RIGHT(1, 0, KeyEvent.VK_RIGHT),
    DOWN(0, 1, KeyEvent.VK_DOWN),
    LEFT(-1, 0, KeyEvent.VK_LEFT);

    private int dx;
    private int dy;
    private int ke;

    private Direction(int dx, int dy, int ke) {
        this.dx = dx;
        this.dy = dy;
        this.ke = ke;
    }

    public int getDx() {
        return dx;
    }

    public int getDy() {
        return dy;
    }

    public int getKe() {
        return ke;
    }

    public static Direction getDirection(int ke) {
        for (Direction d : Direction.values()) {
            if (d.getKe() == ke) {
                return d;
            }
        }
        return null;
    }
}
```

#### wormgame.domain
* Classes
    * Piece: has its location
    * Apple extends Piece
    * Worm extends Piece

#### wormgame.game
* Classes
    * WormGame extends Timer implements ActionListener
```java
package wormgame.game;

import wormgame.Direction;
import wormgame.domain.Apple;
import wormgame.domain.Piece;
import wormgame.domain.Worm;
import wormgame.gui.Updatable;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Random;

public class WormGame extends Timer implements ActionListener {

    private int width;
    private int height;
    private boolean continues;
    private Updatable updatable;
    private Worm worm;
    private Apple apple;
    private Random random;

    public WormGame(int width, int height) {
        super(1000, null);

        this.width = width;
        this.height = height;
        this.continues = true;

        addActionListener(this);
        setInitialDelay(2000);

        worm = new Worm(width/2, height/2, Direction.DOWN);
        // create an apple (random coordinates [0, width[, [0, height[ )
        random = new Random();
        setRandomApple();
    }

    private void setRandomApple() {
        Apple app = randomApple();
        while(worm.runsInto(app)) {
            app = randomApple();
        }
        setApple(app);
    }

    private Apple randomApple() {
        return new Apple(random.nextInt(width), random.nextInt(height));
    }

    public boolean continues() {
        return continues;
    }

    public void setUpdatable(Updatable updatable) {
        this.updatable = updatable;
    }

    public int getHeight() {
        return height;
    }

    public int getWidth() {
        return width;
    }

    private boolean wormHitsBorder() {
        Piece lastPiece = worm.lastPiece();
        boolean out = (lastPiece.getX() >= width) ||
                (lastPiece.getY() >= height);
        out |= (lastPiece.getX() < 0) ||
                (lastPiece.getY() < 0);
        return out;
    }

    @Override
    public void actionPerformed(ActionEvent ae) {
        if (!continues) {
            return;
        }

        // move the worm
        worm.move();

        // if the worm runs into the apple
        // it eats the apple and grow
        // new apple is randomly created
        if (worm.runsInto(apple)) {
            worm.grow();
            setRandomApple();
        }

        // if the worm runs into itself
        // or it hits the border
        // variable continue is set to be false
        if (worm.runsIntoItself() ||
            wormHitsBorder()) {
            continues = false;
        }

        // call update, which is a method of the variable updatable
        // which implements the interface Updatable
        updatable.update();

        // call setDelay method, which is inherited from the Timer class
        // the game velocity should grow as the length increases
        // call setDelay(1000/worm.getLength()); for that
        setDelay(1000 / worm.getLength());

    }

    public Worm getWorm() {
        return worm;
    }

    public void setWorm(Worm worm) {
        this.worm = worm;
    }

    public Apple getApple() {
        // returns the apple of the wormGame
        return apple;
    }

    public void setApple(Apple apple) {
        // sets the apple on the worm game
        this.apple = apple;
    }
}
```

#### wormgame.gui
* Updatable Interface
* Classes:
    * UserInterface(WormGame game, int sideLength)
        * creates a drawing board and add to the JFrame component
    * DrawingBoard(WormGame game, int pieceLength) implements Updatable
        * draws board based on game
        * updates (repaint) the board when the update() method is called
        * the Updatable interface is given to WormGame by setUpdatable method
    * KeyboardListener(Worm worm)
        * listens to the key and update the worm's direction
        * listener is added to the JFrame in UserInterface

```java
package wormgame.gui;

public interface Updatable {
    void update();
}
```
```java
package wormgame.gui;

import wormgame.game.WormGame;

import javax.swing.*;
import java.awt.*;

public class UserInterface implements Runnable {

    private JFrame frame;
    private WormGame game;
    private int sideLength;
    private DrawingBoard board;

    public UserInterface(WormGame game, int sideLength) {
        this.game = game;
        this.sideLength = sideLength;
    }

    @Override
    public void run() {
        frame = new JFrame("Worm Game");
        int width = (game.getWidth() + 1) * sideLength + 10;
        int height = (game.getHeight() + 2) * sideLength + 10;

        frame.setPreferredSize(new Dimension(width, height));

        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);

        createComponents(frame.getContentPane());

        frame.pack();
        frame.setVisible(true);
    }

    public void createComponents(Container container) {
        // Create drawing board first which then is added into container-object.
        board = new DrawingBoard(game, sideLength);
        container.add(board);
        // After this, create keyboard listener which is added into frame-object
        frame.addKeyListener(new KeyboardListener(game.getWorm()));
    }

    public Updatable getUpdatable() {
        // returns the drawingBoard
        return board;
    }

    public JFrame getFrame() {
        return frame;
    }
}
```
```java
package wormgame.gui;

import wormgame.domain.Piece;
import wormgame.game.WormGame;

import javax.swing.*;
import java.awt.*;
import java.util.List;

public class DrawingBoard extends JPanel implements Updatable {
    private WormGame wormGame;
    private int pieceLength;

    public DrawingBoard(WormGame wormGame, int pieceLength) {
        // int pieceLength: the dimension of the pieces (length and height)
        super.setBackground(Color.WHITE);
        this.wormGame = wormGame;
        this.pieceLength = pieceLength;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        // draws the worm and the apple
        // worm color: Color.BLACK
        // use Graphics object's fill3DRect method for worm
        drawWorm(g);
        // apple color: Color.RED
        // use Graphics object's fillOval method for apple
        g.setColor(Color.RED);
        drawPiece(wormGame.getApple(), g, true);
    }

    private void drawWorm(Graphics g) {
        List<Piece> pieces = wormGame.getWorm().getPieces();
        for(Piece piece : pieces) {
            g.setColor(Color.BLACK);
            drawPiece(piece, g, false);
        }
    }

    private void drawPiece(Piece piece, Graphics g, boolean oval) {
        int x = pieceLength * piece.getX();
        int y = pieceLength * piece.getY();
        if (oval) {
            g.fillOval(x, y, pieceLength, pieceLength);
        } else {
            g.fill3DRect(x, y, pieceLength, pieceLength, false);
        }
    }

    // implement the interface Updatable
    @Override
    public void update() {
        // has to call repaint method of JPanel
        repaint();
    }
}
```
```java
package wormgame.gui;

import wormgame.Direction;
import wormgame.domain.Worm;

import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public class KeyboardListener implements KeyListener {
    private Worm worm;

    public KeyboardListener(Worm worm) {
        this.worm = worm;
    }

    @Override
    public void keyPressed(KeyEvent e) {
        // the direction is assigned to worm
        worm.setDirection(Direction.getDirection(e.getKeyCode()));
    }

    @Override
    public void keyTyped(KeyEvent e) {

    }

    @Override
    public void keyReleased(KeyEvent e) {

    }
}
```

----
reference
[mooc.fi, week12, Exercise 49: WormGame](https://materiaalit.github.io/2013-oo-programming/part2/week-12/)
