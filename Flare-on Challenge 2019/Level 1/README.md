## Leverl 1
source: http://flare-on.com/

# Challenge

An exe that waits for key

# Solution

The program is written in C# .NET so Reflector (.NET decompiler) may be helpfull.\

![](theformsinRef.png)

If we go to the void function `FireButton_Click` there is comperison between the text box and the string `"RAINBOW"`\
![](FireButton_Click.png)

And its the correct value.\
Next we have another code we need to enter of stage 2. By looking at the stage2 Form,\
there is fuction call named `isValidWeaponCode` which takes our input value.
![](isValidWeaponCode.png)

There is a the function XOR every char by 'A' stores is in char array and comperes it with\
```
['\x0003', ' ', '&', '$', '-', '\x001e', '\x0002', ' ', '/', '/', '.', '/']
```
``` C#
            char[] code = new char[] { '\x0003', ' ', '&', '$', '-', '\x001e', '\x0002', ' ', '/', '/', '.', '/' };
            for(int i=0; i<code.Length;i++)
            {
            Console.Write((char)(code[i]^'A'));
            }
```
and the output is: __Bagel_Cannon__ which is our code for stage2 and we get the flag:__Kitteh_save_galixy@flare-on.com__
