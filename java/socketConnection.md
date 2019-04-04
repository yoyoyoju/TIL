# Socket Connection
Socket connection for a chat room; example from HeadFirst Java Chapeter 15.

### Java API netwroking package

* java.net

#### Socket connection

* Socket: java.net.Socket class
    * an object between two machines
    * the two machines have information about each other (IP address, TCP port number)
    * need to know *IP address* and *TCP port number*
    * `Socket chatSocket = new Socket("196.164.1.103", 5000);`


#### read from a socket

* use streams to communicate over a Socket connection
* How to:
    1. Make a Scoket connection to the server
     `Socket chatSocket = new Socket("196.164.1.103", 5000);`
    2. Make an InputStreamReader chained to the Socket's low-level (connection) input stream
    ```java
    InputStreamReader stream = new InputStreamReader(chatSocket.getInputStream());
    // chatSocket.getInputStream() : bytes from server
    // InputStreamReader : convert the bytes to characters
    ```
    3. Make a BufferedReader and read
    ```java
    BufferedReader reader = new BufferedReader(stream);
    // BufferedReader : buffered characters
    String message = reader.readLine()
    ```


#### write data to a Socket
* use PrintWriter
* How to:
    1. Make a Socket connection
     `Socket chatSocket = new Socket("196.164.1.103", 5000);`
    2. Make a PrintWrite chained to the Socket's low-lever output stream
    ```java
    PrintWriter writer = new PrintWriter(chatSocket.getOutpuStream());
    // chatSocket.getOutputStream: bytes to server
    // PrintWriter : bridge between character data and the bytes
    ```
    3. Write something
    `writer.println("message");`
