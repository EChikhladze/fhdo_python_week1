n = int(input("Enter the number of elements: "))
input_list = [tuple(input(f"Enter element {i + 1}: ").split()) for i in range(n)]
sorted_list = sorted(input_list, key = lambda x : x[len(x) - 1])
print(input_list)
print(sorted_list)