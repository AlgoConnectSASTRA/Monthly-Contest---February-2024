#given a string s containing only lowercase alphabets of length n, check if the subsequence 'azac' is present

def solution(n, s):
    # Write your code here
    required = 'azac'
    j = 0
    i = 0
    while j<4 and i<n:
        if s[i]==required[j]:
            j += 1
        i += 1
    if j==4:
        return "YES"
    else :
        return "NO"
