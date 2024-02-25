# Problem link 
https://www.hackerrank.com/contests/monthly-contest-february-2024/challenges/split-into-teams-1-1

# Approach 
1. We want the number of people in a team to be as minimum as possible to have maximum number of teams
2. If we take one people per team, the score wouldn't be equal
3. But we can take two people per team and have equal score based on the following observation
       a. assume n = 10, then 1 + 10, 2 + 9, 3 + 8 ...
       b. This gives exactly n/2 teams with equal score, with as minimum people as possible per team
4. For odd numbers, we can just ignore the last one and do the same. 
