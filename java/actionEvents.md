# Managing Action Events
* Action event listeners listen to the UI components they are assigned to
* according to actions on an UI component, 
 the UI component calls a particular method of all the action event listeners assigned to it
* Action event listeners are classes which implement a particulare interface, 
 and whose instances can be assigned to UI components
* `ActionListener` (interface)
    * defines the method `void actionPerformed(ActionEvent e)`
