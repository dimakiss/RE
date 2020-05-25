## Harshil55's It's Easy
source: https://crackmes.one/crackme/5ebebde133c5d449d91ae4ec

# Challenge

An exe file that waits for `Name` and `Serial Key`\
Output `Wrong Serial Key` if incorrect

# Solution

I opened the exe with die.exe and it's detected that this program is written in __.NET__\
!()[die.png]

The dnSpy can be used here to decompile the exe file. I opened the exe in dnSpy.\
The main form contains a method called `btnCheck_Click` which decide if the name and the serial matches.\

!()[dnspy.png]

__text__ which must be larger than 4, stores the upper case of the 4 characters of the name.\
__text2__ stores the serial key.\
The __text__ 3,4,5 saves the `text` form __productId__ 1,2,3  respectively.\
productId is a Label object which assigned by the method `InitializeComponent` where we can see the text value of every Label.\
* __text3(productId1)__="X398"
* __text4(productId2)__="33CE"
* __text5(productId3)__="A639"

Back to the ` btnCheck_Click` method __text2__ compered with __value__ when __value = text3 + text + text4 + text5__\
So if the serial key should look like that: X398+Name+33CEA639 when its string value so the __+__ is just joining the strings.

!()[solution.png]
