# animation code

* simple example code
```java
import javax.swing.*;
import java.awt.*;
public class SimpleAnimation{
    int x = 70;
    int y = 70;
    public static void main(String[] args) {
        SimpleAnimation gui = new SimpleAnimation();
        gui.go();
    }
    public void go() {
        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        MyDrawPanel drawPanel = new MyDrawPanel();
        frame.getConstentPane().add(drawPanel);
        frame.setSize(300, 300);
        frame.setVisible(true);

        for(int i = 0; i<130; i++) {
            x++;
            y++;
            drawPanel.repaint();
            try{
                Thread.sleep(50);
            } catch (Exception ex) {
            }
        }
    }

    class MyDrawPanel extends JPanel {
        public void paintComponent( Graphics g) {
            g.setColor(Color.white);
            g.fillRect(0, 0, this.getWidth(), this.getHeight());
            g.setColor(Color.green);
            g.fillOval(x, y, 40, 40);
        }
    }
}
```

* example - music animation
```java
import javax.sound.midi.*;
import java.io.*;
import javax.swing.*;
import java.awt.*;

public class MiniMusicPlayer3 {
    static JFrame f = new JFrame("Music Video");
    static MyDrawPanel ml;
    public static void main(String[] args) {
        MiniMusicPlayer3 mini = new MiniMusicPlayer3();
        mini.go();
    }

    public void setUpGui() {
        ml = new MyDrawPanel();
        f.setContentPane(ml);
        f.setBounds(30, 30, 300, 300);
        f.setVisible(true);
    }
    
    public void go() {
        setUpGui();
        try {
            Sequencer sequencer = MidiSystem.getSequencer();
            sequencer.open();
            // register my controller event listener to the sequencer
            // my listener is MyDrawPanel
            // int array representing the list of controller events I want (#127)
            sequencer.addControllerEventListener(ml, new int[] {127});
            sequence seq = new Sequence(Sequence.PPQ, 4);
            Track track = seq.createTrack();

            int r = 0;
            for (int i=0; i<60; i+=4) {
                r = (int) ((Math.random() * 50) + 1);
                track.add(makeEvent(144,1,r, 100, i));  // NOTE ON
                track.add(makeEvent(176, 1, 127, 0, i));    // controllerEvent is 176
                track.add(makeEvent(128, 1, r, 100, i + 2));    // NOTE OFF
            }
            sequencer.setSequence(seq);
            sequencer.setTempoInBPM(120);
            sequencer.start();
        } catch (Exception ex) {ex.printStackTrace();}
    }

    public MidiEvent makeEvent(int comd, int chan, int one, int two, int tick) {
        MidiEvent event = null;
        try {
            ShortMessage a = new ShortMessage();
            a.setMessage(comd, chan, one, two);
            event = new MidiEvent(a, tick);
        } catch (Exception e) {
        }
        return event;
    }

    class MyDrawPanel extends JPanel implements ControllerEventListener {
        boolean msg = false;
        public void controlChange(ShortMessage event) {
            msg = true;
            repaint();
        }

        public void paintComponent(Graphics g) {
            // paint only when the event has occured
            if (msg) {
                int r = (int) (Math.random() * 250);
                int gr = (int) (Math.random() * 250);
                int br = (int) (Math.random() * 250);

                g.setColor(new Color(r, gr, b));
                int ht = (int) ((Math.random() * 120) + 10);
                int width = (int) ((Math.random() * 120) + 10);
                int x = (int) ((Math.random() * 40) + 10);
                int y = (int) ((Math.random() * 40) + 10);
                g.fillRect(x, y, ht, width);
                msg = false;
            }
        }
    }
}
```

----
*headfirst java* ch12

