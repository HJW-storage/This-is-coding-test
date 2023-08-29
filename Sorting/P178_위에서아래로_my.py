N = int(input())

nums = []
for i in range(N):
    # temp = int(input())
    # nums.append(temp)
    nums.append(int(input()))
    
nums.sort(reverse=True)
# nums = sorted(nums, reverse=True)
for i in nums:
    print(i, end=' ')
    
