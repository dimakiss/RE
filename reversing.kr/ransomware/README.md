# Ransomware

source: http://reversing.kr/challenge.php

## Challenge
we have an exe file that wait for us to input a key, text file that tells us to `Decrypt File (EXE)` and file seems like the file we need to decrypt.

![](Dialogbox.jpg)

## Solution

PEview show saction names UPX1, PEiD tells the same and  deep scan shows that the exe was packed with `UPX 0.89.6`

![](PEview.png) ![](PEiD.png)
