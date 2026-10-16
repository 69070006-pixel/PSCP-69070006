"""shorten"""
nums = []

while True:
    n = int(input())
    if n == -1:
        break
    nums.append(n)

if nums:
    start = nums[0]
    end = nums[0]
    result = []

    for i in range(1, len(nums)):
        if nums[i] == end + 1:
            end = nums[i]
        else:
            if start == end:
                result.append(str(start))
            else:
                result.append(f"{start}-{end}")

            start = nums[i]
            end = nums[i]

    if start == end:
        result.append(str(start))
    else:
        result.append(f"{start}-{end}")

    print(", ".join(result))
