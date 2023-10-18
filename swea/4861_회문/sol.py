import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # N:배열수 M:문자열크기

    # 인풋데이터로 matrix리스트 채우기 
    matrix = []
    for _ in range(N):
        matrix.append(input())

    result = ''
    # 가로 기준점 구하기 위한 반복
    for i in range(N):
        for j in range(N-M+1):
            
            # 시작점에서 한칸씩 이동하며 문자열 앞뒤 비교
            for row in range(M//2): # 문자열을 절반으로 나눠서(0~절반/절반~끝) 앞구간에서만 반복비교 
                front = matrix[i][j+row]
                back = matrix[i][j+M-row-1]#[i] 반대쪽은 [len() -i -1] 응용 

                if front == back: 
                    continue # 범위내 문자열이 계속 같은지 확인 
                else:
                    break # 다름을 발견한 순간 for문 깨고 나가서 j+1 확인
            else: # 반복문에서 문자열의 앞뒤가 동일한지 확인 (= break 안만났을 경우)
                for k in range(M): 
                    result += matrix[i][j+k] # 시작점 i,j 위치에서부터 문자열 길이 M 범위 내에 있는 문자 합치기 

    # 세로 기준점 구하기 위한 반복:
    for j in range(N):
        for i in range(N-M+1):
            for col in range(M//2):
                front = matrix[i+col][j] 
                back = matrix[i+M-col-1][j]

                if front == back:
                    continue
                else:
                    break

            else:
                for k in range(M):
                    result += matrix[i+k][j]




    print(f'#{tc} {result}')

