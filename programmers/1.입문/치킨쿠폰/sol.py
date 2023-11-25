def solution(chicken):
    eaten = 0 # 먹은 서비스치킨 수
    coupon = chicken # 남은 쿠폰 수(처음 쿠폰수 = 주문한 치킨수)

    while coupon // 10 > 0:
        # 서비스치킨 => 쿠폰수를 10장으로 나눈 몫
        service = coupon // 10 

        # eaten에 서비스치킨 더하기
        eaten += service
        
        # 남은 쿠폰 수 => 서비스치킨수 + 나머지 
        coupon = service + (coupon%10)

    return eaten
    

print(solution(100))
print(solution(1081))
print(solution(1999))