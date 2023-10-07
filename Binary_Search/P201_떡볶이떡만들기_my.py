n, m = map(int, input().split())
rice_cake = list(map(int, input().split()))
rice_cake.sort()    # 오름차순 정렬
# print(rice_cake)


final_result = 0
def solution(start, end):
    result = 0
    mid = (n-1)//2
    # height 높이 이후의 인덱스만 검사하면 된다. 
    # height보다 낮은 쪽은 어차피 떡이 안잘려서 계산할 필요 없음.
    
    # 이진탐색의 개념
    while end - start > 1 and mid - start > 1:
        mid = (start + end) // 2
        height = rice_cake[mid] # 중간값으로 높이 시작.
        
        for i in range(mid, n):
            result += rice_cake[i] - height # 높이 계산
        
        # 만약 결과랑 일치하면 리턴. 이진 탐색의 개념으로 height 값의 어림을 계산하는 것.
        if result == m:
            return height
        elif result < m:
            end = mid - 1
        else:
            start = mid + 1
        result = 0  # 초기화
        
    # print("여기로 옴")
    # print((start, end))
    # 리턴이 안되면 사잇값이라는 의미.
    if end == n-1:
        to = rice_cake[end]+1
    else:
        to = rice_cake[end+1]
    # print(to)
    for h in range(rice_cake[start], to):
        for j in range(start, n):
            tmp = rice_cake[j] - h # 높이 계산
            if tmp > 0:
                result += tmp
        # print(result)
        # 만약 결과랑 일치하면 리턴. 
        if result == m:
            return h
        else:
            result = 0  # 초기화 
            

# 결과 출력
final_result = solution(0, n-1)
print(final_result)
