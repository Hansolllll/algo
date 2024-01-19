def solution(strings, n):
    answer = []
    for i in range(len(strings)):
        # n번째 문자를 각 단어 앞에 붙이기 
        strings[i] = strings[i][n]+strings[i] 
    # n번째 문자 붙은 상태에서 정렬 후 두번째문자부터 끝까지 슬라이싱
    return list(map(lambda x: x[1:], sorted(strings)))

    # 오답 
    # dic = {}
    # for char in sorted(strings):
    #     if char[n] not in dic:
    #         dic[char[n]] = char 
    #     else: 
    #         dic[(char[n]+'a')] = char

    # return list(map(lambda x: x[-1], sorted(dic.items())))

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))