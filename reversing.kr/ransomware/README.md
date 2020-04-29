# Ransomware

source: http://reversing.kr/challenge.php

## Challenge
we have an exe file that wait for us to input a key, text file that tells us to `Decrypt File (EXE)` and file seems like the file we need to decrypt.

![](Dialogbox.jpg)

## Solution

PEview show saction names UPX1, PEiD tells the same and  deep scan shows that the exe was packed with `UPX 0.89.6`

![](PEview.png) ![](PEiD.png)

I unpacked that UPX manually.Finding the OEP with olly,after `PUSHAD` in `0xECECE0` Memory Brakepoint on access word on the esp value,
the program will brake few lines before the jump to OEP.

![](OEP.png)

Dumping in `0x44AC9B` the imports was reconstructed with `RECconstractor` whic point us that the import in `RVA 4BFFC`.
After going to DUMP in ollyDbg to `RVA 4BFFC`-->`0x44BFFC` the imports seems to start at `0x44c000` to `0x44C0CC` -->`import size=0xCC`, imports fixed and the exe works fine

IDA shows that the main function has alot of junck instruction 

`
push eax
pop eax
push ebx
pop ebx
pusha
popa
nop
`
