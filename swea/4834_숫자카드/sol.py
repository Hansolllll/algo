import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    numbers = input()

    count = 0
    count_num = 0
    # 반복문으로 numbers 안에 num이 몇개있는지 세고,
    # count와 비교해서 더 크다면 count에 저장
    # 그 때의 숫자를 count_num에 저장  
    for num in numbers:
        if numbers.count(num) > count:
            count = numbers.count(num)
            count_num = num
        elif numbers.count(num) == count:
            if num > count_num:
                count_num = num

    print(f'#{tc} {count_num} {count}')


# 풀이 1
# for tc in range(1, T+1):
#     N = int(input())
#     numbers = input()
#     # N:카드장수 numbers:카드배열

#     counter = [0 for i in range(10)]
#     #counter = [0] * 10와 동일
   
#     for number in numbers:
#         counter[int(number)] += 1

#     card_count = 0
#     card_number = 0

#     for idx, value in enumerate(counter):
#         if card_count <= value:
#             card_count = value
#             card_number = idx
    
#     print(f'#{tc} {card_number} {card_count}')