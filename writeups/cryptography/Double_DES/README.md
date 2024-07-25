# Double DES #
This is a write-up for [Double Des](https://play.picoctf.org/practice/challange/140).  
`Heap 3` rated medium
The given files are at the `file` directory.  

## The Challenge ##
> I wanted an encryption service that's more secure than regular DES, but not as slow as 3DES...  
> The flag is not in standard format.  
> nc mercury.picoctf.net 33425
> [ddes.py](./files/ddes.py)

## How I Solve ## 
As we learned at the class, double des is not so good. We can use the "meet in the middle" approach.  
I created a [solve.py](./files/solve.py) files that do exactly what we talked about in class.  

I gave him:  
1. plain text that I choose
2. the cypher of the same plain text
3. the cypher of the flag

The output was that the flag is `af5fa5d565081bac320f42feaf69b405`, looks a little weird but the challenge says that the flag is not in the standard format so I tried it, and it worked! We found the flag

