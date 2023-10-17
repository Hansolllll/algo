import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))


    num_list = []
    # while len(num_list) < 11:
    while True:
        max_num = 0
        for i in range(len(numbers)):
            if numbers[i] > max_num:
                max_num = numbers[i]
            
        num_list.append(max_num)
        numbers.remove(max_num)

        min_num = 100000000
        for j in range(len(numbers)):
            if numbers[j] < min_num:
                min_num = numbers[j]

        num_list.append(min_num)
        numbers.remove(min_num)

        if len(num_list) == 10:
            break

    temp = map(str, num_list)
    result = ' '.join(temp)
    print(f'#{tc} {result}')