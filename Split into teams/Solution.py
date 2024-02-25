# students numbered from 1 to n
# their scores are given in an array -> ith score belongs to the ith student
# split the students into teams in a way that sum of scores of each team is equal
# find the maximum number of teams that can be formed this way
def solution(n):
    # Write your code here
    if n%2 == 0:
        return n//2
    else:
        return math.ceil(n/2)
