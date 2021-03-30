def solution(n, m):
    gcd = GCD(n,m)
    lcm = LCM(gcd,n,m)
    return gcd, lcm

def GCD(a,b):
    if b==0:
        return a
    else:
        return GCD(b, a%b)

def LCM(gcd,a,b):
    return a*b//gcd

print(solution(3,12))
# https://programmers.co.kr/learn/courses/30/lessons/12940
