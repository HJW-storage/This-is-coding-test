def change_AB(nums_A, nums_B, K):
    # 시간복잡도 : 정렬 - O(NlogN)
    nums_A.sort()   # 오름차순 정렬  ex) A = [1, 2, 3, 4, 5]
    nums_B.sort(reverse = True)   # 내림차순 정렬  ex) B = [6, 6, 5, 5, 5]
    
    for i in range(K):
        if nums_A[i] < nums_B[i]:
            nums_A[i], nums_B[i] = nums_B[i], nums_A[i] # 스와프 
        else:   # 그 이후 동작은 의미 없음으로 반복문 탈출.
            break

    # print(nums_A)
    # print(nums_B)
    return sum(nums_A)

N, K = map(int, input().split())
nums_A = list(map(int, input().split()))
nums_B = list(map(int, input().split()))

result = change_AB(nums_A, nums_B, K)
print("K번의 바꿔치구 후 A 배열의 합은 : {}".format(result))