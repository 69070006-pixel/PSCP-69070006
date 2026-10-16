"""Giraffe"""
n = int(input())
height = []

for i in range(n):
    height.append(int(input()))

count = 0

if n == 1:
    count = 1
else:
    for i in range(n):
        if not i:
            if height[i] > height[i + 1]:
                count += 1
        elif i == n - 1:
            if height[i] > height[i - 1]:
                count += 1
        elif height[i] > height[i - 1] and height[i] > height[i + 1]:
            count += 1

print(count)
