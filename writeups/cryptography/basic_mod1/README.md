# basic-mod1

This is the write-up for the challenge "basic-mod1" challenge in PicoCTF

# The challenge

## Description
We found this weird message being passed around on the servers, we think we have a working decryption scheme.
Download the message here.
Take each number mod 37 and map it to the following character set: 0-25 is the alphabet (uppercase), 26-35 are the decimal digits, and 36 is an underscore.
Wrap your decrypted message in the picoCTF flag format (i.e. picoCTF{decrypted_message})

![](img/screenshot1.png)

![image](https://github.com/Afek-Sulimani/hadassah-picoctf-2024-writeups/assets/73389421/ae5de958-7244-48c5-8431-ccedcb558498)


## Hints
1. Do you know what mod 37 means?
2. mod 37 means modulo 37. It gives the remainder of a number after being divided by 37.

## Initial look
file named "message.txt" contains a list of numbers
# How to solve it
First I followed the description and opened the file - "message.txt" which contained the following:

```bash
350 63 353 198 114 369 346 184 202 322 94 235 114 110 185 188 225 212 366 374 261 213
```

I performed the mod operation with 37 on all list values. And I got the following result:
```bash
[17, 26, 20, 13, 3, 36, 13, 36, 17, 26, 20, 13, 3, 36, 0, 3, 3, 27, 33, 4, 2, 28]
```

I created a code in Python that for each numerical value the mapping is adjusted according to the requirements and I got the following result:
```bash
R0UND_N_R0UND_ADD17EC2
```
Voila!!! 😎


The flag is `picoCTF{R0UND_N_R0UND_ADD17EC2}`

