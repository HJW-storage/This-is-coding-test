# 재귀함수 활용

# made by JW
def gcd(a,b):
    # a가 항상 더 큰수가 되도록.
    if a < b:
        temp = a
        a = b
        b = temp
    if a % b == 0:
        return b
    else:
        r = a % b
        return gcd(b, r)
    
a , b = map(int, input().split())
result = gcd(a, b)
print(result)
        
        
# # 모범 답안
# def gcd(a, b):
#     if a % b == 0:
#         return b
#     else:
#         return gcd(b, a % b)
#         # a, b 대소 비교를 안해도 한번 실행이 되면 a가 더 큰 값이 된다. 
# print(gcd(192, 162))