def solution(n, arr1, arr2):
    answer = []
    # 이진수로 변환하기 
    for i in range(len(arr1)):
        arr1[i] = bin(arr1[i])[2:]
        arr2[i] = bin(arr2[i])[2:]

        while len(arr1[i]) < n:
            arr1[i] = '0' + arr1[i]
        while len(arr2[i]) < n:
            arr2[i] = '0' + arr2[i]
    # arr 안에서 이진수 자릿수가 모두 0일 때를 제외하고 array에 #추가 
    for i in range(len(arr1)):
        array = ''
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                array += ' '
            else: 
                array += '#'
        # answer에 array 추가 
        answer.append(array)

    return answer

print(solution(5, [9,20,28,18,11], [30,1,21,17,28]))
print(solution(6, [46,33,33,22,31,50], [27,56,19,14,14,10]))