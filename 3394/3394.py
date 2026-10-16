"""ส่งต่อ"""
n, s = map(int, input().split())
a = [int(input()) for _ in range(n)]

visited = set()

while s and s not in visited:
    visited.add(s)
    s = a[s - 1]

print(len(visited))
