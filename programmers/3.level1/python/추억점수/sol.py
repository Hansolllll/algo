def solution(name, yearning, photo):
    answer = []
    dic = {}
    # dic에 이름-점수 추가 
    for i in range(len(name)):
        dic[name[i]] = yearning[i]

    # 반복문으로 photo에 있는 이름 점수로 환산 
    for j in range(len(photo)):
        for k in range(len(photo[j])):
            if photo[j][k] in dic:
                photo[j][k] = dic[photo[j][k]]
            else:
                photo[j][k] = 0
                
        # photo[i] 마다 점수 합 answer에 추가 
        answer.append(sum(photo[j]))
    return answer

print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may", "kein", "kain", "radi"],["may", "kein", "brin", "deny"], ["kon", "kain", "may", "coni"]]))
print(solution(["kali", "mari", "don"], [11, 1, 55], [["kali", "mari", "don"], ["pony", "tom", "teddy"], ["con", "mona", "don"]]))
print(solution(["may", "kein", "kain", "radi"], [5, 10, 1, 3], [["may"],["kein", "deny", "may"], ["kon", "coni"]]))