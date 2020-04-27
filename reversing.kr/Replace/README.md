# Easy Crack
source: http://reversing.kr/challenge.php

## Challenge
we have an exe file that asks for some password 



## Solution
We open `Easy_CrackMe` in IDA we can see that `WinMain` call `DialogBoxParamA` and push the Function at address `0x401020`.

![](main.jpg)

We follow the `401020` function and its call `sub_401080` which seems to be the function that decides if its good password or bad.
The code flow so far `WinMain`-->`401020`-->`401080`
