import pprint
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, 1+T):
    # V:노드수 E:간선수
    V, E = list(map(int, input().split()))

    nodes = [[0] * (V+1) for _ range(V+1)]

    for _ in range(E):
        node = list(map(int, input().split()))
        
        start = node[0]
        end = node[1]

        nodes[start][end] = 1
        nodes[end][start] = 1

    # S:출발노드 G:도착노드
    S, G = list(map(int, input().split()))
    
    #방문체크용 리스트
    check_list = [False] * (V+1)

    # BFS를 구현하기 위한 queue
    queue = [] 

    # 거리계산을 위한 리스트
    distance = [0] *(V+1)

    # 시작전 시작노드 저장
    now = S
    check_list[now] = True
    queue.append(now) 

    while len(queue):
        now = queue.pop(0)
        checck_list[now] = True
        
        # now와 연결되어있는 다른 노드 순회
        for link in range(V+1):
            if  nodes[now][link] == 1:

            # 아직 방문하지 않은 nodes가 있다면
            # if not check_list[link]
            if checck_list[link] == False:
                queue.append(link)

                # 이전노드의 거리 + 1
                distance[link] = distance[now] + 1

    print(distance[G])