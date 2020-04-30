## TheReverser's Find password
source: https://crackmes.one/crackme/5e9f4e8033c5d476117463a9

# Challenge

An `password.exe` file in which written when open `inserisci la password per accedere al programma`\
only guess that its wait for password.
The description also offer us to try and by pass the password check.

# Solution
After entring random pass word its print `password errata.` and `inserisci la password per accedere al programma` again.\
By uploding the file to IDA the `password errata.` is seen in the `Strings window`, the strings's location is `0x4B9091`.\
By xros referensing this string we can see that the only access of this string is in `sub_4B57D0+C8` or `0x04B5898`.\
There is a loop between `0x04B58E8` and `0x04B5902` to `0x04B5890`,\
when `0x04B58FB` has a __memcmp__ call. 

`Note: if we scroll up we will have the strings  djejie and ggkfjgjfrg  ,which seem suspicous but we continue`
![](xref.png)

The program will not brake at the first time we input password, seems there is pre rutine to this code\
its not seems to be importent.

At the second input it will only brake at the conditional jump before it at `0x4B58E8`.\
By setting the zero flag on we will by pass that conditional jump and brake on __memcmp__.\
The __memcmp__ gets 2 values , `s1=006CFEF0  s2=006CFED8`\
![](s1s2.png)

`123` our imput compared with `djejie`(as I thougth) if they are equal\
`EAX` will be equal `0` and the jump at `0x4B5902` will not happaned, the loop wil end the message `benvenuto` will be printed.\
As I told for the first time the password is not correct but the second time it work fine.\
![](solution.png)

In our solution we avoided the 2 conditional jumps at `0x04B58E8` and `0x04B5902`\
by noping them we sopuse to always be right.

```asm
004B58E8 JNZ SHORT password.004B5890 
to
004B58E8 nop

and 
004B5902 JNZ SHORT password.004B5890
to 
004B5902 nop
```

