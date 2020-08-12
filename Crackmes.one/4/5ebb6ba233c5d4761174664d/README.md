## thesaviorsrule's The Ultimate Crack Me
source: https://crackmes.one/crackme/5ebb6ba233c5d4761174664d

# Challenge

A window that asks for a password

# Solution

This program was written by __.NET__, Detect It Easy verified it.\
I opened the exe with `Dnspy`. Go to entry point reveals that the start of the code is at the method __fbbbc()__,\
Which crates an oblject of __mQbbb()__.\
At ____mQbbb()__ __fbbbc()__ and __hbbbc()__ compares `Text` to some global variable.\
__fbbbc():__

![](fbbbc.png)

__hbbbc__ looks the same but without the compare to `""`.

by clicking at __pqcgb.dbbbb__ I got here:

![](dbbbb.png)

I put a breakpoint at the instruction, stepped into __pqcg()__, and run until return. The returned text will be our string.\
The text on return is:__Astolfobestclient__ which is the correct flag.

![](solution.png)
