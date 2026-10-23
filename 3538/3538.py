"""find unpaired letters"""
text = input()
result = ""

for i in text:
    if text.count(i) % 2 and i not in result:
        result += i

if not result:
    print("fully paired")
else:
    print(result)
