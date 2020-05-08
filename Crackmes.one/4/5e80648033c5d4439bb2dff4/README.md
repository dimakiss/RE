## n30np14gu3's WTF(Where This Flag)
source: https://crackmes.one/crackme/5e82f7c733c5d4439bb2e037

# Challenge

An exe file  that askes us for input \
* **0 -maze game**
* **1 -megadecrypt game**

The description of the challenge is
``` 
There are three flags in this program.
The first flag is in the maze.
You will get the second flag by guessing the decryption password.
The third flag is hidden in the depths of the program.
```

# Solution

## The second flag
I opened the program with IDA and traced the function that decide if we input `0` or `1`, by cross referencing\
the string `Welcom to maze game` the string used in `sub_401170` which called by `sub_4046E0`.\
Immidiatly the `cmp     al, 31h` at `0x404D39` and `cmp     al, 30h` at `0x40528B`
![](404D39.png)

If `al== 1 or 0` we get here:
![](404D4E.png)

Under maze game we can see the 'sub_401170' from earlier if we follow `sub_4019C0` 
![](401A51srnd.png)

The number we input is stored in us XORed with `0FF7E6F9Ch` and then compered with `0FF6AFE74h`\
So if __number xor 0FF7E6F9Ch=0FF6AFE74h__ ---> __number=0FF6AFE74h xor 0FF7E6F9Ch__ ---> __1491e8 (1348072)__
![](solution.png) // 1->1348072 ->key

The second key is: __sbh{d0n7_u53_r4nd_f0r_cryp7!}__




