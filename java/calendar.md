# to deal with time
* java.util.Calendar
    * to deal with time
* java.util.Date
    * many Date's methods have been deprecated
    * still good to use getting "time stamp" of now


### Calendar
* to manipulate date
* `Calendar cal = Calendar.getInstance();`
    * most of the world, you will get back a `java.util.GregorianCalendar` instance
* highlights of the Calendar API
    * Key Calendar Fields
        * DATE / DAY_OF_MONTH: get/set the day of month
        * HOUR / HOUR_OF_DAY: get/set the 12 hour or 24 hour value
        * MILLISECOND: get/set the milliseconds
        * MINUTE: get/set the minute
        * MONTH: get/set the month
        * YEAR: get/set the year
        * ZONE_OFFSET: get/set raw offset of GMT in millis
    * Key Calendar Methods
        * add(int field, int amount): adds or subtracts time from the calendar's field
        * get(int field): returns the value of the given calendar field
        * getInstance(): returns a Calendar, you can specify a locale
        * getTimeInMillis(): returns this calendar's time in millis, as a long
        * roll(int field, boolean up): adds or subtracts time without changing larger fields
        * set(int field, int value): sets the value of a given Calendar field
        * set(year, month, day, hour, minute): set a complete time (all int, month is zero-based)
        * setTimeInMillis(long millis): sets a Calendar's time based on a long milli-time
    * example
        ```java
        Calendar c = Calendar.getInstance();
        c.set(2004, 0, 7, 15,40);   // set time to Jan. 7, 2004 at 15:40
        long day1 = c.getTimeInMillis();
        day1 += 1000 * 60 * 60;     // add an hour (as millisecond)
        c.setTimeInMillis(day1);
        System.out.println("new hour " + c.get(c.HOUR_OF_DAY));
        c.add(c.DATE, 35);  // add 35 days to the date (change the month to Feb, in this case)
        System.out.println("add 35 days " + c.getTime());
        c.roll(c.DATE, 35); // ROLL 35 days (does not change the month)
        System.out.println("roll 35 days " + c.getTime());
        c.set(c.DATE, 1);   // just set the date
        ```

