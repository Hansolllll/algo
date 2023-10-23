import sys
sys.stdin = open('input.txt')
              
T = int(input())
for tc in range(1, 1+T):
    # N:화덕 칸수 M:피자수 
    N, M = map(int, input().split())
    # ch:치즈의 양
    ch =  list(map(int, input().split()))
    
    oven = []
    count = 0
    for _ in ch:
        # oven안에 피자가 다 차있지 않으면 피자 추가
        if len(oven) < N:
            oven.append(ch[0])
            ch.remove(ch[0])
       # oven안에 피자가 다 차있는 경우
        if len(oven) == N:
            while True:
                a = oven[-1]
                oven.pop()
                oven.insert(0, a)
                count += 1

            # 피자가 한바퀴 돌았을 때
                if count % M == 0:
                    ch[0] = M//2
                    if ch[0] == 0:
                        oven.pop()
                    else:
                        break

    if len(oven) == 1:
        result = oven[0]

    print(result)


!!!!
    N, M = list(map(int, input().split()))
    # ch:치즈의 양
    Ci =  list(map(int, input().split()))

    #피자 번호 붙이기
    before = []
    for i in range(M):
        before.append([Ci[i]], i)

    #화덕
    queue  = [0] * N

    #완성된목록
    after = []

    #완성피자가 구워야 하는 피자 갯수랑 같아질때까지 반복
    while len(after) != M:
        #화덕입구에 공간이 비었으면
        if queue[0] == 0:
            #넣을 피자가 있다면
            if len(before) != 0:
                #남은 첫번째 피자 치즈의 양과 번호
                cheeze, idx = before.pop(0)
                #화덕에 넣기
                queue.append([cheeze, idx])
                #화덕돌리기
                
        #화덕입구에 공간이 없으면(이미 구워지고 있는 피자가 있는 경우)
        else:
            pass