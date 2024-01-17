def solution(s):
    answer = ''
    # 문자열 내 반복 
    for i in range(len(s)):
        # 공백이라면 공백 추가
        if s[i] == ' ':
            answer += ' '
        
        # 공백이 아니면서 문자열의 길이가 1이상인 경우
        elif len(answer) != 0:
            # answer의 마지막 문자가 소문자거나, 공백일 경우 대문자 넣기
            if answer[-1].islower() or answer[-1]==' ':
                answer += s[i].upper()
            # 그 외의 경우 소문자 넣기
            else:
                answer += s[i].lower()
        
        # answer가 비었을 경우 대문자 추가
        else:
            answer += s[i].upper()
            

    return answer

print(solution("try hello world"))