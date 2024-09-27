<h3 style="text-align:center;">Coelho Compression Algorithm 
</h3>


Ive made an algorithm that compresses data. The algorithm works like below

Have a decompress data (say 1503022, which is equivalent of having some bytes)

Base used was 10, but other bases are possible as well...

Then subtract 

$$1503022 - 1000000$$
$$503022 - 500000$$
$$ 3022 - 3000 $$
$$ 22 - 20 $$
$$ 2 - 2 $$
$$ 0 $$

make a list of subtraeeds
[1000000,50000,3000,20,2]



$1503022 = 1 \times 10^6 + 5 \times 10^4 + 3000 \times 10^3 + 2 \times 10^1 + 2$

use the distributive law of math, and properties of exponent, meaning multiply numbers with same base, and different exponent is equal to base elevate to exponent1+exponent2

So for a exponent example, i multiply
$1 \times 10^6 \times (5 \times 10^{-2})$  , equals $5 \times 10^4$ ...which is the same element on list , 50000

$1 \times 10^6 ( 5 \times 10^{-2} + 3 \times 10^{-3} + 2 \times 10^{-5} + 2 \times 10^{-6})$

Why do i use the exponent law?

because what's inside the parentsys, is a double number...so it only takes 8 bytes..

So compressing uses

first byte = 6
8bytes = stuff inside parenthsys


**This is copy right...**

You can't code (use the idea to code), use this algorithm, distribute the algorithm for others, copied, use the same concepts in the same way, as in this algorithm.

you can't use the algorithm on your code...
you can't change little things ( like base of number choosen) on anything, and use it


you need my explicit permission for the above...

andrealbergaria@gmail.com




