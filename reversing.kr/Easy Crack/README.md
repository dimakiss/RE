# Easy Crack
source : http://reversing.kr/challenge.php

## Challenge
we have and exe file that ask for some password 

![](dialogbox.jpg)


## Solution
We open `Easy_CrackMe` in IDA we can see the that `WinMain` call `DialogBoxParamA` and push the Function at address 401020.

![](main.jpg)

We follow the 401020 function and its call `sub_401080` which seem to be the function that decide if its good password or bad.
The code flow so far `WinMain`-->`401020`-->`401080`

The `GetDlgItemText` function get the buffer address at 0x4010A3 which is memory location, are puts there the password we enter.
right after at 0x4010B0 the second byte compered to 'a'(61h). (`_a`)
the rest of the password is moved to ecx, pushed to 0x401150 function with "5y". There the letters in the index 3,4 compered with "5y". (`_a5y`)

At 0x4010D1 we compere the rest of the password with "R3versing". (`_a5yR3versing`)
after that we check that the first letter is 'E'(45h). (`Ea5yR3versing`)

Note: every jump to 0x401135 is jump to badboy "`Incorrect Password`"
![](check_routine.jpg)

The right password is *Ea5yR3versing*





