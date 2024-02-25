# Problem link :
https://www.hackerrank.com/contests/monthly-contest-february-2024/challenges/find-number-of-paths

# Prerequisites :
Basic mathematics

# Approach :

1. We know that starting is 1 and ending is n.
2. We can have anything from 0 cities to n-2 cities in between 1 and n.
3. We want to calculate all the possible paths so we will take  1+sum of (Paths<sub>i</sub>),

Where Paths<sub>i</sub> is the number of Paths when there are i cities in between 1 and n (1<=i<=n-2).

4. Paths<sub>i</sub> can be simply calculated with (n-2)Pi

Overall the sum can be simplified down to : 1+ (n-2) +(n-2)(n-3) + ... (n-2)!

5. But calculating each term separately will lead to TLE due to O(n<sup>2</sup>), 
But the i-th term is simply, previous term  *(n-2-i)

7. Finally to prevent out of bounds, we mod with (10^9)+7 at each step.
