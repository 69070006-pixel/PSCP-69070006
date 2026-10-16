"""หั่นขนมปัง"""
w, h, m, n = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

x = [0] + x + [w]
y = [0] + y + [h]

a = []
for i in range(m + 1):
    for j in range(n + 1):
        area = (x[i + 1] - x[i]) * (y[j + 1] - y[j])
        a.append(area)

a.sort(reverse=True)
print(a[0], a[1])
