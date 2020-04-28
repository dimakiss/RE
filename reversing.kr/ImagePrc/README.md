# ImagePrc
source: http://reversing.kr/challenge.php

## Challenge
we have an exe file, we can draw on it and click check, but we get `wrong` message. 

![](WrongDialogBox.jpg)


## Solution
I opened the `ImagePr` with ollyDbg and after the `wrong` message pause the program.
After looking at the call stack I got here.

![](wrong message.jpg)
