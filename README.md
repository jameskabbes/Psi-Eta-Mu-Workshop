# Psi-Eta-Mu-Workshop
A timed Python problem-based workshop, presented for the Psi Eta Mu fraternity

# Instructions

## Workshop Instructions
* Members will be divided into teams
* Each team will work together to solve prompts
* 

## Submitting Answers
You are permitted to submit answers as many times as you choose. Be sure to include your team's submission PIN when inputting your answers. Do not share you submission PIN with anyone outside your team!

To submit your answers, submit the [Google Form](https://forms.gle/JcFnwq8agh4SENTL7).
![](static/answer%20submission.png)

## Choosing a Winner
One winning team will be chosen from all participating teams. 

Teams will be ranked on their **most recent submission** by the following criteria, with descending importance:
* Most correct answers
* Speed of submission

Winners will be featured in a congratulatory LinkedIn post :) 

## Hints
* Each team is allowed one hint from James. Simply raise your hand and ask for a hint for one question.

## Integrity
* This is a friendly competition between peers
* Online inspiration in encouraged; StackOverflow, Google, etc.
* Copying entire coding solutions to the prompts is discouraged

# Prompts

## 1. Weather Data
For autumn months (September, October, November) in Vancouver, British Columbia during the years of 1990-2009 (inclusive), what is average range of temperature (in degrees Celsius) experienced in a given day? Round answers to the nearest whole number.

### Data Dictionary
* *time* shows date of reading in YYYY-MM-DD format
* *tavg* shows average temperature for the day in degrees Celsius
* *tmin* shows minimum temperature for the day in degrees Celsius
* *tmax* shows maximum temperature for the day in degrees Celsius

## 2. Friday the 13ths
Find the number of Friday the 13th's that have occurred between January 1st, 1900 and January 1st, 2000.

## 3. Most optimal path
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total is 23. 3+7+4+9 = 23

![](static/triangle.png)

Find the maximum possible total from top to bottom of the triangle below:

```
                  56
                34  31
              47  26  21
            61  41  12  00
          60  88  27  48  64
        40  96  18  80  15  26
      46  76  04  66  16  76  67
    65  60  21  22  65  35  55  18
  43  06  85  10  51  45  71  05  22
57  62  65  62  78  31  91  61  00  81
```


## 4. Table joining 
For all orders in the year of 2010, find the average zip code (rounded to the nearest whole number) of all zip codes (as integers) for the corresponding customer addresses at the given time of the order. 

### Data Dictionary

#### orders.csv
* orderID: the unique order identifier
* datetime: the date the order was placed
* customerID: the customer who place the order

#### addresses.csv
* addressID: the unique address indentifier
* customerID: the customerID associated with this address
* dt_eff: the date the address became accurate (inclusive)
* dt_ends: the date the address expired (exclusive)


## 5. Shrek 
Count the number of times the word **love** appears in the transcript of the film *Shrek (2001)*. Consider **all** text present in the transcript, not just speaking parts. Include the possessive **"love's"** in your count. **Do not** include the plural *"loves"* or any other similar words like *"loved"*, *"lover"*, or *"lovely"*.


# Author
James Kabbes - AGCO