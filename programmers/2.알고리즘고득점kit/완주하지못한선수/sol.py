def solution(participant, completion):
    my_hash = dict()

    for player1 in participant:
        if player1 in my_hash:
            my_hash[player1] += 1
        else:
            my_hash[player1] = 1

    for player2 in completion:
        my_hash[player2] -= 1

    for player, count in my_hash.items():
        if count > 0:
            return player


def solution(participant, completion):
    s_part = sorted(participant)
    s_comp = sorted(completion)
    
    for i in range(len(s_comp)):
        if s_part[i] != s_comp[i]:
            return s_part[i]
        elif s_part[i] == s_comp[i]:
            continue
    return s_part[-1]


print(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))
print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
print(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]))
