# 1. 재귀적으로 구현하기
# def binary_search(array, target, start, end):
#     if start > end:
#         return None
#     mid = (start + end) // 2
    
#     if array[mid] == target:
#         return mid
#     elif array[mid] > target:
#         return binary_search(array, target, start, mid - 1)
#     else:
#         return binary_search(array, target, mid + 1, end)
    
# n, target = list(map(int, input().split()))

# array = list(map(int, input().split()))

# result = binary_search(array, target, 0, n-1)
# if result == None:
#     print("원소가 존재하지 않습니다.")
# else:
#     print(result + 1)
    

# 2. 반복문으로 구현하기
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
    
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n, target = list(map(int, input().split()))

array = list(map(int, input().split()))

result = binary_search(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다.")
else:
    print(result + 1)
    
