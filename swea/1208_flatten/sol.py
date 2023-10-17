import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    dump = int(input())
    # numbers = input()
    # N = 옮길 횟수, number = 상자배열

    number_list = list(map(int, input().split()))
    my_list = sorted(number_list) # 상자 크기순 정렬
    
    for i in range (dump):
        if max(my_list) - min(my_list) > 1:
            my_list[-1] -= 1
            my_list[0] += 1
            my_list = sorted(number_list)
        result = max(my_list) - min(my_list)


    
    print(result)