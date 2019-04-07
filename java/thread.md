# Thread

* Thread from HeadFirst java chapter 15


### Thread class

* methods:
    * `setName(String name)`: set name
    * `getName()`: get name 
    * static methods:
        * `sleep(duration in milliseconds)`
        * `currentThread()`

### How to launch a new thread

* Runnable : in java.lang package
    * Runnable is the job a thread is supposed to run
    * Runnable interface defines one method `public void run()`
    * the `run()` method is put on the bottom of the new stack.
    * example of Runnable:
    ```java
    public class MyRunnable implements Runnable {
        public void run() {
            System.out.println("something to do"); 
        }
    }

    class ThreadTester {
        public static void main(String[] args) {
            Runnable threadJob = new MyRunnable();
            Thread myThread = new Thread(threadJob);
            myThread.start();
        }
    }
    ```

1. Make a Runnable object
    `Runnable threadJob = new MyRunnable();`
2. Make a Thread object and give it a Runnable
    `Thread myThread = new Thread(threadJob);`
3. Start the Thread
    `myThread.start();`


### states of a thread

* new, runnable, running, blocked and dead.
* The thread scheduler decides who runs and who don't.


#### thread to sleep

* sleep method throws InterruptedException
```java
try {
    // pass the sleep duration in milliseconds
    Thread.sleep(2000);
} catch (interruptedException ex) {
    ex.printStackTrace();
}
```


### concurrency issue

* when multiple thread have access to a single object's data.
* one way to deal with it is make the method atomic.
    * use the `synchronized` keyword to modify a method so that only one thread at a time can access it.
    * example
        ```java
        class TestSync implements Runnable {
            private int balance;

            public void run() {
                for(int i=0; i<50; i++) {
                    increment();
                    System.out.println("balance is " + balance);
                }
            }

            public synchronized void increment() {
                // make sure the method completes
                // before any other thread can enter the method
                int i = balance;
                balance = i + 1;
            }
        }

        public class TestSyncTest {
            public static void main (String[] args) {
                TestSync job = new TestSync();
                Thread a = new Thread(job);
                Thread b = new Thread(job);
                a.start();
                b.start();
            }
        }
        ```
    * synchronized keyword within a method
        ```java
        public void go() {
            doStuff();
            synchronized(this) {
                // code, which should be atomic
            }
        }
        ```
    * be careful of deadlock
