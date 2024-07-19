# rail-fence

This is the write-up for the challenge "reil-fence" challenge in PicoCTF

# The challenge

## Description
A type of transposition cipher is the rail fence cipher, which is described [here](https://en.wikipedia.org/wiki/Rail_fence_cipher). Here is one such cipher encrypted using the rail fence with 4 rails. Can you decrypt it?
Download the message [here](https://artifacts.picoctf.net/c/188/message.txt).

## How to solve it
* Download the text file with this text - `Ta _7N6D49hlg:W3D_H3C31N__A97ef sHR053F38N43D7B i33___N6`
* Open Rail fence cipher calculator [for example](https://planetcalc.com/6947/)
* In the description they wrote the text was encrypted using the rail fence with **4 rails**, so insert the text and the key=4 into the calculator, decrypt it and get - `The flag is: WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997`

## flag
The flag is `picoCTF{WH3R3_D035_7H3_F3NC3_8361N_4ND_3ND_4A76B997}`


Cheers 😄