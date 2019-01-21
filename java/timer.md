# Timer
* a class inherits Timer
* provides the time functionality
* In order to work, the class Timer requires a class 
 which implements the ActionListener interface

 ```java
 public class WormGame extends Timer implements ActionListener {

    public WormGame(int width, int height) {
        super(1000, null); // delay, listener
        addActionListener(this);
        setInitialDelay(2000);
    }

    @Override
    public void actionPerformed(ActionEvent ae) {
        if(!continues) {
            return;
        }
    }
 }

 ```

 ------
 reference

 [mooc.fi, week12, Exercise 49:WormGame](https://materiaalit.github.io/2013-oo-programming/part2/week-12/)
