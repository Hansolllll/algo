def solution(n, m):
    n_num = []
    m_num = []
    for _ in range(1, n+1):
        if n % _ == 0:
            n_num.append(_)
    for _ in range(1, m+1):
        if m % _ == 0:
            m_num.append(_)
    num = set(n_num) & set(m_num)
    
    return [max(n_num), n*m/max(n_num)]
            