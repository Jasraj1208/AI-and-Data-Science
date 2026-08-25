arr = [1, 3, 5, 2, 2]
print("PART 1: Equilibrium Point")
print("Array:", arr)
equilibrium_index = -1
for i in range(len(arr)):
    left_sum = sum(arr[:i])
    right_sum = sum(arr[i + 1:])
    print(
        f"Index {i}: "
        f"left sum = {left_sum}, "
        f"right sum = {right_sum}"
    )
    if left_sum == right_sum:
        equilibrium_index = i
        break
print("Equilibrium index:", equilibrium_index)
if equilibrium_index != -1:
    print("Equilibrium element:", arr[equilibrium_index])
else:
    print("No equilibrium point found.")
print("\nPART 2: Slice-Based Equilibrium Check")
for i in range(len(arr)):
    left = arr[:i]
    right = arr[i + 1:]
    left_sum = sum(left)
    right_sum = sum(right)
    print(
        f"Index {i}: "
        f"left = {left}, sum = {left_sum} | "
        f"right = {right}, sum = {right_sum}"
    )
    if left_sum == right_sum:
        print("Equilibrium found!")
        break
numbers = [1, 4, 20, 3, 10, 5]
target = 33
print("\nPART 3: First Contiguous Subarray With Target Sum")
print("Array:", numbers)
print("Target:", target)
found_subarray = None
for start in range(len(numbers)):
    current_sum = 0
    for end in range(start, len(numbers)):
        current_sum += numbers[end]
        print(
            f"Checking {numbers[start:end + 1]} "
            f"-> sum = {current_sum}"
        )
        if current_sum == target:
            found_subarray = numbers[start:end + 1]
            break
        if current_sum > target:
            break
    if found_subarray is not None:
        break
if found_subarray is not None:
    print("First subarray:", found_subarray)
    print("Subarray sum:", sum(found_subarray))
else:
    print("No subarray found.")
print("\nPART 4: Slicing + sum()")
numbers = [2, 7, 5, 1, 9, 4]
target = 13
print("Array:", numbers)
print("Target:", target)
found = False
for start in range(len(numbers)):
    for end in range(start + 1, len(numbers) + 1):
        subarray = numbers[start:end]
        subarray_sum = sum(subarray)
        print(
            f"Subarray {subarray} "
            f"-> sum = {subarray_sum}"
        )
        if subarray_sum == target:
            print("Target found!")
            print("First matching subarray:", subarray)
            found = True
            break
        if subarray_sum > target:
            break
    if found:
        break
if not found:
    print("No contiguous subarray adds up to the target.")
print("\nPART 5: Final Combined Demonstration")
array1 = [2, 3, -1, 8, 4]
print("\nEquilibrium Problem")
print("Array:", array1)
answer = -1
for i in range(len(array1)):
    left_sum = sum(array1[:i])
    right_sum = sum(array1[i + 1:])
    if left_sum == right_sum:
        answer = i
        break
if answer != -1:
    print("Equilibrium index:", answer)
    print("Equilibrium value:", array1[answer])
else:
    print("No equilibrium point found.")
array2 = [1, 2, 3, 7, 5]
target = 12
print("\nSubarray Sum Problem")
print("Array:", array2)
print("Target:", target)
answer_subarray = None
for start in range(len(array2)):
    current_sum = 0
    for end in range(start, len(array2)):
        current_sum += array2[end]
        if current_sum == target:
            answer_subarray = array2[start:end + 1]
            break
        if current_sum > target:
            break
    if answer_subarray is not None:
        break
if answer_subarray is not None:
    print("First matching subarray:", answer_subarray)
    print("Sum:", sum(answer_subarray))
else:
    print("No matching subarray found.")
print("\nAll five parts completed!")