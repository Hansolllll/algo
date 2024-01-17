def solution(s):
    answer = []
    idx_dic = {}
    for i in range(len(s)):
        # 문자가 dic에 있다면 
        if s[i] in idx_dic:
            # answer에 현 위치 - 이전 위치 값 넣기 
            answer.append(i - idx_dic[s[i]])
            # 문자가 key인 value로 현 위치 넣기 
            idx_dic[s[i]] = i
        # 문자가 dic에 없다면 
        else:
            # -1 넣기
            answer.append(-1)
            idx_dic[s[i]] = i

    return answer

print(solution('banana'))
print(solution('foobar'))