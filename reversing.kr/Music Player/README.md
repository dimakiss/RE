# Music Player
source: http://reversing.kr/challenge.php

## Challenge
We have an exe that seems to be a music player.
A readme text file that says the player limited to 1 min, and we have played if for more then 1 min to get see the perfect plag.
We also have an `msvbvm60` DLL file

Note: I added a song longer than 1 min for solving this challenge 


## Solution

We load the exe to olly and immediately we can see that it has a lot of jumps, so to find the main routine and the check routine we will run the exe with ollyDbg and pause after the limited 1 min error shows up. We must open the file first and click play (the left button).
After clicking pause we go to call stack main 
