# ImagePrc
source: http://reversing.kr/challenge.php

## Challenge
we have an exe file, we can draw on it and click check, but we get `wrong` message. 

![](WrongDialogBox.jpg)


## Solution
I opened the `ImagePr` with ollyDbg and after the `wrong` message pause the program.
After looking at the call stack I got here.

![](wrong_message.jpg)

The jump `JNZ SHORT ImagePrc.004013CD` at `0x4013AA` jump to our `wrong` message and if to jump or not decided at the `CMP DL,BL` at `0x4013A8`.

At `0x401381-0x401397` we can see Resource loading there is only one resource file the picture from Resource Hacker:

![](resHacker.jpg)

Because the the location of the loaded resource is in `EAX` and `EAX's` value is moved to `BL` we will asume that `DL` is the values from the program.

Now, we know that the number `FF or 00` seems to be the code for the image, the name of thats challenge is ImagPrc what means we need to get the original picture.
The resource section have 9060 bytes we need to check the window parameters to try and convert it to the original picture.

![](windowparameters.jpg)
