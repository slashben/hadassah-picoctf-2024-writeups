# README #
This is the write-up for the challenge "substituion 0" challenge in PicoCTF
# Description
A massage has come in but it seems to be all scrambled.
Luckily it seems to have the key at the beginning. can you crack the subtitution cipher?
download the massage here: https://artifacts.picoctf.net/c/152/message.txt

this is the msg: 
![img.png](img.png)

# How to solve it
Everything that is in A will be replaced by D, and everything that is in D will be replaced by some other character, but the characters will always be fixed. For example, A might have been replaced by P, B might have been replaced by A, all All the Cs might have been replaced by Q. This is the key that i'll be using.
im using https://www.dcode.fr/cipher-identifier. pasting the key and the massage,
and gets the flag: picoCTF{5UB5717U710N_3V0LU710N_59533A2E}