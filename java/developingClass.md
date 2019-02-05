# developing a Class
* Figure out what the class is supposed to do
* list the instance variables and methods
* write prepcode for the methods
    * prepcode: a form of pseudocode to focus on the logic
* write test code for the methods
* implement the class
* test the methods
* debug and reimplement as needed

### PrepCode
* includes three parts
    * instance variable declarations
        `DECLARE an int array to hold the location cells. Call it locationCells.`
    * method declarations
        `DECLARE a checkYourself() method that takes a String for the user's guess ("1","3",etc) checks it, and returns a result representing a "hit", "miss", or "kill".`
    * method logic
        ```
        METHOD: String checkYourself(String userGuess)
            GET the user guess as a String parameter
            CONVERT the user guess to an int
            REPEAT with each of the location cells in the int array
                // COMPARE the user guess to the location cell
                IF the user guess matches
                    INCREMENT the number of hits
                    // FIND OUT if it was the last location cell:
                    IF number of hits is 3, RETURN "kill" as the result
                    ELSE it was not a kill, so RETURN "hit"
                    END IF
                ELSE the user guess did not match, so RETURN "miss"
                END IF
            END REPEAT
            ```


### Extreme Programming
    * make small, but frequent, releases
    * Develop in iteration cycles
    * Don't put in anything that's not in the spec
    * write the test code first
    * work regular hours
    * refactor whenever and wherever you notice the opportunity
    * don't release anything until it passes all the tests
    * set realistic schedules, based around small releases
    * keep it simple
    * program in pairs, and move people around so that everybody knows pretty much everything about the code




-----
reference:
*headfirst java* chapter 5
