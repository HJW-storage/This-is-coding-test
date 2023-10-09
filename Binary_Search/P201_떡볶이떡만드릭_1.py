n , m = map(int, input().split())
rice = list(map(int, input().split()))

# print(rice)
end = max(rice)
def solution(arr, start, end):
    height = 0
    result = 0  # 결과값 
    
    while start <= end:
        mid = (start + end) // 2
        
        # 소비자가 가져가는 떡의 총 합 높이 구하기
        for i in rice:
            if i - mid > 0 :
                height += i - mid
                
        if height == m:
            return mid
        elif height < m:
            end = mid-1
        else:
            # 딱 정확하게 떡이 안 잘리는 경우 적어도 m이상을 가져간다고 했다. 
            # 그렇기에 height > m 일 때, result 에 저장해두고 return 한다. 
            result = mid
            
            start = mid+1

        print(start, mid, end)    
        height = 0  # 초기화 
        
    return result 

max_height = solution(rice, 0, end)
print(max_height)