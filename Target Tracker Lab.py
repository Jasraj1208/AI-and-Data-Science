numbers = [1, 3, 5, 2, 2]
print("PART 1: Track Array Sum")
print("Array:", numbers)
total_sum = sum(numbers)
print("Total array sum:", total_sum)
print("\nPART 2: Check Left-Right Balance")
for i in range(len(numbers)):
    left = numbers[:i]
    right = numbers[i + 1:]
    left_sum = sum(left)
    right_sum = sum(right)
    print(
        f"Index {i}: "
        f"left sum = {left_sum}, "
        f"right sum = {right_sum}"
    )
    if left_sum == right_sum:
        print("  -> Left and right sides are balanced!")
print("\nPART 3: Find Equilibrium Point")
equilibrium_index = -1
for i in range(len(numbers)):
    left_sum = sum(numbers[:i])
    right_sum = sum(numbers[i + 1:])
    if left_sum == right_sum:
        equilibrium_index = i
        break
if equilibrium_index != -1:
    print("Equilibrium point found!")
    print("Index:", equilibrium_index)
    print("Value:", numbers[equilibrium_index])
else:
    print("No equilibrium point found.")
print("\nPART 4: Grow a Subarray Window")
array = [1, 4, 20, 3, 10, 5]
target = 33
print("Array:", array)
print("Target:", target)
for start in range(len(array)):
    current_sum = 0
    for end in range(start, len(array)):
        current_sum += array[end]
        window = array[start:end + 1]
        print(
            f"Window: {window} "
            f"-> Sum: {current_sum}"
        )
        if current_sum >= target:
            break
print("\nPART 5: Search for Target Sum")
array = [1, 4, 20, 3, 10, 5]
target = 33
found_subarray = None
for start in range(len(array)):
    current_sum = 0
    for end in range(start, len(array)):
        current_sum += array[end]
        if current_sum == target:
            found_subarray = array[start:end + 1]
            break
        if current_sum > target:
            break
    if found_subarray is not None:
        break
if found_subarray is not None:
    print("Target sum found!")
    print("Subarray:", found_subarray)
    print("Sum:", sum(found_subarray))
else:
    print("No subarray with the target sum was found.")
print("\n===================================")
print("Five-part activity completed!")
print("===================================")