# Position
sourse: http://reversing.kr/challenge.php

## Challnge
An `Position.exe` and `ReadMe.txt`:
```
ReversingKr KeygenMe


Find the Name when the Serial is 76876-77776
This problem has several answers.

Password is ***p
```

## Solution

I opened the exe with IDA pro and looked for the `Wrong` sting in the string window.\
The cross-reference sends us to `sub_401CD0`:\
![](sub_401CD0.png)

Which checks if the reurn value of the `sub_401740` function is 0 or not.\
`sub_401740` looks dificult but its acually pretty easy IDA's Psrudocode did a grate job.\
All this function does is to check if there are valid inputs and make a simple calclation to see if name mathces the serial\
\
![](sub_401740_overview.png)\

### valid inputs:
* for name :non repeating characters length 4
* for serial : 5 numbers followed by '-' and another 5 numbers

### name serial match
The code takes every character shift its by the numbers 1-4 and add 1 or 5 depend if the char location is even or odd .\
Then it takes the next character (int pairs) and sums the value its got from the other character and mathes the values to with the serial.\
I added blow pard of the Psrudocode code that was generted by IDA and i added few commnts to make it more readable.\
\
![](Psrudocode_part.png)

There is same calculation for char in position 2 and 3, I made simple python script that takes the Name and give u the sireal And vice versa,\
look for `Solution.py`

```
python Solution.py
bump
```

Our solution for the serial __76876-77776__ is __bump__\\
![](Solution.png)
