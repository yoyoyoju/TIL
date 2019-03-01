# bufferedWriter
* BufferedWriter and FileWriter
    * FileWriter writes each and every thing I pass to the file each and every time
    * BufferedWriter holds all the stuff I write to it until it's full. Only when it is full, the FileWriter actually will write to the file on the disk.
    * one can send data before the buffer is full by `flush()` it.
    * BufferedWriter is a chain stream, while FileWriter is a connection stream
* `BufferedWriter writer = new BufferedWriter(new FileWriter(aFile));`

----
reference
*headfirst java* ch14
