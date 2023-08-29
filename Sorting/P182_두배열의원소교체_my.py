# 해당 문제의 제약조건 N <= 10^5 이므로 완전탐색은 불가. 
# 정렬 라이브러리 사용. O(NlogN)

def change_AB(nums_A, nums_B, K):
    # 시간복잡도 : 정렬 - O(NlogN)
    nums_A.sort()   # 오름차순 정렬  ex) A = [1, 2, 3, 4, 5]
    nums_B.sort()   # 오름차순 정렬  ex) B = [5, 5, 5, 6, 6]
    
    len_b = len(nums_B) - 1
    
    for i in range(K):
        if nums_A[i] < nums_B[len_b - i]:
            nums_A[i], nums_B[len_b - i] = nums_B[len_b - i], nums_A[i]     # 스와프 

    # print(nums_A)
    # print(nums_B)
    return sum(nums_A)

N, K = map(int, input().split())
nums_A = list(map(int, input().split()))
nums_B = list(map(int, input().split()))

result = change_AB(nums_A, nums_B, K)
print("K번의 바꿔치구 후 A 배열의 합은 : {}".format(result))

    