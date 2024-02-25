def solution(n):
    mod=int(1e9)+7
    res=1
    i=n-2
    Pathsi=1
    while(i>0):
        Pathsi=(Pathsi * i) %mod
        res=(res+Pathsi)%mod
        i-=1
    return res
