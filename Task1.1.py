nums = iter(range(1, 1000))
val = []
for num in nums:
    if (num % 3) == 0 or (num % 5 == 0):
        val.append(num)

print('sum :', sum(val))
