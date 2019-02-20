# MIDI
* to play sound


### what do we need
* Sequencer
    * like a music CD player
* Sequence
    * like a music CD
* Track
    * holds the songs
* MIDI event
    * the actual music information
* Sequence plays Sequence. Sequence has a Track. Track holds Midi Events


### five steps
1. Get a Sequencer and open it
    ```java
    Sequencer player = MidiSystem.getSequencer();
    player.open();
    ```
2. Make a new Sequence
    ```java
    Sequence seq = new Sequence(timing, 4);
    ```
3. Get a new Track from the Sequence
    ```java
    Track t = seq.createTrack();
    ```
4. Fill the Track with MidiEvents and give the Sequence to the Sequencer
    ```java
    // example of MidiEvent
    ShortMessage a = new ShortMessage();
    a.setMessage(144, 1, 44, 100);
    MidiEvent noteOn = new MidiEvent(a, 1);
    t.add(noteOn);
    // another MidiEvent
    ShortMessage b = new ShortMessage();
    b.setMessage(128, 1, 44, 100);
    MidiEvent noteOff = new MidiEvent(b, 16);
    t.add(noteOff);
    // give the Sequence to the Sequencer
    player.setSequence(seq);
    ```
5. play
    ```java
    player.start();
    ```


### MidiEvent
* A MidiEvent is an instruction for part of a song
    * describe *what to do* 
        * use message
            ```java
            // make a Message
            ShortMessage a = new ShortMessage();
            // Put the instruction in the message
                // start playing note 44
            a.setMessage(144, 1, 44, 100);
            ```
    * *when to do it*
        * when to start playing the note (a NOTE ON event)
        * when to stop playing the note (NOTE OFF event)
            ```java
            // make a new MidiEvent using the Message
                // trigger message `a`, at the first bead (beat 1)
            MidiEvent noteOn = new MidiEvent(a,1);
            ```
    * add the MidiEvent to the Track
        ```java
        track.add(noteOn);
        ```

### Message
* message describes what to do for MidiEvent
* use `setMessage()`
    * message type: 
        * the first argument to setMessage is always the message type
        * the other three arguments represent different things depending on the message type
            * 144: note on (start playing) 
                ```java
                // note on, channel 1, note 20, velocity 100
                a.setMessage(144, 1, 20, 100);
                ```
            * 128: note off (stop playing)
                ```java
                // note off, channel 1, note 20, velocity 100
                b.setMessage(128, 1, 20, 100);
                ```
                * Channel
                    * like a musician in a band
                * note to play
                    * a number from 0 to 127, going from low to high notes
                * velocity
                    * how fast and hard
                    * 0 is soft, 100 is a good default
            * 192: change the instrument
                ```java
                // before the note-playing message
                // change-instrument, in channel 1, to instrument 102
                first.setMessage(192, 1, 102, 0);
                ```

---
reference
*headfirst java* chapter11
