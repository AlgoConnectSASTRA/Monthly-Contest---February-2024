# Problem link 
https://www.hackerrank.com/contests/monthly-contest-february-2024/challenges/azac/problem

# Prerequisite 
What is a subsequence ? -> https://www.geeksforgeeks.org/subsequence-meaning-in-dsa/

# Approach 
1. Initiate a substring with the value 'azac' [temp = 'azac']
2. Declare two pointers, one for the string and one for the subsequence [ i = 0, j = 0]
3. Iterate through the given string. If s[i] == temp[j], increment j
4. Break when j becomes 4 or when i reaches the end of the string.
