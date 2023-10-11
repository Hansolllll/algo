import math

def solution(numer1, denom1, numer2, denom2):
    if denom1 != denom2:
        denom = denom1 * denom2
        numer = (denom2 * numer1) + (denom1 * numer2)
    else:
        denom = denom1
        numer = numer1 + numer2
    
    g_c_d = math.gcd(numer, denom)
    answer = [int(numer / g_c_d), int(denom / g_c_d)]

    return answer


print(solution(1, 2, 3, 4))
print(solution(9, 2, 1, 3))