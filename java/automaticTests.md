# Automatic Tests
```javaj
String input = "translate\n" + "monkey\n" +
                "translate\n" + "cheese\n" +
                "add\n" + "cheese\n" + "juusto\n" +
                "quit\n";
Scanner reader = new Scanner(input);
Dictionary dictionary = new Dictionary();
TextUserInterface ui = new TextUserInterface(reader, dictionary);
ui.start();
```
