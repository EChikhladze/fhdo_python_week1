s1 = input("Enter a string containing digits: ")
nums = [int(ch) for ch in s1 if ch.isdigit()]
sum = 0
for n in nums:
    sum += n

avg = sum / len(nums)

print(nums)
print(f"sum: {sum}")
print(f"avg: {avg}")