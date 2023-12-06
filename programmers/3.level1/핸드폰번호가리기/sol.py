def solution(phone_number):
    # 방법 1
    answer = ['*' for i in range(len(phone_number)-4)]
    for i in range(len(phone_number)-4, len(phone_number)):
        answer.append(phone_number[i])


    return ''.join(answer)

    # 방법 2
    answer = ['*' for i in range(len(phone_number)-4)]
    return ''.join(answer) + phone_number[-4:]

print(solution('01033334444'))
print(solution('027778888'))