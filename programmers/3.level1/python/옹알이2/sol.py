def solution(babbling):
    words = ['aya', 'ye', 'woo', 'ma']
    count = 0

    for i in range(len(babbling)):
        # 연속된 발음이 없다면
        if 'aya'*2 not in babbling[i] and 'ye'*2 not in babbling[i] and 'woo'*2 not in babbling[i] and 'ma'*2 not in babbling[i]:
            # 앞 글자들이 words에 포함되어있다면 반복해서 제거 
            while babbling[i][:2] in ['ye', 'ma'] or babbling[i][:3] in ['aya', 'woo']:
                if babbling[i][:3] in words:
                    babbling[i] = babbling[i][3:]

                elif babbling[i][:2] in words:
                    babbling[i] = babbling[i][2:]
        # 모두 제거한 후의 길이가 0이라면 count +1
        if len(babbling[i]) == 0:
            count += 1
        
    return count

print(solution(["aya", "yee", "u", "maa"]))
print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))
print(solution(['yeye', 'ayama', 'mama']))