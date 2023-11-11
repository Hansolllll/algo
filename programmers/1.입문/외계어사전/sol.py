def solution(spell, dic):
    for i in range(len(dic)):
        val = []
        # dic 단어 내부 문자 반복
        for char in dic[i]:
            # dic에서 i번째 단어 안에 있는 문자 수와 spell 안의 문자 수 비교
            # (dic[i] 안의 중복 문자 고려)
            if dic[i].count(char) == spell.count(char):
                # 같다면 빈 리스트에 1 추가
                val.append(1)
            # val리스트 길이는 문자수 동일한 경우의 수 
            # => 이게 spell 길이와 동일할 경우는 spell 내의 문자가 모두 dic[i]에 있단 의미
            if len(val) == len(spell):
                return 1
            
    return 2

            

print(solution(["p", "o", "s"], ["sod", "eocd", "qixm", "adio", "soo"]))
print(solution(["z", "d", "x"], ["def", "dww", "dzx", "loveaw"]))
print(solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"]))
