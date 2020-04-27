# Music Player
source: http://reversing.kr/challenge.php

## Challenge
We have an exe that seems to be a music player.
A readme text file that says the player limited to 1 min, and we have played if for more then 1 min to get see the perfect plag.
We also have an `msvbvm60` DLL file

Note: I added a song longer than 1 min for solving this challenge 


## Solution

We load the exe to olly and immediately we can see that it has a lot of jumps, so to find the main routine and the check routine we will run the exe with ollyDbg and pause after the limited 1 min error shows up. We must open the file first and click play (the left button).
After clicking pause we go to call stack and we can see that the message box was called from `0x4045DE`

![](call_stack.jpg)

After scrolling up you can see that the routine starts at `0x4044C0` after jumping from `0x4023C5`.
If we scroll up from the `0x4045DE` line we can the comparison `CMP EAZ,0EA60`, `EA60h = 60000`. It seems like its the comparison if the time is less them `60000ms` which is `60 sec` if `EAX>EA60` show error message.
In `0x40455D` we can see that the value from `EBP-A4` moved to `EAX`.


I will try to patch the jumps at `0x40456B` so the jump will be taken no matter what time passed.

`0040456B JL Music_Pl.004045FE `----> `0040456B JMP  Music_Pl.004045FE `

We save the patch to knew exe `Music_Player1.exe` after running it we get an error 

![](error.jpg)

Its seems like the password we are looking for is `stenCare` but to know for for sure we will try to find where the error coming from.

We open exe with ollyDBG run untill the error massage after that we pause and look at the call stack like before.

![](call_stack_error2.jpg)

Nothing helpfull, we look at the stack and we scroll down (alot) untill we arrive here, the first function that returns to our main code.

![](return_stack.jpg)

