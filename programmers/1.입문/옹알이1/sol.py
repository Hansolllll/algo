from itertools import permutations
def solution(babbling):
    answer = 0
    say = ['aya', 'ye', 'woo', 'ma']
    
    # 2,3,4개 골라 조합가능한 단어 만든 후 say에 추가
    for a,b in permutations(['aya', 'ye', 'woo', 'ma'], 2):
        say.append(a+b)
        
    for a,b,c in permutations(['aya', 'ye', 'woo', 'ma'], 3):
        say.append(a+b+c)

    for a,b,c,d in permutations(['aya', 'ye', 'woo', 'ma'], 4): 
        say.append(a+b+c+d)

    # babbling에 있는 단어가 say에 있는지 확인
    for char in babbling:
        if char in say:
            answer += 1

    return answer

print(solution(["aya", "yee", "u", "maa", "wyeoo"]))
print(solution(["ayaye", "uuuma", "ye", "yemawoo", "ayaa"]))