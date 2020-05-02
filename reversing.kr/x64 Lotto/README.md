# x64 Lotto

source: http://reversing.kr/challenge.php

## Challenge
we have an exe file that asks for some input 

![](cmd.png)

After inputing 6 differnt numbers the program restarts, if the input is not a number the program glitch.

## Solution

I opened the program in IDA the main function saves the 6 numbers as we told, and run check rution.\
If the every thing is correct the main routin keep forword to `0x014000114B` if not we go back to the numbers input.

![](maincheck.jpg)


Because there is no use in the input numbers later (after the check routine)\
I will jump from `0x140001128` to `0x14000114B` by this jump i will skip the check routine.\
In __x64__ the jump are by offsets, If the `EIP` is `1000` for example in order to jump to `1010` I will need to `JMP 0x0E` there is __0x2__ added to avoid infinite jump to current EIP.

I need to jump from `0x140001128` to `0x14000114B` its __0x23__ bytes so the the instruction is `JMP 0x21` \
or in hex, `EB 21`
I oreder to edit this instruction in hex editor we need to know the __Raw data offeset__.\
IDA tells us in the top of the main funtion `Offset to raw data for section: 00000400` , and the instration is in RVA `0x140001128` or in offsrt `0x128`.\
So the instruction's location is `0x400+0x128=0x528`

__Before:__ ![](HexEditBefore.png)\
__After:__ ![](HexEditAfter.png)






the password is from_GHL2_-_! \
to do write ups 
