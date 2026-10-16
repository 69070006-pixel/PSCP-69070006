"""findspy"""
m = int(input())
n = int(input())

group1 = set()
group2 = set()

for _ in range(m):
    group1.add(input().strip())

for _ in range(n):
    group2.add(input().strip())

result = sorted(group1 & group2, reverse=True)

if result:
    for student_id in result:
        print(student_id)
else:
    print("Nope")
