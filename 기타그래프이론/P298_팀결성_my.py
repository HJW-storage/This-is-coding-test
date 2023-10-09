def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
def check_team(parent, s1, s2):
    global result
    s1 = find_parent(parent, s1)
    s2 = find_parent(parent, s2)
    if s1 == s2:
        # print("YES")
        result.append("YES")
    else:
        # print("NO")
        result.append("NO")
        
        
# 7 8
# 0 1 3
# 1 1 7
# 0 7 6
# 1 7 1
# 0 3 7
# 0 4 2
# 0 1 1
# 1 1 1

result = []
n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i
    
for _ in range(m):
    p, s1, s2 = map(int, input().split())
    if p == 0:
        union_parent(parent, s1, s2)
    else:
        check_team(parent, s1 ,s2)
        
for i in result:
    print(i)