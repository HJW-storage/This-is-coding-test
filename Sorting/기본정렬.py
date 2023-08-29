# 선택 정렬 - 주어진 배열에서 가장 작은 값을 찾아 인덱스 0번부터 순차적으로 교체하여 오름차순으로 정렬한다. O(n^2)
def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] # 스와프 
    print(arr)
    
    
# 삽입 정렬 - 알맞은 위치에 삽입한다. 정렬을 시작하기전 이전까지는 정렬이 완료되어있는 상태.
def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):   # 인덱스 i부터 1까지 감소하며 반복하는 문법
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j] # 한칸씩 이동.
            else:   # 자신보다 작거나 같은 데이터를 만나면 해당 위치에서 멈춘다. 
                break
    print(arr)
    
    
# 큌 정렬 - 피벗을 기준으로 큰 숫자와 작은 숫자를 교환
def quick_sort_1(arr, start, end):
    if start >= end:  # 원소가 1개인 경우 종료
        return
    
    pivot = start   # 피벗은 첫번쨰 원소
    left = start + 1
    right = end
    
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:   # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            arr[left], arr[right] = arr[right], arr[left]
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 큌 정렬 다시 반복 수행
    quick_sort_1(arr, start, right-1)
    quick_sort_1(arr, right+1, end)
    # print(arr)
    return arr

# 큌 정렬 - 파이썬의 장점 이용
def quick_sort_2(arr):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(arr) <= 1:
        return arr
    
    pivot = arr[0]  # 피벗은 첫번째 원소
    tail = arr[1:]  # 피벗을 제외한 리스트
    
    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분
    
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환한다.
    return quick_sort_2(left_side) + [pivot] + quick_sort_2(right_side)

arr1 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
arr2 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
arr3 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
arr4 = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
selection_sort(arr1)
insertion_sort(arr2)
print(quick_sort_1(arr3, 0, len(arr3) - 1))
print(quick_sort_2(arr4))