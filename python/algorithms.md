### Guess and Check
reference: 6001x lec2
* guess and check:
    * guess a value for solution
    * check if the solution is correct
    * keep guessing until find solution or guessed all values
    * the process is exhaustive enumeration
        * works on problems with a finite number of possibilities
        * good way to generate guesses in an organized manner
* useful to think about a decrementing function
    * maps set of program variables into an integer
    * when loop is entered, value is non-negative
    * when value is `<= 0`,, loop terminates and
    * value is decreased every time through loop

#### approximate solutions
* to find a good enough solution.
    * if the difference is less than some small value (let's say epsilon)
* start with a guess and increment by some small value


### Bisection Search
* pick a guess in the middle of the possible range
* at each stage, reduce range of values to search by half
* guess converges on the order of `log_2 N` steps
* bisection search works when value of function varies monotonically with input (problems with 'ordering property')
